# 과정 개요

## 1. 과정 소개

중학교 취미반을 위한 **12주 AI + 웹 프로그래밍** 과정입니다.  
학생들은 HTML, CSS, JavaScript 기초를 배운 뒤 AI API와 간단한 이미지 분류를 웹 페이지에 연결하여, **「나만의 AI 학습 도우미」** 웹사이트를 완성합니다.

---

## 2. 학습 목표

### 전체 목표
- 웹 페이지의 기본 구조(HTML/CSS/JS)를 이해하고 직접 수정할 수 있다.
- 버튼·입력창 등 간단한 인터랙션을 만들 수 있다.
- AI API를 호출하여 질문하고 답을 화면에 표시할 수 있다.
- (선택) Teachable Machine으로 만든 모델을 웹에 연결할 수 있다.
- 완성한 웹사이트를 1분 내외로 시연·설명할 수 있다.

### 기대하지 않는 것 (취미반 기준)
- Python/Flask/Django 풀스택 개발
- 딥러닝 이론 (역전파, 손실 함수 등)
- 복잡한 백엔드·데이터베이스
- 실제 SMS/이메일 발송 API 연동

---

## 3. 최종 프로젝트: AI 학습 도우미

| 기능 | 포함 주차 | 설명 |
|------|-----------|------|
| 자기소개·레이아웃 | 1~2 | HTML/CSS 기본 |
| OX/계산 퀴즈 | 3~4 | JavaScript 기초 |
| AI 챗봇 | 5~8 | API + 말풍선 UI |
| AI 퀴즈 생성 | 6~7 | 텍스트 생성 활용 |
| 이미지 분류 | 9~10 | Teachable Machine |
| 통합 페이지 | 11 | 탭 또는 섹션으로 묶기 |
| 발표 | 12 | 전시회 |

**테마 변경 가능:** AI 일기 조언, 사물 구분 게임 등 — 5~10주 구조는 동일하게 유지

---

## 4. 12주 로드맵

### Phase 1 — 웹 기초 (1~4주)
- HTML/CSS로 페이지 만들기
- JavaScript로 버튼·입력·간단한 퀴즈

### Phase 2 — AI 연결 (5~8주)
- AI API로 챗봇
- AI로 퀴즈·학습 도우미 기능
- 채팅처럼 보이는 UI (말풍선, 대화 기록)

### Phase 3 — 이미지 AI & 마무리 (9~12주)
- Teachable Machine + 웹캠
- 기능 통합
- 발표회

---

## 5. 권장 기술 스택

| 구분 | 추천 | 이유 |
|------|------|------|
| 편집·실행 | Replit, CodePen, Glitch | 설치 없이 바로 시작 |
| AI | OpenAI API / Google Gemini API | 챗봇·퀴즈 생성 |
| 이미지 AI | Google Teachable Machine | 드래그앤드롭, 중학생 적합 |
| 호스팅 | GitHub Pages, Netlify, Vercel | 무료, URL 공유 쉬움 |
| API 키 | 선생님 발급·관리 | 학생에게 키 직접 노출 금지 |

자세한 내용: [appendix/tech-stack.md](appendix/tech-stack.md)

---

## 6. 수업 시간 배분 (90분 예시)

| 시간 | 내용 |
|------|------|
| 0~10분 | starter 배포, 실행, 이번 주 🟢 목표 |
| 10~25분 | 개념 설명 + 데모 |
| 25~60분 | 🟢 전원 완료 (개별 속도) |
| 60~75분 | 🟡 / 🔴 (선택) 또는 멘토링 |
| 75~90분 | 30초 시연, 선택 과제 안내 |

60분 수업: 시연 5분, 🟡 시간 10분 줄이기

---

## 7. 폴더·자료 운영

```
Google Drive / AI웹반 /
├── Week01/starter.zip
├── Week02/starter.zip
├── ...
├── Week12/starter.zip
└── FAQ.pdf
```

- **매주 같은 위치**에 starter 업로드 → 링크만 메시지에 붙이기
- 지난 주 기능이 starter에 **이미 포함** → 과제 누락 학생도 0에서 시작

---

## 8. 관련 문서

- 차별화·과제: [01-teaching-principles.md](01-teaching-principles.md)
- 채팅·이메일: [02-communication.md](02-communication.md)
- 평가·발표: [03-assessment.md](03-assessment.md)
- 주차별 상세: [weeks/](weeks/)
