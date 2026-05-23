from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

class Pokemon:
    def __init__(self, name, hp, max_ph):
        self.name = name
        self.hp = hp
        self.max_ph = max_ph

    def attack(self):
        return random.randint(10, 25)

    def heal(self):
        return random.randint(10, 25)

    def reset(self):
        self.hp = self.max_ph

player = Pokemon("Pikachu", 100, 100)
enemy = Pokemon("Charmander", 100, 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heal")
def heal():
    global player, enemy

    if player.hp <= 0 or enemy.hp <= 0:
        return jsonify({
            "message": "게임 종료!"
        })

    player_heal = player.heal()
    player.hp += player_heal

    if enemy.hp < 0:
        enemy.hp = 0

    message = f"피카츄의 회복! {player_heal} 회복!"

    if enemy.hp > 0:
        enemy_heal = enemy.heal()
        enemy.hp += enemy_heal

        if player.hp < 0:
            player.hp = 0

        message += f"\n파이리의 회복! {enemy_heal} 회복!"

    return jsonify({
        "player_hp": player.hp,
        "enemy_hp": enemy.hp,
        "message": message
    })


@app.route("/attack")
def attack():
    global player, enemy

    if player.hp <= 0 or enemy.hp <= 0:
        return jsonify({
            "message": "게임 종료!"
        })

    player_damage = player.attack()
    enemy.hp -= player_damage

    if enemy.hp < 0:
        enemy.hp = 0

    message = f"피카츄의 공격! {player_damage} 데미지!"

    if enemy.hp > 0:
        enemy_damage = enemy.attack()
        player.hp -= enemy_damage

        if player.hp < 0:
            player.hp = 0

        message += f"\n파이리의 반격! {enemy_damage} 데미지!"

    return jsonify({
        "player_hp": player.hp,
        "enemy_hp": enemy.hp,
        "message": message
    })


@app.route("/reset")
def reset():
    global player, enemy

    player.reset()
    enemy.reset()

    return jsonify({
        "message": "게임 리셋 완료"
    })


app.run(debug=True)