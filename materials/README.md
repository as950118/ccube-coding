# 포켓몬 배틀 프로젝트 — 파이썬 교재 묶음

이 폴더는 저장소 루트의 `app.py`, `templates/index.html`을 기준으로 한 **함수·클래스·스킬** 수업용 교재입니다.

## 구성

| 파일 | 용도 |
|------|------|
| [01-functions-lesson.md](01-functions-lesson.md) | **1주차 — 함수** 차시 |
| [02-classes-lesson.md](02-classes-lesson.md) | **2주차 — 클래스** 차시 |
| [03-skills-lesson.md](03-skills-lesson.md) | **3주차 — 기술(스킬) 표** 차시 |
| [reference/app_week2_complete.py](reference/app_week2_complete.py) | **2주차 완성본** (함수 + `Pokemon`) |
| [reference/app_week3_skills.py](reference/app_week3_skills.py) | **3주차 목표 예시** (스킬 dict + `Battle`) |
| [visual/flow-browser-flask.html](visual/flow-browser-flask.html) | 브라우저 ↔ Flask 흐름(프로젝터용) |
| [visual/function-blocks.html](visual/function-blocks.html) | `attack` 로직을 블록으로 나누는 시각화 |
| [visual/class-pokemon-diagram.html](visual/class-pokemon-diagram.html) | 공통 클래스 + 인스턴스 2개 개념도 |

## 수업 순서

1. **1주차(함수)** — `attack` 안의 중복·긴 흐름을 `roll_damage`, `apply_damage` 등으로 쪼갠 뒤, `skill` 쿼리를 `request`로 읽기.
2. **2주차(클래스)** — `player` / `enemy` 딕셔너리를 `Pokemon` 클래스로 바꾸고 `take_damage`, `reset`, `is_alive` 메서드 도입.  
   → 루트 `app.py`가 **2주차 완성 상태**입니다.
3. **3주차(스킬)** — `SKILLS` 딕셔너리로 기술별 공격/회복 규칙 정리, (선택) 적 랜덤 기술·`Battle` 클래스.

## 파일 열기

- 마크다운: Cursor, VS Code, Typora 등에서 열면 됩니다.
- HTML: 브라우저로 직접 열어 전자칠판·프로젝터에 표시하면 됩니다.
- 참고 코드: `reference/` 폴더 — 학생 실습 전후 비교·교사용 정답용.
