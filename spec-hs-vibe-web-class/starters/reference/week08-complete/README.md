# 나만의 BBS (v2) — 공공데이터 대시보드

Flask + SQLite 게시판에 회원가입·로그인·권한(v1)과 공공데이터 API 대시보드(v2)를 더한 버전입니다.

## 무엇인가요

목록·상세·작성·수정·삭제 + 회원가입·로그인·본인 글만 수정/삭제 + 미세먼지 공공데이터 대시보드를
갖춘 게시판입니다. API 호출·가공·화면 표시는 AI 없이 직접 작성했고, 도전 과제(지역 필터·그래프
라이브러리 등)만 AI와 함께 확장했습니다.

## 왜 만들었나요

우리가 쓴 글만 보여주던 게시판에, 정부가 공개한 실제 데이터(미세먼지)를 가져와 보여주면 어떨지
궁금해서 시작했습니다. API가 실패해도 화면이 죽지 않도록 샘플 데이터로 대체하는 구조도 함께
연습했습니다.

## 어떻게 열어보나요

```
pip install -r requirements.txt
cp .env.example .env
# .env에 data.go.kr에서 발급받은 PUBLIC_DATA_API_KEY를 채운다 (안 채워도 샘플 데이터로 동작)
python app.py
```

`http://localhost:5001` 접속. `/dashboard`에서 대시보드 확인.

## 폴더 구조

```
├── app.py
├── opendata.py
├── data/
│   └── sample_air_quality.json
├── .env.example
├── templates/
│   ├── list.html / detail.html / new.html / edit.html
│   ├── signup.html / login.html
│   └── dashboard.html
└── notes/
    ├── opendata-log.md
    └── why-opendata.md
```

## 다음에 할 일

- [ ] Chart.js 등 그래프 라이브러리로 교체
- [ ] 조회 이력을 DB에 저장해 히스토리 페이지 만들기
- [ ] 미니앱(포트폴리오 #2) 주제로 다른 공공데이터 붙이기 (Week9)
