AI웹반 13주차 reference — Three.js 스마트홈 시연용 데모
===========================================================

이 폴더는 교육용 `week13-starter` 와 분리된 참고용 데모입니다.

- 화면: Three.js 3D 스마트홈
- backend: Flask
- 저장: SQLite (`smarthome.db`)
- 목적: 학생 과제용보다는 교사 시연 / 확장 아이디어 참고

실행
----
1. `pip install -r requirements.txt`
2. `python app.py`
3. 브라우저에서 표시된 주소 열기

포인트
------
- `index.html` 은 Three.js 로 공간과 장치를 렌더링합니다.
- `/api/status`, `/api/device/toggle`, `/api/device/all`, `/api/plant/water`
  API 는 Flask 가 처리합니다.
- 센서 변화 / 랜덤 이벤트 / 최근 이벤트 목록은 SQLite 상태를 기반으로 동작합니다.

비교
----
- `starters/week13-starter/` → 학생용 / 읽기 쉬운 구조
- `starters/reference/week13-threejs-demo/` → 시연용 / 시각 효과 중심 구조
