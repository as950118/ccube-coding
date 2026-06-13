# 1주차 — Flask + HTML: 서버가 보내는 자기소개 페이지

**Phase:** Python + 웹 기초 | **소요:** 60~90분

---

## 🟢 목표 (전원)

Replit **Run** → Flask 서버가 **자기소개 HTML 페이지**를 브라우저에 보여준다.

---

## 이번 주의 3층 구조 (소개)

| 층 | 이번 주 | 다음에 |
|----|---------|--------|
| **Python/Flask** | `app.py`가 페이지를 **보내줌** | API·AI 호출 |
| **웹** | `templates/index.html` 수정 | CSS, fetch |
| **AI** | 「주방+셰프」 비유만 | 5주차부터 |

시각 자료: `pokemon/materials/visual/flow-browser-flask.html` (브라우저↔Flask)

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | starter Fork, **Run**, 미리보기 URL |
| 10~25분 | `app.py` 3줄 + `templates/index.html` 관계 |
| 25~55분 | 🟢: `h1`, `p` 이름·소개 수정 |
| 55~70분 | 🟡: 취미 `ul`/`li` |
| 70~85분 | 「Flask = 주방, HTML = 접시」30초 시연 |
| 85~90분 | 선택 과제 |

---

## starter 포함

```
app.py                 → @app.route("/") render_template
templates/index.html   → 🟢 수정 구역
static/style.css
requirements.txt
```

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `templates/index.html` — 이름, 소개 1문장
2. [ ] Run 후 스크린샷

### 🟡
3. [ ] 취미 목록 `ul`/`li`

### 🔴
4. [ ] `app.py`의 `STUDENT_NAME` 변수 바꾸고 template `{{ }}` 연결 (2주 미리보기)

---

## 교사 메모

- **index.html 직접 더블클릭 X** — 반드시 Flask **Run**
- `app.py`는 이번 주 **읽기만** (2주차부터 🟢)

---

## 다음 주 (Week02)

- Python 변수 → Jinja2 `{{ name }}` + CSS
