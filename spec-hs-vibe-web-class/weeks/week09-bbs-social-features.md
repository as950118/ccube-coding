# 9주차 — BBS 확장: 댓글 · 검색 · 권한(RBAC) · 실시간 채팅

**Phase:** 입문(재설계) | **소요:** 4시간
**대상:** 특목고 진학 준비 중학생
**원본 대응:** 인프런 원본 매핑 없음 — 6~8주차에 이어지는 **자체 재설계 트랙**(BBS·웹 아키텍처)
**선수:** 8주차 — BBS v2(회원가입·로그인·권한·공공데이터 대시보드) 완성

---

## 오늘의 목표

오늘이 끝나면 학생은 아래를 **말로 설명**하고 **손으로 실행**할 수 있어야 한다.

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | 브라우저-서버 **요청/응답 사이클**을 자기 코드로 설명한다 | "댓글 쓰기 버튼을 누르면 무슨 일이 일어나?"에 순서대로 답함 |
| 2 | 게시글에 **댓글**을 달고, DB에서 **1:N 관계**로 저장한다 | 한 글에 댓글 여러 개, `comments.post_id`로 연결 |
| 3 | **검색**으로 원하는 글을 찾는다 | `/?q=키워드` 접속 시 제목·내용에 키워드가 있는 글만 보임 |
| 4 | **권한(RBAC)** — 일반 계정과 관리자 계정이 다른 일을 할 수 있게 만든다 | 관리자만 남의 글 삭제·공지 고정 가능 |
| 5 | **실시간(WebSocket)**과 기존 요청/응답 방식의 차이를 체험한다 | 새로고침 없이 채팅 메시지가 화면에 뜸 |
| 6 | 실시간 채팅은 **AI와 함께** 구현하며, AI가 만든 코드를 읽고 설명할 수 있다 | 소켓 이벤트(`send_message`/`new_message`) 흐름을 손으로 짚어 설명 |
| 7 | 8주차까지의 기능이 오늘 추가 후에도 그대로 동작한다 | 목록·상세·작성·수정·삭제·회원·권한·대시보드가 함께 동작 |

### 특목고 연결 (오늘 심을 한 문장)

> 지금까지는 "글을 쓰고 고치는" 게시판이었다. 오늘은 **사람과 사람이 상호작용하는** 커뮤니티로 한 단계 올라간다 —
> 댓글은 「글에 반응하기」, 검색은 「원하는 정보 찾기」, 권한은 「역할에 따라 할 수 있는 일이 다르기」, 채팅은 「실시간으로 연결되기」다.
> 넷 다 우리가 매일 쓰는 서비스(SNS·커뮤니티·학교 알림)의 핵심 구조이며, 오늘은 그 구조를 코드로 직접 만든다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「나만의 BBS — 커뮤니티 버전(v3)」**

8주차 BBS(회원·권한·공공데이터 대시보드가 있는 게시판)를 **그대로 이어쓴다**. 댓글·검색·관리자 권한·실시간 채팅 4가지를 추가한다.

### 오늘 진행 방식 — "개념 하나 → 기능 하나"

오늘은 4개 기능을 하나씩 순서대로 만든다. 매 기능마다 **① 관련 개념을 5~10분 안에 압축 설명 → ② 바로 그 자리에서 구현**하는 미션 방식으로 진행한다. 설명만 듣는 시간을 최소화하고, 배운 것을 즉시 자기 코드에 적용해 눈으로 확인하는 데 집중한다.

**댓글·검색·권한(2~4장)은 AI 없이 직접 코드를 작성한다.** 실시간 채팅(5장)은 지금까지와 완전히 다른 개념(WebSocket)이 새로 필요하므로, **AI와 함께 구현하는 도전 과제**로 진행한다 — AI가 짜주는 코드를 그대로 복붙하지 않고, 무슨 일이 일어나는지 설명할 수 있어야 한다.

### 완성 모습 (🟢🟡🔴)

| # | 기능 | 난이도 | 최소 내용 |
|---|------|--------|-----------|
| 1 | **댓글** | 🟢 | 글 상세 페이지에서 댓글 작성·목록·삭제(본인/관리자) |
| 2 | **검색** | 🟢 | 목록 상단 검색창 → 제목/내용에 키워드 포함된 글만 표시 |
| 3 | **권한(RBAC)** | 🟡 | 관리자 계정은 남의 글/댓글 삭제, 공지 고정 가능 |
| 4 | **실시간 채팅** | 🔴 (AI 도전) | `/chat`에서 새로고침 없이 메시지 송수신 |

### 폴더 구조 (수업 종료 시 예시)

```
week06-bbs/                        ← 6~8주차 폴더를 이어씀
├── app.py                         ← 댓글·검색·권한·채팅 라우트 추가
├── make_admin.py                  ← 신규: 특정 계정을 관리자로 바꾸는 1회성 스크립트
├── opendata.py
├── bbs.db
├── requirements.txt                ← flask-socketio 추가
├── templates/
│   ├── list.html                  ← 검색창, 공지 고정 표시 추가
│   ├── detail.html                ← 댓글 목록·입력 폼, 관리자 삭제/공지 버튼 추가
│   ├── new.html / edit.html
│   ├── signup.html / login.html
│   ├── dashboard.html
│   └── chat.html                  ← 신규: 실시간 채팅 화면
└── notes/
    ├── db-relations.md            ← 신규: 댓글 1:N 관계 워크시트
    ├── rbac-notes.md              ← 신규: 권한 분기표(비로그인/일반/관리자)
    ├── why-social-features.md     ← 신규: 회고
    └── realtime-log.md            ← 신규: AI와 만든 채팅 기록
```

### 성공 기준 (🟢🟡)
1. 로그인한 사용자가 글에 댓글을 달고, 다른 계정으로 보면 그 댓글이 보인다
2. 본인 댓글만 삭제 버튼이 보인다 (관리자는 전부 보임)
3. `/?q=키워드`로 제목·내용을 검색하면 해당하는 글만 목록에 남는다
4. `make_admin.py`로 관리자로 바꾼 계정은 남의 글·댓글을 삭제하고 공지를 고정/해제할 수 있다
5. 일반 계정은 여전히 본인 글만 수정·삭제할 수 있다 (기존 권한 유지)
6. 6~8주차 기능(CRUD·회원·권한·대시보드)이 오늘 추가 후에도 그대로 동작한다

---

## 4시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:20 | A | 0 · 1 | Week8 회고 · 오늘 미션 소개 · 요청/응답 사이클 압축 설명 |
| 0:20~1:10 | B | 2 | 🟢 댓글 — DB 1:N 관계 · 라우트 · 화면 (직접) |
| 1:10~1:20 | — | — | 휴식 |
| 1:20~2:00 | C | 3 | 🟢 검색 — 쿼리스트링 · SQL LIKE (직접) |
| 2:00~2:45 | D | 4 | 🟡 권한(RBAC) — 관리자 계정 · 삭제/공지 권한 확장 (직접) |
| 2:45~2:55 | — | — | 휴식 |
| 2:55~3:45 | E | 5 | 🔴 AI 도전 — 실시간 채팅(WebSocket) |
| 3:45~4:00 | F | 6 | 발표 · 회고 · Week10 예고 |

---

# 본문 — 챕터별 상세

---

## 0. Week8에서 이어가기

### 0.1. 60초 복습 퀴즈 (구두)

1. 8주차에 추가한 것은? → **공공데이터 API 대시보드**
2. API 호출이 실패해도 화면이 죽지 않게 한 방법은? → **샘플 데이터로 대체(예외처리)**
3. 인증(Authentication)과 인가(Authorization)의 차이는? → **누구인지 확인 / 이 행동을 해도 되는지 확인**

### 0.2. 오늘 문제 제기

> 지금까지 BBS는 "혼자 쓰고 혼자 고치는" 게시판이었다. 다른 사람 글에 **반응**할 방법이 없고, 글이 많아지면 원하는 글을 **찾을** 방법이 없고, 모든 회원이 **똑같은 권한**만 가지고 있고, 실시간으로 **대화**할 방법도 없다.
> 오늘은 이 네 가지 — 댓글·검색·권한·실시간 — 를 하나씩 추가해서, 진짜 커뮤니티에 가까운 게시판으로 만든다.

### 0.3. 오늘 한 문장 목표 (학생 작성)

예시:
> 「게시판에 댓글과 검색을 달고, 관리자 계정을 만들고, 실시간 채팅방을 추가한다.」

---

## 1. 오늘 배우는 개념 압축 강의 (10분)

### 1.1. 요청/응답 사이클 — 우리가 이미 쓰고 있던 구조

지금까지 만든 모든 기능(목록·상세·글쓰기·로그인)은 사실 전부 같은 패턴이었다.

```
① 브라우저가 서버에 요청(request)을 보낸다   — 예: "POST /posts/3/comments"
② 서버(Flask)가 요청을 받아 코드를 실행한다   — 예: DB에 댓글 INSERT
③ 서버가 응답(response)을 돌려준다           — 예: "상세 페이지로 이동해"
④ 브라우저가 응답을 받아 화면을 다시 그린다    — 예: 새 페이지 로딩, 댓글이 보임
```

오늘 만들 댓글·검색·권한 기능도 전부 이 4단계다. 다만 5장의 실시간 채팅만 예외 — 이 사이클을 깨고 **서버가 먼저 브라우저에 말을 거는** 새로운 방식(WebSocket)을 쓴다. (5장에서 자세히 다룬다.)

### 1.2. 오늘 배우는 4개 키워드

| 키워드 | 한 줄 |
|--------|------|
| **1:N 관계** | 글 하나에 댓글 여러 개가 달릴 수 있는 DB 구조 (`comments.post_id`가 `posts.id`를 가리킴) |
| **쿼리스트링** | URL 뒤에 붙는 `?key=value` — 검색어·필터 조건을 서버에 전달하는 방법 |
| **RBAC(역할 기반 접근 제어)** | 사용자를 "역할(role)"로 나누고, 역할마다 할 수 있는 일을 다르게 정하는 방식 |
| **WebSocket** | 브라우저-서버가 요청 없이도 **양방향으로 계속 연결**되어 있는 통신 방식 |

### 1.3. 오늘 하지 않는 것 (Non-goals)

- 댓글 대댓글(계층형 댓글) — 오늘은 **1단계 댓글**만
- 검색어 자동완성·형태소 분석 — 오늘은 **단순 LIKE 검색**만
- 회원가입 화면에서 "관리자로 가입" 같은 옵션 — 관리자는 **교사가 스크립트로 승격**
- 채팅 다중 방(room) 나누기, 귓속말, 파일 전송 — 오늘은 **채팅방 1개**만
- 채팅 메시지 암호화·삭제·신고 기능

---

## 2. 댓글 — DB 1:N 관계 (🟢, 직접)

### 2.1. `comments` 테이블 설계

| 컬럼 | 타입 | 의미 |
|------|------|------|
| `id` | INTEGER (자동증가) | 댓글 고유 번호 |
| `post_id` | INTEGER | 이 댓글이 달린 글 (`posts.id` 참조) |
| `user_id` | INTEGER | 이 댓글을 쓴 사용자 (`users.id` 참조) |
| `content` | TEXT | 댓글 내용 |
| `created_at` | TEXT | 작성 시각 |

> **관계:** 글 하나(`posts`)에 댓글 여러 개(`comments`)가 달릴 수 있다 — **1 : N**. 7주차에 배운 `users`-`posts` 관계와 똑같은 모양이다.

### 2.2. 테이블 생성 코드

```python
def create_tables():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user',
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER,
            is_notice INTEGER NOT NULL DEFAULT 0,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            user_id INTEGER,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (post_id) REFERENCES posts(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    # 8주차까지 없던 컬럼을 이어쓰는 DB에 추가 (한 번만 실행됨, 이미 있으면 조용히 넘어감)
    for statement in [
        "ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'user'",
        "ALTER TABLE posts ADD COLUMN is_notice INTEGER NOT NULL DEFAULT 0",
    ]:
        try:
            conn.execute(statement)
        except sqlite3.OperationalError:
            pass
    conn.commit()
    conn.close()
```

> `role`·`is_notice` 컬럼을 여기서 미리 추가해 두는 이유: 4장(권한)에서 바로 쓰기 위해서다. 지금은 값만 준비해 두고, 실제로 사용하는 코드는 4장에서 작성한다.

### 2.3. 댓글 작성·삭제 라우트

```python
@app.route("/posts/<int:post_id>/comments", methods=["POST"])
def create_comment(post_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    content = request.form.get("content", "").strip()
    if not content:
        return redirect(url_for("detail", post_id=post_id))

    conn = get_db()
    conn.execute(
        "INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)",
        (post_id, session["user_id"], content)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("detail", post_id=post_id))


@app.route("/comments/<int:comment_id>/delete", methods=["POST"])
def delete_comment(comment_id):
    conn = get_db()
    comment = conn.execute("SELECT * FROM comments WHERE id = ?", (comment_id,)).fetchone()
    if comment is None:
        conn.close()
        return "댓글 없음", 404

    is_owner = comment["user_id"] == session.get("user_id")
    is_admin = session.get("role") == "admin"
    if not (is_owner or is_admin):
        conn.close()
        return "권한 없음", 403

    conn.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("detail", post_id=comment["post_id"]))
```

### 2.4. `detail` 라우트 — 댓글 함께 불러오기

```python
@app.route("/posts/<int:post_id>")
def detail(post_id):
    post = get_post_or_404(post_id)
    if post is None:
        return "글 없음", 404

    conn = get_db()
    comments = conn.execute("""
        SELECT comments.*, users.username
        FROM comments
        LEFT JOIN users ON comments.user_id = users.id
        WHERE comments.post_id = ?
        ORDER BY comments.id ASC
    """, (post_id,)).fetchall()
    conn.close()

    return render_template("detail.html", post=post, comments=comments)
```

### 2.5. `templates/detail.html` — 댓글 영역 추가

기존 상세 화면(`{{ post.content }}` 아래)에 추가한다.

```html
<hr>
<h2>댓글 ({{ comments|length }})</h2>
<ul class="comments">
  {% for c in comments %}
  <li>
    <span class="meta">{{ c.username or "익명" }} · {{ c.created_at }}</span>
    <p>{{ c.content }}</p>
    {% if session.get("user_id") == c.user_id or session.get("role") == "admin" %}
    <form method="POST" action="/comments/{{ c.id }}/delete" style="display:inline">
      <button class="delete" type="submit">삭제</button>
    </form>
    {% endif %}
  </li>
  {% else %}
  <li>아직 댓글이 없습니다.</li>
  {% endfor %}
</ul>

{% if session.get("user_id") %}
<form method="POST" action="/posts/{{ post.id }}/comments">
  <textarea name="content" placeholder="댓글을 입력하세요" required></textarea>
  <button type="submit">댓글 작성</button>
</form>
{% else %}
<p><a href="/login">로그인</a>하면 댓글을 쓸 수 있습니다.</p>
{% endif %}
```

### 2.6. 검증 체크리스트

- [ ] 로그인 후 댓글을 작성하면 상세 페이지에 바로 보인다
- [ ] 비로그인 상태에서는 댓글 입력창 대신 로그인 안내가 보인다
- [ ] 본인이 쓴 댓글에만 삭제 버튼이 보인다
- [ ] 게시글을 삭제해도 서버가 죽지 않는다 (댓글이 남아 있어도 오류 없이 동작 — 오늘은 연쇄 삭제까지는 하지 않는다)

---

## 3. 검색 — 쿼리스트링과 SQL LIKE (🟢, 직접)

### 3.1. 쿼리스트링이란

URL 뒤에 `?q=파이썬`처럼 붙는 부분이다. 폼(`<form method="GET">`)을 GET으로 제출하면 브라우저가 자동으로 이 형태로 만들어 서버에 보낸다. 6주차에 배운 "`?` 파라미터로 SQL Injection을 막는다"의 `?`와는 **다른 것**이니 헷갈리지 않도록 짚고 넘어간다 — 저건 SQL 쿼리 안의 자리표시자, 이건 URL의 쿼리스트링이다.

### 3.2. `index` 라우트에 검색 추가

```python
@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    conn = get_db()

    if q:
        keyword = f"%{q}%"
        posts = conn.execute("""
            SELECT posts.*, users.username
            FROM posts
            LEFT JOIN users ON posts.user_id = users.id
            WHERE posts.title LIKE ? OR posts.content LIKE ?
            ORDER BY posts.is_notice DESC, posts.id DESC
        """, (keyword, keyword)).fetchall()
    else:
        posts = conn.execute("""
            SELECT posts.*, users.username
            FROM posts
            LEFT JOIN users ON posts.user_id = users.id
            ORDER BY posts.is_notice DESC, posts.id DESC
        """).fetchall()

    conn.close()
    return render_template("list.html", posts=posts, q=q)
```

> `posts.is_notice DESC`를 정렬에 넣은 이유: 4장에서 만들 "공지 고정" 글이 검색 결과에서도 위에 오도록 미리 넣어 둔다.

**직접 확인해보기:**
- `f"%{q}%"`처럼 문자열을 **미리 만든 다음** `?` 자리에 넣는 이유는? → SQL문 자체를 문자열로 이어붙이면(`"...LIKE '%" + q + "%'"`) SQL Injection에 노출된다. `?`에 값만 넘기면 sqlite3가 안전하게 처리한다.

### 3.3. `templates/list.html` — 검색창 추가

```html
<form method="GET" action="/" class="search">
  <input type="text" name="q" value="{{ q or '' }}" placeholder="제목·내용 검색">
  <button type="submit">검색</button>
  {% if q %}<a href="/">전체보기</a>{% endif %}
</form>
```

### 3.4. 검증 체크리스트

- [ ] `/?q=` + 실제 글에 있는 단어로 검색하면 해당 글만 남는다
- [ ] 검색 결과가 없으면 "글이 없습니다" 문구가 보인다 (에러가 아니라)
- [ ] 검색창을 비우고 다시 제출하면 전체 글이 보인다
- [ ] 검색 중에도 댓글·글쓰기 등 기존 기능이 그대로 동작한다

---

## 4. 권한(RBAC) — 관리자 계정 만들기 (🟡, 직접)

### 4.1. 지금까지의 권한 vs 오늘의 권한

| 7주차까지 | 오늘 |
|-----------|------|
| 로그인 여부만 구분 (인증) | **역할(role)**로 구분 (인가) |
| "내 글인가?"만 검사 | "내 글인가? **또는** 내가 관리자인가?" 검사 |
| 모든 회원이 동등 | `user`(일반) / `admin`(관리자) |

### 4.2. 관리자 계정 만들기 — `make_admin.py`

회원가입 화면에 "관리자로 가입" 버튼을 두지 않는다 — 관리자는 아무나 스스로 될 수 없어야 하기 때문이다. 대신 서버 쪽에서 직접 DB를 고치는 1회성 스크립트를 만든다.

```python
"""
관리자 계정 만들기 — 한 번만 실행.
    python make_admin.py 내아이디
"""
import sqlite3
import sys

if len(sys.argv) < 2:
    print("사용법: python make_admin.py 아이디")
    raise SystemExit(1)

username = sys.argv[1]
conn = sqlite3.connect("bbs.db")
cursor = conn.execute("UPDATE users SET role = 'admin' WHERE username = ?", (username,))
conn.commit()

if cursor.rowcount == 0:
    print(f"'{username}' 계정을 찾을 수 없습니다. 먼저 회원가입하세요.")
else:
    print(f"'{username}' → admin 완료. 로그아웃 후 다시 로그인하면 적용됩니다.")
```

```
python make_admin.py 내아이디
```

> 이미 로그인 중이었다면 `session`에는 예전 역할이 남아 있으므로, **로그아웃 후 다시 로그인**해야 관리자 권한이 화면에 반영된다. (세션이 로그인 시점의 정보를 "기억"만 하고 있기 때문 — 7주차에 배운 세션 개념이 여기서 다시 등장한다.)

### 4.3. 로그인 시 `role`을 세션에 저장

```python
if user and check_password_hash(user["password_hash"], password):
    session["user_id"] = user["id"]
    session["username"] = user["username"]
    session["role"] = user["role"]
    return redirect(url_for("index"))
```

### 4.4. 권한 검사 함수 확장

```python
def require_owner(post):
    """수정: 본인 글만 (관리자도 예외 없음 — 남의 글 내용을 관리자가 마음대로 고치지 않는다)"""
    if post is None:
        return "글 없음", 404
    if post["user_id"] != session.get("user_id"):
        return "권한 없음", 403
    return None


def require_owner_or_admin(post):
    """삭제: 본인 글이거나 관리자면 허용"""
    if post is None:
        return "글 없음", 404
    is_owner = post["user_id"] == session.get("user_id")
    is_admin = session.get("role") == "admin"
    if not (is_owner or is_admin):
        return "권한 없음", 403
    return None


def require_admin():
    if session.get("role") != "admin":
        return "관리자만 가능합니다", 403
    return None
```

`delete_post`만 `require_owner` 대신 `require_owner_or_admin`으로 바꾼다 — **수정은 본인만, 삭제(운영)는 관리자도 가능**하다는 정책을 코드로 표현한 것이다.

```python
@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = get_post_or_404(post_id)
    err = require_owner_or_admin(post)
    if err:
        return err
    ...
```

### 4.5. 공지 고정 — 관리자 전용 기능

```python
@app.route("/posts/<int:post_id>/notice", methods=["POST"])
def toggle_notice(post_id):
    err = require_admin()
    if err:
        return err

    conn = get_db()
    conn.execute("UPDATE posts SET is_notice = 1 - is_notice WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("detail", post_id=post_id))
```

`1 - is_notice`는 0↔1을 뒤집는 트릭이다 (0이면 1, 1이면 0) — 켜져 있으면 끄고, 꺼져 있으면 켠다.

### 4.6. 화면에 관리자 표시 · 버튼 노출

```html
<!-- nav (list.html, detail.html 공통) -->
{% if session.get("username") %}
  <span>{{ session.username }}님{% if session.get("role") == "admin" %} <b>(관리자)</b>{% endif %}</span>
{% endif %}
```

```html
<!-- detail.html의 actions 영역 -->
{% if session.get("role") == "admin" %}
<form method="POST" action="/posts/{{ post.id }}/notice" style="display:inline">
  <button type="submit">{{ "공지 해제" if post.is_notice else "공지 고정" }}</button>
</form>
{% endif %}
```

```html
<!-- list.html — 공지 글 표시 -->
<li>
  {% if post.is_notice %}<span class="notice">📌 공지</span>{% endif %}
  <a href="/posts/{{ post.id }}">{{ post.title }}</a>
  ...
</li>
```

### 4.7. 검증 체크리스트

- [ ] 일반 계정으로는 남의 글에 "삭제" 버튼이 안 보인다 (본인 글만)
- [ ] `make_admin.py`로 관리자로 만든 계정은 남의 글에도 "삭제" 버튼이 보인다
- [ ] 관리자도 남의 글 "수정" 버튼은 안 보인다 (삭제와 수정 권한이 다름을 확인)
- [ ] 관리자가 "공지 고정"을 누르면 목록 맨 위에 📌 표시와 함께 올라온다
- [ ] 일반 계정에는 공지 고정 버튼 자체가 안 보인다

---

## 5. 🔴 AI 도전 — 실시간 채팅 (WebSocket)

### 5.1. 왜 지금까지 방식으로는 "실시간"이 안 되는가

지금까지 만든 모든 기능은 **브라우저가 먼저 물어봐야** 서버가 답한다(요청/응답). 채팅방에서 상대가 메시지를 보냈을 때 내 화면에 바로 뜨려면, 서버가 **먼저** 내 브라우저에 "새 메시지 왔어"라고 말을 걸 수 있어야 한다. 이걸 가능하게 하는 게 **WebSocket**이다 — 한 번 연결되면 브라우저와 서버가 전화하듯 계속 연결된 채로 양쪽에서 아무 때나 메시지를 보낼 수 있다.

| | 지금까지(HTTP 요청/응답) | 오늘(WebSocket) |
|---|---|---|
| 비유 | 편지를 보내고 답장을 기다림 | 전화 통화 — 계속 연결된 채로 대화 |
| 누가 먼저 말하나 | 항상 브라우저가 먼저 | 아무 쪽이나 먼저 가능 |
| 연결 | 요청마다 새로 연결 | 한 번 연결되면 계속 유지 |

### 5.2. 오늘은 왜 AI와 함께 만드나

댓글·검색·권한은 지금까지 배운 "요청→응답→DB" 패턴을 **그대로 반복**하는 것이라 직접 짤 수 있다. 실시간 채팅은 **완전히 새로운 통신 방식**(Flask-SocketIO 라이브러리, 이벤트 기반 코드)이 필요해서, 오늘은 AI의 힘을 빌려 빠르게 완성하고 — 대신 **AI가 만든 코드가 무슨 일을 하는지 한 줄씩 설명할 수 있는 것**을 목표로 한다.

### 5.3. 준비

```
pip install flask-socketio
```

### 5.4. AI에게 요청하는 기본 틀 (Plan 먼저)

댓글·검색·권한(2~4장)이 끝난 뒤에만 진행한다.

```
목표: 이 Flask 게시판(app.py)에 실시간 채팅 기능을 추가하고 싶어.

요구사항:
- flask-socketio를 사용한다
- /chat 라우트: 로그인한 사용자만 접속 가능, 최근 채팅 메시지 30개를 DB에서 불러와 보여준다
- chat_messages 테이블(id, username, content, created_at)에 메시지를 저장한다
- 클라이언트가 send_message 이벤트로 메시지를 보내면,
  서버가 DB에 저장하고 new_message 이벤트로 모든 접속자에게 broadcast한다
- templates/chat.html: socket.io 클라이언트 CDN을 쓰고,
  메시지 목록 + 입력창 + 전송 버튼으로 구성한다
- 기존 라우트(목록/상세/댓글/검색/권한/대시보드)는 건드리지 않는다
- app.run(...) 대신 socketio.run(app, ...)으로 바꿔야 하는 것도 알려줘

먼저 계획만 제안해줘: 어떤 파일이 어떻게 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

### 5.5. AI가 만든 코드에서 반드시 짚고 넘어갈 것

AI가 구현을 마치면, 코드를 그대로 쓰기 전에 아래를 **직접 찾아 표시**한다 (제출물에 포함).

- [ ] `SocketIO(app)`을 어디서 만들었는가?
- [ ] 서버가 메시지를 받는 이벤트 이름은? (`@socketio.on("...")`)
- [ ] 서버가 모든 클라이언트에게 방송하는 코드 줄은 어디인가? (`emit(..., broadcast=True)`)
- [ ] 브라우저 쪽 JS에서 소켓 연결을 만드는 줄은 어디인가? (`io()`)
- [ ] `app.run(...)`이 `socketio.run(app, ...)`으로 바뀌었는가? (안 바꾸면 실시간 기능이 동작하지 않는다)

### 5.6. 참고 — 완성되면 이런 모양이다 (교사·조교 참고용, 학생에게 먼저 보여주지 않는다)

```python
from flask_socketio import SocketIO, emit

socketio = SocketIO(app)

@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db()
    messages = conn.execute(
        "SELECT * FROM chat_messages ORDER BY id DESC LIMIT 30"
    ).fetchall()
    conn.close()
    return render_template("chat.html", messages=list(reversed(messages)))


@socketio.on("send_message")
def handle_send_message(data):
    if "user_id" not in session:
        return
    username = session.get("username", "익명")
    content = (data.get("content") or "").strip()
    if not content:
        return

    conn = get_db()
    conn.execute(
        "INSERT INTO chat_messages (username, content) VALUES (?, ?)",
        (username, content)
    )
    conn.commit()
    conn.close()

    emit("new_message", {"username": username, "content": content}, broadcast=True)


if __name__ == "__main__":
    create_tables()
    # 최신 flask-socketio는 프로덕션 경고 때문에 allow_unsafe_werkzeug=True가 없으면
    # 개발 서버 실행 자체가 막힌다 — 교육용 로컬 실습이므로 켜 둔다.
    socketio.run(app, debug=True, port=5001, allow_unsafe_werkzeug=True)
```

`create_tables()`에도 `chat_messages` 테이블 생성이 함께 추가되어야 한다는 것을 AI 결과물에서 확인한다. `RuntimeError: The Werkzeug web server is not designed to run in production` 에러가 나면 `allow_unsafe_werkzeug=True`가 빠진 것이다.

### 5.7. 검증 체크리스트

- [ ] `/chat` 접속 시 로그인 안 한 상태면 로그인 페이지로 보낸다
- [ ] 두 개의 브라우저(또는 시크릿창)로 각각 접속해서, 한쪽에서 메시지를 보내면 **새로고침 없이** 다른 쪽에도 바로 보인다
- [ ] 서버를 껐다 켜도 이전 메시지 30개가 그대로 보인다 (DB 저장 확인)
- [ ] 5.5의 체크리스트를 채워서 제출한다

---

## 6. 정리 · 공유 · 다음 주

### 6.1. 30~60초 공유 스크립트

```
게시판에 댓글·검색·관리자 권한·실시간 채팅을 추가했습니다.
댓글과 검색은 지금까지 배운 요청/응답 방식 그대로 직접 만들었고,
실시간 채팅은 WebSocket이라는 새로운 방식이 필요해서 AI와 함께 만들었습니다.
```

### 6.2. `notes/db-relations.md` 작성

```markdown
# 댓글 1:N 관계 워크시트

- posts 테이블의 기본키:
- comments 테이블에서 posts를 가리키는 컬럼:
- 글 하나를 지우면 댓글은 어떻게 될까? (오늘 코드 기준으로 직접 확인해서 적기)

# 오늘 막혔던 점

# 다음에 하고 싶은 것
```

### 6.3. `notes/rbac-notes.md` 작성

```markdown
# 권한 분기표

| 상황 | 비로그인 | 일반 회원 | 관리자 |
|------|----------|-----------|--------|
| 글 읽기 | | | |
| 댓글 쓰기 | | | |
| 본인 글 수정 | | | |
| 본인 글 삭제 | | | |
| 남의 글 삭제 | | | |
| 공지 고정 | | | |

(각 칸에 O/X로 채우기)
```

### 6.4. `notes/why-social-features.md` — 회고 3줄

```
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

### 6.5. `notes/realtime-log.md` — AI와 만든 기록

```markdown
# AI에게 준 프롬프트

# AI가 설명한 구조 요약 (SocketIO(app), @socketio.on, emit 등)

# 내가 직접 확인한 것 (5.5 체크리스트)

# 막혔던 점
```

### 6.6. 오늘 배운 것 체크

- [ ] 댓글 — DB 1:N 관계
- [ ] 검색 — 쿼리스트링·SQL LIKE
- [ ] 권한(RBAC) — role 기반 접근 제어
- [ ] 실시간(WebSocket) — 요청/응답과의 차이, AI와 함께 구현

### 6.7. 다음 주 예고 (Week10)

- 오늘까지 6~9주차로 **회원·권한·공공데이터·댓글·검색·RBAC·실시간 채팅**이 있는 BBS(v3)를 완성했다
- 다음 주 초반에 **미니앱(포트폴리오 #2) 주제**를 가볍게 정하고(한 페이지 미니 PRD), 남은 시간에 바로 구현을 시작한다 — 오늘 만든 커뮤니티 기능 경험이 그대로 재료가 된다

미리 생각해 오기 (숙제 아님):
> 오늘 만든 기능(댓글/검색/권한/실시간) 중 하나를 내가 관심 있는 다른 주제의 앱에 옮겨 쓴다면, 어떤 모습일까?

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수 · AI 없이 직접 작성)
- [ ] `comments` 테이블 · 댓글 작성/삭제 라우트 · 화면
- [ ] 검색(`?q=`) — SQL LIKE
- [ ] `notes/db-relations.md` 작성

### 🟡 (권장 · 직접)
- [ ] `role` 컬럼 · `make_admin.py` · 관리자 삭제/공지 권한
- [ ] `notes/rbac-notes.md` 작성

### 🔴 (도전 · AI와 함께)
- [ ] `flask-socketio` 실시간 채팅 (`/chat`)
- [ ] 5.5 체크리스트 채우기
- [ ] `notes/realtime-log.md` 작성

### 제출
- `app.py` (+ `make_admin.py`, `templates/chat.html` 완료 시)
- `notes/db-relations.md` · `notes/rbac-notes.md` · `notes/why-social-features.md`
- (완료 시) `notes/realtime-log.md`

---

## 교사 메모

### 진행 팁
- **2~4장은 AI 없이 진행** — 6~8주차와 같은 원칙. 이 세 기능은 지금까지 배운 패턴의 반복 적용이므로 직접 짜야 체화된다.
- **5장(실시간 채팅)만 예외적으로 AI 사용을 허용**하는 이유를 수업 시작에 명확히 안내한다 — "몰라서 AI를 쓰는 것"과 "새로운 개념이라 AI로 속도를 내고 대신 이해했는지 확인하는 것"의 차이를 강조.
- `role`·`is_notice` 컬럼은 2장(댓글) 단계에서 미리 `create_tables()`에 넣어 둔다 — 4장에서 다시 스키마를 건드리지 않도록 하기 위한 설계이니 순서를 바꾸지 않는다.
- `make_admin.py` 실행 후 **로그아웃→재로그인**을 꼭 시켜본다. 세션에 남은 예전 role 때문에 "권한이 안 바뀌었다"는 질문이 반드시 나온다 — 오히려 세션 개념을 복습할 좋은 기회다.
- 실시간 채팅은 시간이 부족한 반이 많을 것이다. **2~4장까지만 끝나도 오늘 목표는 달성**한 것으로 인정하고, 5장은 다음 시간 시작 전 과제로 남겨도 무방하다.
- Flask 개발 서버로 `flask-socketio`를 쓸 때 `eventlet`/`gevent` 설치가 필요할 수 있다 (`pip install eventlet`) — 수업 전 강사 환경에서 미리 `socketio.run()` 실행까지 확인할 것.

### 설명용 한 장 요약 (칠판)

```
댓글: posts(1) -- comments(N)   [DB 관계]
검색: /?q=키워드 -> WHERE title LIKE ? OR content LIKE ?   [쿼리스트링 + SQL]
권한: users.role ('user'|'admin') -> require_owner_or_admin()   [RBAC]
채팅: 요청/응답 대신 계속 연결 -> socketio.on / emit(broadcast=True)   [WebSocket]

오늘 결과 → BBS v3 (댓글 + 검색 + 관리자 권한 + 실시간 채팅)
다음 → 미니앱 주제 선정(가볍게) + 구현 시작 (Week10)
```

### FAQ

**Q. 관리자로 로그인했는데 삭제 버튼이 안 보여요.**
A. `make_admin.py` 실행 후 로그아웃→재로그인을 안 했을 가능성이 높다. 세션에는 로그인 시점의 role만 저장돼 있다.

**Q. 검색했더니 아무것도 안 나와요.**
A. `LIKE`는 대소문자·띄어쓰기까지 정확히 부분일치해야 한다. `%키워드%`가 제대로 만들어졌는지, 실제 글 제목/내용에 그 단어가 있는지 먼저 확인.

**Q. 댓글은 지웠는데 글을 지우니 오류가 나요.**
A. 오늘 코드는 글 삭제 시 연쇄 삭제(cascade)를 하지 않는다. 관리자 메모 수준의 이슈로 남기고, 원하는 반은 🔴 확장으로 "글 삭제 시 댓글도 함께 삭제"를 AI 도전 과제에 추가해도 좋다.

**Q. 실시간 채팅에서 새로고침해야만 메시지가 보여요.**
A. 클라이언트 JS에서 `socket.on("new_message", ...)` 리스너가 안 걸려 있거나, 서버가 `emit`에 `broadcast=True`를 빠뜨렸을 가능성이 크다. AI에게 "new_message 이벤트를 받는 리스너가 없는 것 같다"고 구체적으로 알려주고 다시 요청한다.

**Q. `ModuleNotFoundError: flask_socketio`**
A. `pip install flask-socketio` 미실행. `requirements.txt`에도 추가했는지 확인.

---

## 부록 A — 학생용 프롬프트 치트시트 (5장 AI 도전 전용)

```
[기본 틀 — 5.4 참고]
목표: 이 Flask 게시판에 flask-socketio로 실시간 채팅(/chat)을 추가한다.
요구사항: 로그인 필요, chat_messages 테이블에 저장, send_message -> new_message broadcast.
기존 라우트는 건드리지 않는다. 먼저 계획만 제안해줘.

[막혔을 때 — 실시간이 안 될 때]
new_message 이벤트를 받는 클라이언트 리스너가 안 보여. socket.on("new_message", ...) 코드가 chat.html에 있는지 확인하고 고쳐줘.

[막혔을 때 — 서버가 안 켜질 때]
app.run(...)을 socketio.run(app, ...)으로 바꿨는지 확인해줘. eventlet이 필요하면 설치 명령도 알려줘.

[확장 아이디어]
채팅 메시지에 "몇 명 접속 중"을 함께 보여주고 싶어. connect/disconnect 이벤트로 접속자 수를 세는 방법을 계획만 제안해줘.
```

---

## 부록 B — 트러블슈팅 표

| 증상 | 원인(대개) | 대응 |
|------|-----------|------|
| 댓글 작성 후 500 에러 | `comments` 테이블 미생성 | `create_tables()`에 댓글 테이블 생성 코드가 있는지, 서버를 재시작했는지 확인 |
| 검색 결과가 항상 전체 글 | `q` 조건 분기 누락 | `if q:` 블록이 실제로 쓰이는지, `request.args.get("q")` 오타 확인 |
| 관리자인데 남의 글 삭제 안 됨 | `require_owner`를 그대로 씀 | `delete_post`에서 `require_owner_or_admin`으로 바꿨는지 확인 |
| 공지 고정이 안 풀림 | `1 - is_notice` 대신 `1`로 고정 대입 | 토글 로직(`1 - is_notice`) 재확인 |
| 채팅이 본인 화면에만 안 보임/두 번 보임 | `emit`에서 `broadcast=True` 빠짐 / 클라이언트가 리스너를 두 번 등록 | emit 옵션 확인, `io()` 연결이 한 번만 생성되는지 확인 |
| socket.io 클라이언트 CDN 버전 불일치 | `flask-socketio` 버전과 프론트 `socket.io.js` 버전이 안 맞음 | AI에게 설치된 `flask-socketio` 버전에 맞는 CDN 버전을 물어보고 교체 |
| `RuntimeError: The Werkzeug web server is not designed to run in production` | 최신 flask-socketio가 개발 서버 직접 실행을 기본 차단 | `socketio.run(app, ..., allow_unsafe_werkzeug=True)` 추가 (교육용 로컬 실습이므로 허용) |

---

## 다음 주(Week10)로 이어지는 다리

오늘로 6~9주차 4주에 걸쳐 **회원·권한·공공데이터·댓글·검색·RBAC·실시간 채팅**까지 갖춘 커뮤니티형 BBS(v3)를 완성했다.
다음 주는 이 경험을 재료 삼아, 학생이 스스로 고른 주제의 **미니앱(포트폴리오 #2)** 구현을 시작한다 — 주제 선정과 최소 계획(미니 PRD)은 가볍게 10주차 초반 30분 안에 끝내고, 남은 시간은 바로 구현에 쓴다.
