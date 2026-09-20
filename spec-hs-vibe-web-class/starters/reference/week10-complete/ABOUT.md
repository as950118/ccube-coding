# AI 학교생활 도우미 (OpenAI API + 나이스 급식) — 교사 참고 · 완성 예시

**수업안:** [../../../weeks/week10-ai-service.md](../../../weeks/week10-ai-service.md)

학생용 starter는 [../../week10/](../../week10/) 입니다.
이 폴더는 **조교·교사 참고용**입니다. 수업 중에는 학생에게 통째로 배포하지 않고, 막힌 부분만 해당 함수를 보여줍니다.
학생이 수업 자료(docs 10주차)의 5장 코드를 직접 따라 치는 것이 핵심입니다.

## 이 예시에 대해

10주차 자료의 `school_bot` 구조(`app.py` · `neis.py` · `templates/index.html`)를 **OpenAI API 기준**으로 구현했습니다.
원 자료(Gemini)와의 대응:

| 개념 | Gemini (`google-genai`) | 이 예시 (`openai`) |
|------|------------------------|--------------------|
| 클라이언트 | `genai.Client()` (`GEMINI_API_KEY`) | `OpenAI()` (`OPENAI_API_KEY`) |
| 단일 대화 | `models.generate_content(contents=...)` | `responses.create(input="...")` |
| 연속 대화 | `chats.create()` + `send_message()` (SDK가 기록 관리) | **대화 기록 리스트를 직접 유지**해 매번 `input=[...]`로 전달 |
| 시스템 지침 | `GenerateContentConfig(system_instruction=)` | `instructions=` |
| 이미지 | `types.Part.from_bytes(...)` | `{"type":"input_image","image_url":"data:image/png;base64,..."}` |
| 응답 텍스트 | `response.text` | `response.output_text` |

> 교육 포인트: OpenAI에는 `chats.create`에 해당하는 "세션 객체"가 없다. 그래서 **"연속 대화 = 이전 대화를 매번 함께 보내는 것"** 이라는 원리가 코드에 그대로 드러난다(`chat_with_history`).

원 자료 대비 바뀐 점(의도적):
- **나이스 키 하드코딩 제거** — `NEIS_API_KEY` 환경 변수(선택). 키가 없어도 샘플 모드(5건)로 동작한다. 키를 코드에 쓰지 않는다는 오늘의 성공 기준과 모순되지 않게 하려는 것.
- 챗봇 응답을 `innerHTML`이 아닌 `textContent`로 렌더링(응답 속 HTML 실행 방지), 챗 기록을 서버에서 다시 그려 POST 후에도 유지.
- 급식: 조식·중식·석식 중 **중식 우선**, 알레르기 번호표를 프롬프트에 함께 제공(AI가 번호 뜻을 추측하지 않도록).
- 오류(429·인증 실패)를 화면에 친절한 문장으로 표시, 업로드 5MB 제한.

## 파일

```
week10-complete/
├── ABOUT.md            ← 이 안내 (교사용)
├── README.md           ← 완성된 프로젝트 README 예시
├── app.py              ← Flask 서버 (급식·공지·사진·챗봇 라우트, 세션별 대화 기록)
├── neis.py             ← 나이스 API 모듈 (학교코드·오늘 급식)
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html      ← 원문(초록)/AI 해설(보라) 영역 분리 화면
└── notes/
    ├── ai-log.md           ← 실험 기록 예시
    └── why-ai-service.md   ← 회고 예시
```

## 실행 방법 (시연용)

```
pip install -r requirements.txt
cp .env.example .env    # OPENAI_API_KEY 입력
python app.py
```

`http://localhost:5001` — 학교 이름 조회 → 원문/AI 해설 분리 확인 → 챗봇에 "내일 체육 준비물은 물이야" 후 "내일 뭘 챙겨야 해?" → 「초기화」 → 다시 질문(모르게 됨) → 다른 브라우저(시크릿 창)에서 대화가 섞이지 않는지 확인.

## 확인 포인트

- `app.py`: 키가 코드에 없는가 (`OpenAI()`가 환경 변수를 읽음), `chat_with_history`가 기록을 매번 함께 보내는가
- `app.py`: `session["user_key"]` → `user_chats` 딕셔너리로 브라우저별 대화가 분리되는가
- `neis.py`: 원문을 가공하지 않고 `<br/>`만 줄바꿈으로 바꾸는가, 급식이 없을 때 AI를 호출하지 않는가
- `index.html`: 원문 영역(`.official`)과 AI 영역(`.ai`)이 시각적으로 분리되는가
- 실제 호출 검증(2026-09-20, 모델 `gpt-4.1-mini`): 나이스 학교 검색·중식 파싱, 챗봇 문맥 유지·초기화·브라우저 분리, 공지 요약, 사진(PNG) 판독, 급식 AI 브리핑(알레르기 번호 풀이 정확)을 실제 OpenAI 키로 확인했다. 사진은 선명한 합성 시간표 1장만 시험했으므로, 흐린 사진에서 「확인 필요」가 나오는지는 수업 전에 실물 사진으로 한 번 확인할 것.
- **챗봇은 시스템 지침이 공지 요약과 다르다.** 처음에 공지 요약용 지침(「제공된 공지에 없으면 확인 필요」)을 챗봇에도 썼더니, 학생이 대화로 알려준 「내일 체육 준비물은 물이야」를 「공지에 없다」며 기억하지 않았다. 그래서 챗봇은 `CHAT_PROMPT`(대화 중 알려준 내용은 근거로 사용, 대화에 없는 것만 「확인 필요」)를 쓴다 — 수업에서 「지침 하나가 동작을 좌우한다」는 사례로 보여줄 만하다.
