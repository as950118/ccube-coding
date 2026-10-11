# 11주차 — AI 에이전트 · 하네스 · MCP: 내 도구를 AI에게 쥐여 주기

---

## 오늘의 목표

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | **AI 에이전트**를 「모델 + 도구 + 루프」로 설명한다 | `step5_agent.py` 로그의 🧠🔧👀를 가리키며 한 번의 반복을 말로 설명 |
| 2 | 에이전트에 **도구를 하나 더** 붙여 여러 단계 질문을 풀게 한다 | 「중간고사 첫날 급식?」에 학사일정 → 급식 순서로 도구 2개를 호출 |
| 3 | **하네스**가 모델 바깥에서 하는 일(도구 실행·반복 제한·권한·기억)을 안다 | 내 하네스와 Claude Code를 비교표로 정리 |
| 4 | **MCP**로 내 Python 함수를 Claude Code의 도구로 연결한다 | `/mcp`에 `school` connected, Claude Code가 내 도구로 급식 조회 |

### 특목고 연결 (오늘 심을 한 문장)

> AI가 「똑똑해 보이는」 이유의 절반은 모델이 아니라 **모델을 감싼 프로그램(하네스)과 쥐여 준 도구**에 있다. 무엇을 AI에게 맡기고, 무엇은 내 코드가 통제하는지 설계하는 것 — 이것이 탐구·면접에서 「AI를 어떻게 썼는가」에 대한 깊이 있는 답이 된다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「김반장 에이전트 + school MCP 서버」** (`school_agent/`)

| # | 기능 | 난이도 | 최소 내용 |
|---|------|--------|-----------|
| 1 | 에이전트 루프 관찰 | 🟢 | `step5_agent.py` 실행, 급식 질문에서 🧠→🔧→👀→✅ 로그 확인 |
| 2 | 도구 추가 (학사일정) | 🟢 | Claude Code로 TODO 3곳을 채워 `get_school_schedule` 추가, 도구 2개 질문 성공 |
| 3 | MCP 서버 연결 | 🟢 | `school_mcp.py`를 `claude mcp add`로 연결, Claude Code에서 급식 조회 |
| 4 | MCP 도구 추가 | 🟡 | MCP 서버에도 `school_schedule` 도구 추가 |
| 5 | 하네스 비교 | 🟡 | `notes/agent-log.md` 비교표 4칸 채우기 |

### 폴더 구조

```
school_agent/
├── neis.py            ← 10주차 neis.py + get_schedule() (starter 제공)
├── step5_agent.py     ← 실습 1: 내가 만든 하네스 (에이전트 루프)
├── school_mcp.py      ← 실습 2: MCP 서버 (Claude Code에 꽂는 도구)
├── requirements.txt   ← openai, requests, python-dotenv, mcp
├── .env               ← OPENAI_API_KEY (GitHub 금지)
└── notes/
    ├── agent-log.md
    └── why-agent.md
```

Starter: [starters/week11/](../starters/week11/) · 완성 예시: [starters/reference/week11-complete/](../starters/reference/week11-complete/)

---

## 2시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:20 | A | 0 · 1 | 10주차 `chat_reply()` 다시 읽기 → 「이게 이미 에이전트였다」· 세 개념 · 그림 한 장 |
| 0:20~0:50 | B | 2 | 🟢 실습 1 — 에이전트 루프 관찰 · 학사일정 도구 추가 |
| 0:50~0:55 | — | — | 휴식 |
| 0:55~1:40 | C | 3 | 🟢 실습 2 — `school_mcp.py`를 Claude Code에 연결 · 🟡 MCP 도구 추가 |
| 1:40~1:50 | D | 4 | 🟡 하네스 비교 — 같은 `neis.py`, 다른 하네스 |
| 1:50~2:00 | E | 5 | 회고 · 캡스톤 연결 · 숙제(몸풀기 질문지) 안내 |

> 2시간이라 B·C에 여유가 없다. **C(MCP 연결)가 오늘의 하이라이트**이므로 B가 밀리면 실습 1-2(도구 추가)를 C 뒤로 미루거나 완성 예시로 시연하고 넘어간다.

---

# 본문 — 챕터별 상세

## 0. 교사 사전 준비 (수업 전)

- [ ] **OpenAI 크레딧 확인.** 10주차와 같은 키·예산 정책. ⚠️ 2026-10-04 확인 시점에 수업용 키의 크레딧이 소진(429 `credit_balance_exhausted`)되어 있었다 — 충전 후 `step5_agent.py`를 1회 실제 실행해 볼 것. 에이전트는 질문 1개에 모델을 2~3번 부르므로 10주차보다 호출 수가 늘어난다(그래도 소형 모델이라 소액).
- [ ] **Python 3.10 이상** 확인. MCP Python SDK(`mcp` 2.x)의 요구 사항이다. 3.9 이하 학생은 수업 전에 업그레이드.
- [ ] **`mcp` 2.x 주의:** 인터넷 예제 대부분은 1.x의 `from mcp.server.fastmcp import FastMCP`를 쓴다. 2.x에서는 `from mcp.server import MCPServer`로 이름이 바뀌어 옛 예제를 그대로 붙이면 `ModuleNotFoundError`가 난다. Claude Code가 옛 코드를 제안할 때도 있으니 starter 코드를 기준으로 한다.
- [ ] **Claude Code 로그인 상태**를 학생 PC마다 확인 (`claude` 실행 → 프롬프트가 뜨면 OK).
- [ ] **교사 PC에서 `claude mcp add` → `/mcp` → 질문**까지 1회 리허설. 시연용 학교·날짜를 정해 둔다(예: 서울과학고등학교, 급식이 있는 평일).
- [ ] 학생 PC의 **python 절대경로**를 구하는 방법을 판서해 둔다 (3.3 참고). 실습 2에서 가장 많이 막히는 곳이다.
- [ ] 숙제용 [docs/2026진학반_보충_캡스톤주제선정.docx](../docs/2026진학반_보충_캡스톤주제선정.docx)의 몸풀기 질문지를 배포 준비.

---

## 1. 개념 — 에이전트 · 하네스 · MCP (20분)

### 1.1. 도입 질문: 「지난주에 우리는 에이전트를 만들었을까?」

10주차 `app.py`의 `chat_reply()`를 화면에 띄운다.

```python
for _ in range(3):                                   # ← 반복(루프)
    response = call_model(work, instructions, tools=[MEAL_TOOL])   # ← 모델이 생각
    calls = [item for item in response.output if item.type == "function_call"]
    if not calls:
        return response.output_text                  # ← 도구가 필요 없으면 답
    ...
        "output": run_meal_tool(call.arguments),     # ← 우리 코드가 도구 실행
```

답: **그렇다.** 모델이 「급식 조회가 필요하다」고 스스로 판단하고, 우리 코드가 실행하고, 결과를 다시 모델에게 보여주는 반복 — 이것이 에이전트의 최소 형태다.

### 1.2. 세 개념

| 개념 | 한 줄 정의 | 10주차·오늘 코드에서 |
|------|------------|----------------------|
| **AI 에이전트** | 목표를 받으면 「생각 → 도구 사용 → 결과 확인」을 답이 나올 때까지 **반복**하는 AI | `run_agent()` 의 `for step in range(MAX_STEPS)` |
| **하네스(harness)** | 모델 **바깥**에서 그 반복을 돌려 주는 프로그램. 도구를 실행하고, 반복 횟수를 제한하고, 권한을 확인하고, 기억(대화 기록)을 관리한다 | `step5_agent.py` 전체 = 작은 하네스 / **Claude Code = 큰 하네스** |
| **MCP** (Model Context Protocol) | 도구를 **어느 하네스에나** 꽂을 수 있게 맞춘 표준 규격 — 「AI용 USB-C」 | `school_mcp.py` 하나로 Claude Code·Claude 데스크톱 등 MCP를 지원하는 어디서든 쓸 수 있다 |

### 1.3. 그림 한 장 (판서)

```
              ┌───────────────── 하네스 (Claude Code / step5_agent.py) ─────────────────┐
  사용자 ───▶ │  ① 질문 + 도구 설명서 ──▶ [ 모델 ]  "급식 조회가 필요해" (요청만 함)      │
              │                              │                                           │
              │  ③ 결과를 다시 모델에게 ◀── ② 하네스가 도구 실행 ── 🔌 MCP ── school_mcp.py │
              │        (답이 나올 때까지 반복, 최대 N번)                       └─ neis.py ─▶ 나이스
              └─────────────────────────────────────────────────────────────────────────┘
```

### 1.4. 비유 (학생용)

- **모델** = 아주 똑똑하지만 손이 없는 두뇌
- **도구** = 손 (급식 조회, 일정 조회, 파일 쓰기…)
- **하네스** = 두뇌와 손을 연결하고, 「이건 해도 돼? / 열 번 넘게 하면 멈춰」를 관리하는 몸
- **MCP** = 어느 몸에나 끼울 수 있는 표준 규격의 손

> **교사 포인트:** 「AI가 직접 나이스에 접속한다」는 오해를 반드시 깬다. 10주차에 강조한 **「요청은 AI가, 실행은 우리 코드가」**가 에이전트·MCP에서도 그대로다. Claude Code가 파일을 고치는 것도 사실 Claude Code(하네스)가 실행해 주는 것이다.

### 1.5. 오늘 하지 않는 것 (Non-goals)

- 웹 화면(Flask) — 오늘은 터미널과 Claude Code에서만 동작
- 서브에이전트·Hooks·Skills — 개념만 한 줄로 언급(「하네스가 제공하는 다른 확장 기능」)
- 원격(HTTP) MCP 서버·배포 — 내 PC에서만 실행되는 stdio 서버만
- 에이전트가 파일을 쓰거나 지우는 「위험한」 도구 — 오늘 도구는 **읽기 전용**(조회)만

---

## 2. 실습 1 — 에이전트 루프 눈으로 보기 (🟢, 30분)

### 2.1. 준비

```
starters/week11/ 내용을 school_agent/ 로 복사
python --version                                  ← 3.10 이상
python -m pip install -r requirements.txt
```

`.env`(또는 PyCharm 환경 변수)에 `OPENAI_API_KEY` — 10주차와 같다.

### 2.2. 실습 1-1: 실행하고 관찰 (10분)

```
python step5_agent.py
나: 서울과학고등학교 9월 29일 급식 뭐야?
```

로그 예시:

```
🧠 [1단계] 모델에게 묻는 중...
🔧 도구 요청: get_school_meal({"school_name":"서울과학고등학교","date":"20260929"})
👀 결과: {"school": "서울과학고등학교", "date": "20260929", "menu": "*율무밥 ..."}

🧠 [2단계] 모델에게 묻는 중...

✅ 답: 9월 29일 서울과학고 점심은 율무밥, 육개장, ...
```

이어서 **도구가 없는 질문**을 해 본다: 「서울과학고 다음 주 학사일정 알려줘」 → 학사일정 도구가 없으므로 「확인 필요」 또는 「조회할 수 없다」로 답해야 정상. (지어내면 시스템 지침의 한계 관찰 자료 → `notes/agent-log.md`)

**확인 질문:** 「🧠 단계마다 모델에게 보내는 `work` 리스트는 어떻게 변할까?」 → 매 단계 도구 요청과 결과가 쌓인다(1 → 3 → 5개). 10주차 「연속 대화 = 기록을 통째로 다시 보내기」와 같은 원리.

### 2.3. 실습 1-2: Claude Code로 도구 하나 더 붙이기 (20분)

`step5_agent.py`의 `TODO(실습 1-2)` 3곳(도구 설명서 · 실행 함수 · 등록)을 Claude Code에게 맡긴다. `neis.get_schedule()`은 이미 있다.

```
step5_agent.py의 TODO(실습 1-2) 3곳을 채워서 학사일정 도구 get_school_schedule을 추가해 줘.
- neis.py의 get_schedule(office_code, school_code, from_date, to_date)를 사용해
- 인자는 school_name, from_date, to_date (날짜는 YYYYMMDD)
- get_school_meal과 같은 모양으로 만들고, 다른 코드는 건드리지 마
```

그다음 **도구 두 개가 필요한 질문**:

```
나: 서울과학고 중간고사 첫날 급식이 뭐야? 10월 5일부터 2주 안에 있어
```

기대 로그: `get_school_schedule` → (중간고사 날짜 확인) → `get_school_meal(…, "20261006")` → 답.

> **교사 포인트:** 「학사일정을 먼저 보고 그 날짜로 급식을 조회하라」는 순서를 **우리는 코드에 쓰지 않았다.** 모델이 도구 설명서만 보고 계획을 세웠다 — 이것이 「함수 호출 1회」와 「에이전트」의 차이다. 학생에게 「내가 순서를 정해 줬나?」를 꼭 묻는다.

### 2.4. 검증 체크리스트

- [ ] 급식 질문에서 🧠→🔧→👀→✅ 로그가 보인다
- [ ] 도구 추가 전, 학사일정 질문에 일정을 지어내지 않는다
- [ ] 도구 추가 후, 「중간고사 첫날 급식」 질문에 도구 2개가 순서대로 호출된다
- [ ] `MAX_STEPS`를 1로 바꾸면 무슨 일이 생기는지 확인했다 (하네스의 안전장치)

---

## 3. 실습 2 — 내 코드를 MCP 서버로 만들기 (🟢, 45분)

### 3.1. 코드 읽기 (5분)

```python
from mcp.server import MCPServer
import neis

mcp = MCPServer("school")

@mcp.tool()
def school_meal(school_name: str, date: str) -> str:
    """나이스(NEIS) 공식 데이터에서 학교의 급식(중식) 메뉴를 조회한다. date는 YYYYMMDD."""
    ...

if __name__ == "__main__":
    mcp.run()   # stdio
```

`step5_agent.py`와 비교시킨다:

| | step5_agent.py | school_mcp.py |
|--|--|--|
| 도구 설명서 | `TOOLS` 딕셔너리를 손으로 작성 | **함수 이름·타입·docstring이 자동으로** 설명서가 됨 |
| 루프(하네스) | 직접 작성 | **없음** — Claude Code가 한다 |
| 쓸 수 있는 곳 | 이 파일 안에서만 | MCP를 지원하는 모든 하네스 |

> MCP 서버 파일에는 **모델 호출도, 루프도, API 키도 없다.** 도구만 있다. 「도구 쪽」과 「하네스 쪽」이 분리되었다는 게 핵심.

### 3.2. 단독 실행해 보기 (2분)

`python school_mcp.py` → **아무것도 출력되지 않고 멈춰 있으면 정상**이다(Claude Code의 입력을 기다리는 중). Ctrl+C로 종료.

### 3.3. Claude Code에 연결 (15분)

**① python 절대경로 구하기** — `mcp`가 설치된 그 python이어야 한다.

| OS | 명령 |
|----|------|
| Mac | `which python` 또는 `which python3` → 예: `/Users/me/school_agent/.venv/bin/python` |
| Windows | `where python` → 예: `C:\Users\me\AppData\Local\Programs\Python\Python312\python.exe` |
| PyCharm | Settings → Python Interpreter에 표시된 경로 |

**② 등록** (`school_agent` 폴더에서)

```bash
# Mac
claude mcp add school -- /Users/me/school_agent/.venv/bin/python /Users/me/school_agent/school_mcp.py

# Windows (PowerShell)
claude mcp add school -- C:\Users\me\...\python.exe C:\Users\me\school_agent\school_mcp.py
```

- `school` = 서버 이름(아무거나), `--` 뒤 = 서버를 띄우는 명령
- 나이스 인증키가 있으면 `-e NEIS_API_KEY=...`를 `--` 앞에 붙인다(없어도 샘플 모드로 동작)
- 기본 범위(local)라 **이 폴더에서 연 Claude Code에만** 연결된다

**③ 확인**

```bash
claude mcp list          # school ... ✓ Connected
```

Claude Code를 `school_agent` 폴더에서 실행 → `/mcp` 입력 → `school` 서버 · 도구 `school_meal` 확인.

### 3.4. Claude Code에게 묻기 (10분)

```
서울과학고등학교 내일 급식 뭐야? school 도구로 조회해 줘.
```

관찰 포인트:
1. Claude Code가 **도구 사용 허락을 묻는다** → 내 하네스(`step5`)에는 없던 기능 = 하네스의 「권한」 역할
2. 답 아래에 도구 호출 기록이 보인다 → `step5`의 🔧 로그와 같은 것
3. 이어서 「그럼 모레는?」 → 학교 이름을 기억한다 → 하네스의 「기억」 역할

### 3.5. 🟡 MCP 서버에도 학사일정 도구 추가 (10분)

`school_mcp.py`의 `TODO(🟡)`를 Claude Code에게 맡긴다 → **Claude Code를 다시 시작**(서버 코드가 바뀌면 재연결 필요) → `/mcp`에서 도구 2개 확인 → 「중간고사 첫날 급식」 질문.

> 재미있는 장면: Claude Code가 **자기 자신이 쓸 도구를 고친다.**

### 3.6. 검증 체크리스트

- [ ] `claude mcp list`에서 `school`이 Connected
- [ ] `/mcp`에서 `school_meal` 도구가 보인다
- [ ] Claude Code가 내 도구로 조회한 급식이 나이스 원문과 같다
- [ ] (🟡) 도구 2개가 보이고, 두 도구를 순서대로 쓰는 질문에 답한다

---

## 4. 하네스 비교 — 같은 `neis.py`, 다른 하네스 (🟡, 10분)

`notes/agent-log.md` 비교표를 채우고 2~3명 발표.

| | 내 하네스 (`step5_agent.py`) | Claude Code |
|--|--|--|
| 도구 설명서는 누가 썼나 | 내가 `TOOLS`에 손으로 | `@mcp.tool()`이 함수에서 자동 생성 |
| 도구 실행 전 허락을 받나 | 아니오 | 예 (권한 확인) |
| 최대 몇 번 반복하나 | `MAX_STEPS = 5` | Claude Code가 관리 |
| 이전 대화를 기억하나 | 아니오 (질문마다 새로) | 예 (세션 안에서) |

정리 멘트: **같은 모델·같은 도구라도 하네스가 다르면 안전성·편의성이 달라진다.** 회사들이 「모델」만큼 「하네스」를 열심히 만드는 이유. 서브에이전트·Hooks·Skills도 하네스가 제공하는 기능이다(오늘은 이름만).

---

## 5. 회고 · 캡스톤 연결 · 숙제 (10분)

### 5.1. 회고 — `notes/why-agent.md`

- 에이전트 / 하네스 / MCP를 각각 한 문장으로
- **내 캡스톤에 AI를 붙인다면 어떤 도구를 줄까? AI에게 맡기지 않을 것은?**

### 5.2. 숙제 — 캡스톤 주제 준비 (필수)

캡스톤 주제 확정이 12주차 블록 A로 옮겨졌으므로, 다음 주 전까지 아래를 해 온다.

- [ ] [보충_캡스톤주제선정.docx](../docs/2026진학반_보충_캡스톤주제선정.docx)의 **몸풀기 질문지** A~E 답 적기, ★ 3개 표시
- [ ] 마음이 가는 1개로 「나는 [누구]의 [어떤 불편]을 [무엇]으로 돕는다」 한 문장 써 오기
- [ ] (선택) 그 주제에 쓸 수 있는 공공데이터·API 하나 찾아 오기 — 오늘처럼 **도구로 만들 수 있는 데이터**인지가 실현성 기준

---

## 트러블슈팅

| 증상 | 원인 및 해결 |
|------|--------------|
| `ModuleNotFoundError: No module named 'mcp'` | 실행한 python에 패키지 없음. `python -m pip install -r requirements.txt`를 **같은 python**으로 |
| `No module named 'mcp.server.fastmcp'` (2.x 안내 메시지) | 인터넷/AI가 준 1.x 예제. `from mcp.server import MCPServer`로 바꾸고 `FastMCP(...)` → `MCPServer(...)` |
| `pip install mcp` 실패 / 설치는 되는데 import 오류 | Python 3.9 이하. 3.10 이상 설치 후 인터프리터 교체 |
| `claude mcp list`에서 Failed to connect | ① python 경로가 `mcp` 없는 python ② 파일 경로 오타 ③ 상대경로 사용 → **둘 다 절대경로**로. `claude mcp remove school` 후 다시 add |
| Connected인데 Claude Code가 도구를 안 씀 | 질문에 「school 도구로 조회해 줘」를 붙인다. `/mcp`에서 도구가 보이는지 확인 |
| 서버 코드를 고쳤는데 반영 안 됨 | Claude Code 재시작 (서버는 Claude Code가 켤 때 띄운다) |
| MCP 서버가 연결 직후 끊김 | `school_mcp.py`·`neis.py`에 `print()`를 넣음. stdio는 출력 자체가 통신선이라 print가 대화를 깬다. 디버깅은 `step5`에서 |
| `python school_mcp.py`가 멈춰 있음 | 정상. Claude Code(클라이언트)를 기다리는 중. Ctrl+C |
| `RateLimitError` / 429 `insufficient_quota` | 크레딧 소진 — 교사에게. (MCP 실습 2는 OpenAI 키 없이도 된다 — Claude Code가 모델 역할) |
| 학사일정이 5건만 나옴 | 나이스 샘플 모드(키 없음) 제한. 기간을 1~2주로 좁히거나 `NEIS_API_KEY` 설정 |
| 에이전트가 같은 도구를 반복 호출하다 「N단계 안에 답을 못 찾았어요」 | 학교 이름·날짜가 모호함. 질문을 구체적으로. 하네스의 `MAX_STEPS`가 막아 준 것 — 좋은 관찰 자료 |

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수)
- [ ] `step5_agent.py` 실행, 🧠🔧👀 로그를 보고 루프 한 바퀴를 설명
- [ ] 학사일정 도구 추가, 도구 2개 질문 성공
- [ ] `school_mcp.py`를 Claude Code에 연결해 급식 조회
- [ ] 숙제: 몸풀기 질문지 + 한 문장 피치

### 🟡
- [ ] MCP 서버에 `school_schedule` 추가
- [ ] 하네스 비교표 4칸

### 🔴
- [ ] 10주차에 안 쓴 다른 나이스 API(시간표 `hisTimetable`/`misTimetable` 등)로 MCP 도구를 하나 더 만들기
- [ ] 내 캡스톤 후보 데이터를 MCP 도구 하나로 감싸 보기 — 12주차 실현성 증거가 된다

---

## 다음 주(Week12)로 이어지는 다리

오늘은 「데이터를 도구로 만들어 AI에게 쥐여 주는」 법을 익혔다. 다음 주는 블록 A에서 **캡스톤 주제를 확정**하고 바로 구현에 들어간다. 「내 주제의 데이터를 도구 하나로 만들 수 있는가」가 좋은 실현성 체크 질문이 된다.
