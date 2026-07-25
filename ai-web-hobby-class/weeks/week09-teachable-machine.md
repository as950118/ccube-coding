# 9주차 — Teachable Machine: 두 번째 AI (이미지)

**Phase:** 이미지 AI | **소요:** 60~90분

---

## 🟢 목표 (전원)

Flask 페이지 안 **이미지 AI 섹션** — TM 모델 URL → 업로드 → 분류 결과.

---

## 텍스트 AI vs 이미지 AI

| | 5~8주 | 9~10주 |
|--|-------|--------|
| AI 종류 | OpenAI/Gemini | Teachable Machine |
| 호출 위치 | **Python** (Flask) | **브라우저** (JS) |
| 이유 | 키·prompt 보호 | TM이 브라우저용 설계 |

> **둘 다 AI + 웹** — 「누가 AI를 부르나」만 다름

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~15분 | TM 데모 (교사), 2클래스 모델 |
| 15~25분 | Week09 starter, `#image-ai` 섹션 |
| 25~55분 | 🟢: `MODEL_URL` 붙여넣기 |
| 55~70분 | 🟡: 클래스명 한글 |
| 70~85분 | 30초 시연 |
| 85~90분 | 선택 과제 |

---

## Flask 역할

- `/` template에 TM `<script>` 포함
- (선택) `@app.route("/image-lab")` 별도 페이지

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] MODEL_URL 테스트
2. [ ] 결과 CSS

### 🟡
3. [ ] 본인 TM 모델 만들기

### 🔴
4. [ ] 확률 % 표시

---

## starter 포함

```
app.py                 → [🟢] MODEL_URL (Flask는 페이지·URL만)
templates/index.html   → #image-ai + TM CDN 스크립트
static/script.js       → tmImage.load / predict (🟡한글 · 🔴%)
static/style.css       → [🟢] .result
requirements.txt       → flask (openai 불필요)
```

완성 예: `starters/reference/week09-complete/`

---

## 다음 주 (Week10)

- 웹캠 + TM
