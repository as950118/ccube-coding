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
- [ ] week06 ~ week12

## reference

🟡🔴 완성 예: `reference/week{N}-complete/`

## zip

교사 Drive 업로드용: `week{N}-starter.zip` (폴더 압축)

```bash
cd starters && zip -r week02-starter.zip week02-starter \
  -x "*.DS_Store" -x "*__pycache__*" -x "*.pyc"
```
