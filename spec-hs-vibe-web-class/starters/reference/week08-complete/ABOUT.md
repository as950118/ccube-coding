# BBS 확장 · 공공데이터 API · 대시보드 (교사 참고 · 완성 예시)

**수업안:** [../../../weeks/week08-bbs-opendata-dashboard.md](../../../weeks/week08-bbs-opendata-dashboard.md)

학생용 starter는 [../../week08/](../../week08/) 입니다.
이 폴더는 **조교·교사 참고용**입니다. 수업 중(API 호출·가공·대시보드를 직접 작성하는 동안)에는 학생에게 통째로 배포하지 않습니다. 단, **수업 종료 직전** 시간 내에 못 끝낸 학생에게는 다음 주(미니앱 PRD·ROADMAP)를 같은 출발선에서 시작할 수 있도록 **따라잡기용으로 전달해도 됩니다** — 자세한 기준은 [weeks/week08-bbs-opendata-dashboard.md](../../../weeks/week08-bbs-opendata-dashboard.md)의 "진행 팁"을 참고하세요.

## 이 예시에 대해

[week07-complete](../week07-complete/)(6주차 CRUD + 7주차 회원·권한)를 그대로 이어받아,
공공데이터 API 호출(`opendata.py`)과 `/dashboard` 화면만 더했습니다. `app.py`는
week07-complete와 동일한 CRUD·회원·권한 코드에 `/dashboard` 라우트 하나를 추가한 것입니다.
`bbs.db`는 실행 시 자동 생성되므로 포함하지 않습니다.

**중요:** API 호출(`opendata.py`)·가공·`/dashboard` 라우트는 학생이 AI 없이 직접 작성하는
구간입니다 — 수업 중 이 코드를 통째로 복사해 주지 않습니다. 지역 선택 드롭다운까지는 🟡(직접),
그 이상(Chart.js, 이력 저장 등)만 "AI 도전 과제로 만든 것"이라는 설정입니다.

## 파일

```
week08-complete/
├── ABOUT.md                 ← 이 안내 (교사용)
├── README.md                ← 완성된 프로젝트 README 예시
├── app.py                   ← Flask 서버 (CRUD + 회원·권한 + 대시보드)
├── opendata.py               ← 공공데이터 API 호출 + 가공(fetch_air_quality)
├── data/
│   └── sample_air_quality.json  ← 오프라인·키 미승인 시 대체 샘플
├── .env.example              ← PUBLIC_DATA_API_KEY · SECRET_KEY
├── requirements.txt
├── templates/
│   ├── list.html / detail.html / new.html / edit.html
│   ├── signup.html / login.html
│   └── dashboard.html        ← 표 + CSS 막대그래프 + 지역 선택
└── notes/
    ├── opendata-log.md       ← 사용 API·가공값 기록 예시
    └── why-opendata.md       ← 회고 예시
```

## 실행 방법 (시연용)

```
pip install -r requirements.txt
cp .env.example .env   # PUBLIC_DATA_API_KEY를 비워 둬도 샘플 데이터로 동작 시연 가능
python app.py
```

`http://localhost:5001` 접속 → 회원가입·로그인·글쓰기·본인 글만 수정삭제·대시보드가 모두
동작하는지 확인. `.env`의 `PUBLIC_DATA_API_KEY`를 비운 채로 `/dashboard`에 접속하면
"샘플 데이터" 배지가 뜨는 것도 함께 시연하면 좋다 (오늘 예외처리 목표).

## 확인 포인트

- `opendata.py`: `fetch_air_quality`가 예외를 밖으로 던지지 않고 항상 `(rows, source)`를 돌려주는가?
- `app.py`: `PUBLIC_DATA_API_KEY` 같은 키 문자열이 코드에 직접 적혀 있지 않은가? (`.env`로만 관리)
- `dashboard.html`: `source`에 따라 "실시간"/"샘플 데이터" 배지가 바뀌는가?
- 학생 결과물에서 API 호출·가공·대시보드 라우트가 **AI 프롬프트 없이** 완성됐는지 (6장 도전 과제만 AI 사용 대상)
- 6·7주차 기능(CRUD·회원·권한)이 대시보드 추가 이후에도 그대로 동작하는지
