# 클라이언트-서버-DB 구조 (예시)

```
[클라이언트]  --- 요청(Request) --->  [서버(백엔드)]  --- 조회/저장 --->  [DB]
 (브라우저)                              (Flask)                        (SQLite)
              <--- 응답(Response) ---                <--- 결과 ---
```

## 오늘 만든 BBS에서 각 부분은 무엇인가

- 클라이언트(프론트엔드): `templates/list.html`, `templates/detail.html`, `templates/new.html` — 브라우저에 실제로 보이는 화면
- 서버(백엔드): `app.py`의 `index`, `detail`, `new_form`, `create_post`, `delete_post` 라우트 — 요청을 받아 어떤 화면을 보여줄지, DB를 어떻게 다룰지 결정
- DB: `bbs.db`의 `posts` 테이블 — 글 제목·본문·작성 시각이 실제로 저장되는 곳

## 요청 하나를 골라 순서대로 따라가 보기

예: "글쓰기 폼을 제출했을 때"

1. 클라이언트가 `/new` 폼에서 `POST /posts` 요청을 보낸다 (제목·본문 포함)
2. 서버의 `create_post` 라우트가 요청을 받아 값을 꺼낸다 (`request.form.get(...)`)
3. 서버가 DB에 `INSERT INTO posts (...) VALUES (?, ?)` 쿼리를 실행한다
4. 서버가 클라이언트를 `/`(목록)로 리다이렉트해 응답한다 → 새 글이 목록에 보임
