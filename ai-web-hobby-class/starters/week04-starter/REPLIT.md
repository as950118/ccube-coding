# Replit 템플릿 — 4주차 starter (Flask + OX 퀴즈)

**브라우저**는 O/X만 보내고, **Python**이 문제·정답·채점을 담당합니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week04-starter` 폴더 업로드 또는 Import
3. **Run** → O/X 버튼 클릭 → 맞/틀 확인
4. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. Q1 **O** 클릭 → 「맞아요!」 확인
4. Q2 **O** 클릭 → 「틀려요」 확인 (정답은 X)
5. F12 → **Network** 탭에서 `/api/check?q=0&answer=O` 확인

## 파일 안내

| 파일 | 4주차 |
|------|-------|
| `app.py` | `QUESTIONS` dict, `/api/check` (🟡 4번째 문제 · 🔴 `/api/score`) |
| `templates/index.html` | Jinja2 `{% for q in questions %}` (읽기) |
| `static/script.js` | O/X 클릭 → `fetch` |
| `static/style.css` | 🟢 `.feedback.correct` / `.wrong` 색 |

## 3층 구조 (4주차)

```
O/X 클릭 → script.js fetch → app.py check_answer() → JSON → 화면
```

3주차: `fetch('/api/add')` → 이번 주: `fetch('/api/check')` → 5주차: `fetch('/api/chat')`

## 문제 해결

| 증상 | 해결 |
|------|------|
| 맞/틀 안 나옴 | **Run** 다시 / F12 Console 확인 |
| 문제 문장 안 바뀜 | `app.py` 저장 후 Run 재시작 |
| fetch failed | `app.py` 에 `/api/check` 있는지 확인 |
| ModuleNotFoundError: flask | Replit이 requirements 설치 대기 후 Run |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week04-ox-quiz.md`
- 3주차와 차이: **계산 API** → **채점 API** (데이터는 여전히 Python)
- 완성 예: `starters/reference/week04-complete/`
