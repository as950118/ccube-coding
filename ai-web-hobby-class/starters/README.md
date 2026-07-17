# starter 템플릿 (Flask)

주차별 `week{N}-starter/` — **Python + Flask + templates + static**

## 규칙

- [appendix/architecture.md](../appendix/architecture.md)
- [appendix/tech-stack.md](../appendix/tech-stack.md)
- [01-teaching-principles.md](../01-teaching-principles.md)

## 구조

```
week{N}-starter/
├── app.py                 ← Python · Flask · (5주~) AI
├── requirements.txt
├── templates/index.html
├── static/style.css
├── static/script.js
└── README.txt
```

## 진행

- [x] week01-starter — Flask + HTML 자기소개
- [x] week02-starter — Python 변수 + Jinja2 + CSS
- [x] week03-starter — Python 함수 + fetch API
- [x] week04-starter — Python OX 퀴즈 + /api/check
- [x] week05-starter — Python call_ai() + /api/chat (AI)
- [x] week06-starter — Python build_quiz_prompt() + /api/generate-quiz
- [x] week07-starter — 라우트 통합 (챗봇·퀴즈 탭, 🔴 OX)
- [x] week13-starter — Flask + SQLite + IoT 스마트홈 대시보드 (보너스)
- [ ] week08 ~ week12

## reference

🟡🔴 완성 예: `reference/week{N}-complete/`

추가 참고:
- `reference/week13-threejs-demo/` — Three.js + Flask + SQLite 기반 3D 스마트홈 시연용 예시

## zip

교사 Drive 업로드용: `week{N}-starter.zip` (폴더 압축)

```bash
cd starters && zip -r week02-starter.zip week02-starter \
  -x "*.DS_Store" -x "*__pycache__*" -x "*.pyc"
```
