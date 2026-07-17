# 7주차 — Flask 라우트 통합: AI 학습 도우미 한 앱

**Phase:** Python + AI + 웹 | **소요:** 60~90분

---

## 🟢 목표 (전원)

**하나의 Flask 앱**에서 챗봇·퀴즈·(4주 OX) 탭/메뉴로 이동.

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~10분 | Week07 starter — `app.py` 라우트 목록 보기 |
| 10~25분 | `index.html` 섹션 + JS 탭 |
| 25~55분 | 🟢: 사이트 제목, 탭 이름 |
| 55~70분 | 🟡: `call_ai` system prompt 「친절한 튜터」 |
| 70~85분 | 중간 시연 (선택) |
| 85~90분 | 선택 과제 |

---

## app.py 라우트 (통합)

| 경로 | 역할 |
|------|------|
| `/` | 전체 페이지 |
| `/api/chat` | AI 챗 |
| `/api/generate-quiz` | AI 퀴즈 |
| `/api/check` | OX 채점 (4주) |

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `APP_TITLE` (Python) + 화면 제목
2. [ ] 탭 2개 클릭 확인

### 🟡
3. [ ] Python `TUTOR_PROMPT` 상수

### 🔴
4. [ ] OX를 세 번째 탭으로

---

## starter 포함

```
app.py                 → [🟢] APP_TITLE · [🟡] TUTOR_PROMPT · /api/chat · /api/generate-quiz · /api/check
templates/index.html   → 탭 UI (챗봇·퀴즈 · 🔴 OX 주석)
static/script.js       → 탭 전환 + fetch
static/style.css       → 탭·패널 스타일
requirements.txt       → flask + openai
```

완성 예: `starters/reference/week07-complete/` (OX 3탭 포함)

---

## 다음 주 (Week08)

- Python `messages: list[dict]` + 말풍선 UI
