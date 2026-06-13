# Replit 템플릿 — 2주차 starter (Flask + 변수 + CSS)

**Python 변수**를 바꾸면 **HTML 화면**이 함께 바뀌는 구조를 배웁니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week02-starter` 폴더 업로드 또는 Import
3. **Run** → `app.py` 변수 수정 → 미리보기 확인
4. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. `app.py` → [🟢] `STUDENT_NAME`, `INTRO` 수정
4. 미리보기 새로고침 → `{{ name }}` 반영 확인

## 파일 안내

| 파일 | 2주차 |
|------|-------|
| `app.py` | ✅ 🟢 변수 수정 |
| `templates/index.html` | `{{ name }}` 이해 (직접 수정 X) |
| `static/style.css` | 🟡 배경·글자색 |
| `static/script.js` | 읽기 (3주~ fetch) |

## 3층 구조 (2주차)

```
app.py 변수 → render_template → index.html {{ }} → 브라우저
                    ↓
              style.css (꾸미기)
```

## 문제 해결

| 증상 | 해결 |
|------|------|
| 이름 안 바뀜 | `app.py` 저장 후 **Run** 다시 / 새로고침 |
| `{{ name }}` 그대로 보임 | `render_template` 에 `name=` 전달 확인 |
| ModuleNotFoundError: flask | Replit이 requirements 설치 대기 후 Run |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week02-css-buttons.md`
- 1주차와 차이: HTML 직접 수정 → **Python 변수** 수정
