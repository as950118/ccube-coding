# 오늘 파일별 MVC 매핑 (예시)

| 파일 | M/V/C | 왜 그렇게 분류했나 |
|------|-------|---------------------|
| models/post.py | Model | 데이터(글 하나)를 표현하는 순수 객체 |
| repositories/post_repository.py | Model | 데이터 접근 방법의 "약속"(interface) |
| repositories/sqlite_post_repository.py | Model | 그 약속을 SQLite로 구현 |
| templates/*.html | View | 사용자가 보는 HTML 화면 |
| static/react-list.html | View | 같은 데이터를 다른 방식(React)으로 보여주는 또 다른 화면 |
| app.py | Controller | 요청을 받아 Model(repo)에 묻고 View에 넘김 |
