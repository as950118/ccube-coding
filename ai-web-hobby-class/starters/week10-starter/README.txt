AI웹반 10주차 starter — 웹캠 + Teachable Machine
==================================================

🟢 웹캠 켜기 → 「분류하기」로 결과 확인! (결과 라벨 CSS 꾸미기)
🟡 「지금 뭐야?」 버튼 — 계속 눌러보지 않아도 실시간으로 분류
🔴 확률 80% 이상일 때만 결과 강조 (script.js 주석 해제)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. 9주차와 같은 모델을 쓰거나, Teachable Machine 에서 새로 학습
   (teachablemachine.withgoogle.com → Image Project → Export → Upload → 링크 복사)
2. app.py 의 MODEL_URL 에 붙여넣기 (끝에 / 필수!)
3. Run → 카메라 허용 → 「분류하기」

카메라를 막았거나 카메라가 없는 기기라면?
-----------------------------------------
자동으로 9주차처럼 "사진 업로드" 모드로 바뀝니다. 그래도 🟢 완료할 수 있어요!

핵심 개념
---------
9주차: 사진 업로드 → model.predict()
10주차: tmImage.Webcam 으로 카메라 켜기 → 똑같은 model.predict()!
Flask 역할 = 페이지 + MODEL_URL 전달 (Python은 여전히 AI 호출 안 함)

폴더 구조
---------
app.py               ← 🟢 MODEL_URL
templates/index.html ← #image-ai 섹션 (웹캠 + 업로드 대체) + TM CDN
static/script.js     ← tmImage.Webcam · predict · 🟡 지금뭐야 · 🔴 80%↑ 강조
static/style.css     ← 🟢 .result / .webcam-container
requirements.txt     ← flask 만 (openai 불필요!)

11주차에서 텍스트 AI + 이미지 AI를 한 페이지로 전부 통합합니다.
