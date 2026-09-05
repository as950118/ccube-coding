# 나만의 BBS — 구조화 버전 (v1)

6주차 BBS를 class·interface·디자인 패턴(MVC/DI/IoC/POJO/헥사고날)으로 리팩터링하고, React 목록 화면을 추가한 버전입니다.

## 무엇인가요

`app.py`에 뒤섞여 있던 라우트·SQL·화면 로직을 Model(`models/`, `repositories/`)·View(`templates/`, `static/react-list.html`)·Controller(`app.py`)로 나눴습니다. 구조 리팩터링은 AI 없이 직접 했고, React 화면만 도전 과제로 AI와 함께 만들었습니다.

## 어떻게 열어보나요

```
pip install flask
python app.py
```

- `http://localhost:5001` — 기존 화면(목록/상세/작성/수정/삭제/검색)
- `http://localhost:5001/static/react-list.html` — React 목록 화면

## 폴더 구조

```
├── app.py
├── models/post.py
├── repositories/
│   ├── post_repository.py
│   ├── sqlite_post_repository.py
│   └── memory_post_repository.py
├── templates/
└── static/react-list.html
```

## 다음에 할 일

- [ ] Repository를 하나 더 만들어 어댑터 교체 감각 익히기
- [ ] React 화면에 작성 폼도 추가해보기
- [ ] 커스텀 커맨드·MCP로 워크플로 자동화 (Week8)
