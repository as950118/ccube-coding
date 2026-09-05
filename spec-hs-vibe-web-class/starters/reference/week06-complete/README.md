# 나만의 BBS (v0)

Flask + SQLite로 만든 최소 게시판(BBS)입니다. 클라이언트-서버-DB 3단 구조를 손으로 만들어 본 첫 서비스형 프로젝트입니다.

## 무엇인가요

목록·상세·작성·수정·삭제를 갖춘 게시판입니다. 글을 쓰면 SQLite에 저장되고, 서버를 껐다 켜도 데이터가 유지됩니다. 핵심 기능은 AI 없이 직접 작성했고, 검색 기능만 도전 과제로 AI와 함께 추가했습니다.

## 왜 만들었나요

지금까지 만든 사이트는 파일을 열면 끝인 정적 페이지였습니다. 실제 웹 서비스가 어떻게 "저장하고 다시 불러오는지" 직접 만들어 보며 이해하고 싶어서 시작했습니다.

## 어떻게 열어보나요

```
pip install flask
python app.py
```

`http://localhost:5001` 접속.

## 폴더 구조

```
├── app.py
├── templates/
│   ├── list.html
│   ├── detail.html
│   ├── new.html
│   └── edit.html
└── notes/
    ├── architecture.md
    └── why-3tier.md
```

## 다음에 할 일

- [ ] class·interface로 구조 리팩터링 (Week7)
- [ ] React로 목록 화면 다시 만들기 (Week7)
