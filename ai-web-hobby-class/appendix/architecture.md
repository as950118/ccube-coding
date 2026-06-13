# 아키텍처 — Python + 웹 + AI 를 어떻게 묶는가

## 1. 왜 3가지를 같이 배우나?

| 층 | 역할 | 비유 |
|----|------|------|
| **웹 (HTML/CSS/JS)** | 화면 · 버튼 · 입력 | 카페 **홀** (손님이 보는 곳) |
| **Python (Flask)** | 규칙 · 계산 · AI 호출 | 카페 **주방** (일 처리) |
| **AI (API / TM)** | 똑똑한 답 · 문제 생성 · 이미지 분류 | **특급 셰프** (주방에서 부름) |

> **AI + 웹 결합** = 브라우저에서 버튼을 누르면 **Python이 AI를 호출**하고, 결과를 **웹 화면**에 보여주는 흐름

JS만으로 AI API를 직접 호출하는 방식은 **키 노출·보안** 문제가 있어, 이 과정에서는 **Python(Flask)이 AI의 문지기** 역할을 합니다.

---

## 2. 데이터 흐름 (전 과정 공통)

```
[학생] 버튼 클릭 / 질문 입력
        ↓
[JavaScript] fetch("/api/...")  ← 웹
        ↓
[Flask app.py] Python 함수 실행  ← Python
        ↓
(5주차~) OpenRouter API              ← AI
        ↓
JSON 응답 → JS가 화면에 표시     ← 웹
```

**1주차:** Flask가 HTML 페이지만 보냄 (아직 API 없음)  
**3주차~:** `/api/add` 같은 Python API 등장  
**5주차~:** `/api/chat` 에서 Python이 AI 호출  
**9주차~:** Teachable Machine은 **브라우저에서** 이미지 AI (같은 페이지 안의 두 번째 AI)

---

## 3. 프로젝트 폴더 구조 (starter 공통)

```
week{N}-starter/
├── app.py              ← Python · Flask · AI 호출 (🟢🟡🔴)
├── requirements.txt
├── templates/
│   └── index.html      ← HTML (🟢)
├── static/
│   ├── style.css       ← CSS (🟢)
│   └── script.js       ← fetch · 화면 갱신 (🟡)
└── README.txt
```

---

## 4. 주차별 — 누가 무엇을 하나?

| 주 | Python | 웹 | AI |
|----|--------|-----|-----|
| 1 | Flask로 페이지 서빙 | HTML 자기소개 | (개념 소개) |
| 2 | 변수 → template | CSS 꾸미기 | — |
| 3 | `def add()` + `/api/add` | fetch + 결과 표시 | — |
| 4 | OX 문제·정답 dict, `/api/check` | O/X 버튼 | — |
| 5 | `/api/chat` + AI SDK | 질문 입력·답 표시 | OpenRouter |
| 6 | `build_quiz_prompt()` | 퀴즈 영역 | AI 생성 |
| 7 | 라우트 통합 | 탭·메뉴 | AI |
| 8 | `messages[]` 저장 | 말풍선 UI | AI |
| 9 | (선택) TM 페이지 라우트 | 이미지 업로드 UI | Teachable Machine |
| 10 | — | 웹캠 | TM |
| 11 | app.py 전 기능 | 한 페이지 | 텍스트 AI + 이미지 AI |
| 12 | — | 발표·배포 | 시연 |

---

## 5. 포켓몬 배틀 프로젝트와의 연결

저장소의 `pokemon/app.py` 와 **같은 패턴**입니다.

| 포켓몬 배틀 | AI 학습 도우미 |
|-------------|----------------|
| `attack()` Flask 라우트 | `/api/chat` |
| Python `Pokemon` 클래스 | Python `questions` dict |
| JS `fetch('/attack?skill=...')` | JS `fetch('/api/chat', ...)` |
| JSON `{ message, hp }` | JSON `{ reply }` |

함수·클래스 수업 경험이 있으면 Flask + AI로 자연스럽게 이어집니다.

---

## 6. 시각 자료 (프로젝터용)

`visual/flow-browser-flask-ai.html` — 브라우저 ↔ Flask ↔ AI 3단 다이어그램 (추가 예정)

포켓몬 자료의 `flow-browser-flask.html` 을 1~2주차에 임시로 사용해도 됩니다.
