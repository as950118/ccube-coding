# week09 — BBS 확장: 댓글·검색·권한·실시간 채팅 (starter)

**수업안:** [../../weeks/week09-bbs-social-features.md](../../weeks/week09-bbs-social-features.md)
**학생용 자료:** [../../docs/2026진학반_9주차-draft.md](../../docs/2026진학반_9주차-draft.md) (아직 초안 — docx 미작성)

## 이 폴더 사용법

이번 주는 **8주차 BBS 폴더를 그대로 이어쓴다.** 새 저장소를 만들지 않는다.

**댓글·검색·권한(1~3단계)은 AI 없이 직접 코드를 작성한다.** 실시간 채팅(4단계)만 AI와 함께 만든다 — 지금까지와 다른 새 개념(WebSocket)이 필요하기 때문이다.

1. `comments` 테이블을 추가하고, 댓글 작성/삭제 라우트와 `detail.html`의 댓글 영역을 직접 작성한다
2. `/` 라우트에 검색(`?q=`, SQL `LIKE`)을 추가하고 `list.html`에 검색창을 넣는다
3. `users.role`·`posts.is_notice` 컬럼을 추가하고, `make_admin.py`로 관리자 계정을 만든 뒤 남의 글 삭제·공지 고정 권한을 구현한다
4. `pip install flask-socketio` 후, `notes/realtime-log.md`에 적을 프롬프트로 AI와 함께 `/chat` 실시간 채팅을 만든다 — 완성되면 5.5(수업안) 체크리스트를 직접 채운다
5. `notes/db-relations.md` · `notes/rbac-notes.md` · `notes/why-social-features.md`를 채운다
6. 시간이 남으면 도전 확장(댓글 대댓글, 검색 결과 하이라이트, 접속자 수 표시 등)을 진행한다

## 포함된 파일

```
week09/
├── README.md                  ← 이 안내
└── notes/
    ├── db-relations.md        ← 댓글 1:N 관계 워크시트 (신규 작성 권장)
    ├── rbac-notes.md          ← 권한 분기표 워크시트 (신규 작성 권장)
    ├── why-social-features.md ← 회고 (신규 작성 권장)
    └── realtime-log.md        ← AI와 만든 실시간 채팅 기록 (신규 작성 권장)
```

이번 주는 8주차 `app.py`/`templates/`를 직접 이어서 고치는 것이 핵심이라, 새로 복사해 넣는 스켈레톤 파일은 없다. 수업안(`weeks/week09-bbs-social-features.md`)의 2~5장 코드를 보며 자기 프로젝트에 직접 반영한다.

## 성공 기준 (🟢🟡, AI 없이)

- [ ] 댓글을 작성하면 상세 페이지에 보이고, 본인 댓글만 삭제 버튼이 보인다
- [ ] `/?q=키워드` 검색 시 제목·내용에 키워드가 있는 글만 남는다
- [ ] `make_admin.py`로 관리자로 만든 계정이 남의 글 삭제·공지 고정을 할 수 있다
- [ ] 일반 계정은 여전히 본인 글만 수정·삭제할 수 있다
- [ ] 6~8주차 기능(CRUD·회원·권한·대시보드)이 그대로 동작한다

## 🔴 도전 과제 (여기서만 AI 사용)

댓글·검색·권한 핵심이 끝난 뒤에만 진행한다.

```
목표: 이 Flask 게시판(app.py)에 flask-socketio로 실시간 채팅(/chat)을 추가한다.

요구사항:
- 로그인한 사용자만 /chat 접속 가능
- chat_messages 테이블(id, username, content, created_at)에 저장
- send_message 이벤트를 받으면 DB 저장 후 new_message로 전체 broadcast
- 기존 라우트(목록/상세/댓글/검색/권한/대시보드)는 건드리지 않는다

먼저 계획만 제안해줘. 내가 "진행"이라고 하면 그때 구현해줘.
```

구현이 끝나면 수업안 5.5의 체크리스트(SocketIO(app)/이벤트 이름/broadcast 코드 위치/클라이언트 io() 연결/socketio.run 전환 여부)를 직접 찾아 `notes/realtime-log.md`에 적는다.

## 완성 예시 (교사·조교용)

[../reference/week09-complete/](../reference/week09-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기. (단, 시간 내에 못 끝낸 학생에게는 수업 종료 직전 교사가 따라잡기용으로 전달할 수 있음)

자세한 진행·🟡🔴 과제는 [weeks/week09-bbs-social-features.md](../../weeks/week09-bbs-social-features.md) 참고.
