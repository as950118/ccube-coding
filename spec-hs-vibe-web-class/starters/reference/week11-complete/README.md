# week11-complete — 김반장 에이전트 · school MCP 서버 (완성 예시)

[starters/week11](../../week11/)의 TODO를 모두 채운 버전. 교사·조교용.

| 파일 | 내용 |
|------|------|
| `neis.py` | 학교 검색 · 급식 · **학사일정(`get_schedule`)** |
| `step5_agent.py` | 도구 2개(`get_school_meal`, `get_school_schedule`) + 에이전트 루프(`MAX_STEPS=5`) + 단계별 로그 |
| `school_mcp.py` | 같은 기능을 MCP 도구 2개(`school_meal`, `school_schedule`)로 노출 (mcp 2.x `MCPServer`) |

## 실행

```bash
python -m pip install -r requirements.txt   # Python 3.10+
python step5_agent.py                        # OPENAI_API_KEY 필요
claude mcp add school -- "$(which python)" "$PWD/school_mcp.py"   # Mac (Windows는 수업안 참고)
```

## 검증 기록 (2026-10-04)

- `school_mcp.py` — MCP Python 클라이언트로 stdio 연결해 도구 목록 2개 확인, 서울과학고 급식(9/29)·학사일정(10/5~10/16, 중간고사 10/6~8) 실제 조회 성공, 없는 학교는 안내 문구 반환.
- `step5_agent.py` — 루프·도구 실행 경로를 가짜 모델로 확인(학사일정 → 급식 → 최종 답, 나이스는 실제 호출). **실제 OpenAI 호출은 미확인** — 확인 시점에 수업용 키의 크레딧이 소진(429 `credit_balance_exhausted`)되어 있었음. 수업 전 크레딧 충전 후 1회 시연 필요.
- Claude Code에 실제로 `claude mcp add` 해서 질문하는 과정은 교사 PC에서 1회 확인 필요.

## 시연 질문 예시

- 「서울과학고등학교 9월 29일 급식 뭐야?」 — 도구 1회
- 「서울과학고 10월 5일부터 2주 동안 학사일정 알려줘」 — 학사일정 도구
- 「서울과학고 중간고사 첫날 급식이 뭐야? 10월 5일부터 2주 안에 있어」 — 도구 2개를 순서대로 (에이전트다운 질문)
