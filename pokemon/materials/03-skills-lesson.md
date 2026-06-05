# 차시 3 — 기술(스킬)마다 다른 규칙 만들기

**대상:** 중학생 · 차시 2까지 `Pokemon` 클래스와 `request`로 `skill` 읽기를 마친 상태  
**소요:** 약 60~90분  
**기준 코드:** 프로젝트 루트의 `app.py` (2주차 완성본), `materials/reference/app_week2_complete.py`

---

## 1. 이 차시에서 배우는 것

- 버튼마다 다른 `skill` 값이 서버로 전달되는 흐름을 **데이터(딕셔너리)**로 정리할 수 있다.
- 같은 `attack()` 라우트 안에서 **기술별로 데미지·메시지·효과**를 다르게 줄 수 있다.
- (심화) 턴 전체를 `Battle` 클래스로 묶어 Flask 라우트를 더 짧게 만든다.

**3주차 주제를 이렇게 잡은 이유**

| 후보 | 장점 | 3주차에 적합한 이유 |
|------|------|---------------------|
| **기술별 다른 규칙** (추천) | 버튼 3개가 이미 있음, 체감이 큼 | 1·2주차(함수·클래스)를 그대로 이어서 확장 |
| HTML/CSS `class` 속성 | 화면 예쁘게 | 파이썬 `class`와 이름만 같아 혼동 가능 — 별도 차시로 분리 권장 |
| 타입 상성(불>풀>물) | 게임답다 | 조건·딕셔너리가 많아져 4주차 심화용으로 좋음 |
| 적 AI / 확률 빗나감 | 재미 요소 | B·C단계에서 `random`으로 자연스럽게 추가 |

> **권장 순서:** A(스킬 딕셔너리) → B(회복·공격 분기) → C(적도 기술 고르기) → D(`Battle` 클래스, 시간 남을 때)

---

## 2. 지금 2주차 완성본이 하는 일

2주차 끝 상태에서는 이미 다음이 됩니다.

- `Pokemon`가 HP·데미지·회복·리셋을 담당  
- `roll_damage`, `clamp_hp` 같은 **규칙 함수**가 분리됨  
- `request.args.get("skill")`로 어떤 버튼을 눌렀는지 읽음  
- `skill_damage()` 딕셔너리로 **데미지 범위만** 다름  

3주차는 “데미지만 다르다”에서 한 단계 더 — **행동 종류**까지 다르게 만듭니다.

---

## 3. 핵심 개념: 스킬 = 작은 설계도 묶음

한 기술을 **딕셔너리 한 줄**로 표현합니다.

```python
SKILLS = {
    "thunder": {
        "name": "전기쇼크",
        "kind": "attack",
        "damage": (15, 25),
    },
    "quick": {
        "name": "전광석화",
        "kind": "attack",
        "damage": (8, 14),
    },
    "heal": {
        "name": "회복",
        "kind": "heal",
        "heal": (10, 20),
    },
}
```

- `kind`가 `"attack"`이면 `take_damage`, `"heal"`이면 `heal` 메서드 호출  
- 나중에 `"kind": "buff"` 같은 값을 추가하기 쉬움  
- **같은 패턴**으로 플레이어·적 기술표를 각각 둘 수 있음  

**한 줄 메시지(학생용):**  
> “버튼 이름(`skill`)은 **열쇠**이고, `SKILLS` 딕셔너리가 **그 열쇠에 맞는 규칙 상자**예요.”

---

## 4. 실습 과제(난이도 순)

### A단계 — 스킬 딕셔너리로 통합 (★)

- `skill_damage()` 함수를 없애고 `SKILLS` 상수로 교체  
- `get_skill(skill_id)` 함수: 없는 id면 기본 기술 반환  
- 로그에 `SKILLS[skill]["name"]` 사용 → 하드코딩 문자열 줄이기  

**체크:** 전기쇼크 / 전광석화 / 10만볼트를 눌렀을 때 데미지 범위와 로그가 달라지는지.

### B단계 — 공격 vs 회복 한 라우트로 (★★)

지금은 `/attack`과 `/heal`이 나뉘어 있습니다. 3주차 목표 중 하나는:

```python
skill_data = get_skill(request.args.get("skill", "thunder"))

if skill_data["kind"] == "attack":
    low, high = skill_data["damage"]
    amount = roll_damage(low, high)
    enemy.take_damage(amount)
    message = f"{player.name}의 {skill_data['name']}! {amount} 데미지!"
elif skill_data["kind"] == "heal":
    low, high = skill_data["heal"]
    amount = roll_damage(low, high)
    player.heal(amount)
    message = f"{player.name}의 {skill_data['name']}! {amount} 회복!"
```

- 회복 버튼: `fetch('/attack?skill=heal')` 로 바꿔도 됨 (REST 이름은 나중에 논의)  
- **적 턴**은 그대로: 살아 있으면 반격  

### C단계 — 적도 기술表 + 랜덤 선택 (★★★)

```python
ENEMY_SKILLS = {
    "scratch": {"name": "할퀴기", "kind": "attack", "damage": (8, 15)},
    "ember": {"name": "불꽃세례", "kind": "attack", "damage": (12, 22)},
}

def enemy_turn(enemy: Pokemon, player: Pokemon) -> str:
    skill_id = random.choice(list(ENEMY_SKILLS.keys()))
    skill = ENEMY_SKILLS[skill_id]
    damage = roll_damage(*skill["damage"])
    player.take_damage(damage)
    return f"{enemy.name}의 {skill['name']}! {damage} 데미지!"
```

- “반격!” 고정 문구 → **적이 어떤 기술을 썼는지** 로그에 표시  
- `random.choice`로 매 턴 다른 기술 — 게임이 훨씬 살아남  

### D단계 — `Battle` 클래스 (★★★★, 선택)

```python
class Battle:
    def __init__(self, player: Pokemon, enemy: Pokemon):
        self.player = player
        self.enemy = enemy

    def run_player_turn(self, skill_id: str) -> str:
        ...

    def run_enemy_turn(self) -> str:
        ...

    def run_turn(self, skill_id: str) -> str:
        if not self.player.is_alive() or not self.enemy.is_alive():
            return "게임 종료!"
        msg = self.run_player_turn(skill_id)
        if self.enemy.is_alive():
            msg += "\n" + self.run_enemy_turn()
        return msg
```

Flask 라우트는:

```python
message = battle.run_turn(skill)
return jsonify({...})
```

**역할 분리:** Flask = HTTP, `Battle` = 게임 규칙.

### E단계 — 고급 액션 아이디어 (도전)

시간·수준이 되면 아래 중 **하나만** 골라 확장:

| 아이디어 | 배우는 것 | 구현 힌트 |
|----------|-----------|-----------|
| **명중률** | 확률 + 조건 | `random.random() < 0.9` 실패 시 “빗나감!” |
| **연속 공격** | 반복문 | `for _ in range(2): ...` |
| **자기 데미지** | 트레이드오프 | 10만볼트: 큰 데미지 + `player.take_damage(5)` |
| **기술 쿨다운** | 상태 저장 | `Pokemon`에 `self.cooldowns = {}` |
| **타입 상성** | 중첩 dict | `TYPE_CHART["fire"]["grass"] = 1.5` |

---

## 5. 프론트엔드(선택)

2주차 HTML은 이미 `attack('thunder')` 등을 보냅니다. 3주차에서:

- 회복 버튼을 `attack('heal')`로 통일하거나, `/heal` 유지 후 서버만 정리  
- 로그에 `\n`이 있으므로 `white-space: pre-line` 유지 (이미 `style.css`에 있음)  
- (보너스) 기술 버튼 클릭 시 짧은 CSS 애니메이션 — **파이썬 class와 HTML class는 다른 개념**이라고 짚기 좋음  

---

## 6. 정리 질문

1. `SKILLS["thunder"]`와 `SKILLS.get("thunder")`의 차이는?  
2. 같은 `attack()` 함수 안에서 `if kind == "attack"` / `"heal"`로 나누는 이유는?  
3. `Battle` 클래스를 만들면 Flask `attack()` 함수가 짧아지는 이유는?

---

## 7. 교사용 대본(마크다운)

### 도입(약 5분)

“2주까지 우리는 캐릭터를 `Pokemon`로 만들고, 버튼마다 `skill`이라는 이름을 서버에 보냈어요. 그런데 지금은 데미지 숫자만 조금 다를 뿐이에요. 오늘은 **전기쇼크랑 회복이 진짜 다른 행동**이 되게 만들 거예요. 포켓몬 게임에서 기술마다 설명이 다른 것처럼, 우리도 **기술표**를 코드로 적어 둡니다.”

### 개념(약 10분)

“딕셔너리 안에 또 딕셔너리를 넣을 수 있어요. 바깥 키는 `thunder`, `heal` 같은 **기술 id**고, 안쪽에는 이름, 종류, 데미지 범위가 들어갑니다. 새 기술을 추가할 때 `if skill == 'xxx'`를 계속 늘리는 대신, **표에 한 줄 추가**하면 끝나게 만드는 게 목표예요.”

### 라이브 코딩(약 15분)

“`SKILLS`를 파일 위쪽에 선언합니다. `attack()`에서 `skill = request.args.get(...)` 다음에 `skill_data = get_skill(skill)` … `kind`가 attack이면 적에게, heal이면 플레이어에게. 한 번 돌려 보면 회복 버튼 눌렀을 때 적 HP가 안 깎이고 플레이어 HP가 오르죠?”

### 실습(약 25~40분)

“A단계 끝난 팀은 B로. C까지 간 팀은 옆 팀에게 ‘적이 이번 턴에 뭐 썼는지’ 로그 보여 주기.”

### 마무리(약 5분)

“함수는 규칙 조각, 클래스는 캐릭터, 오늘은 **기술표**로 규칙을 데이터로 모았어요. 게임을 키울수록 `if`가 길어지는 대신 **표를 고치는** 쪽이 더 안전해집니다. 다음에는 타입 상성이나 명중률 같은 **한 가지 고급 규칙**만 골라서 E단계에 도전해 보면 좋아요.”

---

## 8. 부록 — 3주차 목표 스켈레톤

학생이 A→B까지 채우기 좋은 뼈대입니다. `materials/reference/app_week3_skills.py`와 비교해 볼 수 있습니다.

```python
SKILLS = {
    "thunder": {"name": "전기쇼크", "kind": "attack", "damage": (15, 25)},
    "quick": {"name": "전광석화", "kind": "attack", "damage": (8, 14)},
    "volt": {"name": "10만볼트", "kind": "attack", "damage": (20, 30)},
    "heal": {"name": "회복", "kind": "heal", "heal": (10, 20)},
}


def get_skill(skill_id: str) -> dict:
    return SKILLS.get(skill_id, SKILLS["thunder"])


def resolve_player_action(player: Pokemon, enemy: Pokemon, skill_id: str) -> str:
    skill = get_skill(skill_id)
    if skill["kind"] == "attack":
        amount = roll_damage(*skill["damage"])
        enemy.take_damage(amount)
        return f"{player.name}의 {skill['name']}! {amount} 데미지!"
    if skill["kind"] == "heal":
        amount = roll_damage(*skill["heal"])
        player.heal(amount)
        return f"{player.name}의 {skill['name']}! {amount} 회복!"
    return "알 수 없는 기술!"
```

---

## 9. 2주차 ↔ 3주차 변경 요약

| 항목 | 2주차 완성 | 3주차 목표 |
|------|------------|------------|
| 스킬 정보 | `skill_damage()` 튜플 | `SKILLS` dict of dict |
| 회복 | `/heal` 별도 라우트 | (선택) `/attack` + `kind: heal` |
| 적 행동 | 고정 반격 데미지 | `ENEMY_SKILLS` + 랜덤 |
| 턴 로직 | `attack()` 함수 안 | (선택) `Battle.run_turn()` |
