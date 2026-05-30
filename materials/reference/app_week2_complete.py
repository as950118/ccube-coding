import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# --- 차시 1: 게임 규칙 함수 ---

def roll_damage(low: int, high: int) -> int:
    return random.randint(low, high)


def clamp_hp(hp: int) -> int:
    return max(hp, 0)


# --- 차시 2: Pokemon 클래스 ---

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


def is_game_over(player: Pokemon, enemy: Pokemon) -> bool:
    return not player.is_alive() or not enemy.is_alive()


def game_over_response(player: Pokemon, enemy: Pokemon, message: str = "게임 종료!"):
    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": message,
    })


def skill_damage(skill: str) -> tuple[int, int, str]:
    """플레이어 기술별 (최소 데미지, 최대 데미지, 로그용 이름)."""
    skills = {
        "thunder": (15, 25, "전기쇼크"),
        "quick": (8, 14, "전광석화"),
        "volt": (20, 30, "10만볼트"),
    }
    return skills.get(skill, (10, 20, "공격"))


player = Pokemon("Pikachu", 100)
enemy = Pokemon("Charmander", 100)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/attack")
def attack():
    global player, enemy

    if is_game_over(player, enemy):
        return game_over_response(player, enemy)

    skill = request.args.get("skill", "thunder")
    low, high, label = skill_damage(skill)
    player_damage = roll_damage(low, high)
    enemy.take_damage(player_damage)

    message = f"{player.name}의 {label}! {player_damage} 데미지!"

    if enemy.is_alive():
        enemy_damage = roll_damage(10, 20)
        player.take_damage(enemy_damage)
        message += f"\n{enemy.name}의 반격! {enemy_damage} 데미지!"

    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": message,
    })


@app.route("/heal")
def heal():
    global player, enemy

    if is_game_over(player, enemy):
        return game_over_response(player, enemy)

    player_heal = roll_damage(10, 20)
    player.heal(player_heal)
    message = f"{player.name}의 회복! {player_heal} 회복!"

    if enemy.is_alive():
        enemy_heal = roll_damage(5, 15)
        enemy.heal(enemy_heal)
        message += f"\n{enemy.name}의 회복! {enemy_heal} 회복!"

    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": message,
    })


@app.route("/reset")
def reset():
    global player, enemy

    player.reset()
    enemy.reset()

    return jsonify({
        "player_hp": player.hp_percent(),
        "enemy_hp": enemy.hp_percent(),
        "message": "게임 리셋 완료",
    })


if __name__ == "__main__":
    app.run(debug=True)
