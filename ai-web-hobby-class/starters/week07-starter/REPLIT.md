# Replit 템플릿 — 7주차 starter (Flask 라우트 통합)

**하나의 Flask 앱**에서 챗봇·퀴즈 탭으로 이동합니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week07-starter` 폴더 업로드 또는 Import
3. **Secrets** (🔒) → `OPENROUTER_API_KEY` 설정
4. **Run** → 탭 전환 + 챗봇·퀴즈 확인
5. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. 「AI 챗봇」·「AI 퀴즈」 탭 클릭해 보기
4. `app.py` 의 `APP_TITLE` 바꾸고 Run 재시작 → 제목 확인
5. (선택) `TUTOR_PROMPT` 문장 바꿔 보기

## 파일 안내

| 파일 | 7주차 |
|------|-------|
| `app.py` | `APP_TITLE` (🟢), `TUTOR_PROMPT` (🟡), `/api/chat`·`/api/generate-quiz`·`/api/check` |
| `templates/index.html` | 탭 + 패널 (🔴 OX 탭 주석) |
| `static/script.js` | 탭 전환 + fetch |
| `static/style.css` | 탭·패널 스타일 |

## 라우트 한눈에

```
/                  → 전체 페이지
/api/chat          → AI 챗 (POST)
/api/generate-quiz → AI 퀴즈 (GET)
/api/check         → OX 채점 (🔴)
```

## 문제 해결

| 증상 | 해결 |
|------|------|
| 탭이 안 바뀜 | `script.js` 로드·콘솔 에러 확인 |
| AI 답 안 나옴 | Secrets `OPENROUTER_API_KEY` 확인 |
| OX 탭 안 보임 | `index.html` 에서 OX 탭 버튼 주석 해제 (🔴) |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week07-ai-study-helper.md`
- 완성 예: `starters/reference/week07-complete/`
