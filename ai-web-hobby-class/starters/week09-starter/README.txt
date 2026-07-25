AI웹반 9주차 starter — Teachable Machine 이미지 AI
==================================================

🟢 MODEL_URL 붙여넣기 → 사진 업로드 → 분류 결과!
🟡 클래스명 한글 (LABEL_KO)
🔴 확률 % 표시 (script.js 주석 해제)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. Teachable Machine (teachablemachine.withgoogle.com)
   → Image Project → 클래스 2개 학습 → Export → Upload → 링크 복사
2. app.py 의 MODEL_URL 에 붙여넣기 (끝에 / 필수!)
3. Run → 사진 선택 → 분류하기

핵심 개념
---------
텍스트 AI(5~8주): Python이 OpenRouter 호출 (키 필요)
이미지 AI(9~10주): 브라우저가 TM 호출 (키 없음!)
Flask 역할 = 페이지 + MODEL_URL 전달

폴더 구조
---------
app.py               ← 🟢 MODEL_URL
templates/index.html ← #image-ai 섹션 + TM CDN
static/script.js     ← tmImage.load · predict
static/style.css     ← 🟢 .result
requirements.txt     ← flask 만 (openai 불필요!)

10주차에서 웹캠을 연결합니다.
