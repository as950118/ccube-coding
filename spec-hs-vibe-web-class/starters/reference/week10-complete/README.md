# 미니 방명록

이름과 메시지를 남기면 새로고침해도 사라지지 않는 방명록입니다.

## 문제

배운 것을 화면에 남기고, 다른 사람도 남길 수 있게 하고 싶었다.

## 구조 (3단 아키텍처)

- **프론트(Vercel)**: `frontend/` — Vite + 순수 JS
- **백엔드(Render)**: `backend/` — Flask API, Supabase 접근을 전담
- **DB(Supabase)**: Postgres `items` 테이블

프론트는 Supabase를 직접 모릅니다. 백엔드 API만 호출합니다.

## 데모

- 배포 URL: (배포 후 여기에 적기)

## 로컬 실행

```bash
cd backend && pip install -r requirements.txt && cp .env.example .env && python app.py
cd frontend && npm install && cp .env.example .env && npm run dev
```

## 사용법

1. 이름과 메시지를 입력하고 "저장" 클릭
2. 목록에 바로 반영됨
3. 새로고침해도 남아있음 (DB에 저장됐기 때문)

## 회고

- 오늘 배운 것: 3단 아키텍처(프레젠테이션·애플리케이션·데이터)를 실제로 나눠 배포하는 법
- 막혔던 점: (여기에 적기)
- 다음에 하고 싶은 것: (여기에 적기)
