AI웹반 6주차 starter — Python prompt + AI 퀴즈 생성
====================================================

🟢 DEFAULT_SUBJECT 바꾸기 → 퀴즈 생성하기 → AI 퀴즈 확인!
🟡 build_quiz_prompt() 에 「쉬운 난이도」 추가
🔴 OX 형식으로 파싱·표시 (선택)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. 교사: Secrets 에 OPENROUTER_API_KEY 설정 (openrouter.ai/keys)
2. Run 버튼
3. 「퀴즈 생성하기」 클릭 → AI 퀴즈 확인
4. F12 → Network 탭에서 GET /api/generate-quiz 확인

핵심 개념
---------
버튼 클릭 → script.js fetch → app.py build_quiz_prompt() → call_ai() → OpenRouter → JSON → 화면
5주차: 질문을 그대로 AI에게 보냄
6주차: Python이 prompt 문장을 설계한 뒤 AI에게 보냄!

폴더 구조
---------
app.py               ← 🟢 DEFAULT_SUBJECT · build_quiz_prompt() · /api/generate-quiz
templates/index.html ← 과목 입력·퀴즈 결과 영역
static/script.js     ← 🟢 fetch /api/generate-quiz
static/style.css     ← 🟢 .quiz-result 색·배경
requirements.txt     ← flask + openai

7주차에서 챗봇(/api/chat) + 퀴즈를 한 앱(탭)으로 합칩니다.
