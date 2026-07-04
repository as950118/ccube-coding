# Python + AI + 웹 프로그래밍 취미반 — 12주 커리큘럼

**대상:** 중학교 (취미반, 수준 편차 있음)  
**기간:** 12주 (약 3개월)  
**주당:** 60~90분  
**최종 결과물:** Flask 기반 「나만의 AI 학습 도우미」웹앱

---

## 이 과정의 정체성

| ❌ 이전 (웹 위주) | ✅ 지금 (Python + AI + 웹) |
|------------------|---------------------------|
| 정적 HTML / JS만 | **Flask(Python)** 서버 |
| JS가 AI API 직접 호출 | **Python이 AI 호출** (키 보호) |
| 5주차부터야 AI | 1주차부터 「서버·웹·AI」 구조 소개 |
| OX 퀴즈 in JS | OX **정답 판정 in Python** |

→ [appendix/architecture.md](appendix/architecture.md) 에서 3층 구조 설명

---

## 폴더 구성

| 경로 | 용도 |
|------|------|
| [00-overview.md](00-overview.md) | 과정 개요, 로드맵 |
| [01-teaching-principles.md](01-teaching-principles.md) | 🟢🟡🔴, starter, 과제 |
| [02-communication.md](02-communication.md) | 카톡·이메일 |
| [03-assessment.md](03-assessment.md) | 평가·발표 |
| [appendix/architecture.md](appendix/architecture.md) | **Python+웹+AI 구조** |
| [weeks/](weeks/) | 주차별 수업 (12) |
| [messages/](messages/) | 메시지 템플릿 |
| [starters/](starters/) | Flask starter zip |

---

## 12주 한 줄 요약

| 주 | Python | 웹 | AI | 🟢 목표 |
|----|--------|-----|-----|---------|
| 1 | Flask 실행 | HTML 자기소개 | 구조 소개 | Run → 페이지 |
| 2 | template 변수 | CSS | — | Python 이름→화면 |
| 3 | `def add`, `/api/add` | fetch | — | Python 계산 |
| 4 | OX dict, `/api/check` | O/X 버튼 | — | Python 채점 |
| 5 | `/api/chat` + SDK | 질문 UI | **텍스트 AI** | AI 답 |
| 6 | quiz prompt | 표시 | AI 생성 | AI 퀴즈 |
| 7 | 라우트 통합 | 탭 | AI | 한 앱 |
| 8 | `messages[]` | 말풍선 | AI | 채팅 UI |
| 9 | 라우트 | 업로드 UI | **TM** | 이미지 분류 |
| 10 | — | 웹캠 | TM | 실시간 |
| 11 | app 통합 | 메뉴 | 둘 다 | 완성 |
| 12 | — | 발표 | 시연 | 1~2분 |

---

## 보너스 확장

- [weeks/week13-smart-home-dashboard.md](weeks/week13-smart-home-dashboard.md)  
  Flask + SQLite + 평면도형 스마트홈 대시보드. 웹이 센서와 장치를 제어하는 느낌을 주는 보너스 프로젝트입니다.

---

## 교사 체크리스트

- [ ] Replit **Python** Repl (Flask) 템플릿
- [ ] AI API 키 → Replit Secrets (`OPENROUTER_API_KEY`)
- [ ] `pokemon/` 프로젝트 — Flask 패턴 참고용
- [ ] 학부모 카톡 · 학생 디스코드
- [ ] Drive `AI웹반/Week01~12/`
- [ ] [messages/email-week0-orientation.md](messages/email-week0-orientation.md)

---

## starter 구조 (매주)

```
app.py              ← Python · Flask · (5주~) AI
templates/index.html
static/style.css
static/script.js
requirements.txt
```

---

## 보너스 단일 파일 예제

- `starters/reference/bonus-smart-home-dashboard/index.html`  
  HTML/CSS/JavaScript만으로 만든 가짜 IoT 스마트홈 대시보드 예제입니다. 학생들이 "웹이 장치를 제어하는 느낌"을 체험할 수 있는 독립 실행형 샘플입니다.

- `starters/reference/week13-threejs-demo/index.html`  
  Three.js 로 만든 3D 스마트홈 시연용 데모입니다. 교육용 starter 와 분리된, Flask + SQLite 기반 시각 효과 중심의 참고 예시입니다.
