# 기술 스택 — Python + Flask + 웹 + AI

## 1. 전체 구조

```
Python 3.11+  +  Flask  +  HTML/CSS/JS  +  OpenRouter  +  Teachable Machine
     ↑              ↑            ↑                  ↑                    ↑
  규칙·AI호출    서버·API      화면·fetch        5~8주 텍스트 AI      9~10주 이미지 AI
```

아키텍처: [architecture.md](architecture.md)

---

## 2. 개발 환경

| 도구 | 용도 |
|------|------|
| **Replit (Python Repl)** | Flask Run, Secrets, Deploy — **취미반 1순위** |
| VS Code + venv | 교사 로컬·고급 학생 |
| `pokemon/app.py` | Flask + fetch 패턴 **참고 코드** |

### Replit 설정
- `.replit`: `run = "python app.py"` 또는 gunicorn
- Secrets: `OPENROUTER_API_KEY` (또는 직접 `GEMINI_API_KEY` 등)
- 학생 Repl = 템플릿 Fork

---

## 3. Python / Flask

### requirements.txt (기본)
```
flask>=3.0
```

### 5주차~ (AI)
```
flask>=3.0
openai>=1.0
```
또는 `google-generativeai` (Gemini)

### 학생이 건드리는 app.py 패턴
```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="홍길동")

@app.route("/api/chat", methods=["POST"])
def chat():
    question = request.json.get("question", "")
    # 🟢: prompt 문자열만 수정
    reply = call_ai(question)  # 교사/🟡: AI 호출
    return jsonify({"reply": reply})
```

---

## 4. 웹 (templates + static)

| 파일 | 역할 |
|------|------|
| `templates/index.html` | HTML, Jinja2 `{{ name }}` (2주~) |
| `static/style.css` | CSS |
| `static/script.js` | `fetch("/api/...")` — **3주~** |

### JS → Python fetch (3주~)
```javascript
const res = await fetch("/api/add?a=3&b=5");
const data = await res.json();
document.getElementById("result").textContent = data.sum;
```

---

## 5. AI (텍스트) — Python에서만 호출

**권장:** [OpenRouter](https://openrouter.ai) — OpenAI SDK 호환, 한 API 키로 여러 모델 사용

| 서비스 | Python | 비고 |
|--------|--------|------|
| **OpenRouter** | `openai` SDK + `base_url` | `google/gemma-4-31b-it:free` 등 — **5~8주 기본 (무료)** |
| Gemini (직접) | `google-generativeai` | 무료 티어, `call_ai()` 별도 구현 |

```python
# app.py — OpenRouter (starter 기본)
from openai import OpenAI

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"  # 무료 — openrouter.ai/collections/free-models

client = OpenAI(
    base_url=OPENROUTER_BASE_URL,
    api_key=os.environ["OPENROUTER_API_KEY"],
)
response = client.chat.completions.create(
    model=AI_MODEL,
    messages=[{"role": "user", "content": question}],
)
```

**금지:** 학생 `script.js`에 API 키 하드코딩  
**권장:** `os.environ["OPENROUTER_API_KEY"]` (Replit Secrets)

**무료 한도 (OpenRouter):** 분 20회 · 일 50회 (크레딧 $10 충전 시 일 1,000회). 다른 무료 모델: `openrouter/free` (자동 선택) 또는 [free-models](https://openrouter.ai/collections/free-models)

---

## 6. AI (이미지) — Teachable Machine

- **9~10주:** 브라우저에서 TM JavaScript API
- Flask `app.py`는 같은 `index.html` 안 **섹션/탭**만 제공
- 「텍스트 AI = Python」, 「이미지 AI = 브라우저」 차이를 9주차에 설명

---

## 7. 배포 (11~12주)

| 방법 | 비고 |
|------|------|
| **Replit Deploy** | Flask 그대로 — **추천** |
| GitHub Pages | 정적만 — Flask 불가 |

발표 URL = Replit Deploy 링크

---

## 8. 피하는 것

- Django, SQLAlchemy, JWT 로그인
- JS에서 OpenAI 직접 호출 (키 노출)
- PyTorch / 직접 모델 학습
- SMS·실제 이메일 발송 API

**대안:** `mailto:` 링크 (11주 🔴)

---

## 9. starter zip 규칙

```
week{N}-starter/
├── app.py                 ← 🟢🟡🔴 (Python)
├── requirements.txt
├── templates/index.html   ← 🟢 (HTML)
├── static/
│   ├── style.css          ← 🟢
│   └── script.js          ← 🟡 (fetch)
└── README.txt
```

- Week N = 1~(N-1) 기능 **app.py + template에 포함**
