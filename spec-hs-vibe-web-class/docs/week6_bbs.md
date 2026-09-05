# 2026 진학반 - 6주차

## 웹 서비스 만들기 - BBS

---

# 오늘의 목표
오늘이 끝나면 아래를 말로 설명하고 손으로 실행할 수 있어야 한다.

| 번호 | 목표 | 확인 방법 |
| :-- | :-- | :-- |
| 1 | 클라이언트·서버·DB 3단 구조를 안다 | 그림을 보고 요청→응답 흐름을 순서대로 설명 |
| 2 | 프론트엔드·백엔드·DB의 역할 차이를 안다 | "이 파일/코드는 어디 담당?"을 스스로 분류 |
| 3 | Flask로 라우트(엔드포인트)를 만든다 | `GET /`, `GET /posts/<id>` 등이 브라우저에서 동작 |
| 4 | SQLite에 글을 저장·조회한다 | 새 글 작성 → 서버 재시작해도 데이터가 남음 |
| 5 | BBS 핵심 3화면(목록·상세·작성)을 완성한다 | 브라우저에서 목록→상세→작성이 실제로 이어짐 |

---

# 오늘 완성할 프로그램
Flask(백엔드) + SQLite(DB) + HTML 템플릿(프론트)으로 만드는 최소 게시판

| 번호 | 화면/기능 | 최소 내용 |
| :-- | :-- | :-- |
| 1 | 목록 (`GET /`) | 저장된 글 제목이 리스트로 보임 |
| 2 | 상세 (`GET /posts/<id>`) | 목록에서 클릭하면 제목+본문 전체가 보임 |
| 3 | 작성 (`GET /new`, `POST /posts`) | 폼 제출 시 DB에 저장되고 목록에 반영됨 |
| 4 | DB | `posts` 테이블에 글이 실제로 쌓임 (서버 재시작 후에도 유지) |

---

# 1. 오늘 만들 것 — BBS(게시판)란?

## 1.1. BBS = Bulletin Board System
인터넷 초창기부터 있던 가장 기본적인 웹 서비스 형태. 
지금의 커뮤니티·카페·포럼 사이트도 근본은 같은 구조.

## 1.2. 최소 BBS 3화면
```text
[ 목록 ] GET / → 저장된 글 제목 리스트
[ 상세 ] GET /posts/<id> → 글 하나의 제목+본문
[ 작성 ] GET /new (폼) + POST /posts (저장)
```

## 1.3. `posts` 테이블 설계
| 번호 | 컬럼 | 타입 | 의미 |
| :-- | :-- | :-- | :-- |
| 1 | `id` | INTEGER (자동증가) | 글 고유 번호 |
| 2 | `title` | TEXT | 제목 |
| 3 | `content` | TEXT | 본문 |
| 4 | `created_at` | TEXT | 작성 시각 (자동 기록) |

## 1.4. 폴더 구조
```text
week06-bbs/
├── app.py          ← Flask 서버 (라우트 전부 여기)
├── bbs.db          ← SQLite 파일 (자동 생성)
├── templates/
│   ├── list.html   ← 목록 화면
│   ├── detail.html ← 상세 화면
│   └── new.html    ← 글쓰기 폼
```

---

# 2. Flask 시작하기

## 2.1. Flask란?
파이썬으로 웹 서버를 만들게 해주는 도구. "이 주소로 요청이 오면 이 함수를 실행해라"를 연결해 준다.

## 2.2. 준비 (터미널)
필요한 라이브러리를 설치합니다.
```bash
pip install flask
```

## 2.3. 함께 따라하기 — 첫 라우트
아래와 같이 기본적인 구조를 작성합니다.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "안녕, BBS!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

아래와 같이 실행합니다.
```bash
python app.py
```

## 2.4. 기본 용어 정리
| 용어 | 뜻 |
| :-- | :-- |
| 라우트(route) | "이 주소(경로)로 요청이 오면" 규칙 |
| `@app.route("/api")` | 데코레이터 — 아래 함수를 이 주소(“/api”)에 연결 |
| `GET` | 데이터를 조회하는 요청 (기본값) |
| `POST` | 데이터를 보내서 저장하는 요청 |
| 템플릿(Template) | 웹 화면의 뼈대(HTML)로, 서버에서 데이터를 받아 동적으로 화면을 생성해주는 틀 |
| CSS | 웹 화면을 예쁘게 꾸미고 레이아웃을 배치하는 디자인 언어 |
| JS(JavaScript) | 웹 화면에 움직임을 주거나 버튼 클릭 같은 사용자의 동작에 반응하게 만드는 프로그래밍 언어 |

---

# 3. SQLite로 Data 저장하기

## 3.1. DB(DataBase)란?
프로그램이 꺼져도 데이터가 사라지지 않고 안전하게 보관되며, 필요할 때 언제든 꺼내 쓸 수 있게 도와준다.
여기서 사용하게 될 SQLite는 설치 없이 파일 하나(`.db`)로 동작하는 가벼운 데이터베이스이다. 

## 3.2. 함께 따라하기 — 테이블 생성
```python
import sqlite3
from pathlib import Path

'''
...app.py 기존내용
'''

DATABASE = Path(__file__).resolve().parent / "bbs.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    app.run(debug=True, port=5001)
```
`app.run()` 직전에 `create_table()`을 한 번 호출하면, 서버를 켤 때마다 테이블이 없으면 생성한다.

## 3.3. SQL 문법
| 문법 | 의미 | 예 |
| :-- | :-- | :-- |
| `SELECT * FROM posts` | 전체 글 조회 | 목록 화면 |
| `SELECT * FROM posts WHERE id = ?` | 특정 글 하나 조회 | 상세 화면 |
| `INSERT INTO posts (title, content) VALUES (?, ?)` | 새 글 저장 | 작성 화면 |

> 왜 `?`를 사용하는지 생각해보기.

---

# 4. BBS 핵심 기능

| 번호 | 화면/기능 | 설명 |
| :-- | :-- | :-- |
| 1 | 목록 (`GET /`) | 저장된 글 목록 조회 |
| 2 | 상세 (`GET /posts/<id>`) | 개별 글 내용 확인 |
| 3 | 작성 (`GET /new`, `POST /posts`) | 새 글 등록 |
| 4 | 수정 (`GET /.../edit`, `POST /.../edit`) | 기존 글 수정 |
| 5 | 삭제 (`POST /.../delete`) | 글 삭제 |

## 4.1. 목록 · 상세 · 작성 라우트
```python
from flask import Flask, request, render_template, redirect, url_for

# ... (app, get_db, create_table은 위와 동일)

@app.route("/")
def index():
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("list.html", posts=posts)

@app.route("/posts/<int:post_id>")
def detail(post_id):
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    return render_template("detail.html", post=post)

@app.route("/new")
def new_form():
    return render_template("new.html")

@app.route("/posts", methods=["POST"])
def create_post():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()
    
    conn = get_db()
    conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    
    return redirect(url_for("index"))
```

## 4.2. 수정 · 삭제 라우트
목록·상세·작성과 똑같은 패턴이다 — 화면 보여주기(`GET`)와 DB 바꾸기(`POST`)만 반복된다.

```python
@app.route("/posts/<int:post_id>/edit")
def edit_form(post_id):
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    return render_template("edit.html", post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def update_post(post_id):
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()
    
    conn = get_db()
    conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, post_id))
    conn.commit()
    conn.close()
    
    return redirect(url_for("detail", post_id=post_id))

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    conn = get_db()
    conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for("index"))
```

*   `edit_form`은 왜 `GET`인가? → 화면만 보여주기 때문 (아직 DB를 바꾸지 않음)
*   `update_post`는 왜 `POST`인가? → DB 내용을 실제로 바꾸기 때문
*   `UPDATE ... WHERE id = ?`에서 `WHERE`를 빼면 어떻게 될까? → 모든 글이 같은 내용으로 바뀐다

## 4.3. 템플릿 직접 작성하기

**templates/list.html**
```html
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>BBS</title>
</head>
<body>
    <h1>게시판</h1>
    <a href="/new">글쓰기</a>
    <ul>
        {% for post in posts %}
        <li><a href="/posts/{{ post.id }}">{{ post.title }}</a> — {{ post.created_at }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/detail.html**
```html
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{{ post.title }}</title>
</head>
<body>
    <a href="/">목록으로</a>
    <h1>{{ post.title }}</h1>
    <p>{{ post.created_at }}</p>
    <p>{{ post.content }}</p>
    <a href="/posts/{{ post.id }}/edit">수정</a>
    <form method="POST" action="/posts/{{ post.id }}/delete" style="display:inline">
        <button type="submit">삭제</button>
    </form>
</body>
</html>
```

**templates/edit.html**
(`new.html`과 거의 같고, `value`로 기존 값을 미리 채워 넣는다)
```html
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>글 수정</title>
</head>
<body>
    <h1>글 수정</h1>
    <form method="POST" action="/posts/{{ post.id }}/edit">
        <input name="title" value="{{ post.title }}" required><br>
        <textarea name="content" required>{{ post.content }}</textarea><br>
        <button type="submit">저장</button>
    </form>
</body>
</html>
```

**templates/new.html**
```html
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>글쓰기</title>
</head>
<body>
    <h1>새 글 쓰기</h1>
    <form method="POST" action="/posts">
        <input name="title" placeholder="제목" required><br>
        <textarea name="content" placeholder="내용" required></textarea><br>
        <button type="submit">저장</button>
    </form>
</body>
</html>
```

## 4.4. 검증 체크리스트
- [ ] `/`에서 글 목록이 보인다
- [ ] 목록의 제목을 클릭하면 상세 화면으로 이동한다
- [ ] `/new`에서 폼을 제출하면 목록에 새 글이 추가된다
- [ ] 상세에서 "수정"을 누르면 기존 내용이 채워진 폼이 뜨고, 저장하면 바뀐다
- [ ] 상세에서 "삭제"을 누르면 글이 목록에서 사라진다
- [ ] 서버를 껐다 켜도 남은 글이 유지된다 (DB 저장 확인)

---

# 5. CSS 직접 추가하기
아래 CSS를 각 템플릿의 `<head>` 안에 `<style>...</style>`로 직접 붙여 넣는다.
```html
<style>
    body { font-family: sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; }
    input, textarea { width: 100%; box-sizing: border-box; padding: 8px; margin-bottom: 8px; }
    button { padding: 8px 16px; }
</style>
```
여백(margin), 폭(max-width) 숫자를 직접 바꿔보고 화면이 어떻게 달라지는지 확인한다.

---

# 6. AI와 함께 상상한 기능·스타일 만들기
기본적인 라우트·SQL·템플릿이 어떻게 동작하는지 알기 때문에, AI가 만든 코드도 읽고 판단할 수 있다.

## 6.1. AI에게 요청하는 기본 틀 (Plan 먼저)
```text
목표: 오늘 만든 BBS에 (내가 상상한 기능/스타일)을 추가한다.

제약:
- 기존 목록·상세·작성·수정·삭제 기능은 그대로 유지
- 파일: app.py, templates/ 안에서만 수정

먼저 계획만 제안해줘: 어떤 라우트/파일이 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

## 6.2. 예시 아이디어 — 검색 기능
```text
목표: 목록 화면에 제목 검색창을 추가한다.
GET /?q=검색어 형태로, 제목에 검색어가 포함된 글만 보여줘.
SQL은 LIKE 연산자를 사용하되, 반드시 ? 파라미터로 값을 넣어줘 (SQL Injection 방지).
```

## 6.3. 예시 아이디어 — fetch로 비동기 글쓰기 (React로 가는 다리)
지금까지는 폼을 제출하면 페이지 전체가 새로고침됐다. `fetch`를 쓰면 페이지를 새로고침하지 않고도 서버와 데이터를 주고받을 수 있다 — 다음 주 React가 이 방식 위에서 동작한다.

```text
/new 페이지의 폼 제출을 fetch로 바꿔줘.
서버에는 새 라우트 POST /api/posts (JSON 응답)를 추가하고,
성공하면 새로고침 없이 목록 페이지로 이동해줘.
기존 POST /posts(폼 방식)는 그대로 남겨둬도 돼.
```
> `POST /posts`와 `POST /api/posts`(JSON)의 차이를 알아본다.

## 6.4. 자유 상상 — 나만의 기능/스타일 1개
1. 내가 만들고 싶은 것을 한 줄로 먼저 적어본다 (예: "댓글을 달고 싶다", "다크 테마로 바꾸고 싶다", "글마다 태그를 달고 싶다").
2. 그다음 6.1의 틀에 채워 넣어 AI에게 요청한다.
3. 결과 코드를 받으면 반드시 한 줄씩 읽고, 모르는 부분은 AI에게 설명해 달라고 물어본다.

---

# 7. 정리

## 7.1. 기능 구현 요약
```text
제 BBS는 (기능)을 만들었습니다.
클라이언트는 ○○, 서버는 ○○, DB는 ○○ 역할을 합니다.
직접 만든 부분은 ○○, AI 도전 과제로 만든 부분은 ○○입니다.
```

## 7.2. 회고 3줄
```text
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

## 7.3. 오늘 배운 것
- 클라이언트-서버-DB 3단 구조
- Flask 라우트(`@app.route`)
- SQLite 저장(`INSERT`)·조회(`SELECT`)·수정(`UPDATE`)·삭제(`DELETE`)
- 목록·상세·작성·수정·삭제가 서로 연결됨
