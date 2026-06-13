AI웹반 5주차 starter — Python + AI 챗봇 ★
==========================================

🟢 DEFAULT_QUESTION 바꾸기 → 기본 질문 보내기 → AI 답 확인!
🟡 입력창에 질문 쓰고 「내 질문 보내기」
🔴 「생각 중…」 로딩 표시 (JS)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. 교사: Secrets 에 OPENROUTER_API_KEY 설정 (openrouter.ai/keys)
2. Run 버튼
3. 「기본 질문 보내기」 클릭 → AI 답 확인 (무료 모델: google/gemma-4-31b-it:free)
4. F12 → Network 탭에서 POST /api/chat 확인

핵심 개념
---------
버튼 클릭 → script.js fetch POST → app.py call_ai() → OpenRouter → JSON → 화면
API 키는 Python(Flask)만! JS에는 키 없음!

폴더 구조
---------
app.py              ← 🟢 DEFAULT_QUESTION · 🟡 call_ai() · /api/chat
templates/index.html ← 질문 입력·답 영역
static/script.js    ← 🟢 fetch POST /api/chat (🔴 로딩)
static/style.css    ← 🟢 .reply 색·배경
requirements.txt    ← flask + openai (OpenRouter는 OpenAI 호환 API)

6주차부터 Python이 prompt 를 설계합니다 (build_quiz_prompt).
