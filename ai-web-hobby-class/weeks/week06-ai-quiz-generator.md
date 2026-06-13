# 6주차 — Python prompt + AI 퀴즈 생성

**Phase:** Python + AI + 웹 | **소요:** 60~90분

---

## 🟢 목표 (전원)

버튼 → `/api/generate-quiz` → **Python의 prompt 함수** → AI → 퀴즈 텍스트 화면.

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week06 starter |
| 10~25분 | `build_quiz_prompt(subject)` — 🟢: `subject` 문자열만 |
| 25~55분 | 🟢: 「영어 단어」→「과학」 등 |
| 55~70분 | 🟡: 4주차 OX 형식으로 파싱 (Python 또는 JS) |
| 70~85분 | 30초 시연 |
| 85~90분 | 선택 과제 |

---

## Python이 AI를 「부리는」 방법

```python
# [🟢]
def build_quiz_prompt(subject: str) -> str:
    return f"중학생용 {subject} 퀴즈 3문제를 OX 형식으로 만들어줘."

@app.route("/api/generate-quiz")
def api_quiz():
    subject = request.args.get("subject", "영어 단어")
    prompt = build_quiz_prompt(subject)
    text = call_ai(prompt)
    return jsonify({"quiz": text})
```

> AI + 웹: **prompt는 Python**, **표시는 웹**

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `subject` 기본값 변경
2. [ ] 결과 영역 CSS

### 🟡
3. [ ] prompt에 「쉬운 난이도」 추가

### 🔴
4. [ ] 생성 결과 → 4주차 `/api/check` 와 연동 아이디어

---

## 다음 주 (Week07)

- `/api/chat` + `/api/generate-quiz` 한 `index.html` 탭
