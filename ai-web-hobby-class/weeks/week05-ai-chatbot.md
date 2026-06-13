# 5주차 — Python + AI: Flask가 AI에게 질문하기 ★

**Phase:** Python + AI + 웹 | **소요:** 60~90분

---

## 🟢 목표 (전원)

질문 입력 → fetch `/api/chat` → **Python이 AI API 호출** → `{ "reply": "..." }` → 화면 표시.

---

## 이번 주의 3층 구조 (드디어 완성!)

| 층 | 이번 주 | 다음에 |
|----|---------|--------|
| **Python/Flask** | `call_ai()` + `/api/chat` POST | `build_quiz_prompt()` |
| **웹** | 질문 입력·답 표시 | 퀴즈 생성 영역 |
| **AI** | OpenRouter (Python에서만) | prompt 설계 |

```
[JS fetch POST] → [Flask call_ai()] → [OpenRouter] → JSON → [화면]
```

- API 키: **Replit Secrets** — `app.py`만 접근
- JS에는 키 **없음** (보안!)

시각 자료: `appendix/architecture.md` §2 + 4주차 `fetch('/api/check')` 비교

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week05 starter Fork, **Secrets** `OPENROUTER_API_KEY` (교사) |
| 10~25분 | `call_ai(question)` — 🟢는 `DEFAULT_QUESTION`만 |
| 25~55분 | 🟢: `DEFAULT_QUESTION` 변경 → 기본 질문 보내기 |
| 55~70분 | 🟡: 입력창 질문 → POST JSON `{ "question": "..." }` |
| 70~85분 | 30초 시연: 「브라우저→Python→AI→화면」 |
| 85~90분 | 선택 과제 |

---

## starter 포함

```
app.py                 → [🟢] DEFAULT_QUESTION  (🟡 call_ai · 🔴 system prompt)
templates/index.html   → 질문 입력·답 영역 (읽기·이해)
static/script.js       → [🟢] fetch POST /api/chat  (🔴 로딩)
static/style.css       → [🟢] .reply 색·배경
requirements.txt       → flask + openai
```

---

## Python ↔ 웹 역할 분담

| 역할 | 담당 |
|------|------|
| AI API 호출·API 키 | **Python** `call_ai()` |
| 질문 입력·답 표시 | **웹** JS + HTML |
| 기본 질문 문장 | **Python** `DEFAULT_QUESTION` |

→ 4주차 채점도 Python이 했듯, **AI도 Python이 부름** — 웹은 보여주기만

---

## 핵심 코드

```python
# app.py — [🟢]
DEFAULT_QUESTION = "중학생에게 공부 팁 한 가지만 알려줘"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"

# [🟡] starter에 이미 연결됨 — SDK 호출 이해
def call_ai(question: str) -> str:
    client = OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=os.environ["OPENROUTER_API_KEY"],
    )
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content

@app.route("/api/chat", methods=["POST"])
def api_chat():
    q = (request.json or {}).get("question", "").strip() or DEFAULT_QUESTION
    return jsonify({"reply": call_ai(q), "question": q})
```

```javascript
// static/script.js — [🟢] fetch POST (4주차 GET과 다름!)
const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
});
const data = await res.json();
replyEl.textContent = data.reply;
```

> **4주차와 같은 패턴:** fetch → Flask → Python 함수 → JSON  
> **이번 주 차이:** Python 함수 뒤에 **AI API**가 붙음

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `DEFAULT_QUESTION` 바꾸기 → Run → 기본 질문 보내기
2. [ ] AI 답 스크린샷 + `.reply` CSS 색 변경

### 🟡
3. [ ] 입력창에 직접 질문 보내기

### 🔴
4. [ ] 「생각 중…」 로딩 (JS — starter 주석 해제)

---

## 교사 메모

- **수업 전 필수:** Replit 템플릿 Secrets에 `OPENROUTER_API_KEY` 설정 ([openrouter.ai/keys](https://openrouter.ai/keys), 학생 Repl은 Fork만)
- **4주차와 차이:** GET `/api/check` → **POST `/api/chat`** + AI 응답 (몇 초 걸림)
- F12 → **Network** 탭에서 `POST /api/chat` 요청 body·응답 JSON 확인 권장
- **무료 모델:** starter 기본값 `google/gemma-4-31b-it:free` (140+ 언어, $0). 다른 무료 모델은 [free-models](https://openrouter.ai/collections/free-models) 참고
- **무료 한도:** 계정당 분 20회·일 50회 (크레딧 $10 충전 시 일 1,000회) — 수업 전 교사 Repl에서 1회 테스트
- Gemini 직접 사용 시: `requirements.txt`에 `google-generativeai`, `call_ai()` 교체 (tech-stack.md 참고)
- 🔴 로딩은 AI 응답 대기 UX — 8주차 말풍선 UI로 발전
- 완성 예: `starters/reference/week05-complete/`

---

## 다음 주 (Week06)

- `build_quiz_prompt()` — Python prompt 설계 + AI
