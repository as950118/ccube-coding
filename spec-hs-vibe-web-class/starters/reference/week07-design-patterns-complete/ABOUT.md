# class·interface·디자인 패턴 + React (교사 참고 · 완성 예시, 보관됨)

> ⚠️ **보관됨(displaced):** 7주차는 이제 [../week07-complete/](../week07-complete/)(회원가입·로그인·권한)입니다. 이 폴더는 참고용으로만 보관합니다.

**수업안:** [../../../weeks/_displaced/week07-design-patterns.md](../../../weeks/_displaced/week07-design-patterns.md)

학생용 starter는 [../../week07/](../../week07/) 입니다.
이 폴더는 **조교·교사 참고용**이며, 수업 중 학생에게 통째로 배포하지 않습니다.

## 이 예시에 대해

[week06-complete](../week06-complete/)의 BBS를 이어받아, `models/`·`repositories/`로 구조를 나누고 React 목록 화면을 추가한 버전입니다. 수업안 2~5장(🟢🟡 구조 리팩터링, AI 없이 직접)·6장(🔴 React, AI 사용)의 참고 코드를 그대로 담았습니다. `bbs.db`는 실행 시 자동 생성되므로 포함하지 않습니다.

**중요:** 2~5장(POJO/interface/구현체/DI/IoC/헥사고날)은 학생이 AI 없이 직접 타이핑하는 구간입니다 — 수업 중 `models/`·`repositories/`·`app.py`를 통째로 복사해 주지 않습니다. `static/react-list.html`만 "AI 도전 과제로 만든 것"이라는 설정입니다.

## 파일

```
week07-complete/
├── ABOUT.md                          ← 이 안내 (교사용)
├── README.md                         ← 완성된 프로젝트 README 예시
├── app.py                            ← Controller (DI로 repo 주입)
├── models/
│   └── post.py                       ← POJO
├── repositories/
│   ├── post_repository.py            ← interface (Port)
│   ├── sqlite_post_repository.py     ← SQLite 구현체 (Adapter)
│   └── memory_post_repository.py     ← 메모리 구현체 (다른 Adapter)
├── templates/                        ← week06-complete에서 이어받은 Jinja View
├── static/
│   └── react-list.html               ← 🔴 React View (AI 도전 과제 예시)
└── notes/
    ├── mvc-mapping.md                ← 파일별 M/V/C 매핑 예시
    └── why-layers.md                 ← 왜 층을 나눴는가 예시
```

## 실행 방법 (시연용)

```
pip install flask
python app.py
```

`http://localhost:5001` — 목록·상세·작성·수정·삭제·검색이 그대로 동작하는지 확인.
`http://localhost:5001/static/react-list.html` — React가 `/api/posts`를 fetch해 목록을 보여주는지 확인.

## 헥사고날 시연 (5장)

`app.py`에서 `repo = SqlitePostRepository("bbs.db")`를 `repo = MemoryPostRepository()`로 바꾸고 재실행 — 나머지 코드를 전혀 안 건드려도 목록·상세·작성·수정·삭제가 동일하게 동작하는지 보여줍니다 (단, 재시작하면 데이터가 사라짐).

## 확인 포인트

- app.py: `sqlite3` import·SQL 문자열이 전혀 없는가? (전부 `repo.xxx()` 호출)
- repositories: `PostRepository`의 추상 메서드 5개를 두 구현체 모두 빠짐없이 구현했는가?
- notes/mvc-mapping.md: 학생이 파일마다 "왜 그렇게 분류했는지" 이유를 적었는가?
- 학생 결과물에서 2~5장이 **AI 프롬프트 없이** 완성됐는지 (6장 React만 AI 사용 대상)
