# week10 — AI 서비스 연동: OpenAI API · 나이스 급식 (starter)

**수업안:** [../../weeks/week10-ai-service.md](../../weeks/week10-ai-service.md)
**학생용 자료:** [../../docs/2026진학반_10주차-draft.md](../../docs/2026진학반_10주차-draft.md) (아직 초안 — docx 미작성)

## 이 폴더 사용법

오늘은 **새 프로젝트 폴더 `school_bot/`을 만든다** (BBS와 별개). 이 폴더의 `step1~4` 파일은 수업 자료 2~4장의
실습 코드를 한 파일씩 실행해 볼 수 있게 담아 둔 것이다. 5장(Flask 웹 서비스)의 `app.py` · `neis.py` ·
`templates/index.html`은 **수업 자료를 보며 직접 작성**한다.

1. **환경 준비** — `python -m pip install -r requirements.txt`, 환경 변수 `OPENAI_API_KEY` 등록(PyCharm 실행 설정의 Environment variables, 또는 `.env`). 키를 코드에 적지 않는다.
2. `step1_single.py` — 단일 대화. 두 번 실행해 이전 내용을 기억하지 못함을 확인
3. `step2_chat.py` — 연속 대화. 「내일 체육 준비물은 물이야」→「내일 뭘 챙겨야 해?」→「초기화」→ 다시 질문
4. `step3_system_prompt.py` — 시스템 지침. `instructions=` 줄을 주석 처리하며 환각 차이 비교
5. `step4_image.py` — 시간표·안내문 사진(`notice.jpg`) 분석
6. `school_bot/` 폴더에 `neis.py` → `app.py` → `templates/index.html` 순서로 작성하고 `python app.py`(포트 5001)로 실행
7. `notes/ai-log.md` · `notes/why-ai-service.md`를 채운다

## 포함된 파일

```
week10/
├── README.md
├── requirements.txt          ← openai, flask, requests, python-dotenv
├── .env.example              ← OPENAI_API_KEY 자리 (실제 키는 .env에, GitHub 금지)
├── .gitignore                ← .env 제외
├── step1_single.py           ← 단일 대화
├── step2_chat.py             ← 연속 대화 (대화 기록 리스트)
├── step3_system_prompt.py    ← 시스템 지침
├── step4_image.py            ← 이미지 분석
└── notes/
    ├── ai-log.md             ← 단일/연속·환각·사진 대조 실험 기록
    └── why-ai-service.md     ← 회고
```

## 성공 기준

- [ ] `OPENAI_API_KEY`를 환경 변수로 분리했고, 코드·화면·GitHub 어디에도 키가 없다
- [ ] 단일 대화는 이전 내용을 기억하지 못하고, 연속 대화는 기억함을 직접 확인했다
- [ ] 공지에 없는 일정을 지어내지 않고 「확인 필요」로 출력된다
- [ ] 사진에서 글자를 읽어오고, 원본과 하나씩 대조해 봤다
- [ ] 학교 급식 원문(나이스)과 AI 브리핑이 화면에서 따로 표시된다
- [ ] 브라우저 2개로 열어도 챗봇 대화가 섞이지 않는다

## 완성 예시 (교사·조교용)

[../reference/week10-complete/](../reference/week10-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기.

자세한 진행은 [weeks/week10-ai-service.md](../../weeks/week10-ai-service.md) 참고.
