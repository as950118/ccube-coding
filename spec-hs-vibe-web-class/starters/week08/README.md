# week08 — BBS 확장 · 공공데이터 API · 대시보드 (starter)

**수업안:** [../../weeks/week08-bbs-opendata-dashboard.md](../../weeks/week08-bbs-opendata-dashboard.md)
**학생용 자료:** [../../docs/2026진학반_8주차.docx](../../docs/2026진학반_8주차.docx) ⚠️ 아직 구식(자동화·MCP) 내용 — [2026진학반_8주차-draft.md](../../docs/2026진학반_8주차-draft.md) 참고해 재작성 필요

## 이 폴더 사용법

이번 주는 **7주차 BBS(`week06-bbs/`) 폴더를 그대로 이어쓴다.** 새 저장소를 만들지 않는다.

**API 호출·가공·대시보드 라우트(오늘 핵심)는 AI 없이 직접 코드를 작성한다.** AI는 도전 과제에서만 쓴다.

1. [data.go.kr](https://www.data.go.kr)에서 "한국환경공단_에어코리아_대기오염정보" 활용신청을 하고 인증키를 받는다 (승인 전에도 3~7단계는 샘플 데이터로 먼저 진행 가능)
2. `pip install requests python-dotenv`
3. 이 폴더의 `opendata.py`·`data/sample_air_quality.json`·`.env.example`을 BBS 프로젝트 폴더로 복사한다
4. `.env.example`을 `.env`로 복사하고, 발급받은 인증키를 붙여넣는다 (`.env`는 `.gitignore`에 추가)
5. `opendata.py`의 **`# TODO` 부분만 직접 채운다** — `fetch_raw`(API 호출)와 `parse_items`(가공)
6. `python opendata.py`로 단독 실행해 원본 JSON 구조를 먼저 확인한 뒤, 가공 결과가 리스트로 잘 나오는지 확인한다
7. `app.py`에 `/dashboard` 라우트를 추가하고, `templates/dashboard.html`을 만들어 표+막대그래프로 보여준다
8. nav에 "대시보드" 링크를 추가한다
9. `notes/opendata-log.md`·`notes/why-opendata.md`를 채운다
10. 시간이 남으면 도전 과제(아래)에서만 AI를 사용해 지역 필터·그래프 라이브러리 등을 추가한다

## 포함된 파일

```
week08/
├── README.md                      ← 이 안내
├── opendata.py                    ← 스켈레톤 (fetch_raw · parse_items에 # TODO)
├── data/
│   └── sample_air_quality.json    ← 오프라인·키 미승인 시 대체용 샘플 데이터
├── .env.example                   ← PUBLIC_DATA_API_KEY 키 이름만 (커밋 대상)
└── notes/
    ├── opendata-log.md            ← 사용한 API·받은 값·막힌 점 기록
    └── why-opendata.md            ← 왜 공공데이터인가 · 회고
```

`opendata.py`는 **함수 이름·구조만 있고 로직은 비어 있다.** `# TODO`가 달린 부분(API 요청 파라미터, JSON 파싱)을 직접 채우는 것이 오늘 핵심이다 — AI에게 채워 달라고 하지 않는다. `fetch_air_quality`(성공하면 실시간, 실패하면 샘플)는 이미 완성되어 있으니 그대로 둔다.

## 성공 기준 (🟢, AI 없이)

- [ ] `.env`에 인증키가 있고, `opendata.py`/`app.py`에는 키 문자열이 직접 보이지 않는다
- [ ] `python opendata.py` 실행 시 실시간 또는 샘플 데이터가 리스트로 출력된다
- [ ] `/dashboard` 접속 시 표와 막대그래프가 보인다
- [ ] `.env`를 지워도 서버가 죽지 않고 샘플 데이터로 화면이 뜬다
- [ ] 기존 게시판(목록·상세·작성·수정·삭제·회원·권한)이 그대로 동작한다

## 🔴 도전 과제 (여기서만 AI 사용)

핵심 기능이 모두 동작한 뒤에만 진행한다.

```
목표: 대시보드 v2에 (지역 필터 / Chart.js 그래프 / 조회 이력 저장 / 다른 공공데이터)를 추가한다.

제약:
- fetch_air_quality의 "실패 시 샘플 데이터" 구조는 그대로 유지
- app.py, opendata.py, templates/ 안에서만 수정

먼저 계획만 제안해줘: 어떤 함수/라우트/파일이 바뀌는지.
내가 "진행"이라고 하면 그때 구현해줘.
```

## 완성 예시 (교사·조교용)

[../reference/week08-complete/](../reference/week08-complete/) — 학생이 막혔을 때만 참고. 수업 중 바로 복사하지 않기. (단, 시간 내에 못 끝낸 학생에게는 수업 종료 직전 교사가 따라잡기용으로 전달할 수 있음 — 진행 팁 참고)

자세한 진행·🟡🔴 과제는 [weeks/week08-bbs-opendata-dashboard.md](../../weeks/week08-bbs-opendata-dashboard.md) 참고.
