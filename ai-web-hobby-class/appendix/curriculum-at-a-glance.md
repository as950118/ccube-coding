# 12주 커리큘럼 일람표 (Python + AI + 웹)

| 주 | Phase | Python (Flask) | 웹 | AI | 🟢 목표 |
|----|-------|----------------|-----|-----|---------|
| 1 | 기초 | `app.py` Run, `/` | HTML 자기소개 | 3층 구조 소개 | Run → 페이지 |
| 2 | 기초 | `render_template(name=...)` | CSS | — | Python 이름→화면 |
| 3 | 기초 | `def add`, `/api/add` | fetch | — | Python 계산 결과 |
| 4 | 기초 | OX dict, `/api/check` | O/X 버튼 | — | Python OX 채점 |
| 5 | AI | `/api/chat` + SDK | 질문·답 UI | OpenRouter | AI 답 |
| 6 | AI | `build_quiz_prompt()` | 퀴즈 영역 | AI 생성 | AI 퀴즈 |
| 7 | AI | 라우트 통합 | 탭·메뉴 | AI | 챗+퀴즈 한 앱 |
| 8 | AI | `messages[]` | 말풍선 | AI | 채팅 UI |
| 9 | 이미지 | `/` TM 섹션 | 업로드 | Teachable Machine | 분류 |
| 10 | 이미지 | — | 웹캠 | TM | 실시간 |
| 11 | 통합 | app.py 전체 | UI 통일 | 텍스트+이미지 | 완성 |
| 12 | 발표 | Deploy | 시연 | — | 1~2분 |

---

## Phase 요약

```
[1~4]  Python+Flask+웹     → fetch로 Python API (AI 없음)
[5~8]  Python이 AI 호출    → 텍스트 AI + 채팅 UI
[9~10] TM in browser       → 이미지 AI (같은 Flask 앱)
[11~12] 통합·Replit Deploy → 발표
```

---

## 메시지 체크 (매주)

- [ ] 수업 전: [chat-before-class](../messages/chat-before-class-template.md)
- [ ] 수업 후: [chat-after-class](../messages/chat-after-class-template.md)
- [ ] 일요일: [email-weekly-letter](../messages/email-weekly-letter-template.md)

---

## 참고 코드

- Flask + fetch: `pokemon/app.py`, `pokemon/templates/index.html`
- 3층 다이어gram: [architecture.md](architecture.md)
