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

## 실제로 검증한 내용 (2026-09-11, 이 세션에서 확인)

- Supabase 새 프로젝트 생성 → SQL Editor에서 `supabase_schema.sql` 실행까지 **정상 동작 확인**
- 백엔드 `pip install -r requirements.txt` **로컬에서 클린 설치 확인** (Python 3.14 / supabase-py 2.9.1)
- Render Web Service 생성 폼(Root Directory·Build/Start Command·Free plan·환경변수 2개)까지 **설정 확인**
- **주의:** Supabase가 API 키 체계를 새로 바꿨습니다 — 예전 `anon`/`service_role`(JWT 형식) 대신
  `sb_publishable_...` / `sb_secret_...` 형식이 기본입니다. 이 프로젝트의 `SUPABASE_SERVICE_KEY`는
  새 형식의 **secret key**(구 service_role과 같은 역할)를 가리킵니다. 프로젝트가 "Legacy anon,
  service_role API keys" 탭에 있는 이전 형식 키를 쓰는 경우 supabase-py 사용법은 동일합니다.
- 시크릿 키(SUPABASE_SERVICE_KEY)를 실제로 Render에 입력해 백엔드 배포 → 프론트 배포 → 브라우저
  E2E CRUD까지는 **이 세션에서 완료하지 않았습니다.** API 키/토큰을 대신 입력하는 행위는 Claude가
  하지 않기 때문입니다(정책상 금지) — 이 단계는 항상 학생 본인(또는 교사)이 직접 붙여넣어야
  합니다. 수업 중에도 동일하게 안내하세요: **"AI에게 시크릿 키를 대신 입력해 달라고 하지 않는다"**
  는 것 자체가 보안 교육 포인트입니다.

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
