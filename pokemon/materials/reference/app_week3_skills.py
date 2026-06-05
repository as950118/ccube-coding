"""
3주차 목표 예시 — 스킬 딕셔너리 + 적 랜덤 기술 + Battle 클래스.
2주차 완성본(app_week2_complete.py)에서 A~D 단계를 모두 적용한 참고용 코드.
"""
import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

SKILLS = {
    "thunder": {"name": "전기쇼크", "kind": "attack", "damage": (15, 25)},
    "quick": {"name": "전광석화", "kind": "attack", "damage": (8, 14)},
    "volt": {"name": "10만볼트", "kind": "attack", "damage": (20, 30)},
    "heal": {"name": "회복", "kind": "heal", "heal": (10, 20)},
}

ENEMY_SKILLS = {
    "scratch": {"name": "할퀴기", "kind": "attack", "damage": (8, 15)},
    "ember": {"name": "불꽃세례", "kind": "attack", "damage": (12, 22)},
}


def roll_damage(low: int, high: int) -> int:
    return random.randint(low, high)


def clamp_hp(hp: int) -> int:
    return max(hp, 0)


def get_skill(skill_id: str) -> dict:
    return SKILLS.get(skill_id, SKILLS["thunder"])


class Pokemon:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    def take_damage(self, amount: int) -> None:
        self.hp = clamp_hp(self.hp - amount)

    def heal(self, amount: int) -> None:
        self.hp = min(self.hp + amount, self.max_hp)

    def reset(self) -> None:
        self.hp = self.max_hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def hp_percent(self) -> int:
        return int(self.hp / self.max_hp * 100)


class Battle:
    def __init__(self, player: Pokemon, enemy: Pokemon):
        self.player = player
        self.enemy = enemy

    def run_player_turn(self, skill_id: str) -> str:
        skill = get_skill(skill_id)
        if skill["kind"] == "attack":
            amount = roll_damage(*skill["damage"])
            self.enemy.take_damage(amount)
            return f"{self.player.name}의 {skill['name']}! {amount} 데미지!"
        if skill["kind"] == "heal":
            amount = roll_damage(*skill["heal"])
            self.player.heal(amount)
            return f"{self.player.name}의 {skill['name']}! {amount} 회복!"
        return "알 수 없는 기술!"

    def run_enemy_turn(self) -> str:
        skill_id = random.choice(list(ENEMY_SKILLS.keys()))
        skill = ENEMY_SKILLS[skill_id]
        amount = roll_damage(*skill["damage"])
        self.player.take_damage(amount)
        return f"{self.enemy.name}의 {skill['name']}! {amount} 데미지!"

    def run_turn(self, skill_id: str) -> str:
        if not self.player.is_alive() or not self.enemy.is_alive():
            return "게임 종료!"
        message = self.run_player_turn(skill_id)
        if self.enemy.is_alive():
            message += "\n" + self.run_enemy_turn()
        return message


player = Pokemon("Pikachu", 100)
enemy = Pokemon("Charmander", 100)
battle = Battle(player, enemy)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/attack")
def attack():
    skill = request.args.get("skill", "thunder")
    message = battle.run_turn(skill)
    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": message,
    })


@app.route("/heal")
def heal():
    message = battle.run_turn("heal")
    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": message,
    })


@app.route("/reset")
def reset():
    player.reset()
    enemy.reset()
    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": "게임 리셋 완료",
    })


if __name__ == "__main__":
    app.run(debug=True)
