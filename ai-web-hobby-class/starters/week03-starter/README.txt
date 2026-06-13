AI웹반 3주차 starter — Python 함수 + fetch
==========================================

🟢 숫자 2개 입력 → 더하기 버튼 → 3+5=8 확인!
   시간 남으면 static/style.css 의 .result 색·배경 바꿔보세요.
🟡 app.py 에 subtract 함수 + /api/sub 추가 (교사 힌트 참고)
🔴 0·빈 값 입력 시 「숫자를 입력하세요」 (Python 또는 JS)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. Run 버튼
2. 미리보기에서 숫자 3, 5 입력 → 더하기 클릭
3. 「3 + 5 = 8」 이 나오면 성공!

핵심 개념
---------
버튼 클릭 → script.js fetch → app.py add() → JSON → 화면

폴더 구조
---------
app.py              ← 🟢 add() 함수 · /api/add (🟡 subtract)
templates/index.html ← 숫자 입력·버튼 (읽기·이해)
static/script.js    ← 🟢 fetch (포켓몬 attack 과 같은 패턴)
static/style.css    ← 🟡 .result 색 바꾸기
requirements.txt

5주차부터 app.py 가 AI API 를 호출합니다.
