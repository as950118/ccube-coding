# 나만의 BBS (v3) — 커뮤니티 버전

Flask + SQLite 게시판에 댓글·검색·관리자 권한(RBAC)·실시간 채팅을 더한 버전입니다.

## 무엇인가요

회원가입·로그인·권한·공공데이터 대시보드(v2)까지 있던 게시판에 댓글·검색·관리자 권한·
실시간 채팅을 추가했습니다. 댓글·검색·권한은 AI 없이 직접 작성했고, 실시간 채팅만 AI와
함께 만들었습니다 — 지금까지와 다른 새 통신 방식(WebSocket)이 필요했기 때문입니다.

## 왜 만들었나요

혼자 쓰고 고치던 게시판을 다른 사람과 상호작용할 수 있는 커뮤니티로 만들어보고 싶었습니다.
댓글로 반응하고, 검색으로 찾고, 관리자와 일반 회원의 역할을 나누고, 실시간으로 대화하는
네 가지 기능이 지금 쓰는 대부분의 서비스에 공통으로 들어있다는 걸 직접 만들며 확인했습니다.

## 어떻게 열어보나요

```
pip install -r requirements.txt
cp .env.example .env
python app.py
```

`http://localhost:5001` 접속.

관리자 계정을 만들려면 회원가입 후:

```
python make_admin.py 내아이디
```

실행하고 **로그아웃 후 다시 로그인**합니다.

## 폴더 구조

```
├── app.py
├── make_admin.py
├── opendata.py
├── data/
│   └── sample_air_quality.json
├── .env.example
├── requirements.txt
├── templates/
│   ├── list.html / detail.html / new.html / edit.html
│   ├── signup.html / login.html
│   ├── dashboard.html
│   └── chat.html
└── notes/
    ├── db-relations.md
    ├── rbac-notes.md
    ├── why-social-features.md
    └── realtime-log.md
```

## 다음에 할 일

- [ ] 댓글 대댓글(답글) 기능
- [ ] 채팅방을 주제별로 여러 개로 나누기
- [ ] 미니앱(포트폴리오 #2) 주제 정하고 구현 시작 (Week10)
