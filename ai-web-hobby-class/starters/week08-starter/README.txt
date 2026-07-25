AI웹반 8주차 starter — Python 대화 기록 + 채팅 UI
=================================================

🟢 말풍선 색 2종 바꾸기 → 대화 2턴 테스트!
🟡 Enter 전송 · /api/chat 가 history 반환
🔴 /api/clear — 대화 기록 비우기 (버튼 주석 해제)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. Secrets 에 OPENROUTER_API_KEY 설정
2. Run
3. 질문 보내기 → 말풍선 2개(나·AI) 확인
4. 한 번 더 보내기 → 대화가 쌓이는지 확인

핵심 개념
---------
Python messages: list[dict] 에 대화 저장
JS appendMessage() 로 .bubble-user / .bubble-ai 표시
텍스트 AI 파트(5~8주) 마무리!

폴더 구조
---------
app.py               ← messages list · /api/chat · /api/clear
templates/index.html ← 채팅창 · 말풍선 영역
static/script.js     ← appendMessage · history 렌더
static/style.css     ← 🟢 .bubble-user / .bubble-ai

9주차부터 Teachable Machine (브라우저 이미지 AI)입니다.
