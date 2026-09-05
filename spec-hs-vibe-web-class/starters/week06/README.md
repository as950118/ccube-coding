# week06 — 웹은 어떻게 동작하는가 · 나만의 BBS (starter)

**수업안:** [../../weeks/week06-bbs-basics.md](../../weeks/week06-bbs-basics.md)
**학생용 자료:** [../../docs/2026진학반_6주차.docx](../../docs/2026진학반_6주차.docx) ⚠️ 아직 구식(프로필 배포) 내용 — [2026진학반_6주차-draft.md](../../docs/2026진학반_6주차-draft.md) 참고해 재작성 필요

## 이 폴더 사용법

이번 주는 4~5주차 프로필 프로젝트와 **완전히 별개의 새 저장소**를 만든다. 프론트(HTML) + 백엔드(Flask) + DB(SQLite)로 동작하는 첫 서비스형 프로젝트다.

**오늘 핵심 기능(목록·상세·작성·수정·삭제)은 AI 없이 직접 코드를 작성한다.** AI는 맨 마지막 도전 과제에서만 쓴다.

1. `pip install flask`로 준비한다 (사전과정을 거쳤다면 이미 설치돼 있을 수 있음)
2. 이 폴더의 `app.py`·`templates/`를 그대로 복사해서 시작한다 — 라우트 이름·URL·`get_db`/`create_table`은 이미 채워져 있고, 각 라우트/템플릿의 **`# TODO`·`<!-- TODO -->` 부분만 직접 채운다**
3. 수업안 5장을 참고해 SQL·`render_template`·`redirect` 코드를 직접 작성한다 (AI에게 시키지 않는다)
4. `python app.py`로 로컬에서 실행한다 (`localhost:5001`)
5. `notes/architecture.md`에 클라이언트-서버-DB 그림과 오늘 만든 BBS의 각 부분을 채운다
6. `notes/why-3tier.md`에 회고를 남긴다
7. 시간이 남으면 도전 과제(아래)에서만 AI를 사용해 기능/스타일을 추가한다

## 포함된 파일

```
week06/
├── README.md                  ← 이 안내
├── app.py                     ← 스켈레톤 (라우트 껍데기 + TODO, 로직은 비어 있음)
├── templates/
│   ├── list.html              ← 스켈레톤 (TODO)
│   ├── detail.html            ← 스켈레톤 (TODO)
│   ├── new.html                ← 스켈레톤 (TODO)
│   └── edit.html               ← 스켈레톤 (TODO)
└── notes/
    ├── architecture.md        ← 클라이언트-서버-DB 그림 + 오늘 BBS 매핑 워크시트
    └── why-3tier.md           ← 왜 이렇게 구조를 나눴는가 · 회고
```

`app.py`·`templates/`는 **뼈대(라우트 URL, 임포트, DB 헬퍼)만 있고 로직은 비어 있다.** `# TODO`가 달린 부분(SQL 쿼리, `render_template` 호출, HTML 표시·폼)을 직접 채우는 것이 오늘 핵심이다 — AI에게 채워 달라고 하지 않는다.

## 성공 기준 (🟢, AI 없이)

- [ ] `python app.py`로 서버가 로컬에서 실행된다
- [ ] 목록·상세·작성·수정·삭제 5기능이 모두 동작한다
- [ ] 서버를 껐다 켜도 글이 남아 있다 (DB 저장 확인)
- [ ] `notes/architecture.md`에 3단 구조가 오늘 만든 BBS에 매핑되어 있다

## 🔴 도전 과제 (여기서만 AI 사용)

5기능이 모두 동작한 뒤에만 진행한다.

```
목표: 오늘 만든 BBS에 (내가 상상한 기능/스타일)을 추가한다.

제약:
- 기존 목록·상세·작성·수정·삭제 기능은 그대로 유지
- 파일: app.py, templates/ 안에서만 수정

먼저 계획만 제안해줘: 어떤 라우트/파일이 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

예시 아이디어: 제목 검색(LIKE + `?` 파라미터), fetch 기반 비동기 글쓰기(`/api/posts`), 댓글, 다크 테마, 태그 등 — 자세한 프롬프트는 수업안 7장 참고.

## 완성 예시 (교사·조교용)

[../reference/week06-complete/](../reference/week06-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기. (단, 시간 내에 못 끝낸 학생에게는 수업 종료 직전 교사가 따라잡기용으로 전달할 수 있음 — 진행 팁 참고)

자세한 진행·🟡🔴 과제는 [weeks/week06-bbs-basics.md](../../weeks/week06-bbs-basics.md) 참고.
