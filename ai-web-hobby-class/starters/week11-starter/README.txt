AI웹반 11주차 starter — 통합 (챗봇·퀴즈·OX·이미지 AI)
====================================================

🟢 APP_TITLE · STUDENT_NAME 바꾸기 → 메뉴 4개 클릭 확인 + 스크린샷!
🟡 챗봇 탭에 「지우기」 버튼 직접 추가 (JS 실습, weeks/week11-integration.md 참고) / TUTOR_PROMPT · 다크모드 힌트
🔴 퀴즈 탭에도 「지우기」 추가 / Replit Deploy → URL 받기 (12주차 발표 준비)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. 교사: Secrets 에 OPENROUTER_API_KEY 설정
2. 9~10주차와 같은 Teachable Machine 모델이 있다면 app.py 의 MODEL_URL 에 붙여넣기 (끝에 / 필수)
   → 없어도 챗봇·퀴즈·OX 3개는 그대로 동작합니다 (이미지 AI는 선택)
3. Run 버튼
4. 「AI 챗봇」·「AI 퀴즈」·「OX 퀴즈」·「이미지 AI」 메뉴 전환 확인

핵심 개념
---------
한 app.py 에 라우트 여러 개 + 브라우저 이미지 AI가 한 화면에:
  /                   → 전체 페이지 (메뉴 4개 UI)
  /api/chat           → 5주차 AI 챗
  /api/generate-quiz  → 6주차 AI 퀴즈
  /api/check          → 4주차 OX
  (JS) Teachable Machine → 9~10주차 이미지 AI (Python은 MODEL_URL만 전달)

폴더 구조
---------
app.py               ← 🟢 APP_TITLE · STUDENT_NAME · MODEL_URL / 🟡 TUTOR_PROMPT
templates/index.html ← 메뉴 4개 + 패널 + footer "made by {{ name }}"
static/script.js     ← 메뉴 전환 + fetch(챗/퀴즈/OX) + TM 웹캠/업로드
static/style.css     ← 통일된 메뉴·패널 스타일 (🟡 다크모드 힌트 포함)
requirements.txt     ← flask + openai

12주차에서 이 앱의 Deploy URL로 발표합니다!
