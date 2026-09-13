# BBS 확장 — 댓글·검색·권한(RBAC)·실시간 채팅 (교사 참고 · 완성 예시)

**수업안:** [../../../weeks/week09-bbs-social-features.md](../../../weeks/week09-bbs-social-features.md)

학생용 starter는 [../../week09/](../../week09/) 입니다.
이 폴더는 **조교·교사 참고용**입니다. 수업 중(댓글·검색·권한을 직접 작성하는 동안)에는 학생에게
통째로 배포하지 않습니다. 단, **수업 종료 직전** 시간 내에 못 끝낸 학생에게는 다음 주(미니앱
구현)를 같은 출발선에서 시작할 수 있도록 **따라잡기용으로 전달해도 됩니다**.

## 이 예시에 대해

[week08-complete](../week08-complete/)(6~8주차: CRUD + 회원·권한 + 공공데이터 대시보드)를
그대로 이어받아, 댓글(`comments` 테이블) · 검색(`?q=`) · 관리자 권한(`users.role`,
`posts.is_notice`) · 실시간 채팅(`flask-socketio`, `chat_messages` 테이블)을 추가했습니다.
`bbs.db`는 실행 시 자동 생성되므로 포함하지 않습니다.

**중요:** 댓글·검색·권한(`app.py`의 해당 라우트, `templates/list.html`·`detail.html`)은 학생이
AI 없이 직접 작성하는 구간입니다 — 수업 중 이 코드를 통째로 복사해 주지 않습니다. 실시간 채팅
(`/chat`, `flask_socketio` 관련 코드, `templates/chat.html`)만 "AI 도전 과제로 만든 것"이라는
설정이며, 학생이 AI와 함께 만들되 수업안 5.5 체크리스트로 이해도를 확인하는 대상입니다.

## 파일

```
week09-complete/
├── ABOUT.md                 ← 이 안내 (교사용)
├── README.md                ← 완성된 프로젝트 README 예시
├── app.py                   ← Flask 서버 (CRUD + 회원·권한 + 대시보드 + 댓글·검색·RBAC·채팅)
├── make_admin.py            ← 관리자 승격 스크립트
├── opendata.py
├── data/
│   └── sample_air_quality.json
├── .env.example
├── requirements.txt          ← flask-socketio 포함
├── templates/
│   ├── list.html             ← 검색창·공지 표시 추가
│   ├── detail.html           ← 댓글 목록·입력, 관리자 삭제/공지 버튼 추가
│   ├── new.html / edit.html / signup.html / login.html
│   ├── dashboard.html
│   └── chat.html              ← 신규: socket.io 클라이언트 포함 채팅 화면
└── notes/
    ├── db-relations.md        ← 댓글 1:N 관계 워크시트 예시
    ├── rbac-notes.md          ← 권한 분기표 예시
    ├── why-social-features.md ← 회고 예시
    └── realtime-log.md        ← AI와 만든 채팅 기록 예시
```

## 실행 방법 (시연용)

```
pip install -r requirements.txt
cp .env.example .env
python app.py
```

`http://localhost:5001` 접속 → 회원가입 2개 계정(A, B) 생성 → `python make_admin.py A계정`
실행 후 A로 로그아웃/재로그인 → A 계정으로 B의 글 삭제·공지 고정이 되는지, B 계정으로는
안 되는지 시연. `/chat`을 두 브라우저(또는 창)로 열어 실시간 송수신도 함께 시연한다.

## 확인 포인트

- `app.py`: `delete_post`가 `require_owner_or_admin`을 쓰는지 (수정은 `require_owner`만 씀 — 의도적 차이)
- `app.py`: 로그인 시 `session["role"] = user["role"]`을 저장하는지
- `list.html`/`detail.html`: 검색·댓글·관리자 버튼이 조건부로 노출되는지
- `chat.html`: `socketio.run(app, ...)`으로 실행되는지 (`app.run`이 아니라)
- 학생 결과물에서 댓글·검색·권한이 **AI 프롬프트 없이** 완성됐는지 (실시간 채팅만 AI 사용 대상)
- 6~8주차 기능(CRUD·회원·권한·대시보드)이 오늘 추가 이후에도 그대로 동작하는지
