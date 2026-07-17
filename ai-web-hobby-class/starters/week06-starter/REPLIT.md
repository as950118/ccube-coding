# Replit 템플릿 — 6주차 starter (Flask + AI 퀴즈 생성)

**Python**이 `build_quiz_prompt()`로 prompt를 만들고, **AI**가 퀴즈를 생성합니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week06-starter` 폴더 업로드 또는 Import
3. **Secrets** (🔒) → `OPENROUTER_API_KEY` = [OpenRouter](https://openrouter.ai/keys) API 키 입력
4. **Run** → 「퀴즈 생성하기」→ AI 퀴즈 확인
5. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. 「퀴즈 생성하기」클릭 → AI 퀴즈 확인
4. `app.py` 의 `DEFAULT_SUBJECT` 바꾸고 Run 재시작 → 다시 생성
5. F12 → **Network** 탭에서 `GET /api/generate-quiz` 요청·응답 JSON 확인

## 파일 안내

| 파일 | 6주차 |
|------|-------|
| `app.py` | `DEFAULT_SUBJECT` (🟢), `build_quiz_prompt()` (🟢🟡), `/api/generate-quiz` |
| `templates/index.html` | 과목 입력·퀴즈 결과 영역 |
| `static/script.js` | `fetch` GET `/api/generate-quiz` |
| `static/style.css` | 🟢 `.quiz-result` 색·배경 |

## 3층 구조 (6주차)

```
버튼 클릭 → script.js fetch → app.py build_quiz_prompt() → call_ai() → OpenRouter → JSON → 화면
```

5주차: `fetch('/api/chat')` → 이번 주: `fetch('/api/generate-quiz')` + **prompt 설계**

## 문제 해결

| 증상 | 해결 |
|------|------|
| AI 답 안 나옴 / rate limit | 무료 한도 초과 — 잠시 후 재시도 |
| ⚠️ API 키 안내 문구 | 교사가 Secrets `OPENROUTER_API_KEY` 설정 |
| fetch failed | `app.py` 에 `/api/generate-quiz` 있는지 확인 |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week06-ai-quiz-generator.md`
- 완성 예: `starters/reference/week06-complete/`
