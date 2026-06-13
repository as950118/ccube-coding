# 2주차 — Python 변수 + CSS: Flask가 이름을 화면에

**Phase:** Python + 웹 기초 | **소요:** 60~90분

---

## 🟢 목표 (전원)

`app.py`의 **Python 변수**를 바꾸면 → 페이지 **제목·이름**이 함께 바뀐다 (+ CSS로 색 꾸미기).

---

## 이번 주의 3층 구조

| 층 | 이번 주 | 다음에 |
|----|---------|--------|
| **Python/Flask** | 변수 → `render_template` | 함수 + `/api/...` |
| **웹** | Jinja2 `{{ name }}` + CSS | fetch |
| **AI** | — | 5주차부터 |

시각 자료: `pokemon/materials/visual/flow-browser-flask.html` (1주와 동일, 「데이터는 Python」강조)

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week02 starter Fork, **Run** |
| 10~25분 | `STUDENT_NAME = "홍길동"` → `{{ name }}` in template |
| 25~55분 | 🟢: `app.py` 🟢 구역 변수 2~3개 |
| 55~70분 | 🟡: `style.css` 배경·글자색 |
| 70~85분 | 「Python=데이터, HTML=화면」30초 시연 |
| 85~90분 | 선택 과제 |

---

## starter 포함

```
app.py                 → [🟢] STUDENT_NAME, INTRO, HOBBY
templates/index.html   → {{ name }}, {{ intro }} (읽기·이해)
static/style.css       → [🟡] .header, h1 색
requirements.txt
```

---

## Python ↔ 웹 연결 (핵심)

```python
# app.py — [🟢]
STUDENT_NAME = "홍길동"
HOBBY = "축구"

return render_template("index.html", name=STUDENT_NAME, hobby=HOBBY)
```

```html
<!-- templates/index.html -->
<h1>{{ name }}</h1>
<p>취미: {{ hobby }}</p>
```

> 「Python이 데이터, HTML이 화면」— 3주차 API의 준비

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `STUDENT_NAME`, `INTRO` 수정
2. [ ] Run → 이름·소개 반영 확인 + 스크린샷

### 🟡
3. [ ] `.header` 배경색, `h1` 글자색 CSS 변경

### 🔴
4. [ ] `FAVORITE_FOODS` list → template에서 `{% for food in favorite_foods %}` (교사 힌트 제공)

---

## 교사 메모

- **1주차와 차이:** HTML 직접 수정 → **`app.py` 변수** 수정
- `templates/index.html`의 `{{ name }}`은 **그대로 두고** app.py만 바꿔도 됨
- 🔴 for loop는 starter 주석 해제 + `app.py`에 `favorite_foods=` 전달 필요
- 완성 예: `starters/reference/week02-complete/`

---

## 다음 주 (Week03)

- Python **함수** `add(a,b)` + `/api/add` + JS fetch
