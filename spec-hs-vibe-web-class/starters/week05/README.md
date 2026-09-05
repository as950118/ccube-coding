# week05 — Git · GitHub · CLAUDE.md (starter)

**수업안:** [../../weeks/week05-git-memory.md](../../weeks/week05-git-memory.md)  
**학생용 자료:** [../../docs/2026진학반_5주차.docx](../../docs/2026진학반_5주차.docx)

## 이 폴더 사용법

이번 주는 **새 폴더를 만들지 않는다.** 4주차에 만든 `week04-profile`(또는 동등 프로필 폴더) 안에서 그대로 이어간다.

1. 4주차 폴더를 Cursor에서 연다.
2. `notes/` 워크시트를 참고해 README.md · CLAUDE.md를 **먼저 초안**으로 채운다.
3. `git init` → `add` → `commit` → GitHub repo 생성 → `push` 순서로 저장소를 만든다.
4. README.md · CLAUDE.md를 프로젝트 루트에 저장하고 **의미 단위로 2개 이상** 커밋한다.
5. repo URL을 브라우저(가능하면 시크릿 창)에서 열어 확인한다.

## 포함된 파일

```
week05/
├── README.md                  ← 이 안내
└── notes/
    ├── readme-worksheet.md    ← README.md 초안 워크시트
    ├── claude-md-worksheet.md ← CLAUDE.md 초안 워크시트
    └── commit-log.md          ← 오늘 커밋 기록 템플릿
```

`README.md`·`CLAUDE.md` **완성본은 일부러 없다.** 오늘 핵심은 워크시트를 채운 뒤,
그 내용을 바탕으로 **직접(또는 AI와 함께) 완성본을 프로젝트 루트에 작성**하는 것이다.

## Git 기본 흐름 (터미널)

```
git init
git add .
git commit -m "첫 커밋: 프로필 초안 v0"
git branch -M main
git remote add origin <GitHub repo URL>
git push -u origin main
```

## README 초안 프롬프트

```
아래 프로젝트의 README.md 초안을 작성해줘.

프로젝트: 중학생 포트폴리오용 프로필 웹 초안
현재 상태: HTML/CSS로 5섹션(Hero/About/Interests/Projects/Contact) 완성
목표: 6주차에 배포 예정
톤: 담백하고 간결하게, 이모지 남발 금지

구성: 제목 / 한줄소개 / 무엇인가요 / 왜 만들었나요 / 어떻게 열어보나요 / 다음에 할 일
없는 사실(수상 경력, 실제 배포 링크 등)은 만들어내지 마.
```

## CLAUDE.md 초안 프롬프트

```
notes/sitemap.md와 README.md를 참고해서
이 프로젝트의 CLAUDE.md 초안을 만들어줘.

포함할 것: 나(닉네임/목적), 톤, 기술 규칙, 절대 하지 말 것
없는 정보(실명, 학교 등)는 비워두거나 "미정"으로 남겨줘.
```

## 성공 기준 (🟢)

- [ ] `git status`/`add`/`commit`/`push`를 직접 실행했다
- [ ] GitHub repo URL이 브라우저에서 열린다
- [ ] README.md에 프로젝트 설명이 5줄 내외로 있다
- [ ] CLAUDE.md에 이름(닉네임)·톤·금지사항이 최소 1개씩 있다
- [ ] 의미 단위 커밋이 2개 이상이다 (한 덩어리 push 지양)

## 완성 예시 (교사·조교용)

[../reference/week05-complete/](../reference/week05-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기.

자세한 진행·🟡🔴 과제는 [weeks/week05-git-memory.md](../../weeks/week05-git-memory.md) 참고.
