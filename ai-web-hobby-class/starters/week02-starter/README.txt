AI웹반 2주차 starter — Python 변수 + CSS
==========================================

🟢 app.py 의 [🟢] 변수(STUDENT_NAME, INTRO 등) 2~3곳만 바꾸면 OK!
   Run → 페이지에 이름·소개가 자동 반영됩니다.
🟡 시간 남으면 static/style.css 에서 .header 배경색·h1 색 바꿔보세요.
🔴 FAVORITE_FOODS list + template for loop (교사 힌트 참고)
❓ 막히면 starter 를 다시 Fork. 과제는 선택!

실행 (Replit)
-------------
1. Run 버튼
2. app.py 에서 STUDENT_NAME = "내이름" 수정
3. 미리보기 새로고침 → h1 이 바뀌었는지 확인

핵심 개념
---------
app.py (Python 변수) → render_template → templates/index.html {{ name }}

폴더 구조
---------
app.py              ← 🟢 Python 변수 수정
templates/index.html ← {{ name }} 등 (읽기·이해)
static/style.css    ← 🟡 CSS 꾸미기
static/script.js    ← 3주차부터 fetch
requirements.txt

5주차부터 app.py 가 AI API 를 호출합니다.
