# week10 — 미니앱 MVP 구현 · 배포 (starter)

**수업안:** [../../weeks/week10-miniapp-mvp.md](../../weeks/week10-miniapp-mvp.md)

## 이 폴더 사용법

오늘은 **미니앱 주제를 그 자리에서 정하고** 바로 구현·배포한다. 새 저장소를 만든다
(8~9주차 BBS와 별개 프로젝트).

- **저장이 필요 없는 주제**(계산기·변환기·정적 정보 앱 등)라면 `frontend/`만 쓰고,
  이 폴더의 `backend/`는 지운다. Vercel(또는 GitHub Pages)에만 배포하면 끝 (🟢).
- **저장이 필요한 주제**(글쓰기·방명록·좋아요 등)라면 `backend/`까지 써서 3단 구조로
  간다 (🔴, 선택). 아래 순서를 따른다.

## 🔴 3단 구조로 갈 때 순서

1. `backend/supabase_schema.sql`의 테이블·컬럼을 내 주제에 맞게 고친 뒤, Supabase
   프로젝트를 만들고 SQL Editor에서 실행한다
2. `backend/app.py`의 TODO 1~4를 채운다 (Supabase 연결, 라우트 로직)
3. `backend/.env.example`을 `.env`로 복사해 값을 채우고 로컬에서 `python app.py`로
   확인한다
4. `frontend/src/main.js`의 TODO 5~7을 채운다 (API 호출 로직)
5. Render에 백엔드 배포 → Vercel에 프론트 배포 → `frontend/.env`(Vercel 환경변수)에
   Render URL 등록
6. `notes/deploy-log.md`를 채운다

**주의:** Supabase의 `SUPABASE_SERVICE_KEY`(secret key)는 절대 프론트 코드나 커밋에
넣지 않는다 — `.env`는 이미 `.gitignore`에 들어있다. 이 키는 Render 환경변수에만 붙여넣는다.

## 포함된 파일

```
week10/
├── README.md
├── notes/
│   └── deploy-log.md          ← 배포 회고 워크시트
├── backend/                    ← 🔴 3단 구조를 선택했을 때만 사용
│   ├── app.py                  ← TODO 1~4
│   ├── requirements.txt
│   ├── render.yaml
│   ├── supabase_schema.sql     ← TODO 1
│   └── .env.example
└── frontend/
    ├── index.html               ← TODO 0
    ├── src/main.js               ← TODO 5~7
    ├── package.json
    └── .env.example
```

## 성공 기준

### 🟢 (전원)
- [ ] MVP 기능 최소 1개 동작
- [ ] 배포 URL
- [ ] 프로필 웹 Projects에 카드 추가
- [ ] 회고 3줄

### 🔴 (선택 — 3단 구조)
- [ ] Vercel(프론트) · Render(백엔드) · Supabase(DB) 모두 배포되어 서로 통신
- [ ] 저장 → 새로고침해도 데이터 유지되는 CRUD 최소 1개 동작
- [ ] `notes/deploy-log.md` 작성

## 완성 예시 (교사·조교용)

[../reference/week10-complete/](../reference/week10-complete/) — 학생이 막혔을 때만 참고.
자세한 진행·체크리스트는 [weeks/week10-miniapp-mvp.md](../../weeks/week10-miniapp-mvp.md) 참고.
