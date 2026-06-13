# 8주차 — Python 대화 기록 + 채팅 UI

**Phase:** Python + AI + 웹 | **소요:** 60~90분

---

## 🟢 목표 (전원)

질문·AI 답이 **말풍선**으로 2줄 이상 쌓임. (기록은 Python list 또는 JS — starter에 선택)

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10min | Week08 starter |
| 10~25min | `.bubble-user`, `.bubble-ai`, `appendMessage()` |
| 25~55min | 🟢: 말풍선 색 |
| 55~70min | 🟡: `/api/chat` 가 `history` 반환 (Python list) |
| 70~85min | 30초 시연 |
| 85~90min | 선택 과제 |

---

## Python + 웹 분담 (🟡)

```python
# app.py
messages: list[dict] = []

@app.route("/api/chat", methods=["POST"])
def api_chat():
    q = request.json["question"]
    reply = call_ai(q)
    messages.append({"role": "user", "text": q})
    messages.append({"role": "ai", "text": reply})
    return jsonify({"reply": reply, "history": messages})
```

> **텍스트 AI 파트(5~8주) 완료** — 9주부터 **이미지 AI**

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] 말풍선 색 2종
2. [ ] 대화 2턴 테스트

### 🟡
3. [ ] Enter 전송

### 🔴
4. [ ] `/api/clear` — Python list 비우기

---

## 다음 주 (Week09)

- **Teachable Machine** — 브라우저 이미지 AI (같은 Flask 앱 안)
