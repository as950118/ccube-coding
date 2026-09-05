# 8주차 — BBS 확장 · 공공데이터 API · 대시보드

**Phase:** 입문(재설계) | **소요:** 4시간
**대상:** 특목고 진학 준비 중학생
**원본 대응:** 인프런 원본 매핑 없음 — 6·7주차에 이어지는 **자체 재설계 트랙**(BBS·웹 아키텍처)
**선수:** 7주차 — BBS v1(회원가입·로그인·본인 글만 수정/삭제) 완성

---

## 오늘의 목표

오늘이 끝나면 학생은 아래를 **말로 설명**하고 **손으로 실행**할 수 있어야 한다.

| # | 목표 | 확인 방법 |
|---|------|-----------|
| 1 | **공공데이터포털**에서 오픈API를 신청하고 **인증키**를 발급받는다 | 마이페이지에 발급된 인증키가 보임 |
| 2 | 인증키를 코드에 **직접 적지 않고** `.env`로 관리한다 | `app.py`/`opendata.py`에 키 문자열이 없음 |
| 3 | `requests`로 외부 **API를 호출**하고 JSON 응답을 받는다 | 터미널에 원본 JSON이 출력됨 |
| 4 | 받아온 JSON에서 필요한 값만 뽑아 **가공(파싱)**한다 | 지역·수치·등급이 정리된 리스트가 됨 |
| 5 | 가공한 데이터를 **대시보드 화면**(표 + 막대그래프)으로 보여준다 | `/dashboard` 접속 시 표와 막대가 보임 |
| 6 | API가 **실패해도 앱이 죽지 않게** 예외처리한다 | 인터넷을 끊거나 키를 지워도 샘플 데이터로 화면이 뜸 |

### 특목고 연결 (오늘 심을 한 문장)

> 탐구보고서는 **데이터를 모으고 → 가공하고 → 표/그래프로 보여주는** 과정이다.
> 오늘은 그 과정을 코드로 그대로 만든다 — 공공데이터포털이 「데이터를 모으는 곳」, `opendata.py`가 「가공」, 대시보드가 「보여주기」다.

---

## 오늘 완성할 프로그램

### 산출물 이름
**「나만의 BBS — 공공데이터 대시보드(v2)」**

7주차 BBS(회원·권한 있는 게시판)를 **그대로 이어쓴다**. 게시판에 **공공데이터 대시보드 페이지**를 하나 추가한다.

**오늘도 API 호출·가공·대시보드 라우트(2~5장)는 AI 없이 직접 코드를 작성한다.** AI는 6장(도전 과제)에서만 쓴다.

> 오늘 예시는 **에어코리아 대기오염정보(미세먼지) API**를 쓴다. 다른 공공데이터(날씨·유동인구·문화행사 등)로 바꾸고 싶은 학생은 6장 도전 과제에서 자유 주제로 진행해도 좋다 — API를 부르고 가공해서 보여주는 **구조는 동일**하다.

### 완성 모습 (최소 · 🟢)

| # | 화면/기능 | 최소 내용 |
|---|-----------|-----------|
| 1 | **`.env`에 인증키 저장** | `PUBLIC_DATA_API_KEY`가 코드에 하드코딩되지 않음 |
| 2 | **`opendata.py`** | 공공데이터 API를 호출해 리스트(딕셔너리 배열)로 가공해 돌려주는 함수 |
| 3 | **샘플 데이터 대체** | API 실패·키 없음 시 `data/sample_air_quality.json`으로 대체 |
| 4 | **`/dashboard` 라우트** | 가공된 데이터를 받아 화면에 전달 |
| 5 | **대시보드 화면** | 지역별 표(측정소·미세먼지·등급) + 간단 막대그래프 |
| 6 | **네비게이션 연결** | 게시판 상단 nav에 "대시보드" 메뉴 추가 |

### 폴더 구조 (수업 종료 시 예시)

```
week06-bbs/                        ← 6·7주차 폴더를 이어씀
├── app.py                         ← /dashboard 라우트 추가
├── opendata.py                    ← 신규: API 호출 + 가공 함수
├── bbs.db
├── data/
│   └── sample_air_quality.json    ← 신규: 오프라인 대체용 샘플 데이터
├── .env                           ← 신규(커밋 금지): PUBLIC_DATA_API_KEY=...
├── .env.example                   ← 신규: 키 이름만 적힌 예시(커밋 대상)
├── .gitignore                     ← .env, bbs.db, __pycache__ 추가
├── templates/
│   ├── list.html / detail.html / new.html / edit.html   ← 기존(7주차)
│   ├── signup.html / login.html                          ← 기존(7주차)
│   └── dashboard.html             ← 신규: 표 + 막대그래프
└── notes/
    ├── opendata-log.md            ← 신규: 사용한 API·받은 값·막힌 점 기록
    └── why-opendata.md            ← 신규: 왜 공공데이터인가 회고
```

### 성공 기준 (🟢)
1. `.env`에 인증키를 넣고, `app.py`/`opendata.py`에는 키 문자열이 **직접 보이지 않는다**
2. `/dashboard` 접속 시 지역별 표와 막대그래프가 보인다
3. `.env`를 잠깐 지우거나 이름을 바꿔도 서버가 죽지 않고 **샘플 데이터**로 화면이 뜬다
4. 게시판 상단 nav에서 "대시보드" 링크로 이동할 수 있다
5. 6·7주차에 만든 게시판(목록·상세·작성·수정·삭제·회원·권한)이 **그대로** 동작한다

---

## 4시간 타임테이블

| 시간 | 블록 | 챕터 | 내용 |
|------|------|------|------|
| 0:00~0:25 | A | 0 · 1 | Week7 회고 · "공공데이터 API가 뭔가" 문제 제기 |
| 0:25~1:25 | B | 2 · 3 | 🟢 공공데이터포털 인증키 발급 · `.env` · `requests`로 첫 호출(직접) |
| 1:25~1:40 | — | — | 휴식 |
| 1:40~2:50 | C | 4 · 5 | 🟢 데이터 가공 함수 · `/dashboard` 라우트 · 표+막대그래프 (직접) |
| 2:50~3:00 | — | — | 휴식 |
| 3:00~3:45 | D | 6 | 🟡 지역 선택 필터 · 🔴 AI 도전(Chart.js, 이력 저장 등) |
| 3:45~4:00 | E | 7 | 발표 · 회고 · Week9 예고 |

---

# 본문 — 챕터별 상세

---

## 0. Week7에서 이어가기

### 0.1. 60초 복습 퀴즈 (구두)

1. 지난주 추가한 것은? → **회원가입·로그인·본인 글만 수정/삭제**
2. 비밀번호를 DB에 저장할 때 그대로 저장하면 안 되는 이유는? → **해시로 저장해야 함**
3. 인증(Authentication)과 인가(Authorization)의 차이는? → **누구인지 확인 / 이 행동을 해도 되는지 확인**

### 0.2. 오늘 문제 제기

> 지금까지 BBS 안의 데이터는 **우리가 직접 쓴 글**뿐이었다.
> 세상에는 정부·공공기관이 이미 모아 둔 **데이터**가 아주 많다 — 미세먼지, 날씨, 버스 도착 정보, 인구 통계...
> 이런 데이터를 **가져와서(API 호출) → 정리해서(가공) → 보여주면(대시보드)** 어떨까?

- 공공데이터포털(data.go.kr)은 정부기관이 공개한 데이터를 **API**로 제공한다
- 오늘은 그중 하나(대기오염정보)를 게시판에 **대시보드**로 붙인다

### 0.3. 오늘 한 문장 목표 (학생 작성)

예시:
> 「미세먼지 공공데이터를 가져와서 우리 게시판에 대시보드로 보여준다.」

---

## 1. 왜 공공데이터인가

### 1.1. API 복습 — 식당 비유

> 손님(우리 코드)이 메뉴판(API 명세)을 보고 주문(요청)하면, 주방(공공데이터포털 서버)이 요리해서 종업원(API)이 음식(JSON 응답)을 가져다준다.

지금까지 우리 앱은 **손님에게 음식을 파는 주방**(Flask 서버가 브라우저에 응답)이었다.
오늘은 우리 앱이 **동시에 손님도 된다** — 공공데이터포털이라는 다른 식당에 주문을 넣는다.

### 1.2. 오늘 배우는 4개 키워드

| 키워드 | 한 줄 |
|--------|------|
| **오픈API** | 누구나 신청하면 쓸 수 있게 공개한 API |
| **인증키(서비스키)** | "네가 누구인지" API 서버에 증명하는 열쇠 |
| **요청(request) / 응답(response)** | 우리가 보내는 질문 / API가 돌려주는 데이터(JSON) |
| **파싱(parsing)** | 받은 데이터에서 **필요한 값만** 꺼내 정리하는 것 |

### 1.3. 오늘 하지 않는 것 (Non-goals)

- 실시간 자동 새로고침(폴링·WebSocket) — 오늘은 **버튼을 눌러야** 새로 불러옴
- 여러 공공데이터 API를 한 화면에 조합
- 대시보드에 로그인 필요하게 만들기 — 오늘은 **누구나 볼 수 있는** 공개 페이지
- Chart.js 등 그래프 라이브러리 — 오늘 🟢은 HTML/CSS만으로 막대그래프를 흉내 낸다 (라이브러리는 🔴)

---

## 2. 공공데이터포털 인증키 발급 · `.env` (🟢, 직접)

### 2.1. 함께 따라하기 — 인증키 받기

1. [data.go.kr](https://www.data.go.kr) 회원가입 · 로그인
2. 검색창에 **"한국환경공단_에어코리아_대기오염정보"** 검색
3. **활용신청** 클릭 → 활용 목적(교육/실습) 작성 → 신청
   - 이 API는 보통 **자동승인**이라 몇 분~몇 시간 내 승인된다. 수업 전날 미리 신청해 두는 것을 권장한다.
4. 승인되면 **마이페이지 → 오픈API → 활용신청 현황**에서 **일반 인증키(Encoding)** 확인
5. 이 키를 코드에 **직접 붙여넣지 않는다** — `.env` 파일에 넣는다

> ⚠️ 인증키가 아직 승인되지 않았거나 학교 와이파이가 막혀 있어도 괜찮다 — 3장에서 **샘플 데이터로 먼저 구조를 익히고**, 키가 준비되면 그때 실제 API로 바꾼다.

### 2.2. `.env` 만들기

```
# .env (커밋 금지 — .gitignore에 추가)
PUBLIC_DATA_API_KEY=여기에_발급받은_인증키_붙여넣기
```

```
# .env.example (커밋 대상 — 팀원에게 "이런 키가 필요하다"고 알려주는 용도)
PUBLIC_DATA_API_KEY=
```

`.gitignore`에 `.env`를 추가한다 (7주차까지 없었다면 오늘 추가):

```
.env
bbs.db
__pycache__/
```

### 2.3. 패키지 설치

```
pip install requests python-dotenv
```

- `requests` — 다른 서버에 API 요청을 보내는 라이브러리
- `python-dotenv` — `.env` 파일의 값을 `os.environ`으로 읽어 오는 라이브러리

**직접 확인해보기:**
- `.env`에 실제 키가 들어 있는지
- `.gitignore`에 `.env`가 있는지 — `git status`에 `.env`가 **보이면 안 된다**

---

## 3. `requests`로 외부 API 호출하기 (🟢, 직접)

### 3.1. `opendata.py` — 단독 실행으로 먼저 확인

새 파일 `opendata.py`를 만들고, **`app.py`에 연결하기 전에** 이 파일만 단독 실행해서 API 응답 구조를 먼저 눈으로 확인한다.

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"


def fetch_raw(sido="서울"):
    api_key = os.environ.get("PUBLIC_DATA_API_KEY")
    params = {
        "serviceKey": api_key,
        "returnType": "json",
        "numOfRows": 100,
        "pageNo": 1,
        "sidoName": sido,
        "ver": "1.3",
    }
    response = requests.get(API_URL, params=params, timeout=5)
    return response.json()


if __name__ == "__main__":
    data = fetch_raw()
    print(data)  # 오늘 처음엔 그냥 통째로 찍어서 구조를 눈으로 본다
```

```
python opendata.py
```

**직접 확인해보기 (터미널에 찍힌 JSON을 눈으로 읽는다):**
- 가장 바깥은 `response` → `body` → `items`로 들어가는 구조인가?
- `items` 안의 항목 하나(측정소 하나)에 어떤 키(`stationName`, `pm10Value`, `pm25Value`...)가 있는가?
- 값이 문자열("35")로 오는가, 숫자로 오는가?

### 3.2. 실패 상황 미리 만들어보기

- `.env`의 키 이름을 잠깐 오타 내고 실행 → 무슨 일이 일어나는지 관찰
- 인터넷을 끄고 실행 → `requests.exceptions.ConnectionError` 관찰
- 이 관찰이 4장에서 만들 **예외처리**의 근거가 된다

---

## 4. 데이터 가공 — 필요한 값만 뽑기 · 예외처리 (🟢, 직접)

### 4.1. 샘플 데이터 준비

`data/sample_air_quality.json` — 실제 API와 **같은 모양**으로 미리 만들어 둔다 (오프라인·키 미승인 시 대체용).

```json
{
  "response": {
    "body": {
      "items": [
        {"stationName": "종로구", "pm10Value": "38", "pm25Value": "19", "khaiGrade": "2"},
        {"stationName": "강남구", "pm10Value": "52", "pm25Value": "27", "khaiGrade": "3"},
        {"stationName": "마포구", "pm10Value": "29", "pm25Value": "14", "khaiGrade": "1"},
        {"stationName": "송파구", "pm10Value": "61", "pm25Value": "33", "khaiGrade": "3"}
      ]
    }
  }
}
```

### 4.2. 가공 함수 — `fetch_air_quality`

```python
import json
from pathlib import Path

GRADE_LABELS = {"1": "좋음", "2": "보통", "3": "나쁨", "4": "매우나쁨"}
SAMPLE_PATH = Path(__file__).resolve().parent / "data" / "sample_air_quality.json"


def parse_items(raw):
    items = raw["response"]["body"]["items"]
    result = []
    for item in items:
        result.append({
            "station": item.get("stationName", "알 수 없음"),
            "pm10": int(item.get("pm10Value") or 0),
            "pm25": int(item.get("pm25Value") or 0),
            "grade": GRADE_LABELS.get(item.get("khaiGrade"), "정보없음"),
        })
    # 미세먼지 높은 순 정렬
    result.sort(key=lambda row: row["pm10"], reverse=True)
    return result


def load_sample():
    with open(SAMPLE_PATH, encoding="utf-8") as f:
        return parse_items(json.load(f))


def fetch_air_quality(sido="서울"):
    try:
        raw = fetch_raw(sido)
        return parse_items(raw), "live"
    except Exception:
        return load_sample(), "sample"
```

`fetch_air_quality`는 **(데이터, 출처)** 튜플을 돌려준다 — 화면에 "실시간" 또는 "샘플 데이터" 배지를 보여주기 위해서다.

**직접 확인해보기:**
- `except Exception:`이 **너무 넓은 것 아닌가?** 하는 질문이 나오면 좋다 — 오늘은 "API 호출은 실패할 수 있다"는 감각이 목표이므로 넓게 잡아도 된다. 나중에 `requests.exceptions.RequestException`처럼 좁히는 것도 소개만 한다.
- `int(item.get("pm10Value") or 0)` — 값이 없거나 빈 문자열일 때도 죽지 않는지

---

## 5. `/dashboard` 라우트 · 대시보드 화면 (🟢, 직접)

### 5.1. `app.py`에 라우트 추가

```python
from opendata import fetch_air_quality

@app.route("/dashboard")
def dashboard():
    sido = request.args.get("sido", "서울")
    rows, source = fetch_air_quality(sido)
    return render_template("dashboard.html", rows=rows, sido=sido, source=source)
```

### 5.2. `templates/dashboard.html`

막대그래프는 라이브러리 없이 `<div>` 너비(%)로 흉내 낸다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>공공데이터 대시보드</title>
  <style>
    body { font-family: sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; color: #1f2937; }
    .badge { display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 12px; margin-left: 8px; }
    .badge.live { background: #dcfce7; color: #166534; }
    .badge.sample { background: #fef3c7; color: #92400e; }
    table { width: 100%; border-collapse: collapse; margin-top: 16px; }
    th, td { text-align: left; padding: 8px; border-bottom: 1px solid #e5e7eb; }
    .bar-track { background: #f1f5f9; border-radius: 4px; height: 14px; width: 100%; }
    .bar-fill { background: #1d4ed8; height: 14px; border-radius: 4px; }
  </style>
</head>
<body>
  <a href="/">← 게시판으로</a>
  <h1>미세먼지 대시보드
    <span class="badge {{ source }}">{{ "실시간" if source == "live" else "샘플 데이터" }}</span>
  </h1>
  <p>지역: {{ sido }}</p>
  <table>
    <tr><th>측정소</th><th>미세먼지(PM10)</th><th>등급</th><th></th></tr>
    {% for row in rows %}
    <tr>
      <td>{{ row.station }}</td>
      <td>{{ row.pm10 }}</td>
      <td>{{ row.grade }}</td>
      <td style="width:40%">
        <div class="bar-track">
          <div class="bar-fill" style="width: {{ [row.pm10, 100] | min }}%"></div>
        </div>
      </td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
```

### 5.3. 게시판 nav에 대시보드 링크 추가

7주차에 만든 공통 nav(각 템플릿 상단)에 한 줄만 추가한다.

```html
<nav>
  ...
  <a href="/dashboard">대시보드</a>
</nav>
```

### 5.4. 검증 체크리스트

- [ ] `/dashboard` 접속 시 표와 막대그래프가 보인다
- [ ] 값이 큰 지역이 위(정렬)에, 막대가 더 길게 보인다
- [ ] `.env` 키를 지우고 재실행해도 "샘플 데이터" 배지와 함께 화면이 뜬다 (서버가 안 죽는다)
- [ ] 게시판 목록·상세 등 기존 화면이 그대로 동작한다

---

## 6. 🟡🔴 확장 — 지역 필터 · AI와 함께 기능 추가

### 6.1. 🟡 지역 선택 드롭다운 (직접)

```html
<form method="GET" action="/dashboard">
  <select name="sido" onchange="this.form.submit()">
    {% for name in ["서울", "부산", "경기", "인천", "대구"] %}
      <option value="{{ name }}" {{ "selected" if name == sido else "" }}>{{ name }}</option>
    {% endfor %}
  </select>
</form>
```

### 6.2. AI에게 요청하는 기본 틀 (Plan 먼저)

핵심 기능(2~5장)이 끝난 뒤에만 AI를 쓴다.

```
목표: 오늘 만든 대시보드(v2)에 (내가 상상한 기능)을 추가한다.

제약:
- opendata.py의 fetch_air_quality 구조(실패 시 샘플 데이터) 유지
- app.py, opendata.py, templates/ 안에서만 수정

먼저 계획만 제안해줘: 어떤 함수/라우트/파일이 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

### 6.3. 예시 아이디어 — Chart.js로 진짜 그래프

```
목표: dashboard.html의 CSS 막대그래프를 Chart.js 막대 차트로 바꾼다.
CDN으로 Chart.js를 불러오고, rows 데이터를 JS 배열로 넘긴다.
```

### 6.4. 예시 아이디어 — 조회 이력을 DB에 저장

```
목표: /dashboard를 조회할 때마다 dashboard_logs 테이블(sido, pm10_avg, checked_at)에 기록한다.
새 페이지 /dashboard/history 에서 최근 10건을 표로 보여준다.
```

### 6.5. 예시 아이디어 — 다른 공공데이터로 바꾸기

```
목표: 미세먼지 대신 (기상청 날씨 / 서울시 문화행사 등) API로 바꾼다.
opendata.py의 fetch_raw·parse_items만 새 API 구조에 맞게 교체하고,
fetch_air_quality 같은 "실패 시 샘플 데이터" 구조는 그대로 유지한다.
```

---

## 7. 정리 · 공유 · 다음 주

### 7.1. 30~60초 공유 스크립트

```
게시판에 (○○) 공공데이터 대시보드를 추가했습니다.
API에서 받은 데이터 중 ○○만 뽑아서 보여줍니다.
API가 실패하면 ○○로 대체됩니다.
```

### 7.2. `notes/opendata-log.md` 작성

```markdown
# 오늘 연동한 공공데이터

- API 이름:
- 신청·승인까지 걸린 시간:
- 받아온 원본 JSON 구조 (핵심 키만):
- 내가 가공해서 뽑은 값:

# 오늘 막혔던 점

# 다음에 하고 싶은 것
```

### 7.3. `notes/why-opendata.md` — 회고 3줄

```
잘된 점:
막힌 점:
다음에 하고 싶은 것:
```

### 7.4. 오늘 배운 것 체크

- [ ] 공공데이터포털 인증키 발급 · `.env` 관리
- [ ] `requests`로 외부 API 호출
- [ ] JSON 파싱(필요한 값만 뽑기)
- [ ] 대시보드 라우트·화면(표 + 막대그래프)
- [ ] API 실패 시 샘플 데이터로 대체(예외처리)

### 7.5. 다음 주 예고 (Week9)

- 오늘까지 6·7·8주차로 **회원·권한·공공데이터 대시보드**가 있는 BBS를 완성했다
- 다음 주부터는 **미니앱(포트폴리오 #2)**을 위한 PRD·ROADMAP을 스스로 작성한다 — 오늘 만든 대시보드 경험(문제→데이터→화면)이 그대로 재료가 된다

미리 생각해 오기 (숙제 아님):
> 오늘 다룬 공공데이터 말고, 내가 관심 있는 주제로 미니앱을 만든다면 어떤 데이터/기능이 필요할까?

---

## 🟢🟡🔴 과제 카드

### 🟢 (필수 · AI 없이 직접 작성)
- [ ] 공공데이터포털 인증키 발급 · `.env` 저장
- [ ] `opendata.py` — API 호출 + 가공 함수(`fetch_air_quality`)
- [ ] API 실패 시 샘플 데이터로 대체
- [ ] `/dashboard` 라우트 + 표/막대그래프 화면
- [ ] nav에 대시보드 링크
- [ ] `notes/opendata-log.md` · 회고 3줄

### 🟡 (권장 · 직접)
- [ ] 지역 선택 드롭다운
- [ ] 대시보드 화면 스타일 다듬기

### 🔴 (도전 · 여기서만 AI 사용)
- [ ] Chart.js 등 그래프 라이브러리 적용
- [ ] 조회 이력 DB 저장 + 히스토리 페이지
- [ ] 다른 공공데이터 API로 교체

### 제출
- `app.py` + `opendata.py` + `templates/dashboard.html` (또는 스크린샷)
- `notes/opendata-log.md`
- 회고 3줄

---

## 교사 메모

### 진행 팁
- **2~5장도 AI 없이 진행** — 6·7주차와 같은 원칙. "API가 실패할 수 있다"는 감각은 직접 오류를 봐야 남는다.
- 인증키 **승인 지연**이 이 수업의 가장 큰 리스크다. 수업 최소 하루 전에 반 전체가 활용신청을 마치도록 사전 공지한다.
- 승인이 안 된 학생은 3~5장을 **샘플 데이터로 먼저 완성**하고, 승인되면 `.env`만 채워 실시간으로 전환한다 — 실습 흐름이 끊기지 않는다.
- 공공데이터포털 API 스펙(파라미터명·응답 구조)은 기관이 개편할 수 있다. 수업 전 `python opendata.py`로 **직접 한 번 실행해 확인**할 것.
- `requests.get(..., timeout=5)` — timeout을 빼먹으면 학교 와이파이 환경에서 응답이 없을 때 화면이 오래 멈출 수 있다.
- **시간 내에 대시보드를 못 끝낸 학생:** [starters/reference/week08-complete/](../starters/reference/week08-complete/)를 수업 종료 직전에 따라잡기용으로 전달한다. 8·9주차는 미니앱(포트폴리오 #2) 준비로 넘어가므로, 여기서 막힌 채로 넘어가지 않도록 매주 같은 방식으로 캐치업시키는 것이 6·7·8주차 3주 트랙 전체의 원칙이다.

### 설명용 한 장 요약 (칠판)

```
공공데이터포털 → 인증키 발급 → .env
requests.get(API_URL, params={...serviceKey...}) → JSON 응답
파싱 → [{station, pm10, grade}, ...]
실패하면 → 샘플 데이터
/dashboard → 표 + 막대그래프

오늘 결과 → BBS v2 (회원 + 권한 + 공공데이터 대시보드)
다음 → 미니앱 PRD·ROADMAP (Week9)
```

### FAQ

**Q. 인증키가 수업 중에도 승인이 안 났어요.**
A. 4장 샘플 데이터로 전체 흐름을 완성하게 하고, 승인되면 과제로 실시간 전환.

**Q. `requests.exceptions.SSLError` 또는 학교 방화벽 문제가 나요.**
A. 학교 네트워크가 외부 API를 막아둔 경우가 있다. 이 경우 오늘 수업은 샘플 데이터 흐름으로 목표를 달성한 것으로 인정하고, 집에서 실시간 연동을 과제로 남긴다.

**Q. `.env`가 깃허브에 올라갔어요.**
A. 즉시 키를 재발급(폐기 후 재신청)하도록 안내하고, `.gitignore` 확인 + 이미 커밋된 경우 히스토리에서 제거하는 법을 간단히 언급(깊게 다루지 않음).

**Q. `int(item.get("pm10Value") or 0)`가 왜 필요한가요?**
A. 측정소 점검 중이면 값이 `null`이나 빈 문자열로 올 수 있다 — 그대로 `int()`에 넣으면 에러가 나므로 기본값 0으로 방어한다.

---

## 부록 A — 학생용 프롬프트 치트시트 (6장 도전 과제 전용)

```
[기본 틀]
목표: 대시보드 v2에 (기능) 추가.
제약: fetch_air_quality의 "실패 시 샘플 데이터" 구조 유지. app.py/opendata.py/templates/만.
먼저 계획만 제안해줘.

[Chart.js 🔴]
CSS 막대그래프를 Chart.js 막대 차트로 교체. CDN 사용.

[이력 저장 🔴]
dashboard_logs 테이블 + /dashboard/history 페이지.

[다른 공공데이터 🔴]
fetch_raw·parse_items만 새 API에 맞게 교체, 나머지 구조 유지.
```

---

## 부록 B — 트러블슈팅 표

| 증상 | 원인(대개) | 대응 |
|------|-----------|------|
| `SERVICE_KEY_IS_NOT_REGISTERED_ERROR` | 키 미승인 또는 오타 | `.env` 값 재확인, 승인 상태 확인 |
| `requests.exceptions.ConnectionError` | 인터넷/방화벽 차단 | 샘플 데이터 경로로 진행 |
| `KeyError: 'items'` | API 응답 구조가 예상과 다름(에러 응답) | `print(raw)`로 실제 응답 먼저 확인 |
| 막대그래프가 다 100%로 보임 | `min` 필터 누락 또는 pm10 값이 문자열 | `int()` 변환, `[value, 100] \| min` 확인 |
| `.env` 값이 안 읽힘 | `load_dotenv()` 호출 안 함 | `opendata.py`/`app.py` 상단에 `load_dotenv()` 확인 |
| `ModuleNotFoundError: dotenv` | 미설치 | `pip install python-dotenv` |

---

## 다음 주 (Week09)로 이어지는 다리

오늘로 6·7·8주차 3주에 걸쳐 **회원·권한·공공데이터 대시보드가 있는 BBS(v2)**까지 만들었다.
다음 주는 이 경험을 바탕으로, 학생이 스스로 고른 주제의 **미니앱(포트폴리오 #2)**을 위한 PRD·ROADMAP을 작성한다.
