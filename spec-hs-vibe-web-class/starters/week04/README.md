# week04 — 프로필 웹 초안 (starter)

**수업안:** [../../weeks/week04-vibe-basics-profile.md](../../weeks/week04-vibe-basics-profile.md)  
**학생용 자료:** [../../docs/2026진학반_4주차.docx](../../docs/2026진학반_4주차.docx)

## 이 폴더 사용법

1. 이 폴더(`week04`)를 통째로 복사해 `ccube-week04` 또는 `week04-profile`처럼 이름을 바꾼다.
2. Cursor에서 **File → Open Folder**로 연다.
3. **Plan 모드(또는 「코드 없이 계획만」)** 로 사이트맵을 먼저 합의한다. HTML은 「진행」이라고 한 뒤에만 작성한다.
4. `notes/` 템플릿을 채운 뒤, 합의된 구조로 `index.html`(+ CSS)을 만든다.
5. 브라우저로 열어 5섹션이 보이는지 확인한다.

## 포함된 파일

```
week04/
├── README.md              ← 이 안내
└── notes/
    ├── interview.md       ← 나 인터뷰 워크시트
    ├── sitemap.md         ← 섹션 합의 템플릿
    └── why-structure.md   ← 「왜 이 구조인가」메모
```

`index.html`은 **일부러 없다.** 오늘 핵심은 **Plan으로 구조를 정한 뒤** 코드를 만드는 것이다.

## Plan 프롬프트 템플릿

```
목표: 중학생 포트폴리오용 프로필 웹 초안을 만든다.

제약:
- HTML/CSS만 (React/Next 금지)
- 한 페이지 스크롤 + 섹션 id 앵커
- 한국어 UI
- 실명·학교·전화번호·얼굴 사진 넣지 말 것 (닉네임 OK)
- 오늘은 초안(v0). 배포·Git 언급하지 말 것

먼저 계획만 제안해줘:
1) 섹션 목록
2) 파일 구조
3) 각 섹션 최소 콘텐츠
4) 하지 않을 것 (Non-goals)

코드는 내가 "진행"이라고 한 뒤에만 작성해줘.
```

## 구현 프롬프트 (승인 후)

```
합의된 sitemap대로 index.html (+ 필요 시 styles/main.css)을 작성해줘.

필수:
- 섹션 5개, 각 섹션에 id
- 한국어
- Projects는 "Coming soon" 카드 2개
- Contact는 플레이스홀더만 (가짜 개인정보 생성 금지)
- 반응형은 기본만

비주얼:
- 과한 애니메이션·이모지 남발 금지
- 읽기 쉬운 타이포, 단순한 배경
```

## 성공 기준 (🟢)

- [ ] Plan으로 사이트맵이 합의되어 `notes/sitemap.md`에 있다
- [ ] 브라우저에서 Hero → About → Interests → Projects → Contact가 구분되어 보인다
- [ ] 「왜 이 구조인가」1문장을 말할 수 있다
- [ ] About 문장 한 줄을 **직접** 고치고 새로고침했다

## 완성 예시 (교사·조교용)

[../reference/week04-complete/](../reference/week04-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기.

자세한 진행·🟡🔴 과제는 [weeks/week04-vibe-basics-profile.md](../../weeks/week04-vibe-basics-profile.md) 참고.
