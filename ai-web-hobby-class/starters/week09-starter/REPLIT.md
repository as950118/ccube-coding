# Replit 템플릿 — 9주차 starter (Teachable Machine)

Flask 페이지 안에서 **브라우저 이미지 AI**로 분류합니다. API 키 불필요!

## 템플릿 만들기 (교사)

1. `week09-starter` 업로드 / Import
2. 수업 전 2클래스 TM 모델 1개 만들어 `MODEL_URL` 예시 준비
3. Run → 업로드·분류 시연
4. Create Template

## 학생 안내

1. Fork → Run
2. [Teachable Machine](https://teachablemachine.withgoogle.com/) 에서 모델 만들기 (🟡)
   - 또는 교사가 공유한 `MODEL_URL` 사용 (🟢)
3. `app.py` 의 `MODEL_URL` 붙여넣기 (끝에 `/`)
4. Run 재시작 → 사진 선택 → 분류하기

## 파일 안내

| 파일 | 9주차 |
|------|-------|
| `app.py` | `MODEL_URL` (🟢) |
| `templates/index.html` | `#image-ai` + TM 스크립트 |
| `static/script.js` | `tmImage.load` / `predict` (🟡한글 · 🔴%) |
| `static/style.css` | 🟢 `.result` |

## 문제 해결

| 증상 | 해결 |
|------|------|
| 모델 로드 실패 | URL 끝 `/` 확인, TM Share 공개 |
| YOUR_MODEL_ID 경고 | `app.py` MODEL_URL 교체 후 Run |
| 분류 버튼 비활성 | 모델 로드·사진 선택 후 |

## 참고

- 커리큘럼: `weeks/week09-teachable-machine.md`
- 완성 예: `starters/reference/week09-complete/`
