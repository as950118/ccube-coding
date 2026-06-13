# 3주차 — Python 함수 + fetch: 브라우저가 Python에게 계산 부탁

**Phase:** Python + 웹 기초 | **소요:** 60~90분

---

## 🟢 목표 (전원)

웹에서 숫자 2개 입력 → **fetch** → **Python `add()`** → 결과 JSON → 화면 표시.

---

## 이번 주의 3층 구조

| 층 | 이번 주 | 다음에 |
|----|---------|--------|
| **Python/Flask** | `def add()` + `/api/add` + `jsonify` | OX 문제 dict |
| **웹** | `fetch` + 결과 `div` 표시 | O/X 버튼 |
| **AI** | — | 5주차부터 |

시각 자료: `pokemon/materials/visual/flow-browser-flask.html` + `pokemon`의 `fetch('/attack')` 비교

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week03 starter Fork, `pokemon`의 `fetch('/attack')` 비교 |
| 10~25분 | `def add(a,b)`, `@app.route("/api/add")`, `jsonify` |
| 25~55분 | 🟢: 숫자 3+5 테스트, F12 Console 확인 |
| 55~70분 | 🟡: `subtract` 함수 + `/api/sub` |
| 70~85분 | 「브라우저→Python→JSON」30초 시연 |
| 85~90분 | 선택 과제 |

---

## starter 포함

```
app.py                 → [🟢] add(), /api/add  (🟡 subtract)
templates/index.html   → 숫자 입력·버튼 (읽기·이해)
static/script.js       → [🟢] fetch URL 이해
static/style.css       → [🟡] .result 색·배경
requirements.txt
```

---

## 핵심 코드

```python
# app.py — [🟢]
def add(a: int, b: int) -> int:
    return a + b

@app.route("/api/add")
def api_add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"sum": add(a, b)})
```

```javascript
// static/script.js — [🟢] fetch URL만 이해
const res = await fetch(`/api/add?a=${a}&b=${b}`);
const data = await res.json();
```

> **AI 5주차와 같은 패턴:** fetch → Flask → (그때는 AI) → JSON  
> **포켓몬과 같은 패턴:** `fetch('/attack?skill=...')` → Python 함수 → JSON

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] 3+5 = 8 확인
2. [ ] 결과 `div` 색 바꾸기 (`static/style.css` 의 `.result`)

### 🟡
3. [ ] Python `subtract` + `/api/sub` + 빼기 버튼

### 🔴
4. [ ] 0 입력 시 「숫자를 입력하세요」 (Python 또는 JS)

---

## 교사 메모

- **2주차와 차이:** `render_template`로 페이지 전체 전달 → **fetch로 일부 데이터만** 요청
- 수업 전 `pokemon/templates/index.html` 의 `attack()` 함수를 프로젝터로 보여주면 이해가 빠름
- F12 → **Network** 탭에서 `/api/add?a=3&b=5` 요청·응답 JSON 확인 권장
- 🔴 검증은 Python(`return jsonify({"error": ...}), 400`) 또는 JS 둘 다 OK
- 완성 예: `starters/reference/week03-complete/`

---

## 다음 주 (Week04)

- OX 문제·정답을 **Python dict** — JS는 O/X만 전송
