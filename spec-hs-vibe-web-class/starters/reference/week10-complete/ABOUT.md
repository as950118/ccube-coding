# 미니앱 MVP · 3단 아키텍처 배포 (교사 참고 · 완성 예시)

**수업안:** [../../../weeks/week10-miniapp-mvp.md](../../../weeks/week10-miniapp-mvp.md)

학생용 starter는 [../../week10/](../../week10/) 입니다.
이 폴더는 **조교·교사 참고용**입니다. 🟢 전원 코스(프론트만 배포)에는 필요 없고, 🔴 3단 아키텍처
(Vercel·Render·Supabase)를 선택한 학생이 막혔을 때만 참고용으로 보여줍니다.

## 이 예시에 대해

"미니 방명록" — 이름·메시지를 남기면 새로고침해도 남아있는 가장 단순한 저장형 앱입니다.
Week10은 매번 다른 미니앱 주제를 그 자리에서 정하므로, 이 예시는 **주제가 아니라 배포 구조**를
보여주는 용도입니다. 학생은 자기 주제에 맞게 `items` 테이블·필드명만 바꿔서 재사용합니다.

```
[Vercel]                [Render]                [Supabase]
 index.html   --fetch-->  Flask app.py  --SUPABASE_SERVICE_KEY-->  Postgres(items)
 (프레젠테이션)              (애플리케이션)                            (데이터)
```

**핵심은 키 분리입니다.** Supabase `SUPABASE_SERVICE_KEY`(secret key)는 RLS를 우회하는
강력한 키라 프론트/공개 저장소에 절대 노출하면 안 됩니다. 그래서 프론트는 이 키를 아예 모르고,
Render에 배포된 백엔드만 이 키를 (Render 환경변수로) 가지고 있습니다. 프론트는 백엔드의
공개 API(Render URL)만 호출합니다.

## 실제로 검증한 내용 (2026-09-12, 실배포 E2E 완료)

이 Kit은 실제로 Supabase·Render·Vercel에 배포해서 브라우저로 CRUD·새로고침 지속성까지 확인했습니다.

- Supabase 새 프로젝트 생성 → SQL Editor에서 `supabase_schema.sql` 실행 → **정상 동작 확인**
- Render에 백엔드 배포(Free plan, Root Directory·Build/Start Command 설정) → `/api/health`,
  `/api/items` GET·POST **실제 응답 확인** (`https://week10-guestbook-api.onrender.com`)
- Vercel에 프론트 배포(Framework: Vite, Root Directory 지정, `VITE_API_URL` 환경변수) → 배포된
  페이지에서 폼으로 직접 입력 → **새로고침해도 데이터 유지되는 것까지 확인**
- 시크릿 키(`SUPABASE_SERVICE_KEY`) 값 자체는 학생/교사가 Render 환경변수 필드에 직접 붙여넣었습니다
  — Claude는 API 키/토큰 값을 필드에 입력하지 않는다는 원칙을 지켰습니다. 수업 중에도 동일하게
  안내하세요: **"AI에게 시크릿 키를 대신 입력해 달라고 하지 않는다"**는 것 자체가 보안 교육 포인트입니다.

### 🐛 실배포로 찾은 버그: supabase-py 구버전이 새 키 형식을 거부함

Supabase가 API 키 체계를 `anon`/`service_role`(JWT 형식)에서 `sb_publishable_...` /
`sb_secret_...`(비-JWT, opaque 형식)로 바꿨습니다. 그런데 **`supabase-py==2.9.1`은 키를
`^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?...$` 정규식(JWT 형식, 점 2개)으로 검사**해서, 새 형식
키를 넣으면 `SupabaseException("Invalid API key")`를 던지며 **Render 배포가 크래시**했습니다
(`gunicorn` exited with status 1 — 실제로 이 세션에서 재현·확인함).

**해결:** `supabase==2.31.0`으로 올리면 이 정규식 검사 자체가 코드에서 사라져 있어 새 키 형식이
그대로 통과합니다. `requirements.txt`는 이미 2.31.0으로 고정해뒀습니다 — **이보다 낮은 버전으로
내리지 마세요.** 학생이 옛날 튜토리얼을 보고 `pip install supabase==2.9`처럼 구버전을 깔면 똑같은
에러가 재현되니, 이 증상이 나오면 먼저 `pip show supabase`로 버전을 확인하게 하세요.

### 검증에 쓴 실제 배포 (수업 자료 검증용 — 학생 개인 프로젝트 아님)

- Supabase 프로젝트: `week10-guestbook-demo` (as950118's Org)
- Render: `week10-guestbook-api` → `https://week10-guestbook-api.onrender.com`
- Vercel: `week10-guestbook` → `https://week10-guestbook.vercel.app`

이 셋은 Kit이 실제로 동작하는지 검증하려고 만든 것이라, 계속 켜둘 필요가 없으면 이후에 정리(삭제)해도 됩니다.

## 파일

```
week10-complete/
├── ABOUT.md                 ← 이 안내 (교사용)
├── backend/
│   ├── app.py                ← Flask API (GET/POST /api/items)
│   ├── requirements.txt
│   ├── render.yaml            ← Render Blueprint (선택 — 대시보드로 직접 만들어도 됨)
│   ├── supabase_schema.sql    ← Supabase SQL Editor에 붙여넣을 스키마
│   └── .env.example
└── frontend/
    ├── index.html
    ├── src/main.js             ← fetch로 백엔드 API 호출
    ├── package.json            ← Vite
    └── .env.example            ← VITE_API_URL
```

## 실행 방법 (로컬 시연용)

```bash
# 1. Supabase 프로젝트 생성 후 backend/supabase_schema.sql 실행
# 2. 백엔드
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # SUPABASE_URL / SUPABASE_SERVICE_KEY 채우기
python app.py           # http://localhost:5000

# 3. 프론트 (새 터미널)
cd frontend
npm install
cp .env.example .env   # VITE_API_URL=http://localhost:5000
npm run dev
```

## 실제 배포 절차 (Render + Vercel)

1. **Supabase**: 프로젝트 생성 → SQL Editor에서 `supabase_schema.sql` 실행 → Project Settings →
   API Keys에서 URL과 secret key 확인 (secret key는 "Reveal"을 눌러야 보임)
2. **Render**: New → Web Service → GitHub repo 연결 → Root Directory를
   `spec-hs-vibe-web-class/starters/reference/week10-complete/backend`로 지정 → Build Command
   `pip install -r requirements.txt` / Start Command `gunicorn app:app` → **Instance Type: Free**
   선택 → Environment Variables에 `SUPABASE_URL`, `SUPABASE_SERVICE_KEY` 등록 → Deploy
3. **Vercel**: New Project → 같은 repo → Root Directory를
   `spec-hs-vibe-web-class/starters/reference/week10-complete/frontend`로 지정 → Framework
   Preset: Vite → Environment Variables에 `VITE_API_URL` = (2번에서 나온 Render URL) 등록 → Deploy
4. 배포된 Vercel URL 접속 → 이름/메시지 남기기 → 새로고침해도 남아있는지 확인

## 확인 포인트

- `app.py`에서 `SUPABASE_SERVICE_KEY`를 쓰지, `SUPABASE_URL`만 쓰고 anon/publishable 키를
  섞어 쓰고 있지 않은지 (섞으면 RLS 때문에 조용히 실패함)
- 프론트 코드 어디에도 `sb_secret_...` 또는 legacy `service_role` 키 문자열이 없는지
  (있다면 프론트 번들에 그대로 노출됨 — 반드시 백엔드에서만)
- Render 무료 티어 콜드스타트(15분 미사용 후 첫 요청 30~60초) 때문에 "안 되는 줄" 착각하지
  않도록 학생에게 미리 안내했는지
