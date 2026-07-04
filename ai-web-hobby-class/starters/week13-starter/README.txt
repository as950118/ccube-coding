AI웹반 13주차 starter — Flask + SQLite 스마트홈 대시보드
=========================================================

🟢 Flask 서버 실행 → 스마트홈 평면도 화면 확인 → 장치 버튼 눌러보기
🟡 app.py 에 랜덤 이벤트 1개 더 추가하기
🔴 장치 1개를 더 만들고 SQLite 까지 연결하기

실행 (Replit / 로컬)
-------------------
1. Run 버튼 또는 `python app.py`
2. 브라우저에서 대시보드 열기
3. 전등 / 에어컨 / 선풍기 버튼 눌러 상태 바뀌는지 확인
4. `물 주기` 버튼 눌러 토양 습도 올라가는지 확인
5. F12 → Network 탭에서 GET `/api/status`, POST `/api/device/toggle` 확인

핵심 개념
---------
브라우저(JS) → fetch → Flask(Python) → SQLite 저장 → JSON → 화면
센서 값은 진짜 장비가 아니라 Python 이 조금씩 계산합니다.
그래도 DB 에 저장되기 때문에 더 "진짜 시스템"처럼 느껴집니다.

DB
--
- `smarthome.db` 는 첫 실행 때 자동 생성됩니다.
- 상태를 처음부터 다시 시작하고 싶으면 `smarthome.db` 를 지우고 다시 실행하세요.

폴더 구조
---------
app.py                ← Flask + SQLite + 센서 시뮬레이션
templates/index.html  ← 평면도형 스마트홈 화면
static/style.css      ← 카드 + 방 구조 + CSS 2.5D
static/script.js      ← fetch + 1초마다 상태 갱신
requirements.txt      ← Flask

추천 실습
---------
1. `STUDENT_NAME` 바꾸기
2. 위험 기준 (예: 29도 이상) 바꾸기
3. 이벤트 문장 1개 추가하기
4. 새 장치 만들기 (예: 가습기 / TV / 창문)
