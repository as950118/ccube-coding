# Replit 템플릿 — 5주차 starter (Flask + AI 챗봇) ★

**브라우저**는 질문만 보내고, **Python**이 AI API를 호출합니다. API 키는 **Secrets**에만!

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week05-starter` 폴더 업로드 또는 Import
3. **Secrets** (🔒) → `OPENROUTER_API_KEY` = [OpenRouter](https://openrouter.ai/keys) API 키 입력
4. **Run** → 「기본 질문 보내기」→ AI 답 확인
5. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. 「기본 질문 보내기」클릭 → AI 답 확인
4. `app.py` 의 `DEFAULT_QUESTION` 바꾸고 Run 재시작 → 다시 보내기
5. F12 → **Network** 탭에서 `POST /api/chat` 요청·응답 JSON 확인

## 파일 안내

| 파일 | 5주차 |
|------|-------|
| `app.py` | `DEFAULT_QUESTION` (🟢), `call_ai()` (🟡), `/api/chat` |
| `templates/index.html` | 질문 입력·답 영역 (읽기) |
| `static/script.js` | `fetch` POST (🔴 로딩) |
| `static/style.css` | 🟢 `.reply` 색·배경 |

## 3층 구조 (5주차 — AI 등장!)

```
버튼 클릭 → script.js fetch POST → app.py call_ai() → OpenRouter → JSON → 화면
```

4주차: `fetch('/api/check')` → 이번 주: `fetch('/api/chat')` → 6주차: `build_quiz_prompt()`

## 문제 해결

| 증상 | 해결 |
|------|------|
| AI 답 안 나옴 / rate limit | 무료 한도 초과 — 잠시 후 재시도 또는 교사 계정 크레딧 확인 |
| ⚠️ API 키 안내 문구 | 교사가 Secrets `OPENROUTER_API_KEY` 설정 |
| fetch failed | `app.py` 에 `/api/chat` 있는지 확인 |
| ModuleNotFoundError: openai | Replit이 requirements 설치 대기 후 Run |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week05-ai-chatbot.md`
- 4주차와 차이: Python 뒤에 **AI API**가 붙음 (키는 Python만)
- 완성 예: `starters/reference/week05-complete/`
