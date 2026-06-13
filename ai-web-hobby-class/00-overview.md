# 과정 개요

## 1. 과정 소개

중학교 취미반을 위한 **12주 Python + AI + 웹 프로그래밍** 과정입니다.

**Python(Flask)** 으로 서버·규칙·AI 호출을 만들고, **HTML/CSS/JavaScript** 로 화면을 꾸미며, **AI API** 와 **Teachable Machine** 으로 똑똑한 기능을 붙여 **「나만의 AI 학습 도우미」** 웹앱을 완성합니다.

> 단순 「JS로 AI만 호출」이 아니라, **브라우저 ↔ Python ↔ AI** 3층 구조를 체험하는 것이 이 과정의 핵심입니다.  
> 상세: [appendix/architecture.md](appendix/architecture.md)

---

## 2. 학습 목표

### 전체 목표
- **Python:** 변수, 함수, dict/list로 간단한 규칙을 짤 수 있다.
- **Flask:** `@app.route` 로 페이지와 JSON API를 만들 수 있다.
- **웹:** HTML/CSS로 화면을, JavaScript `fetch`로 서버와 통신할 수 있다.
- **AI:** Python에서 AI API를 호출하고, 결과를 웹에 표시할 수 있다.
- **(선택)** Teachable Machine으로 이미지 분류를 같은 사이트에 붙일 수 있다.
- 완성한 웹앱을 1~2분 내외로 시연·설명할 수 있다.

### 기대하지 않는 것 (취미반 기준)
- Django, DB, 로그인/회원가입
- 딥러닝 이론·직접 모델 학습 (코드)
- 복잡한 async·배포 인프라

---

## 3. 최종 프로젝트: AI 학습 도우미 (Flask 앱)

| 기능 | 주차 | Python | 웹 | AI |
|------|------|--------|-----|-----|
| 자기소개 페이지 | 1~2 | Flask `render_template` | HTML/CSS | — |
| 계산·OX 퀴즈 | 3~4 | 함수, dict, `/api/*` | fetch, 버튼 | — |
| AI 챗봇 | 5~8 | `/api/chat`, prompt | 말풍선 UI | OpenAI/Gemini |
| AI 퀴즈 생성 | 6~7 | `build_quiz_prompt()` | 표시 영역 | 텍스트 생성 |
| 이미지 분류 | 9~10 | (정적 라우트) | 업로드·웹캠 | Teachable Machine |
| 통합·발표 | 11~12 | `app.py` 통합 | 한 페이지 | 텍스트 + 이미지 |

---

## 4. 12주 로드맵

### Phase 1 — Python + 웹 기초 (1~4주)
- Flask로 HTML 페이지 서빙
- Python 변수·함수 + JSON API
- JS `fetch`로 Python과 대화
- OX 퀴즈 (정답은 **Python**이 판정)

### Phase 2 — Python + AI + 웹 (5~8주)
- **Python이 AI API 호출** (키는 서버·Secrets)
- AI 퀴즈 생성, 채팅 UI
- 대화 기록 (Python list + 말풍선)

### Phase 3 — 이미지 AI & 마무리 (9~12주)
- Teachable Machine (브라우저) + 같은 Flask 앱 안에 배치
- 웹캠, 전 기능 통합, Replit 배포·발표

---

## 5. 권장 기술 스택

| 구분 | 추천 | 이유 |
|------|------|------|
| **Python** | 3.11+ | Flask, AI SDK |
| **서버** | Flask | pokemon 프로젝트와 동일 패턴 |
| **실행** | Replit (Python Repl) | Flask + Secrets + Deploy |
| **AI (텍스트)** | OpenAI / Gemini | Python SDK, 5~8주 |
| **AI (이미지)** | Teachable Machine | 9~10주, 키 불필요 |
| **API 키** | Replit Secrets | `app.py`만 접근 |

자세한 내용: [appendix/tech-stack.md](appendix/tech-stack.md)

---

## 6. 수업 시간 배분 (90분 예시)

| 시간 | 내용 |
|------|------|
| 0~10분 | starter, **Run**, 브라우저↔Flask 흐름 |
| 10~25분 | 이번 주 Python **또는** 웹 개념 + 데모 |
| 25~60분 | 🟢 전원 완료 |
| 60~75분 | 🟡 / 🔴 |
| 75~90분 | 30초 시연, 선택 과제 |

---

## 7. starter 운영

```
week{N}-starter/
├── app.py
├── templates/index.html
├── static/style.css, script.js
└── requirements.txt
```

- Week N starter = 1~(N-1)주 기능 **이미 app.py·template에 포함**
- 과제 누락 학생도 Run → 🟢부터

---

## 8. 관련 문서

- 아키텍처: [appendix/architecture.md](appendix/architecture.md)
- 차별화·과제: [01-teaching-principles.md](01-teaching-principles.md)
- 채팅·이메일: [02-communication.md](02-communication.md)
- 평가: [03-assessment.md](03-assessment.md)
- 주차별: [weeks/](weeks/)
