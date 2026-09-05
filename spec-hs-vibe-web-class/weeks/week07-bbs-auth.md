# 7주차 — BBS 업그레이드 · 회원가입·로그인·권한

**Phase:** 입문(재설계) | **소요:** 4시간
**대상:** 특목고 진학 준비 중학생
**원본 대응:** 인프런 원본 매핑 없음 — 본 6·7주차는 **자체 재설계 트랙**(BBS·웹 아키텍처)
**선수:** 6주차 — Flask+SQLite BBS(목록·상세·작성·수정·삭제)를 AI 없이 완성

---

## 오늘의 목표

오늘이 끝나면 학생은 아래를 **말로 설명**하고 **손으로 실행**할 수 있어야 한다.

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | **회원가입·로그인·로그아웃**을 구현한다 | 계정을 만들고, 로그인하면 상단에 내 이름이 보임 |
| 2 | **세션(session)**으로 "지금 누가 로그인했는지"를 안다 | 로그인 전·후에 글쓰기 버튼 노출이 달라짐 |
| 3 | **비밀번호를 DB에 그대로 저장하지 않는다** | `generate_password_hash`로 해시 저장, 로그인 시 `check_password_hash` |
| 4 | 글에 **작성자를 연결**한다 | 목록·상세에 작성자 이름이 보임 (`posts.user_id`) |
| 5 | **권한(permission)**을 코드로 구현한다 | 로그인한 사람만 글쓰기, **본인 글만** 수정·삭제 |
| 6 | 6주차 5기능이 **업그레이드 후에도** 동작한다 | 목록·상세·작성·수정·삭제 + 회원 기능이 함께 동작 |

### 특목고 연결 (오늘 심을 한 문장)

> 지난주는 "누구나 글을 쓸 수 있는" 게시판이었다. 오늘은 **"누가 썼는지"와 "누가 고칠 수 있는지"**를 코드로 정한다.
> 4주차에 배운 Permission(「이 행동을 해도 될까?」)이 오늘 **로그인·권한 검사**로 실제 코드가 된다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「나만의 BBS — 회원 기능 버전(v1)」**

6주차 `week06-bbs/` 폴더를 **그대로 이어쓴다**. 익명 게시판에 **회원가입·로그인·작성자 표시·본인 글만 수정/삭제**를 추가한다.

**오늘도 2~4장(회원·권한 핵심 기능)은 AI 없이 직접 코드를 작성한다.** AI는 6장(도전 과제)에서만 쓴다.

### 완성 모습 (최소 · 🟢)

| # | 화면/기능 | 최소 내용 |
|---|-----------|-----------|
| 1 | **회원가입** (`GET /signup`, `POST /signup`) | 아이디·비밀번호로 계정 생성, 중복 아이디 거부 |
| 2 | **로그인** (`GET /login`, `POST /login`) | 맞는 계정이면 세션에 `user_id` 저장 |
| 3 | **로그아웃** (`POST /logout`) | 세션 비우고 목록으로 |
| 4 | **작성자 표시** | 목록·상세에 글 작성자 이름(`username`) 표시 |
| 5 | **로그인해야 글쓰기** | 비로그인 시 `/new` 접근하면 로그인 페이지로 |
| 6 | **본인 글만 수정·삭제** | 다른 사람 글에는 수정·삭제 버튼 안 보임 |
| 7 | **DB** | `users` 테이블 + `posts.user_id` (외래키) |

### 폴더 구조 (수업 종료 시 예시)

```
week06-bbs/                        ← 6주차 폴더를 이어씀
├── app.py                         ← 회원·권한 라우트 추가
├── bbs.db
├── templates/
│   ├── list.html                  ← 작성자·로그인 상태 표시
│   ├── detail.html                ← 본인 글만 수정/삭제 버튼
│   ├── new.html
│   ├── edit.html
│   ├── signup.html                ← 신규
│   └── login.html                 ← 신규
└── notes/
    ├── session-auth.md            ← 세션·권한 흐름 그림
    └── why-auth.md                ← 왜 회원 기능을 넣었는가 회고
```

### 성공 기준 (🟢)
1. 회원가입 → 로그인 → 글쓰기 → 로그아웃 흐름이 동작한다
2. 비로그인 상태에서 `/new`에 가면 로그인 페이지로 보낸다
3. A 계정이 쓴 글을 B 계정으로는 수정·삭제할 수 없다
4. 서버를 껐다 켜도 계정·글이 DB에 남아 있다

---

## 4시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:25 | A | 0 · 1 | Week6 회고 · "왜 회원 기능이 필요한가" |
| 0:25~1:25 | B | 2 · 3 | 🟢 `users` 테이블 · 회원가입·로그인·로그아웃 (AI 없이) |
| 1:25~1:40 | — | — | 휴식 |
| 1:40~2:50 | C | 4 · 5 | 🟢 작성자 연결 · 로그인 필수 · 본인 글만 수정/삭제 (직접) |
| 2:50~3:00 | — | — | 휴식 |
| 3:00~3:45 | D | 6 · 7 | 🟡 상단 네비 직접 꾸미기 · 🔴 AI 도전(댓글 등) |
| 3:45~4:00 | E | 8 | 발표 · 회고 · Week8 예고 |

---

# 본문 — 챕터별 상세

---

## 0. Week6에서 이어가기

### 0.1. 60초 복습 퀴즈 (구두)

1. 지난주 만든 5기능은? → **목록·상세·작성·수정·삭제**
2. `?` 파라미터를 쓰는 이유는? → **SQL Injection 방지**
3. 6주차 Non-goals에 있던 것 중 하나는? → **로그인·회원가입** — 오늘 한다

### 0.2. 오늘 문제 제기

> 지난주 BBS는 **누가 썼는지 모르고**, **아무나 아무 글이나 고칠 수 있다.**
> 실제 커뮤니티·학교 게시판이라면 어떻게 해야 할까?

- 글을 쓰려면 **로그인**해야 한다
- 수정·삭제는 **본인 글만** 가능해야 한다
- 비밀번호는 DB에 **평문으로 저장하면 안 된다**

오늘은 6주차 BBS 위에 이 세 가지를 **직접 코드로** 얹는다.

### 0.3. 오늘 한 문장 목표 (학생 작성)

예시:
> 「회원가입·로그인을 만들고, 내가 쓴 글만 고칠 수 있는 게시판으로 업그레이드한다.」

---

## 1. 왜 회원 기능이 필요한가

### 1.1. 6주차 vs 오늘

| 6주차 (v0) | 오늘 (v1) |
|------------|-----------|
| 익명 글쓰기 | **로그인한 사람만** 글쓰기 |
| 작성자 불명 | 목록·상세에 **작성자 이름** |
| 누구나 수정·삭제 | **본인 글만** 수정·삭제 |
| `posts` 테이블만 | `users` + `posts.user_id` **관계** |

### 1.2. 4주차 Permission과 연결

4주차에서 Permission은 **「이 행동을 해도 될까?」를 묻는 안전장치**였다.
오늘 코드에서 그 질문은 이렇게 바뀐다:

```python
# 글을 쓸 수 있나?
if "user_id" not in session:
    return redirect(url_for("login"))

# 이 글을 고칠 수 있나?
if post["user_id"] != session["user_id"]:
    return "권한 없음", 403
```

### 1.3. 오늘 배우는 3개 키워드

| 키워드 | 한 줄 |
|--------|------|
| **인증(Authentication)** | "너 누구야?" — 로그인으로 확인 |
| **인가(Authorization)** | "너 이거 해도 돼?" — 본인 글만 수정/삭제 |
| **세션(Session)** | 로그인 상태를 서버가 **기억**하는 방법 |

### 1.4. 오늘 하지 않는 것 (Non-goals)

- 이메일 인증·비밀번호 찾기
- OAuth(구글/카카오 로그인)
- JWT·토큰 기반 API 인증 (세션만)
- bcrypt 등 복잡한 해시 (Flask `werkzeug` 기본 해시로 충분)

---

## 2. DB 설계 — `users` 테이블과 관계

### 2.1. `users` 테이블

| 컬럼 | 타입 | 의미 |
|------|------|------|
| `id` | INTEGER (자동증가) | 사용자 고유 번호 |
| `username` | TEXT (UNIQUE) | 로그인 아이디 |
| `password_hash` | TEXT | **해시된** 비밀번호 (평문 저장 금지) |
| `created_at` | TEXT | 가입 시각 |

### 2.2. `posts` 테이블 변경

6주차 `posts`에 **`user_id`** 컬럼을 추가한다.

| 컬럼 | 타입 | 의미 |
|------|------|------|
| `user_id` | INTEGER | 이 글을 쓴 사용자 (`users.id` 참조) |

> **관계:** 한 사용자(`users`)가 여러 글(`posts`)을 쓸 수 있다 — **1 : N**

### 2.3. 함께 따라하기 — 테이블 생성/마이그레이션

기존 `bbs.db`에 글이 있다면, `posts`에 `user_id`를 **ALTER TABLE**로 추가한다.
(새로 시작하는 학생은 `CREATE TABLE`에 처음부터 넣어도 된다.)

```python
def create_tables():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    # 기존 DB에 user_id 컬럼이 없으면 추가 (한 번만 실행됨)
    try:
        conn.execute("ALTER TABLE posts ADD COLUMN user_id INTEGER")
    except sqlite3.OperationalError:
        pass  # 이미 있으면 무시
    conn.commit()
    conn.close()
```

---

## 3. 회원가입·로그인·로그아웃 (🟢, AI 없이)

### 3.1. Flask 세션 준비

```python
from flask import Flask, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
```

`secret_key`는 세션 데이터를 **암호화·서명**하는 열쇠다. 실제 배포 시에는 환경 변수로 바꾼다.

### 3.2. 회원가입

```python
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            return render_template("signup.html", error="아이디와 비밀번호를 입력하세요.")

        password_hash = generate_password_hash(password)
        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("signup.html", error="이미 사용 중인 아이디입니다.")
        conn.close()
        return redirect(url_for("login"))

    return render_template("signup.html")
```

### 3.3. 로그인 · 로그아웃

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("index"))

        return render_template("login.html", error="아이디 또는 비밀번호가 틀립니다.")

    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))
```

**직접 확인해보기:**
- `generate_password_hash`와 `check_password_hash`는 **쌍**이다 — 저장할 때 hash, 로그인할 때 compare
- DB에 `password`가 아니라 `password_hash`만 있는지 확인
- 로그인 후 `session["username"]`이 템플릿에서 쓸 수 있는지 확인

### 3.4. 템플릿 — `signup.html` · `login.html`

`new.html`과 같은 폼 패턴이다. `error`가 있으면 화면에 보여 준다.

```html
<!-- signup.html 예시 -->
<h1>회원가입</h1>
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}
<form method="POST">
  <input name="username" placeholder="아이디" required><br>
  <input name="password" type="password" placeholder="비밀번호" required><br>
  <button type="submit">가입</button>
</form>
<a href="/login">로그인</a>
```

---

## 4. 글에 작성자 연결하기 (🟢, 직접)

### 4.1. 글 작성 시 `user_id` 저장

6주차 `create_post`를 바꾼다 — **로그인한 사용자 id**를 함께 INSERT.

```python
@app.route("/posts", methods=["POST"])
def create_post():
    if "user_id" not in session:
        return redirect(url_for("login"))

    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    conn = get_db()
    conn.execute(
        "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)",
        (title, content, session["user_id"])
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

### 4.2. 목록·상세에 작성자 이름 JOIN

```python
@app.route("/")
def index():
    conn = get_db()
    posts = conn.execute("""
        SELECT posts.*, users.username
        FROM posts
        LEFT JOIN users ON posts.user_id = users.id
        ORDER BY posts.id DESC
    """).fetchall()
    conn.close()
    return render_template("list.html", posts=posts)
```

`list.html`에서 `{{ post.username or "익명" }}`처럼 표시한다.
(6주차에 만든 글은 `user_id`가 NULL일 수 있어 `익명`으로 처리.)

---

## 5. 권한 — 로그인 필수 · 본인 글만 수정/삭제 (🟢, 직접)

### 5.1. 로그인해야 글쓰기

```python
@app.route("/new")
def new_form():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("new.html")
```

### 5.2. 본인 글만 수정·삭제 버튼 보이기

`detail.html` — **템플릿에서** 버튼 노출을 제어:

```html
{% if session.get("user_id") == post.user_id %}
  <a href="/posts/{{ post.id }}/edit">수정</a>
  <form method="POST" action="/posts/{{ post.id }}/delete" style="display:inline">
    <button type="submit">삭제</button>
  </form>
{% endif %}
```

### 5.3. 서버에서도 권한 검사 (중요)

화면에서 버튼을 숨겨도, URL을 직접 치면 우회할 수 있다. **라우트 안에서도** 검사한다.

```python
def get_post_or_404(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT posts.*, users.username FROM posts "
        "LEFT JOIN users ON posts.user_id = users.id "
        "WHERE posts.id = ?", (post_id,)
    ).fetchone()
    conn.close()
    return post

def require_owner(post):
    if post is None:
        return "글 없음", 404
    if post["user_id"] != session.get("user_id"):
        return "권한 없음", 403
    return None

@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit_form(post_id):
    post = get_post_or_404(post_id)
    err = require_owner(post)
    if err:
        return err
    # ... 기존 수정 로직 ...
```

**직접 확인해보기:**
- A로 로그인해 글 작성 → B로 로그인 → A 글 URL에 `/edit` 직접 입력 → **403** 또는 로그인 페이지
- "화면에서 숨김"과 "서버에서 막음" **둘 다** 필요한 이유를 한 문장으로 설명

### 5.4. 검증 체크리스트

- [ ] 회원가입 → 로그인 → 상단(또는 목록)에 내 아이디 표시
- [ ] 로그아웃 후 글쓰기 버튼/링크 동작 변화
- [ ] 새 글에 작성자 이름이 목록·상세에 표시
- [ ] 다른 사람 글에는 수정·삭제 버튼 없음
- [ ] URL 직접 입력으로도 남의 글 수정 불가
- [ ] 6주차 글(익명)은 목록에 그대로 보임

---

## 6. 🟡 상단 네비 · 로그인 상태 표시 (직접, AI 없이)

모든 템플릿 `<body>` 위쪽에 공통으로 넣을 **미니 네비**를 직접 작성한다.

```html
<nav>
  {% if session.get("username") %}
    <span>{{ session.username }}님</span>
    <form method="POST" action="/logout" style="display:inline">
      <button type="submit">로그아웃</button>
    </form>
    <a href="/new">글쓰기</a>
  {% else %}
    <a href="/login">로그인</a>
    <a href="/signup">회원가입</a>
  {% endif %}
  <a href="/">목록</a>
</nav>
```

> 나중에 `templates/base.html` + `{% extends %}`로 빼는 것은 🔴 도전 과제 아이디어.

---

## 7. 🔴 도전 과제 — AI와 함께 기능 확장

핵심 회원·권한 기능이 끝난 뒤에만 AI를 쓴다.

### 7.1. AI에게 요청하는 기본 틀 (Plan 먼저)

```
목표: 오늘 만든 BBS(v1)에 (내가 상상한 기능)을 추가한다.

제약:
- 회원가입·로그인·본인 글만 수정/삭제는 그대로 유지
- app.py, templates/ 안에서만 수정

먼저 계획만 제안해줘: 어떤 테이블/라우트/파일이 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

### 7.2. 예시 아이디어 — 댓글

```
목표: 글 상세 페이지에 댓글을 달 수 있게 한다.
comments 테이블(id, post_id, user_id, content, created_at).
로그인한 사용자만 댓글 작성. 본인 댓글만 삭제.
```

### 7.3. 예시 아이디어 — 내가 쓴 글만 보기

```
목표: 목록에 "전체 / 내 글" 탭을 추가한다.
GET /?mine=1 이면 session.user_id 글만 필터.
```

### 7.4. 예시 아이디어 — `base.html`로 네비 공통화

```
목표: 모든 페이지의 nav를 templates/base.html 한 곳으로 모은다.
Jinja {% extends "base.html" %} {% block content %} 패턴 사용.
```

---

## 8. 정리 · 공유 · 다음 주

### 8.1. 30~60초 공유 스크립트

```
6주차 BBS에 ○○(회원/권한)을 추가했습니다.
로그인하면 ○○, 다른 사람 글은 ○○할 수 없습니다.
Permission을 코드로 넣은 부분은 ○○입니다.
```

### 8.2. `notes/session-auth.md` 작성

```markdown
# 세션·권한 흐름

(로그인 → session 저장 → 글쓰기/수정 시 검사 그림 또는 순서)

# 오늘 막혔던 점

# 다음에 하고 싶은 것
```

### 8.3. 회고 3줄

```
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

### 8.4. 오늘 배운 것 체크

- [ ] 회원가입·로그인·로그아웃
- [ ] 비밀번호 해시 저장
- [ ] Flask `session`
- [ ] `users` ↔ `posts` 관계 (`user_id`)
- [ ] 로그인 필수 · 본인 글만 수정/삭제 (화면 + 서버)

### 8.5. 다음 주 예고 (Week8)

- 공공데이터포털 오픈API 인증키 발급 · `.env` 관리
- `requests`로 외부 API 호출 · JSON 가공
- 오늘 만든 BBS에 **공공데이터 대시보드**를 붙인다

미리 생각해 오기 (숙제 아님):
> 오늘 `/login`·`/signup` 라우트를 추가했는데, 비슷한 폼 페이지가 늘어나면 어떤 불편이 있을까?

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수 · AI 없이 직접 작성)
- [ ] `users` 테이블 + `posts.user_id`
- [ ] 회원가입·로그인·로그아웃
- [ ] 작성자 표시 · 로그인해야 글쓰기
- [ ] 본인 글만 수정·삭제 (템플릿 + 라우트 검사)
- [ ] `notes/session-auth.md`
- [ ] 회고 3줄

### 🟡 (권장 · 직접)
- [ ] 상단 네비에 로그인 상태 표시
- [ ] `signup.html` / `login.html` 최소 스타일

### 🔴 (도전 · 여기서만 AI 사용)
- [ ] 댓글 기능
- [ ] "내 글만 보기" 필터
- [ ] `base.html` 공통 레이아웃

### 제출
- `app.py` + `templates/` (또는 스크린샷)
- `notes/session-auth.md`
- 회고 3줄

---

## 교사 메모

### 진행 팁
- **2~5장도 AI 없이 진행** — 6주차와 같은 원칙. 회원·권한은 "손으로 한 번 짜 봐야" 세션·JOIN·if 검사가 몸에 남는다.
- `werkzeug.security`는 Flask에 포함 — 별도 pip 설치 불필요.
- 기존 6주차 `posts` 데이터가 있으면 `user_id` NULL → 화면에서 "익명" 처리로 충돌을 줄인다.
- **403 vs redirect:** 본인 아닌 글 수정 시 403 문자열 대신 목록으로 redirect + flash 메시지도 가능 — 시간 되면 🟡.
- 비밀번호 해시는 "왜 평문 저장하면 안 되는지" **한 문장**만 — 레인보우 테이블 등은 깊게 X.
- **시간 내에 회원·권한을 못 끝낸 학생:** 수업 종료 직전에 [starters/reference/week07-complete/](../starters/reference/week07-complete/)의 `app.py`·`templates/`를 **따라잡기용으로 전달**하고 자기 코드를 덮어써서라도 8주차를 같은 상태에서 시작하게 한다. 다음 주 대시보드는 오늘 만든 `session`·권한 구조 위에 그대로 얹이므로, 여기서 완전히 막히면 8주차 전체가 밀린다.

### 설명용 한 장 요약 (칠판)

```
회원가입 → users 테이블 (password_hash)
로그인   → session["user_id"] 저장
글쓰기   → posts.user_id = session["user_id"]
수정/삭제 → post.user_id == session["user_id"] ?

오늘 결과 → BBS v1 (회원 + 권한)
다음 → 공공데이터 API · 대시보드 (Week8)
```

### FAQ

**Q. `secret_key`를 뭐라고 적어야 하나요?**
A. 수업용은 `"dev-only-change-me"`로 충분. "실제 서비스에서는 남에게 보이면 안 되는 값"이라고만 설명.

**Q. 6주차에 쓴 글이 author 없이 보여요.**
A. `LEFT JOIN` + `username or "익명"` 처리. 필요하면 교사가 테스트용 user 하나 만들어 UPDATE.

**Q. 로그인해도 session이 안 남아요.**
A. `app.secret_key` 설정 여부, 브라우저 쿠키 차단, `session.clear()` 실수 확인.

**Q. 디자인 패턴(MVC·DI)은 언제 배우나요?**
A. [보충_아키텍처기초](../docs/2026진학반_보충_아키텍처기초.docx) 또는 캡스톤 전후에 선택적으로 다룬다. 7주차는 **기능 업그레이드**에 집중.

---

## 부록 A — 학생용 프롬프트 치트시트 (7장 도전 과제 전용)

```
[기본 틀]
목표: BBS v1에 (기능) 추가.
제약: 회원·권한 기능 유지. app.py, templates/만.
먼저 계획만 제안해줘.

[댓글 🔴]
comments 테이블 + 상세 페이지 댓글 목록/작성/본인 삭제.

[내 글만 🔴]
GET /?mine=1 필터.

[base.html 🔴]
{% extends %} 로 nav 공통화.
```

---

## 부록 B — 트러블슈팅 표

| 증상 | 원인(대개) | 대응 |
|------|-----------|------|
| `IntegrityError` on signup | 아이디 중복 | 에러 메시지 표시 확인 |
| 로그인해도 글쓰기 불가 | session 키 이름 불일치 | `user_id` vs `userId` 등 통일 |
| 남의 글 수정됨 | 라우트에 `require_owner` 없음 | update/delete에도 검사 추가 |
| JOIN 결과 username None | user_id NULL (구 글) | `or "익명"` 또는 마이그레이션 |
| `ModuleNotFoundError: werkzeug` | Flask 미설치 | `pip install flask` |

---

## 다음 주 (Week08)로 이어지는 다리

오늘로 **회원·권한이 있는 BBS v1**까지 만들었다.
다음 주는 이 BBS에 **공공데이터 API·대시보드**를 붙여, 외부 데이터를 가져와 가공·시각화하는 법을 배운다.
