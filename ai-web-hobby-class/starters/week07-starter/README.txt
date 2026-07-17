AI웹반 7주차 starter — Flask 라우트 통합 (AI 학습 도우미)
========================================================

🟢 APP_TITLE 바꾸기 → 탭 2개(챗봇·퀴즈) 클릭 확인!
🟡 TUTOR_PROMPT — 친절한 튜터 system prompt
🔴 OX 퀴즈를 세 번째 탭으로 (index.html 주석 해제)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. 교사: Secrets 에 OPENROUTER_API_KEY 설정
2. Run 버튼
3. 「AI 챗봇」·「AI 퀴즈」 탭 전환 확인
4. F12 → Network 에서 /api/chat , /api/generate-quiz 확인

핵심 개념
---------
한 app.py 에 여러 라우트:
  /                → 전체 페이지 (탭 UI)
  /api/chat        → 5주차 AI 챗
  /api/generate-quiz → 6주차 AI 퀴즈
  /api/check       → 4주차 OX (🔴)

폴더 구조
---------
app.py               ← 🟢 APP_TITLE · 🟡 TUTOR_PROMPT · 라우트 통합
templates/index.html ← 탭 + 패널
static/script.js     ← 탭 전환 + fetch
static/style.css     ← 탭·패널 스타일
requirements.txt     ← flask + openai

8주차에서 messages[] + 말풍선 UI로 채팅을 업그레이드합니다.
