# week11 — AI 에이전트 · 하네스 · MCP (starter)

**수업안:** [../../weeks/week11-agent-harness-mcp.md](../../weeks/week11-agent-harness-mcp.md)
**학생용 자료:** [../../docs/2026진학반_11주차-draft.md](../../docs/2026진학반_11주차-draft.md) (아직 초안 — docx 미작성)

## 이 폴더 사용법

10주차 `school_bot/`과 별개인 **새 폴더 `school_agent/`** 에 이 폴더 내용을 복사해서 시작한다.
`neis.py`는 10주차 것에 학사일정 함수 `get_schedule()`이 추가된 버전이다.

1. **환경 준비** — Python **3.10 이상**인지 확인(`python --version`), `python -m pip install -r requirements.txt`, `OPENAI_API_KEY` 환경 변수 등록(10주차와 동일)
2. **실습 1-1** `python step5_agent.py` — 「○○학교 내일 급식 뭐야?」를 묻고 🧠🔧👀 로그를 관찰. 「다음 주 학사일정 알려줘」도 물어본다(아직 도구가 없다)
3. **실습 1-2** Claude Code로 `TODO(실습 1-2)` 3곳을 채워 학사일정 도구를 붙인다 → 「중간고사 첫날 급식이 뭐야?」
4. **실습 2** `school_mcp.py`를 Claude Code에 연결한다
   ```
   claude mcp add school -- <python 절대경로> <school_mcp.py 절대경로>
   ```
   Claude Code를 다시 열고 `/mcp`로 확인 → 「서울과학고등학교 내일 급식 뭐야?」
5. `notes/agent-log.md` · `notes/why-agent.md`를 채운다

## 포함된 파일

```
week11/
├── README.md
├── requirements.txt      ← openai, requests, python-dotenv, mcp(2.x)
├── .env.example          ← OPENAI_API_KEY 자리 (실제 키는 .env에, GitHub 금지)
├── .gitignore
├── neis.py               ← 10주차 neis.py + get_schedule()
├── step5_agent.py        ← 실습 1: 에이전트 루프 (급식 도구 1개, 학사일정 도구는 TODO)
├── school_mcp.py         ← 실습 2: MCP 서버 (급식 도구 1개)
└── notes/
    ├── agent-log.md      ← 관찰 기록 · 하네스 비교표
    └── why-agent.md      ← 회고 · 캡스톤 연결
```

## 성공 기준

- [ ] `step5_agent.py` 로그에서 「생각 → 도구 요청 → 결과」 반복을 보고 말로 설명할 수 있다
- [ ] 학사일정 도구를 붙여, 도구 두 개가 필요한 질문에 답하게 만들었다
- [ ] `/mcp`에 `school` 서버가 connected로 보이고, Claude Code가 내 도구로 급식을 조회했다
- [ ] 에이전트 · 하네스 · MCP를 한 문장씩 설명할 수 있다

## 완성 예시 (교사·조교용)

[../reference/week11-complete/](../reference/week11-complete/) — 학생이 막혔을 때만 참고.
