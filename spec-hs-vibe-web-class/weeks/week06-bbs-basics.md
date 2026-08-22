# 6주차 — 웹은 어떻게 동작하는가 · 나만의 BBS 만들기

**Phase:** 입문(재설계) | **소요:** 4시간
**대상:** 특목고 진학 준비 중학생
**원본 대응:** 인프런 원본 매핑 없음 — 본 6·7주차는 **자체 재설계 트랙**(BBS·웹 아키텍처)
**선수:** 5주차 — GitHub 저장소·README·CLAUDE.md 완료(Git 흐름 습관) / 4주차 — Plan 모드·권한 개념 / (사전과정 1~2주차를 거쳤다면) Python 클래스·Flask 챗 서버 실습 경험

---

## 오늘의 목표

오늘이 끝나면 학생은 아래를 **말로 설명**하고 **손으로 실행**할 수 있어야 한다.

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | 클라이언트·서버·DB **3단 구조**를 안다 | 그림을 보고 요청→응답 흐름을 순서대로 설명 |
| 2 | 프론트엔드·백엔드·DB의 **역할 차이**를 안다 | "이 파일/코드는 어디 담당?"을 스스로 분류 |
| 3 | Flask로 **라우트(엔드포인트)**를 만든다 | `GET /`, `GET /posts/<id>` 등이 브라우저에서 동작 |
| 4 | SQLite에 글을 **저장·조회**한다 | 새 글 작성 → 서버 재시작해도 데이터가 남음 |
| 5 | BBS **핵심 3화면**(목록·상세·작성)을 완성한다 | 브라우저에서 목록→상세→작성이 실제로 이어짐 |

### 특목고 연결 (오늘 심을 한 문장)

> 지금까지 만든 것은 "파일을 열면 보이는" 정적 페이지였다.
> 오늘부터는 **데이터가 저장되고, 다시 불러와지는** 서비스를 만든다 — 이것이 대부분의 실제 웹 서비스가 동작하는 방식이다.
> 탐구 활동에서도 "그냥 만들었다"보다 **"왜 이렇게 구조를 나눴는가"**를 설명할 수 있어야 한다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「나만의 BBS(게시판) — v0」**

Flask(백엔드) + SQLite(DB) + HTML 템플릿(프론트)으로 만드는 최소 게시판.
(디자인 패턴으로 구조를 리팩터링하고 React를 얹는 것은 **7주차**. 오늘은 **동작하는 3화면**에 집중한다.)

### 완성 모습 (최소 · 🟢)

| # | 화면/기능 | 최소 내용 |
|---|-----------|-----------|
| 1 | **목록** (`GET /`) | 저장된 글 제목이 리스트로 보임 |
| 2 | **상세** (`GET /posts/<id>`) | 목록에서 클릭하면 제목+본문 전체가 보임 |
| 3 | **작성** (`GET /new`, `POST /posts`) | 폼 제출 시 DB에 저장되고 목록에 반영됨 |
| 4 | **DB** | `posts` 테이블에 글이 실제로 쌓임 (서버 재시작 후에도 유지) |

### 폴더 구조 (수업 종료 시 예시)

```
week05-bbs/
├── app.py                 ← Flask 서버 (라우트 전부 여기)
├── bbs.db                 ← SQLite 파일 (자동 생성)
├── templates/
│   ├── list.html          ← 목록 화면
│   ├── detail.html        ← 상세 화면
│   └── new.html           ← 글쓰기 폼
└── notes/
    ├── architecture.md    ← 오늘 그린 클라이언트-서버-DB 그림 설명
    └── why-3tier.md       ← 「왜 이렇게 나눴는가」1문장+
```

> 4주차 프로필 폴더와는 **완전히 별개의 새 폴더**다. 오늘은 콘텐츠(프로필)가 아니라 **서비스 구조**를 배운다.

### 성공 기준 (🟢)
1. `python app.py`(또는 `flask run`)로 서버가 로컬에서 실행된다
2. 새 글을 작성하면 목록에 즉시 나타난다
3. 서버를 껐다 켜도 글이 **그대로 남아 있다** (DB에 저장됐다는 증거)
4. 클라이언트-서버-DB 그림을 보고 오늘 만든 BBS의 각 부분을 손으로 가리킬 수 있다

---

## 4시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:25 | A | 0 · 1 | Week5 회고 · 클라이언트-서버-DB 개념 |
| 0:25~1:25 | B | 2 · 3 · 4 | BBS란? · Flask 첫 라우트 · SQLite 테이블 함께 만들기 |
| 1:25~1:40 | — | — | 휴식 |
| 1:40~2:50 | C | 5 · 6 | 🟢 목록·상세·작성 구현 · 손으로 한 군데 고치기 |
| 2:50~3:00 | — | — | 휴식 |
| 3:00~3:45 | D | 7 · 8 | 🟡 수정/삭제·스타일 · 🔴 검색·비동기 글쓰기 맛보기 |
| 3:45~4:00 | E | 9 | 3단 구조 발표 · 회고 · Week7 예고 |

---

# 본문 — 챕터별 상세

---

## 0. Week5에서 이어가기

### 0.1. 60초 복습 퀴즈 (구두)

1. Git의 4단계 흐름은? → **status → add → commit → push**
2. Plan 모드를 언제 쓴다고 했나? → **파일이 2개 이상 생기거나 섹션이 늘어날 때**
3. Permission의 한 줄 정의는? → **「이 행동을 해도 될까?」를 묻는 안전장치**
4. (사전과정을 거쳤다면) 2주차 채팅 실습에서 서버가 데이터를 저장한 곳은? → **SQLite(.db 파일)**

### 0.2. 오늘은 왜 "새 폴더"인가

4주차 프로필은 **정적 파일**(HTML/CSS)이라 저장 기능이 없었고, 5주차는 그 정적 파일을 **GitHub에 올리는 법**을 배웠다. 오늘은 **글이 저장되는 서비스**를 만들기 때문에 완전히 새로운 종류의 프로젝트로 시작한다.

### 0.3. (해당자만) 사전과정 연결 다리

1~2주차 사전과정에서 파이썬 채팅 서버(`app.py` + `chat.db`)를 만들어본 적이 있다면, 오늘은 그 구조의 **확장판**이다 — 그때는 채팅 메시지 하나만 저장했다면, 오늘은 "제목+본문이 있는 글"을 저장하고 **목록·상세 화면까지** 만든다.

처음이라도 문제없다 — 오늘 챕터 1~4에서 개념부터 다시 짚는다.

### 0.4. 오늘 한 문장 목표 (학생 작성)

예시:
> 「글을 쓰면 저장되고, 목록에서 클릭하면 다시 보이는 게시판을 만든다.」

---

## 1. 웹은 어떻게 동작하는가 — 클라이언트·서버·DB

### 1.1. 지금까지 vs 오늘

| 지금까지 (Week3~4) | 오늘부터 |
|---------------------|-----------|
| `index.html`을 열면 끝 | **요청을 보내면 서버가 처리** |
| 데이터를 저장할 곳이 없음 | **DB에 데이터가 쌓임** |
| 브라우저 혼자서 다 함 | 브라우저(클라이언트) ↔ 서버 ↔ DB, **셋이 나눠서 함** |

### 1.2. 3단 구조 그림 (칠판)

```
[클라이언트]  --- 요청(Request) --->  [서버(백엔드)]  --- 조회/저장 --->  [DB]
 (브라우저,                              (Flask)                        (SQLite)
  프론트엔드)
              <--- 응답(Response) ---                <--- 결과 ---
```

**설명 포인트:**
- **클라이언트(프론트엔드)** = 사용자가 보는 화면. 오늘은 HTML 템플릿.
- **서버(백엔드)** = 요청을 받아서 "무엇을 할지" 처리하는 로직. 오늘은 Flask.
- **DB** = 데이터가 실제로 저장되는 곳. 오늘은 SQLite.

### 1.3. 식당 비유

> 손님(클라이언트)이 메뉴판을 보고 **주문**(요청)하면, 주방(서버)이 **조리**(로직 처리)하고, 재료 창고(DB)에서 필요한 걸 꺼내 와 음식(응답)을 만들어 준다.
> 손님은 주방에 직접 들어가지 않는다 — **정해진 창구(라우트)로만** 주고받는다.

### 1.4. 오늘 하지 않는 것 (Non-goals 안내)

- 배포(인터넷 공개) — 오늘은 **내 컴퓨터(localhost)**에서만
- 로그인·회원가입
- 여러 명이 동시에 쓰는 상황 대비(동시성 처리) — 개념만 언급

---

## 2. 오늘 만들 것 — BBS(게시판)란?

### 2.1. BBS = Bulletin Board System

인터넷 초창기부터 있던 가장 기본적인 웹 서비스 형태. 지금의 커뮤니티·카페·포럼 사이트도 근본은 같은 구조다.

### 2.2. 오늘의 최소 BBS 3화면

```
[ 목록 ]  GET /            → 저장된 글 제목 리스트
[ 상세 ]  GET /posts/<id>  → 글 하나의 제목+본문
[ 작성 ]  GET /new (폼) + POST /posts (저장)
```

### 2.3. `posts` 테이블 설계 (오늘 최소)

| 컬럼 | 타입 | 의미 |
|------|------|------|
| `id` | INTEGER (자동증가) | 글 고유 번호 |
| `title` | TEXT | 제목 |
| `content` | TEXT | 본문 |
| `created_at` | TEXT | 작성 시각 (자동 기록) |

---

## 3. Flask 시작하기

### 3.1. Flask란 (한 줄)

파이썬으로 **웹 서버**를 만들게 해주는 도구. "이 주소로 요청이 오면 이 함수를 실행해라"를 연결해 준다.

### 3.2. 준비 (터미널)

```
pip install flask
```

> 사전과정 1~2주차를 거쳤다면 이미 설치돼 있을 수 있다 — `python -c "import flask"`로 확인.

### 3.3. 함께 따라하기 — 첫 라우트

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "안녕, BBS!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

`python app.py` 실행 → 브라우저에서 `http://localhost:5001` 접속 → 글자가 보이면 성공.

> **포트 5001을 쓰는 이유:** macOS는 5000번을 AirPlay가 이미 쓰고 있는 경우가 많다. 사전과정 채팅 서버도 5001을 썼다 — 이번에도 통일.

### 3.4. 라우트 개념 정리

| 용어 | 뜻 |
|------|-----|
| 라우트(route) | "이 주소(경로)로 요청이 오면" 규칙 |
| `@app.route("/")` | 데코레이터 — 아래 함수를 이 주소에 연결 |
| `GET` | 데이터를 **조회**하는 요청 (기본값) |
| `POST` | 데이터를 **보내서 저장**하는 요청 |

---

## 4. SQLite로 데이터 저장하기

### 4.1. SQLite란 (한 줄)

설치 없이 **파일 하나(`.db`)**로 동작하는 가벼운 데이터베이스. 배우기 좋고, 오늘 같은 소규모 프로젝트에 딱 맞는다.

### 4.2. 함께 따라하기 — 테이블 생성

```python
import sqlite3
from pathlib import Path

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
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()
    conn.close()
```

`app.run()` 직전에 `create_table()`을 한 번 호출하면, 서버를 켤 때마다 "테이블이 없으면 만든다."

### 4.3. SQL 최소 문법 (오늘 쓸 것만)

| 문법 | 의미 | 예 |
|------|------|-----|
| `SELECT * FROM posts` | 전체 글 조회 | 목록 화면 |
| `SELECT * FROM posts WHERE id = ?` | 특정 글 하나 조회 | 상세 화면 |
| `INSERT INTO posts (title, content) VALUES (?, ?)` | 새 글 저장 | 작성 화면 |

**왜 `?`를 쓰나 (중요):** 사용자가 입력한 값을 SQL 문장에 직접 이어붙이면 위험하다(SQL Injection). `?`에 값을 안전하게 끼워 넣는 것이 규칙 — 이 부분은 "왜"까지 짧게 짚어준다.

---

## 5. BBS 핵심 기능 만들기 (🟢 실습)

### 5.1. Plan으로 먼저 계획 요청

```
목표: 게시판(BBS) 웹 서비스를 만든다.

제약:
- 백엔드: Python Flask
- DB: SQLite (파일 기반, posts 테이블)
- 프론트: Flask 템플릿(Jinja) 기반 HTML. React/Vue 등 프레임워크 금지
- 화면 3개: 목록(GET /), 상세(GET /posts/<id>), 글쓰기(GET /new + POST /posts)
- 한국어 UI

먼저 계획만 제안해줘:
1) 라우트 목록과 각 역할
2) posts 테이블 구조
3) templates/ 파일 구조
4) 하지 않을 것 (로그인, 수정/삭제는 이번엔 선택)

코드는 내가 "진행"이라고 한 뒤에만 작성해줘.
```

### 5.2. 나머지 라우트 (교사 데모 · 참고 코드)

```python
from flask import Flask, request, render_template, redirect, url_for

# ... (app, get_db, create_table은 위와 동일)

@app.route("/")
def index():
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return render_template("list.html", posts=posts)

@app.route("/posts/<int:post_id>")
def detail(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
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
    conn.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

### 5.3. 템플릿 최소 예시 (교사 데모)

`templates/list.html`
```html
<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>BBS</title></head>
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

`templates/detail.html`
```html
<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>{{ post.title }}</title></head>
<body>
  <a href="/">목록으로</a>
  <h1>{{ post.title }}</h1>
  <p>{{ post.created_at }}</p>
  <p>{{ post.content }}</p>
</body>
</html>
```

`templates/new.html`
```html
<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>글쓰기</title></head>
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

> 이 코드를 그대로 타이핑시키지 않는다. **Plan 승인 후 AI에게 구현을 맡기고**, 이 스니펫은 교사가 화면 공유로 "이런 모양이 나올 것"을 보여주는 기준점으로 쓴다.

### 5.4. 검증 체크리스트

- [ ] `/`에서 글 목록이 보인다
- [ ] 목록의 제목을 클릭하면 상세 화면으로 이동한다
- [ ] `/new`에서 폼을 제출하면 목록에 새 글이 추가된다
- [ ] 서버를 껐다 켜도 글이 남아 있다 (DB 저장 확인)
- [ ] 빈 제목/내용으로 제출했을 때 이상하게 깨지지 않는다 (완벽한 검증까지는 🟡)

---

## 6. 손으로 한 군데 고치기 (필수 습관)

1. `list.html`의 `<h1>게시판</h1>`을 **자신만의 게시판 이름**으로 직접 수정
2. 저장 → 서버 새로고침(Flask `debug=True`면 자동 반영) → 브라우저 새로고침
3. "내가 바꾼 줄"을 옆 친구에게 보여 주기

---

## 7. 🟡 확장: 수정 · 삭제 · 스타일

### 7.1. 삭제 기능 추가 프롬프트

```
상세 화면에 "삭제" 버튼을 추가해줘.
POST /posts/<id>/delete 라우트로 처리하고,
삭제 후에는 목록으로 이동해줘.
기존 목록·상세·작성 기능은 그대로 유지.
```

### 7.2. 수정 기능 추가 프롬프트 (여유 있으면)

```
상세 화면에 "수정" 버튼을 추가해줘.
GET /posts/<id>/edit로 폼을 보여주고,
POST /posts/<id>/edit로 저장해줘.
```

### 7.3. 최소 스타일 프롬프트

```
list.html, detail.html, new.html에 아주 단순한 CSS만 추가해줘.
과한 색상·애니메이션 금지. 읽기 쉬운 여백과 폰트 크기 정도만.
```

---

## 8. 🔴 도전

### 8.1. 검색 기능

```
목록 화면에 제목 검색창을 추가해줘.
GET /?q=검색어 형태로, 제목에 검색어가 포함된 글만 보여줘.
SQL은 LIKE 연산자를 사용하되, 반드시 ? 파라미터로 값을 넣어줘 (SQL Injection 방지).
```

### 8.2. fetch로 비동기 글쓰기 맛보기 — React로 가는 다리

지금까지는 폼을 제출하면 **페이지 전체가 새로고침**됐다. `fetch`를 쓰면 페이지를 새로고침하지 않고도 서버와 데이터를 주고받을 수 있다 — 다음 주 React가 이 방식 위에서 동작한다.

```
/new 페이지의 폼 제출을 fetch로 바꿔줘.
서버에는 새 라우트 POST /api/posts (JSON 응답)를 추가하고,
성공하면 새로고침 없이 목록 페이지로 이동해줘.
기존 POST /posts(폼 방식)는 그대로 남겨둬도 돼.
```

**포인트:** 오늘의 `POST /posts`(폼)와 `POST /api/posts`(JSON)의 차이를 한 문장으로 — "화면 전체를 다시 그리느냐, 데이터만 주고받느냐."

---

## 9. 정리 · 공유 · 다음 주

### 9.1. 30~60초 공유 스크립트

```
제 BBS는 (기능)을 만들었습니다.
클라이언트는 ○○, 서버는 ○○, DB는 ○○ 역할을 합니다.
막혔던 부분은 ○○였고, ○○로 해결했습니다.
```

### 9.2. `notes/why-3tier.md` 작성

```markdown
# 왜 3단으로 나눴는가

(1~3문장)

# 오늘 막혔던 점
예: SQLite에 저장은 됐는데 화면에 안 보였음 → SELECT 쿼리 순서 문제

# 다음에 하고 싶은 것
```

### 9.3. 회고 3줄

```
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

### 9.4. 오늘 배운 것 체크

- [ ] 클라이언트-서버-DB 3단 구조
- [ ] Flask 라우트(`@app.route`)
- [ ] SQLite 저장(`INSERT`)·조회(`SELECT`)
- [ ] 목록·상세·작성 3화면이 서로 연결됨
- [ ] `?` 파라미터로 안전하게 값 전달하는 습관

### 9.5. 다음 주 예고 (Week7)

- 오늘 만든 BBS를 **class·interface**로 구조화하기
- MVC, DI, IoC, POJO, 헥사고날 아키텍처 — "왜 코드를 이렇게 나누는가"
- React로 목록 화면 새로 만들기 (오늘의 `/api/posts` 맛보기가 다리 역할)

미리 생각해 오기 (숙제 아님):
> 오늘 `app.py` 한 파일에 라우트·DB 코드가 다 섞여 있었는데, 파일이 100개 라우트로 늘어나면 어떻게 될까?

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수 · 수업 중 완료 목표)
- [ ] Flask 서버 로컬 실행
- [ ] 목록·상세·작성 3화면 동작
- [ ] SQLite에 글이 저장되고 유지됨
- [ ] `notes/why-3tier.md` 1문장+
- [ ] 회고 3줄

### 🟡 (권장)
- [ ] 삭제 기능
- [ ] 최소 스타일 CSS
- [ ] 빈 값 제출 시 기본 검증

### 🔴 (도전)
- [ ] 검색 기능 (LIKE + `?` 파라미터)
- [ ] fetch 기반 비동기 글쓰기 + `/api/posts`
- [ ] 수정 기능

### 제출
- `app.py` + `templates/` (또는 스크린샷)
- `notes/why-3tier.md`
- 회고 3줄

---

## 교사 메모

### 진행 팁
- 사전과정(1~2주차)에서 Flask 챗 서버를 이미 만들어본 학급이면 **챕터 1~4를 빠르게** 훑고 5(실습)에 시간을 더 준다. 처음인 학급이면 챕터 3~4에서 속도를 늦춘다.
- `debug=True`는 코드 저장 시 자동 재시작 — 학생이 "고쳤는데 반영이 안 돼요"라고 하면 우선 `debug=True` 여부부터 확인.
- SQL Injection은 깊게 설명하지 않되, `?`를 안 쓰고 문자열을 직접 이어붙이면 왜 위험한지 **한 문장**은 반드시 짚는다.
- 포트 충돌(5000번, macOS AirPlay)이 흔하다 — 5001로 통일해 사고를 줄인다.

### 설명용 한 장 요약 (칠판)

```
클라이언트(브라우저) → 요청 → 서버(Flask) → DB(SQLite)
                      ← 응답 ←            ← 결과 ←

오늘 결과 → 목록·상세·작성 3화면 BBS (로컬)
다음 → class·interface·디자인 패턴으로 리팩터링 + React (Week7)
```

### FAQ

**Q. `ModuleNotFoundError: No module named 'flask'`가 떠요.**
A. `pip install flask` 안 됐거나 다른 파이썬 환경에서 실행 중. 터미널에 찍힌 파이썬 경로 확인 — 조교 호출.

**Q. 글을 썼는데 목록에 안 보여요.**
A. 대개 `conn.commit()` 누락, 또는 `SELECT` 쿼리가 다른 테이블/DB 파일을 보고 있음. `bbs.db` 파일이 실제로 생겼는지부터 확인.

**Q. 서버를 껐다 켜니 글이 사라졌어요.**
A. `CREATE TABLE`을 `IF NOT EXISTS` 없이 매번 새로 만들었거나, DB 파일 경로가 실행 위치마다 달라졌을 가능성. `Path(__file__).resolve().parent` 패턴을 유지했는지 확인.

**Q. HTML/CSS 예쁘게 꾸미는 데 시간을 다 써도 되나요?**
A. 오늘 핵심은 **저장·조회가 되는 구조**다. 스타일은 🟡 — 3화면이 안 되면 먼저 그것부터.

**Q. React를 오늘 바로 써도 되나요?**
A. 다음 주(7주차) 주제다. 오늘은 Flask 템플릿(Jinja)만으로 충분 — 프레임워크 도입은 다음 주에 "왜 필요한가"부터 설명한다.

---

## 부록 A — 학생용 프롬프트 치트시트

```
[Plan]
Flask + SQLite BBS. 화면 3개(목록/상세/작성). 템플릿은 Jinja만.
코드 말고 라우트·테이블·파일 구조만 먼저 제안해줘.

[삭제/수정 🟡]
상세 화면에 삭제(수정) 버튼 추가. 기존 기능은 유지.

[검색 🔴]
목록에 제목 검색. LIKE + ? 파라미터로 SQL Injection 방지.

[비동기 글쓰기 🔴]
/new 폼 제출을 fetch로 전환. POST /api/posts(JSON) 추가.
```

---

## 부록 B — 트러블슈팅 표

| 증상 | 원인(대개) | 대응 |
|------|-----------|------|
| `Address already in use` | 5001 포트가 이미 사용 중 | 이전 `python app.py` 프로세스 종료 후 재실행 |
| 한글이 깨져 보임 | 템플릿에 `<meta charset="UTF-8">` 누락 | 템플릿 `<head>`에 추가 |
| 글쓰기 후 오류 페이지 | `INSERT` 쿼리의 `?` 개수와 값 개수 불일치 | 컬럼 순서·값 순서 다시 확인 |
| 상세 페이지에서 404 | `<id>` 라우트의 타입(`<int:post_id>`) 누락 | 라우트 정의에 `int:` 명시했는지 확인 |

---

## 다음 주 (Week07)로 이어지는 다리

오늘은 **동작하는 BBS**까지다 — 그런데 `app.py` 한 파일에 라우트·SQL·화면 로직이 다 뒤섞여 있다.
다음 주는 이 코드를 **class·interface**로 나누고, **MVC·DI·IoC·POJO·헥사고날 아키텍처** 개념으로 "왜 이렇게 구조를 나누는가"를 배우며, 목록 화면을 **React**로도 만들어본다.
