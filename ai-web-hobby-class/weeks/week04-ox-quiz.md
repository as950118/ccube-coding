# 4주차 — Python OX 퀴즈: 정답은 주방(Python)에서

**Phase:** Python + 웹 기초 | **소요:** 60~90분

---

## 🟢 목표 (전원)

O/X 버튼 → fetch `/api/check` → **Python이 정답 판정** → 「맞아요/틀려요」 JSON.

---

## 이번 주의 3층 구조

| 층 | 이번 주 | 다음에 |
|----|---------|--------|
| **Python/Flask** | `QUESTIONS` dict + `check_answer()` + `/api/check` | `/api/chat` + AI |
| **웹** | O/X 버튼 + 맞/틀 표시 | 질문·답 UI |
| **AI** | — | 5주차부터 |

시각 자료: `pokemon/materials/visual/flow-browser-flask.html` + 3주차 `fetch('/api/add')` 비교

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week04 starter Fork, 3주차 `fetch('/api/add')` 비교 |
| 10~25분 | `QUESTIONS` dict, `check_answer()`, `/api/check?q=0&answer=O` |
| 25~55분 | 🟢: `QUESTIONS[0]` 문장 수정 + O/X 클릭 테스트 |
| 55~70분 | 🟡: 문제 4번째 추가 (Python list) |
| 70~85분 | Phase1 리캡: Flask+fetch — 다음 주 **AI** |
| 85~90분 | 선택 과제 |

---

## starter 포함

```
app.py                 → [🟢] QUESTIONS, check_answer(), /api/check  (🟡 4번째 · 🔴 /api/score)
templates/index.html   → {% for q in questions %} O/X 버튼 (읽기·이해)
static/script.js       → [🟢] fetch /api/check
static/style.css       → [🟢] .feedback.correct / .wrong 색
requirements.txt
```

---

## Python ↔ 웹 역할 분담

| 역할 | 담당 |
|------|------|
| 문제·정답 데이터 | **Python** `QUESTIONS` |
| O/X 버튼·표시 | **웹** JS + HTML |
| 채점 | **Python** `/api/check` |

→ 5주차 AI도 **Python이 판단·호출**, 웹은 보여주기만

---

## 핵심 코드

```python
# app.py — [🟢]
QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
]

def check_answer(q_index: int, user_answer: str) -> bool:
    return user_answer.upper() == QUESTIONS[q_index]["answer"]

@app.route("/api/check")
def api_check():
    q_index = int(request.args.get("q", 0))
    user_answer = request.args.get("answer", "")
    correct = check_answer(q_index, user_answer)
    return jsonify({"correct": correct, "message": "맞아요! 🎉" if correct else "틀려요 😅"})
```

```javascript
// static/script.js — [🟢] fetch URL만 이해
const res = await fetch(`/api/check?q=${qIndex}&answer=${answer}`);
const data = await res.json();
feedbackEl.textContent = data.message;
```

> **3주차와 같은 패턴:** fetch → Flask → Python 함수 → JSON  
> **5주차와 같은 패턴:** fetch → Flask → (그때는 AI) → JSON

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `QUESTIONS[0]` 문장 변경 → Run → 화면 반영 확인
2. [ ] 맞/틀 색 CSS (`.feedback.correct`, `.feedback.wrong`)

### 🟡
3. [ ] `QUESTIONS` 에 문제 4번째 추가 (Python list)

### 🔴
4. [ ] 3문제 모두 답 → `/api/score` 로 총점 표시

---

## 교사 메모

- **3주차와 차이:** 계산 API → **채점 API** (데이터·로직은 여전히 Python)
- 수업 전 3주차 `fetch('/api/add')` 를 프로젝터로 보여주면 이해가 빠름
- F12 → **Network** 탭에서 `/api/check?q=0&answer=O` 요청·응답 JSON 확인 권장
- 문제 문장은 `app.py` 만 바꿔도 됨 — `templates/index.html` 의 `{% for %}` 는 그대로
- 🔴 `/api/score` 는 Python이 맞은 개수를 세는 방식 (starter 주석 해제)
- 완성 예: `starters/reference/week04-complete/`

---

## 다음 주 (Week05) ★ AI 시작

- `/api/chat` — **Python이 OpenAI/Gemini 호출**
