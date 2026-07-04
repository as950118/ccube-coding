# 13주차 — 보너스 프로젝트: Flask + SQLite 스마트홈 대시보드

**Phase:** 보너스 확장 | **소요:** 60~120분

---

## 🟢 목표 (전원)

`fetch('/api/status')` → **Flask(Python)** 가 센서 상태를 계산 → **SQLite** 에 저장 → 웹이 **평면도형 대시보드**로 보여준다.

---

## 이번 주의 3층 구조

| 층 | 이번 주 |
|----|---------|
| **Python/Flask** | 센서 시뮬레이션, 장치 제어 API, 이벤트 생성 |
| **SQLite** | 장치 상태 / 토양 습도 / 최근 이벤트 저장 |
| **웹** | 집 평면도 + CSS 2.5D 장치 + fetch 실시간 갱신 |

> 이제는 "버튼 클릭 → Flask" 에서 한 단계 더 나아가  
> **"버튼 클릭 → Flask → DB 저장 → 다시 화면 반영"** 흐름을 경험합니다.

---

## 왜 SQLite를 붙이나요?

- 새로고침해도 장치 상태가 남아 있음
- 최근 이벤트가 서버에 저장됨
- "진짜 스마트홈 서버" 느낌이 더 강해짐
- 학생들이 **프론트엔드 + 백엔드 + 데이터 저장** 흐름을 한 번에 볼 수 있음

---

## 수업 흐름

| 시간 | 내용 |
|------|------|
| 0~15분 | `week13-starter` 실행, `smarthome.db` 자동 생성 확인 |
| 15~35분 | `app.py` 에서 `init_db()`, `/api/status`, `/api/device/toggle` 읽기 |
| 35~60분 | `script.js` 의 `fetchStatus()` 와 버튼 제어 확인 |
| 60~90분 | 🟢 이름/문구 변경 + 장치 상태 테스트 |
| 90~120분 | 🟡 이벤트 1개 추가 / 🔴 새 장치 추가 |

---

## starter 포함

```
app.py                 → Flask + SQLite + 센서 시뮬레이션 API
templates/index.html   → 평면도형 스마트홈 화면
static/style.css       → 카드 + 방 구조 + CSS 2.5D 효과
static/script.js       → fetch + 실시간 렌더링
requirements.txt       → Flask
README.txt
```

### 시연용 참고 (분리 버전)

- `starters/reference/week13-threejs-demo/index.html`
- `Three.js` 기반 3D 스마트홈 시각 데모
- 별도 `app.py` 와 `SQLite` 를 가진 독립 참고 앱
- 교육용 starter 와 달리 **시각 효과를 우선**한 참고 예시
- 학생용 과제로 바로 쓰기보다는, 수업 시작/마무리 때 "이런 방향으로도 확장할 수 있다"는 시연용으로 적합

---

## 핵심 코드

```python
# app.py
@app.route("/api/status")
def api_status():
    advance_simulation()
    return jsonify(build_dashboard_response())
```

```javascript
// static/script.js
async function fetchStatus() {
    const response = await fetch("/api/status");
    const data = await response.json();
    renderDashboard(data);
}
```

```python
# app.py
def log_event(message: str) -> None:
    conn.execute(
        "INSERT INTO events (message, created_at) VALUES (?, ?)",
        (message, datetime.now().isoformat(timespec="seconds")),
    )
```

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] `STUDENT_NAME` 바꾸기
2. [ ] 전등 / 에어컨 / 선풍기 버튼 눌러 상태 바뀌는지 보기
3. [ ] `물 주기` 버튼 눌러 토양 습도 올라가는지 보기

### 🟡
4. [ ] 랜덤 이벤트 문장 1개 추가
5. [ ] 위험 기준(예: 온도 29도 이상)을 바꿔 보기

### 🔴
6. [ ] 장치 1개 더 추가하기 (예: 가습기, 창문, TV)
7. [ ] DB 테이블에 새 칼럼 추가 후 화면까지 연결하기

---

## 교사 메모

- 이 주차는 **12주 본과정 이후 보너스/심화** 성격입니다.
- 학생 입장에서는 "웹 페이지가 기기를 조작한다"는 감각을 주는 것이 핵심입니다.
- 실제 IoT 장비는 없지만, **센서 값이 조금씩 변하고 DB에 저장**되면 훨씬 현실감이 납니다.
- `smarthome.db` 는 첫 실행 시 자동으로 만들어집니다.
- 상태를 처음부터 다시 시작하고 싶다면 `smarthome.db` 파일을 지우고 다시 실행하면 됩니다.

---

## 연결되는 개념

- 3주차: `fetch('/api/add')`
- 4주차: `fetch('/api/check')`
- 5주차: `fetch('/api/chat')`
- **13주차:** `fetch('/api/status')` + `fetch('/api/device/toggle')` + **SQLite 저장**
