# Replit 템플릿 — 11주차 starter (통합)

**하나의 Flask 앱**에서 챗봇·퀴즈·OX·이미지 AI 메뉴 4개로 이동합니다.

## 템플릿 만들기 (교사)

1. [Replit](https://replit.com) → **Create Repl** → **Python**
2. `week11-starter` 폴더 업로드 또는 Import
3. **Secrets** (🔒) → `OPENROUTER_API_KEY` 설정
4. (선택) `app.py` 의 `MODEL_URL` 을 공개 TM 모델로 교체 — 9~10주차와 같아도 무방
5. **Run** → 메뉴 4개 전환 확인
6. Team → **Create Template**

## 학생 안내 (수업 첫 10분)

1. 템플릿 링크 → **Fork**
2. **Run** 클릭
3. 「AI 챗봇」·「AI 퀴즈」·「OX 퀴즈」·「이미지 AI」 메뉴 클릭해 보기
4. `app.py` 의 `APP_TITLE` · `STUDENT_NAME` 바꾸고 Run 재시작 → 확인
5. (선택) 9~10주차 본인 TM 모델 URL을 `MODEL_URL` 에 붙여넣기
6. (🟡) **JS 실습** — 챗봇 탭에 「지우기」 버튼 + `addEventListener` 직접 추가 (`weeks/week11-integration.md` 의 「JS 핵심 개념」 참고) / `TUTOR_PROMPT` · 다크모드 도전
7. (🔴) 퀴즈 탭에도 「지우기」 추가 / Replit **Deploy** → URL 확보 (12주차 발표용)

## 파일 안내

| 파일 | 11주차 |
|------|-------|
| `app.py` | `APP_TITLE`·`STUDENT_NAME`·`MODEL_URL` (🟢), `TUTOR_PROMPT` (🟡), `/api/chat`·`/api/generate-quiz`·`/api/check` |
| `templates/index.html` | 메뉴 4개(탭) + 패널 + footer `made by {{ name }}` |
| `static/script.js` | 메뉴 전환 + fetch(챗/퀴즈/OX) + TM 웹캠·업로드 대체 |
| `static/style.css` | 통일된 메뉴·패널 스타일 + 🟡 다크모드 힌트 |

## 라우트 한눈에

```
/                  → 전체 페이지 (메뉴 4개)
/api/chat          → AI 챗 (POST)
/api/generate-quiz → AI 퀴즈 (GET)
/api/check         → OX 채점 (GET)
(JS) tmImage       → 이미지 AI, Python 라우트 없음
```

## 문제 해결

| 증상 | 해결 |
|------|------|
| 메뉴가 안 바뀜 | `script.js` 로드·콘솔 에러 확인 |
| AI 답 안 나옴 | Secrets `OPENROUTER_API_KEY` 확인 |
| 이미지 AI 모델 로드 실패 | `MODEL_URL` 끝 `/` 확인, TM Share 공개 설정 |
| 카메라 권한 거부 | 자동으로 파일 업로드 모드로 전환 (정상) |
| 망가짐 | 템플릿 다시 Fork |

## 참고

- 커리큘럼: `ai-web-hobby-class/weeks/week11-integration.md`
- 이전 주차: `starters/week07-starter/`(라우트 통합), `starters/week10-starter/`(웹캠 TM)
