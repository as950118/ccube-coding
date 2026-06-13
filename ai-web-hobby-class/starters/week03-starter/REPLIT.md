# Replit 템플릿 — 3주차 starter (Flask + 함수 + fetch)

**브라우저**가 **Python**에게 계산을 부탁하는 `fetch` 패턴을 배웁니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week03-starter` 폴더 업로드 또는 Import
3. **Run** → 숫자 입력 → 더하기 → 결과 확인
4. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. 숫자 **3**, **5** 입력 → **더하기** 버튼
4. `3 + 5 = 8` 확인 → F12 Console 에러 없는지 확인

## 파일 안내

| 파일 | 3주차 |
|------|-------|
| `app.py` | `def add()`, `/api/add` 이해 (🟡 subtract) |
| `templates/index.html` | 입력·버튼 (읽기) |
| `static/script.js` | `fetch` 이해 — 포켓몬 `attack` 과 비교 |
| `static/style.css` | 🟡 `.result` 색·배경 |

## 3층 구조 (3주차)

```
버튼 클릭 → script.js fetch → app.py add() → JSON → 화면
```

포켓몬: `fetch('/attack?skill=...')` → 이번 주: `fetch('/api/add?a=...&b=...')`

## 문제 해결

| 증상 | 해결 |
|------|------|
| 결과 안 나옴 | **Run** 다시 / F12 Console 확인 |
| `NaN` 표시 | 숫자 입력란에 숫자 있는지 확인 |
| fetch failed | `app.py` 저장 후 Run 재시작 |
| ModuleNotFoundError: flask | Replit이 requirements 설치 대기 후 Run |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week03-js-input.md`
- 포켓몬 비교: `pokemon/templates/index.html` 의 `fetch('/attack')`
- 2주차와 차이: **render_template** → **fetch + API**
