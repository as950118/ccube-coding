# Replit 템플릿 — 10주차 starter (웹캠 + Teachable Machine)

Flask 페이지 안에서 **브라우저 웹캠**으로 TM 이미지 분류를 합니다. API 키 불필요!

## 템플릿 만들기 (교사)

1. `week10-starter` 업로드 / Import
2. 수업 전 2클래스 TM 모델 1개 만들어 `MODEL_URL` 예시 준비 (9주와 같아도 무방)
3. Run → 카메라 허용 → 시연 (권한 거부 시 업로드 모드 대체도 함께 시연)
4. Create Template

## 학생 안내

1. Fork → Run
2. `app.py` 의 `MODEL_URL` 붙여넣기 (끝에 `/`) — 9주차 모델 재사용 가능
3. Run 재시작 → 카메라 허용 → 「분류하기」
4. (🟡) 「지금 뭐야?」로 실시간 분류 체험 + **JS 실습**: 「초기화」 버튼 + `addEventListener` 직접 추가 (`weeks/week10-webcam.md` 의 「JS 핵심 개념」 참고)
5. (🔴) `script.js` 의 80% 강조 코드 주석 해제 / 업로드 모드에도 「초기화」 추가

## 파일 안내

| 파일 | 10주차 |
|------|-------|
| `app.py` | `MODEL_URL` (🟢) |
| `templates/index.html` | `#image-ai` — 웹캠 모드 + 업로드 대체 모드 |
| `static/script.js` | `tmImage.Webcam` / `predict` (🟡 지금뭐야 · 초기화 버튼 실습 · 🔴 80%↑) |
| `static/style.css` | 🟢 `.result` / `.webcam-container` |

## 문제 해결

| 증상 | 해결 |
|------|------|
| 모델 로드 실패 | URL 끝 `/` 확인, TM Share 공개 |
| YOUR_MODEL_ID 경고 | `app.py` MODEL_URL 교체 후 Run |
| 카메라 권한 거부 | 자동으로 9주차 파일 업로드 모드로 전환 (교사 메모 참고) |
| Replit에서 카메라 안 뜸 | Replit은 HTTPS 라 보통 OK — 브라우저 카메라 권한 재확인 |

## 참고

- 커리큘럼: `weeks/week10-webcam.md`
- 9주차 starter: `starters/week09-starter/`
