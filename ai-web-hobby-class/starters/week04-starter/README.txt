AI웹반 4주차 starter — Python OX 퀴즈
======================================

🟢 O/X 버튼 클릭 → Python이 맞/틀 판정 → 화면에 표시!
   app.py 의 QUESTIONS[0] 문장 바꿔보기 + 맞/틀 색 CSS
🟡 QUESTIONS 에 문제 4번째 추가 (Python list)
🔴 3문제 모두 답하면 /api/score 로 총점 표시
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. Run 버튼
2. Q1 에서 O 클릭 → 「맞아요!」 확인
3. Q2 에서 O 클릭 → 「틀려요」 확인 (정답은 X)

핵심 개념
---------
O/X 클릭 → script.js fetch → app.py check_answer() → JSON → 화면
문제·정답 데이터는 Python QUESTIONS dict 에 있음!

폴더 구조
---------
app.py              ← 🟢 QUESTIONS · /api/check (🟡 4번째 문제 · 🔴 /api/score)
templates/index.html ← 문제 목록 (Jinja2 for)
static/script.js    ← 🟢 fetch /api/check
static/style.css    ← 🟢 .feedback.correct / .wrong 색
requirements.txt

5주차부터 app.py 가 AI API 를 호출합니다.
