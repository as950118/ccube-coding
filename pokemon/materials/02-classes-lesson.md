# 차시 2 — 클래스로 플레이어와 적을 “같은 종류”로 만들기

**대상:** 중학생 · 차시 1(함수)에서 `apply_damage` 등으로 코드를 조금 나눠 본 상태가 이상적  
**소요:** 약 60~90분  
**기준 코드:** 프로젝트 루트의 `app.py` (`player`, `enemy` 딕셔너리 구조)

---

## 1. 이 차시에서 배우는 것

- `player`와 `enemy`가 **같은 모양의 데이터**인 이유를 “설계도 한 장”으로 설명할 수 있다.
- `class`, `__init__`, `self`를 이용해 **객체 두 개**를 만든다.
- HP 처리(`take_damage`, `reset` 등)를 **메서드**로 옮겨 Flask 라우트를 짧게 만든다.

**시각 자료:** `visual/class-pokemon-diagram.html`

---

## 2. 지금 코드가 말해 주는 사실

`app.py`에는 구조가 같은 딕셔너리가 두 개 있습니다.

```python
player = {"name": "Pikachu", "hp": 100, "max_hp": 100}
enemy = {"name": "Charmander", "hp": 100, "max_hp": 100}
```

- 키 이름이 같다 → “전투에 참가하는 캐릭터”라는 **같은 종류**  
- 값만 다르다 → **설정(이름, 종족 이미지 등)**이 다름  

클래스는 이걸 한 문장으로 압축합니다.

> “`Pokemon`라는 설계도로 **피카츄 카드**와 **파이리 카드**를 찍어낸다.”

---

## 3. 클래스를 도입하는 최소 단계

### 3-1. `Pokemon` 설계도

학생에게 외우게 할 단어는 최소로:

- `class Pokemon:` — 설계도 시작  
- `def __init__(self, name, max_hp):` — **태어날 때** 정해지는 값  
- `self.name`, `self.hp` — 각 카드마다 따로 가지는 값  

### 3-2. 객체 두 개 만들기

```python
player = Pokemon("Pikachu", 100)
enemy = Pokemon("Charmander", 100)
```

여기서 중요한 질문 하나:

> “`class`는 몇 번 쓰고, `Pokemon(...)`는 몇 번 쓰나요?”

정답: **class 한 번, 생성은 두 번** → 인스턴스가 둘.

### 3-3. 메서드로 옮길 후보(차시 1과 연결)

차시 1에서 만든 `apply_damage(fighter_dict, ...)`를 생각해 보면, 이제는:

- `fighter.take_damage(amount)`  
- `fighter.reset()` → `self.hp = self.max_hp`  
- `fighter.is_alive()` → `self.hp > 0`  

처럼 **“캐릭터가 할 수 있는 동작”**을 붙이면 읽기 쉬워집니다.

---

## 4. Flask와 붙일 때의 실용 팁

### 4-1. JSON으로 보내기

프론트는 퍼센트 막대를 위해 숫자를 기대합니다. 객체로 바꾼 뒤에는 예를 들어:

```python
return jsonify({
    "player_hp": int(player.hp / player.max_hp * 100),
    "enemy_hp": int(enemy.hp / enemy.max_hp * 100),
    "message": message,
})
```

처럼 **딕셔너리로 직렬화**하는 한 줄이 라우트에 들어갈 수 있습니다.  
(또는 `player.to_ui()` 같은 메서드를 클래스에 두면 라우트가 더 짧아짐)

### 4-2. `global` 줄이기

전역 딕셔너리를 고치기 위해 `global player, enemy`를 쓰던 패턴은, 객체를 **같은 이름의 전역 변수**로 두면 여전히 `global`이 필요할 수 있습니다. 중학생 수업에서는:

- “지금은 전역으로 두고 구조만 클래스로 바꾼다”  
- 심화반에서만 “게임 상태를 담는 `Battle` 클래스”로 한 단계 더  

처럼 나누는 것을 권장합니다.

---

## 5. 실습 과제(난이도 순)

### A단계 — `Pokemon` 만들고 출력만 (★)

- `__init__`에서 `self.hp = max_hp`  
- `introduce(self)` 메서드로 `print` 또는 문자열 반환  

### B단계 — `take_damage` / `reset` (★★)

- `take_damage(self, amount)`: HP 감소 + 0 미만 방지  
- `reset(self)`: HP를 max로  

`app.py`의 `/reset` 라우트는 `player.reset(); enemy.reset()` 정도로 줄어들게 합니다.

### C단계 — `attack` 라우트 읽기 리팩터 (★★★)

- `enemy.take_damage(player_damage)`  
- 살아 있으면 `player.take_damage(enemy_damage)`  

### D단계 — (선택) `Battle` 클래스

```python
battle = Battle(player, enemy)
message = battle.run_turn(skill)
```

전투 규칙을 한곳에 모으는 패턴. 시간이 넉넉할 때만.

---

## 6. 흔한 질문 FAQ(교실용)

| 질문 | 답변 방향 |
|------|-----------|
| `self`가 뭐예요? | “지금 이 카드 자기 자신”이라고 부르는 관습적인 이름 |
| 왜 `__init__`에 밑줄이 두 개예요? | 파이썬이 정해 둔 “태어날 때 자동 호출” 자리 — 지금은 패턴으로 받아들이기 |
| 딕셔너리가 더 쉬운데요? | 작을 땐 맞음. 커지면 클래스가 실수를 줄여 줌 |

---

## 7. 정리 질문

1. `Pokemon`는 데이터인가요, 동작인가요? (둘 다 있다고 정리)  
2. 같은 클래스로 만든 `player`와 `enemy`는 어디가 같고 어디가 다른가요?  
3. `reset()`을 클래스 안에 두면 무엇이 좋아지나요?

---

## 8. 교사용 대본(마크다운)

### 도입(약 5분)

“지난 시간에 우리는 `attack()`을 잘게 잘랐어요. 오늘은 잘라낸 조각을 **캐릭터에게 붙일** 거예요. `player`랑 `enemy`를 보면 키가 똑같죠? 이름, hp, max_hp. 이건 우연이 아니라 ‘같은 종류’라는 뜻이에요.”

### 비유(약 5분)

“클래스는 **공장 설계도**예요. 설계도는 한 장인데, 그걸로 찍어낸 제품은 여러 개가 될 수 있어요. 피카츄 제품, 파이리 제품. 제품 하나하나를 객체, 인스턴스라고 불러요.”

### 라이브 코딩(약 15분)

“`class Pokemon:`를 씁니다. `def __init__(self, name, max_hp):`에서 `self.name = name` … 여기까지 저장하고, 아래에 `player = Pokemon('Pikachu', 100)`을 쳐 볼게요. 이제 `player.hp`처럼 점으로 들어가요. 딕셔너리의 `player['hp']`랑 비슷하지만, 오타를 조금 더 잡아 줄 수 있어요.”

### 시각 자료(약 5분)

“`visual/class-pokemon-diagram.html`을 보면, 설계도 하나에서 두 마리가 나왔죠?”

### 실습(약 25~40분)

“A에서 `introduce`까지 된 사람은 B로. `reset`까지 연결한 사람은 Flask `/reset`도 바꿔 보기.”

### 마무리(약 5분)

“함수는 **행동의 이름표**였고, 클래스는 **데이터와 행동을 한 팀으로 묶는 이름표**예요. 다음 시간(3주차)에는 버튼마다 다른 `skill`을 **기술표 딕셔너리**로 정리해서, 공격이랑 회복이 진짜 다른 행동이 되게 만들 거예요.”

---

## 9. 부록 — 참고: 최소 `Pokemon` 예시

수업에서 그대로 타이핑하기보다는, **끝 상태 예시**로만 보여 주고 학생은 A→B 단계로 채우게 하는 편이 안전합니다.

```python
class Pokemon:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def reset(self) -> None:
        self.hp = self.max_hp

    def is_alive(self) -> bool:
        return self.hp > 0
```
