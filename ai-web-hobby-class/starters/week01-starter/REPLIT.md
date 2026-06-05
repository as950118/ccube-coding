# Replit 템플릿 — 1주차 starter (Flask)

**Python + Flask** 로 HTML 페이지를 보내는 첫 주입니다.  
정적 HTML이 아니라 **서버(주방) → 화면(홀)** 구조를 체험합니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week01-starter` 폴더 업로드 또는 Import
3. **Run** → 미리보기에서 자기소개 페이지 확인
4. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭 (중요!)
3. `templates/index.html` → 🟢 이름·소개 수정
4. 미리보기 새로고침

## 파일 안내

| 파일 | 1주차 |
|------|-------|
| `app.py` | 읽기만 — Flask 서버 |
| `templates/index.html` | ✅ 🟢 수정 |
| `static/style.css` | 읽기 (2주~) |
| `static/script.js` | 읽기 (3주~ fetch) |

## 3층 구조 (1주차 소개)

```
Run → app.py (Python) → templates/index.html (웹) → 브라우저
                              ↓
                        5주~ AI API (Python이 호출)
```

## 문제 해결

| 증상 | 해결 |
|------|------|
| 페이지 안 보임 | **Run** 다시 클릭 |
| index.html만 열었는데 다름 | Flask Run 으로 봐야 함 |
| ModuleNotFoundError: flask | Replit이 requirements 설치 대기 후 Run |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- Flask + fetch 패턴: 저장소 `pokemon/app.py`
- 커리큘럼: `ai-web-hobby-class/weeks/week01-html-intro.md`
