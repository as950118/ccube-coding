# 7주차 — class·interface·디자인 패턴(MVC·DI·IoC·POJO·헥사고날) + React

> ⚠️ **보관됨(displaced):** 2026 커리큘럼 재설계로 7주차는 [week07-bbs-auth.md](../week07-bbs-auth.md)(회원·권한 업그레이드)로 대체되었습니다. 본 문서는 보충·교사 참고용으로만 보관합니다.

**Phase:** 입문(재설계) | **소요:** 4시간
**대상:** 특목고 진학 준비 중학생
**원본 대응:** 인프런 원본 매핑 없음 — 본 6·7주차는 **자체 재설계 트랙**(BBS·웹 아키텍처)
**선수:** 6주차 — Flask+SQLite BBS(목록·상세·작성·수정·삭제)를 AI 없이 완성

---

## 오늘의 목표

오늘이 끝나면 학생은 아래를 **말로 설명**하고 **손으로 실행**할 수 있어야 한다.

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | class와 **POJO**를 안다 | `Post`를 프레임워크에 안 묶인 순수 객체로 분리 설명 |
| 2 | **interface**(추상화)를 안다 | `PostRepository`(약속)와 `SqlitePostRepository`(구현)를 구분 설명 |
| 3 | **MVC**로 코드를 재분류한다 | 파일마다 Model/View/Controller 중 무엇인지 손으로 가리킴 |
| 4 | **DI**(의존성 주입)를 코드로 체감한다 | 라우트가 DB를 직접 안 만들고 Repository를 "받는" 구조로 리팩터링 |
| 5 | **IoC**(제어의 역전)를 프레임워크 관점으로 설명한다 | "누가 내 함수를 호출하는가"를 뒤집어 설명 |
| 6 | **헥사고날**(포트&어댑터) 감각을 안다 | SQLite 어댑터를 메모리 어댑터로 한 줄 교체해도 앱이 동작함을 시연 |
| 7 | **React**로 목록 화면 View를 교체한다 | `GET /api/posts`를 fetch해 React 컴포넌트가 렌더 |

### 특목고 연결 (오늘 심을 한 문장)

> 지난주는 "동작하게" 만드는 것이었다. 오늘은 "잘 나눠서, 바꾸기 쉽게" 만드는 것이다.
> 실제 소프트웨어 개발·연구 모두에서 **구조를 설명할 수 있는 능력**은 코드를 짜는 능력만큼 중요하다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「나만의 BBS — 구조화 버전(v1)」**

6주차 `week06-bbs/` 폴더를 **그대로 이어쓴다**. `app.py` 하나에 몰려 있던 라우트·SQL·화면 로직을 class·interface로 나누고, 목록 화면을 React로도 만들어본다.

**오늘도 2~5장(구조 리팩터링)은 AI 없이 직접 코드를 작성한다.** AI는 6장(React 도전 과제)에서만 쓴다 — 이미 손으로 만든 구조를 알고 있어야, AI가 만든 React 코드도 읽고 판단할 수 있다.

### 완성 모습 (최소 · 🟢)

| # | 항목 | 최소 내용 |
|---|------|-----------|
| 1 | **POJO** | `models/post.py`에 `Post` 클래스 — Flask·SQLite를 모른다 |
| 2 | **interface** | `repositories/post_repository.py`에 추상 클래스(`ABC`) |
| 3 | **구현체** | `repositories/sqlite_post_repository.py` — 인터페이스를 구현 |
| 4 | **DI** | `app.py`의 라우트가 `repo`를 주입받아 사용, 직접 DB 연결 안 함 |
| 5 | **동작 유지** | 6주차와 동일하게 목록·상세·작성·수정·삭제가 전부 동작 |

### 폴더 구조 (수업 종료 시 예시)

```
week06-bbs/                        ← 6주차 폴더를 이어씀
├── app.py                         ← 라우트만 남음 (Controller)
├── bbs.db
├── models/
│   └── post.py                    ← Post 클래스 (POJO)
├── repositories/
│   ├── post_repository.py         ← 추상 인터페이스 (Port)
│   ├── sqlite_post_repository.py  ← SQLite 구현체 (Adapter)
│   └── memory_post_repository.py  ← 🟡 메모리 구현체 (다른 Adapter)
├── templates/                     ← 기존 (Jinja View)
├── static/
│   └── react-list.html            ← 🔴 React 목록 화면 (다른 View)
└── notes/
    ├── mvc-mapping.md             ← 파일별 M/V/C 매핑
    └── why-layers.md              ← 왜 층을 나눴는가 회고
```

### 성공 기준 (🟢)
1. `Post` 클래스가 Flask·SQLite import 없이 독립적으로 존재한다
2. `PostRepository`(추상)와 `SqlitePostRepository`(구현)가 분리되어 있다
3. `app.py`의 각 라우트가 `repo.find_all()`처럼 **Repository를 통해서만** DB에 접근한다
4. 6주차의 목록·상세·작성·수정·삭제가 리팩터링 후에도 **그대로 동작**한다

---

## 4시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:25 | A | 0 · 1 | Week6 회고 · "왜 구조를 나누는가" 문제 제기 |
| 0:25~1:25 | B | 2 | 🟢 POJO·interface·구현체 직접 작성 (AI 없이) |
| 1:25~1:40 | — | — | 휴식 |
| 1:40~2:50 | C | 3 · 4 | 🟢 MVC 재분류 · DI 리팩터링 · IoC 미니 실습 (직접) |
| 2:50~3:00 | — | — | 휴식 |
| 3:00~3:45 | D | 5 · 6 | 🟡 헥사고날 어댑터 교체(직접) · 🔴 React 도전(AI 사용) |
| 3:45~4:00 | E | 7 | 발표 · 회고 · Week8 예고 |

---

# 본문 — 챕터별 상세

---

## 0. Week6에서 이어가기

### 0.1. 60초 복습 퀴즈 (구두)

1. 지난주 만든 5기능은? → **목록·상세·작성·수정·삭제**
2. `?` 파라미터를 쓰는 이유는? → **SQL Injection 방지**
3. 지난주 AI는 언제 썼나? → **마지막 도전 과제(검색·비동기 글쓰기)에서만**

### 0.2. 오늘 문제 제기

> 지난주 `app.py` 한 파일에 라우트·SQL·화면 로직이 다 뒤섞여 있었다. 이 파일이 100개 라우트로 늘어나면?

- 원하는 라우트 하나를 찾기 어려워진다
- SQL 문법을 바꾸고 싶은데(SQLite → 다른 DB) 라우트 코드까지 다 뒤져야 한다
- 화면(HTML)만 바꾸고 싶은데 DB 코드까지 같이 보게 된다

오늘은 이 문제를 **역할을 나눠서** 해결한다.

### 0.3. 오늘 한 문장 목표 (학생 작성)

예시:
> 「app.py에 뒤섞여 있던 코드를 역할별로 나누고, 화면 하나(React)를 새로 붙여본다.」

---

## 1. 왜 구조를 나누는가

### 1.1. 오늘 배우는 5개 키워드, 한 줄 예고

| 키워드 | 한 줄 |
|--------|------|
| POJO | 프레임워크에 안 묶인 **순수한 데이터 객체** |
| interface | "이런 기능을 제공하겠다"는 **약속**(구현은 나중) |
| MVC | 화면(View)·로직(Controller)·데이터(Model) **역할 분리** |
| DI | 필요한 것을 직접 안 만들고 **밖에서 받는다** |
| IoC | 내가 함수를 부르는 게 아니라 **프레임워크가 나를 부른다** |

### 1.2. 오늘 하지 않는 것 (Non-goals)

- 진짜 대규모 프로젝트 수준의 폴더 구조(수십 개 계층)
- Java/Spring 실습 (개념만 빌려오고, 코드는 계속 Python)
- 완벽한 테스트 코드 작성(단, 헥사고날 장점 설명에 "테스트하기 쉬워진다"는 언급)

---

## 2. class·POJO·interface — 직접 작성 (🟢, AI 없이)

> 오늘도 AI에게 "리팩터링해줘"라고 시키지 않는다. 아래 코드를 직접 입력하며, **왜 파일을 이렇게 나눴는지** 한 줄씩 이해한다.

### 2.1. `Post` 클래스 (POJO)

**POJO**(Plain Old Java Object)는 원래 자바 용어지만, 뜻은 언어를 안 가린다 — "프레임워크(Flask, SQLite 등)를 전혀 모르는, 데이터만 담는 순수한 객체." 파이썬에서는 종종 **Plain Old Python Object**라고도 부른다.

`models/post.py`
```python
class Post:
    def __init__(self, id, title, content, created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
```

**확인 포인트:** 이 파일 어디에도 `import flask`, `import sqlite3`가 없다. `Post`는 웹인지 콘솔 프로그램인지도 모른다 — 그래서 재사용하기 쉽다.

### 2.2. `PostRepository` — interface(추상 클래스)

파이썬에는 다른 언어의 `interface` 키워드가 없지만, `abc.ABC`로 같은 효과를 낸다: **"이 기능들을 구현해야 한다"는 약속**만 정의하고, 실제 코드는 비워 둔다.

`repositories/post_repository.py`
```python
from abc import ABC, abstractmethod

class PostRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, post_id):
        pass

    @abstractmethod
    def save(self, title, content):
        pass

    @abstractmethod
    def update(self, post_id, title, content):
        pass

    @abstractmethod
    def delete(self, post_id):
        pass
```

**확인 포인트:** 이 파일에도 SQL이 한 줄도 없다. "글을 다 가져온다(`find_all`)"는 약속만 있고, **어떻게** 가져올지는 안 적혀 있다.

### 2.3. `SqlitePostRepository` — 구현체

이제 "어떻게"를 채운다. 6주차 `app.py`에 있던 SQL 코드를 그대로 옮겨온다.

`repositories/sqlite_post_repository.py`
```python
import sqlite3
from models.post import Post
from repositories.post_repository import PostRepository

class SqlitePostRepository(PostRepository):
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def find_all(self):
        conn = self._get_db()
        rows = conn.execute(
            "SELECT * FROM posts ORDER BY id DESC"
        ).fetchall()
        conn.close()
        return [Post(r["id"], r["title"], r["content"], r["created_at"]) for r in rows]

    def find_by_id(self, post_id):
        conn = self._get_db()
        row = conn.execute(
            "SELECT * FROM posts WHERE id = ?", (post_id,)
        ).fetchone()
        conn.close()
        return Post(row["id"], row["title"], row["content"], row["created_at"]) if row else None

    def save(self, title, content):
        conn = self._get_db()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
        )
        conn.commit()
        conn.close()

    def update(self, post_id, title, content):
        conn = self._get_db()
        conn.execute(
            "UPDATE posts SET title = ?, content = ? WHERE id = ?",
            (title, content, post_id)
        )
        conn.commit()
        conn.close()

    def delete(self, post_id):
        conn = self._get_db()
        conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        conn.close()
```

**확인 포인트:** `class SqlitePostRepository(PostRepository):` — 괄호 안이 "이 약속을 지키겠다"는 선언이다. `@abstractmethod`로 정의된 5개를 하나라도 안 만들면 파이썬이 에러를 낸다 — 직접 메서드 하나를 지워서 에러 메시지를 확인해 본다.

---

## 3. MVC 재분류 · DI 리팩터링 (🟢, 직접)

### 3.1. 지금까지 만든 파일을 MVC로 분류

| 파일 | 역할 |
|------|------|
| `models/post.py`, `repositories/*.py` | **Model** — 데이터와 데이터 접근 |
| `templates/*.html` | **View** — 사용자가 보는 화면 |
| `app.py`의 라우트 함수들 | **Controller** — 요청을 받아 Model에 물어보고 View에 넘김 |

### 3.2. `app.py`를 DI로 리팩터링

**DI(Dependency Injection, 의존성 주입)**: 라우트(Controller)가 SQLite 연결을 **직접 만들지 않고**, 이미 만들어진 `repo`를 **받아서** 쓴다.

```python
from flask import Flask, request, render_template, redirect, url_for
from repositories.sqlite_post_repository import SqlitePostRepository

app = Flask(__name__)
repo = SqlitePostRepository("bbs.db")   # ← 여기서 딱 한 번 "조립"

@app.route("/")
def index():
    posts = repo.find_all()
    return render_template("list.html", posts=posts)

@app.route("/posts/<int:post_id>")
def detail(post_id):
    post = repo.find_by_id(post_id)
    return render_template("detail.html", post=post)

@app.route("/new")
def new_form():
    return render_template("new.html")

@app.route("/posts", methods=["POST"])
def create_post():
    repo.save(
        request.form.get("title", "").strip(),
        request.form.get("content", "").strip()
    )
    return redirect(url_for("index"))

@app.route("/posts/<int:post_id>/edit")
def edit_form(post_id):
    post = repo.find_by_id(post_id)
    return render_template("edit.html", post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def update_post(post_id):
    repo.update(
        post_id,
        request.form.get("title", "").strip(),
        request.form.get("content", "").strip()
    )
    return redirect(url_for("detail", post_id=post_id))

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    repo.delete(post_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

**직접 확인해보기:**
- 라우트 함수 안 어디에도 `sqlite3.connect`가 없다 — 전부 `repo.xxx()`로만 DB를 다룬다
- "주입(Injection)"이 일어나는 곳은 **딱 한 줄**, `repo = SqlitePostRepository("bbs.db")`
- 이 한 줄을 지우고 다른 걸 넣으면 무슨 일이 생길까? (→ 5장에서 직접 해본다)

### 3.3. 검증 체크리스트

- [ ] 6주차와 동일하게 목록·상세·작성·수정·삭제가 전부 동작한다
- [ ] `app.py`에 SQL 문자열이 한 줄도 없다
- [ ] `models/post.py`에 Flask·SQLite import가 없다

---

## 4. IoC — 누가 내 함수를 호출하는가 (🟡, 직접)

### 4.1. 일반 코드 vs 프레임워크 코드

```python
# 일반적인 흐름 — 내가 직접 부른다
def greet():
    print("안녕!")

greet()  # 내 코드가 명시적으로 호출
```

그런데 `app.py`의 `index()`, `detail()` 같은 함수들을 우리가 직접 호출한 적이 있는가? **없다.** `@app.route(...)`로 "등록"만 했을 뿐, 브라우저가 요청을 보내면 **Flask가 알아서** 그 함수를 호출한다.

> **IoC(제어의 역전)**: 보통은 내 코드가 흐름을 제어하지만(내가 함수를 부름), 프레임워크를 쓰면 **흐름의 제어권이 프레임워크로 넘어간다**(프레임워크가 내 함수를 부름).

### 4.2. 미니 IoC 흉내내기 (직접 실습, 5~10분)

Flask 내부에서 실제로 벌어지는 일을 아주 단순화해서 재현해 본다.

```python
handlers = {}

def route(path):
    def decorator(func):
        handlers[path] = func
        return func
    return decorator

@route("/")
def index():
    print("index 실행됨!")

# 지금까지 index()를 우리가 직접 호출한 적이 없다.
# "누군가"(여기서는 우리가 만든 미니 프레임워크)가 나중에 대신 호출한다:
handlers["/"]()
```

**확인 포인트:** `@route("/")`가 실행되는 시점과 `handlers["/"]()`이 실행되는 시점은 다르다. `@app.route`도 똑같은 원리로, 여러분의 함수를 "등록"해뒀다가 요청이 올 때 Flask가 대신 호출해 준다.

---

## 5. 🟡 헥사고날 맛보기 — 어댑터 교체 (직접)

### 5.1. Port와 Adapter라는 용어

- **Port(포트)** = `PostRepository` 같은 **interface** — "이런 기능을 제공한다"는 약속
- **Adapter(어댑터)** = `SqlitePostRepository`처럼 그 약속을 **구현한 것** — DB 종류·저장 방식이 달라도 됨

헥사고날 아키텍처(포트와 어댑터 아키텍처)의 핵심 주장: **핵심 로직(Controller·View)은 Port에만 의존하고, 어떤 Adapter를 쓰는지는 몰라도 된다.**

### 5.2. `MemoryPostRepository` 만들기

`repositories/memory_post_repository.py`
```python
from models.post import Post
from repositories.post_repository import PostRepository

class MemoryPostRepository(PostRepository):
    def __init__(self):
        self._posts = []
        self._next_id = 1

    def find_all(self):
        return list(reversed(self._posts))

    def find_by_id(self, post_id):
        return next((p for p in self._posts if p.id == post_id), None)

    def save(self, title, content):
        self._posts.append(Post(self._next_id, title, content, "방금"))
        self._next_id += 1

    def update(self, post_id, title, content):
        post = self.find_by_id(post_id)
        if post:
            post.title = title
            post.content = content

    def delete(self, post_id):
        self._posts = [p for p in self._posts if p.id != post_id]
```

### 5.3. 한 줄만 바꿔서 어댑터 교체

`app.py`에서 딱 한 줄만 바꾼다.

```python
# 이전
repo = SqlitePostRepository("bbs.db")

# 교체
repo = MemoryPostRepository()
```

서버를 다시 실행하면 목록·상세·작성·수정·삭제가 **똑같이 전부 동작한다** — 단, 서버를 껐다 켜면 데이터가 사라진다(메모리이므로).

**직접 확인해보기:** 라우트 코드(`app.py`의 함수들), 템플릿(`list.html` 등) 중 **단 한 줄도 바꾸지 않았다.** 이게 헥사고날의 핵심 이득이다 — Adapter만 갈아 끼우면, Controller·View는 그대로 재사용된다. (실무에서는 이 성질 덕분에 진짜 DB 없이 `MemoryPostRepository`로 빠르게 테스트하기도 한다.)

작업이 끝나면 다시 `repo = SqlitePostRepository("bbs.db")`로 되돌려 놓는다 (오늘 만든 글을 유지하기 위해).

---

## 6. 🔴 도전 과제 — React로 목록 화면 만들기 (여기서만 AI 사용)

지금까지 구조 리팩터링은 전부 직접 했다. React 문법은 오늘 처음이므로, 이번에는 AI 도움을 받아 작성하고 **결과를 읽으며 이해**한다.

### 6.1. `GET /api/posts` 추가 (직접, 짧은 코드)

```python
from flask import jsonify

@app.route("/api/posts")
def api_posts():
    posts = repo.find_all()
    return jsonify([
        {"id": p.id, "title": p.title, "created_at": p.created_at}
        for p in posts
    ])
```

이미 만들어 둔 `repo`를 그대로 쓴다 — DI 덕분에 API 라우트를 추가해도 Repository 코드는 손댈 필요가 없다.

### 6.2. AI에게 React 화면 요청 (Plan 먼저)

```
목표: 오늘 만든 Flask 앱의 GET /api/posts를 이용해, React로 게시글 목록 화면을 만든다.

제약:
- npm/Vite 없이 CDN(React, ReactDOM, Babel standalone)만 사용
- 파일 하나: static/react-list.html
- useState, useEffect, fetch만 사용 (다른 라이브러리 금지)
- 한국어 UI

먼저 계획만 제안해줘: 컴포넌트 구조와 상태(state) 설계.
내가 "진행"이라고 하면 구현해줘.
```

### 6.3. 참고 결과 (교사 데모 · AI가 만들 법한 코드)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>React 목록</title>
  <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    function PostList() {
      const [posts, setPosts] = React.useState([]);

      React.useEffect(() => {
        fetch("/api/posts")
          .then((res) => res.json())
          .then(setPosts);
      }, []);

      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      );
    }

    ReactDOM.createRoot(document.getElementById("root")).render(<PostList />);
  </script>
</body>
</html>
```

`http://localhost:5001/static/react-list.html`로 접속해 확인한다.

### 6.4. 오늘의 연결 포인트

- 이 화면도 **View**다 — MVC의 Model(`repo`)·Controller(`/api/posts`)는 그대로 두고 View만 Jinja → React로 바꾼 것
- `useEffect`는 "화면이 뜨자마자 fetch 실행"을 담당 — 지난주 배운 클라이언트→서버 요청과 같은 흐름이다
- (참고) 오늘은 npm/Vite 없는 CDN 방식만 다룬다. 정식 React 프로젝트 빌드 방식은 추후 별도로 다룰 수 있다.

---

## 7. 정리 · 공유 · 다음 주

### 7.1. 30~60초 공유 스크립트

```
오늘은 app.py를 Model/View/Controller로 나눴습니다.
Repository를 ○○(Sqlite/Memory)로 바꿔도 나머지 코드는 그대로였습니다.
React 도전 과제에서는 ○○을 만들었습니다.
```

### 7.2. `notes/mvc-mapping.md` 작성

```markdown
# 오늘 파일별 MVC 매핑

| 파일 | M/V/C |
|------|-------|
| models/post.py | Model |
| repositories/*.py | Model |
| templates/*.html | View |
| static/react-list.html | View |
| app.py | Controller |
```

### 7.3. `notes/why-layers.md` 작성

```markdown
# 왜 층을 나눴는가
(1~3문장)

# 오늘 막혔던 점

# 다음에 하고 싶은 것
```

### 7.4. 회고 3줄

```
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

### 7.5. 오늘 배운 것 체크

- [ ] POJO — 프레임워크에 안 묶인 순수 객체
- [ ] interface(`ABC`) — 약속과 구현의 분리
- [ ] MVC — Model/View/Controller 역할 구분
- [ ] DI — 라우트가 Repository를 "받아서" 씀
- [ ] IoC — 프레임워크가 내 함수를 대신 호출
- [ ] 헥사고날 — 어댑터만 바꿔도 코어는 그대로

### 7.6. 다음 주 예고 (Week8)

- 커스텀 슬래시 커맨드 · 서브에이전트 입문
- MCP(Model Context Protocol) 개념 + 설치 실습

미리 생각해 오기 (숙제 아님):
> 오늘 Repository를 Sqlite ↔ Memory로 바꿔봤는데, 진짜 서비스라면 언제 이런 교체가 필요할까?

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수 · AI 없이 직접 작성)
- [ ] `models/post.py`(POJO) 분리
- [ ] `repositories/post_repository.py`(interface) + `sqlite_post_repository.py`(구현체)
- [ ] `app.py`를 DI로 리팩터링, 6주차 5기능 그대로 동작
- [ ] `notes/mvc-mapping.md`
- [ ] 회고 3줄

### 🟡 (권장 · 직접)
- [ ] IoC 미니 실습(4.2) 직접 실행해보기
- [ ] `memory_post_repository.py` 작성 + 한 줄 교체로 동작 확인

### 🔴 (도전 · 여기서만 AI 사용)
- [ ] `GET /api/posts` 추가
- [ ] React로 `static/react-list.html` 목록 화면 완성

### 제출
- `app.py` + `models/` + `repositories/` (또는 스크린샷)
- `notes/mvc-mapping.md` / `notes/why-layers.md`
- 회고 3줄

---

## 교사 메모

### 진행 팁
- **2~5장도 AI 없이 진행한다** — 6주차와 같은 원칙. React(6장)에서만 AI를 허용해, "새로운 문법은 AI로 빠르게 맛보되 익숙한 백엔드는 손으로 이해한다"는 감각 차이를 준다.
- `abc.ABC`가 낯설면 "그냥 파이썬이 강제로 확인해주는 체크리스트"라고 비유해도 좋다.
- 시간이 부족하면 5장(헥사고날)을 🟡에서 관찰만 하고 넘어가도 된다 — 6장(React)이 더 우선순위 높은 🔴는 아니지만, 학생 흥미 유지에는 도움된다.
- IoC 미니 실습(4.2)은 Flask 없이 순수 파이썬으로 돌아간다 — 이해가 안 되면 Flask 없이 이 코드만 따로 실행해서 보여준다.

### 설명용 한 장 요약 (칠판)

```
POJO      → 프레임워크 모르는 순수 객체 (Post)
interface → 약속만 (PostRepository)
구현체     → 약속을 지킴 (Sqlite / Memory)
MVC       → Model(post,repo) / View(html,react) / Controller(app.py)
DI        → repo를 라우트가 "받아서" 씀
IoC       → Flask가 내 함수를 대신 호출
헥사고날   → 어댑터만 바꿔도 코어는 그대로

오늘 결과 → 구조화된 BBS + React 목록 화면 1개
다음 → 커맨드·서브에이전트·MCP 입문 (Week8)
```

### FAQ

**Q. `abc.ABC`를 안 쓰고 그냥 클래스로만 해도 되나요?**
A. 파이썬은 강제하지 않지만(덕 타이핑), 오늘은 **"약속을 지켰는지 파이썬이 확인해준다"**는 경험을 위해 `ABC`를 명시적으로 쓴다.

**Q. React 코드를 이해 못 했는데 그대로 제출해도 되나요?**
A. `useState`/`useEffect`/`fetch` 세 개만이라도 "이게 뭘 하는지" 한 줄로 설명할 수 있으면 충분하다. 모르면 AI에게 "이 줄이 뭘 하는지 설명해줘"라고 물어보는 것도 오늘의 학습이다.

**Q. 왜 Vite/npm으로 React를 안 하나요?**
A. 오늘은 구조(디자인 패턴)가 핵심이라 빌드 도구까지 더하면 과부하다. CDN 방식으로 개념만 맛본다 — 정식 빌드 환경은 추후 다룰 수 있다.

**Q. MemoryPostRepository로 바꾼 채로 끝내도 되나요?**
A. 오늘 만든 글이 사라지므로, 확인 후 `SqlitePostRepository`로 반드시 되돌린다.

---

## 부록 A — 학생용 프롬프트 치트시트 (6장 React 전용 — 그 전에는 AI 사용 안 함)

```
[React 목록 화면]
Flask GET /api/posts를 fetch하는 React 목록 화면.
CDN만 사용(React/ReactDOM/Babel standalone), npm/Vite 금지.
useState/useEffect/fetch만. 파일 하나(static/react-list.html).
먼저 계획만 제안해줘.
```

---

## 부록 B — 트러블슈팅 표

| 증상 | 원인(대개) | 대응 |
|------|-----------|------|
| `Can't instantiate abstract class` | 추상 메서드 하나를 구현 안 함 | `PostRepository`의 5개 메서드를 모두 구현했는지 확인 |
| 리팩터링 후 화면이 안 뜸 | `repo` import 경로 오류 | `from repositories.sqlite_post_repository import ...` 철자 확인 |
| React 화면이 빈 화면 | `/api/posts`가 404 | Flask에 `api_posts` 라우트를 추가했는지, 서버 재시작했는지 확인 |
| React 콘솔에 Babel 에러 | `<script type="text/babel">` 누락 | JSX가 들어간 `<script>` 태그에 `type="text/babel"` 확인 |

---

## 다음 주 (Week08)로 이어지는 다리

오늘로 **역할이 나뉜 BBS**와 **View 하나를 교체해 본 경험**까지 만들었다.
다음 주는 이 워크플로 자체를 자동화하는 커맨드·서브에이전트·MCP를 맛본다.
