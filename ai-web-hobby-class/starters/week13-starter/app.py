"""
AI웹반 13주차 — 보너스 프로젝트: Flask + SQLite 스마트홈 대시보드

[🟢] 이름/문구 바꾸기 + 장치 버튼 눌러보기
[🟡] 랜덤 이벤트 하나 더 추가하기
[🔴] 새 장치나 센서를 DB까지 연결하기
"""
import os
import random
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "smarthome.db"

STUDENT_NAME = "홍길동"
DASHBOARD_TITLE = "🏠 Smart Home Dashboard"


def get_connection() -> sqlite3.Connection:
    """SQLite 연결을 만들고 dict처럼 읽을 수 있게 설정합니다."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    """필요한 테이블을 만들고, 첫 상태를 한 번만 넣습니다."""
    with get_connection() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS home_state (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                light_level REAL NOT NULL,
                soil_moisture REAL NOT NULL,
                door_open INTEGER NOT NULL DEFAULT 0,
                lamp_on INTEGER NOT NULL DEFAULT 0,
                aircon_on INTEGER NOT NULL DEFAULT 0,
                fan_on INTEGER NOT NULL DEFAULT 0,
                temperature_target REAL NOT NULL,
                humidity_target REAL NOT NULL,
                light_target REAL NOT NULL,
                last_updated TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """
        )

        row = conn.execute("SELECT id FROM home_state WHERE id = 1").fetchone()
        if row is None:
            now = datetime.now().isoformat(timespec="seconds")
            conn.execute(
                """
                INSERT INTO home_state (
                    id, temperature, humidity, light_level, soil_moisture,
                    door_open, lamp_on, aircon_on, fan_on,
                    temperature_target, humidity_target, light_target, last_updated
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (1, 24.2, 52, 64, 58, 0, 0, 0, 0, 24.8, 55, 68, now),
            )

        event_count = conn.execute("SELECT COUNT(*) AS count FROM events").fetchone()["count"]
        if event_count == 0:
            log_event(conn, "스마트홈 서버가 시작되었습니다.")
            log_event(conn, "센서 값은 Flask가 계산하고 SQLite가 기억합니다.")


def log_event(conn: sqlite3.Connection, message: str) -> None:
    """최근 이벤트를 SQLite에 저장합니다."""
    conn.execute(
        "INSERT INTO events (message, created_at) VALUES (?, ?)",
        (message, datetime.now().isoformat(timespec="seconds")),
    )


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


def move_toward(current: float, target: float, max_step: float, noise: float) -> float:
    """목표값 쪽으로 조금씩 이동시키면 센서처럼 자연스럽게 보입니다."""
    difference = target - current
    limited_step = clamp(difference, -max_step, max_step)
    return current + limited_step + random.uniform(-noise, noise)


def load_state(conn: sqlite3.Connection) -> dict:
    row = conn.execute("SELECT * FROM home_state WHERE id = 1").fetchone()
    return dict(row)


def save_state(conn: sqlite3.Connection, state: dict) -> None:
    conn.execute(
        """
        UPDATE home_state
        SET temperature = ?,
            humidity = ?,
            light_level = ?,
            soil_moisture = ?,
            door_open = ?,
            lamp_on = ?,
            aircon_on = ?,
            fan_on = ?,
            temperature_target = ?,
            humidity_target = ?,
            light_target = ?,
            last_updated = ?
        WHERE id = 1
        """,
        (
            state["temperature"],
            state["humidity"],
            state["light_level"],
            state["soil_moisture"],
            state["door_open"],
            state["lamp_on"],
            state["aircon_on"],
            state["fan_on"],
            state["temperature_target"],
            state["humidity_target"],
            state["light_target"],
            state["last_updated"],
        ),
    )


def maybe_refresh_targets(state: dict) -> None:
    """센서 목표값을 가끔만 바꾸면 한 방향으로 조금씩 움직이는 흐름이 생깁니다."""
    if random.random() < 0.25:
        state["temperature_target"] = random.uniform(20.5, 29.0)
    if random.random() < 0.22:
        state["humidity_target"] = random.uniform(34, 72)
    if random.random() < 0.28:
        state["light_target"] = random.uniform(18, 90)


def trigger_random_event(state: dict, conn: sqlite3.Connection) -> None:
    """랜덤 스마트홈 이벤트를 만들고, 필요하면 상태도 함께 바꿉니다."""
    if random.random() >= 0.12:
        return

    event_type = random.choice(
        [
            "door_open",
            "door_close",
            "power_save",
            "rain",
            "hot",
            "dry",
            "sunny",
            "plant_dry",
        ]
    )

    if event_type == "door_open":
        state["door_open"] = 1
        log_event(conn, "현관문이 열렸습니다.")
    elif event_type == "door_close":
        state["door_open"] = 0
        log_event(conn, "현관문이 닫혔습니다.")
    elif event_type == "power_save":
        state["lamp_on"] = 0
        state["fan_on"] = 0
        log_event(conn, "전력이 절약 모드입니다. 사용하지 않는 장치를 잠시 쉬게 했습니다.")
    elif event_type == "rain":
        state["light_target"] = random.uniform(8, 28)
        log_event(conn, "비가 와서 조도가 낮아졌습니다.")
    elif event_type == "hot":
        state["temperature_target"] = random.uniform(28.6, 29.6)
        log_event(conn, "온도가 높아 에어컨 사용을 권장합니다.")
    elif event_type == "dry":
        state["humidity_target"] = random.uniform(31, 36)
        log_event(conn, "실내 공기가 건조해지고 있습니다.")
    elif event_type == "sunny":
        state["light_target"] = random.uniform(70, 92)
        log_event(conn, "햇빛이 들어와 거실이 더 밝아졌습니다.")
    elif event_type == "plant_dry":
        state["soil_moisture"] = clamp(state["soil_moisture"] - random.uniform(3, 6), 0, 100)
        log_event(conn, "화분 흙이 빠르게 마르고 있습니다.")


def advance_one_tick(state: dict, conn: sqlite3.Connection) -> None:
    """1초에 해당하는 센서 변화 1회."""
    maybe_refresh_targets(state)

    state["temperature"] = clamp(
        move_toward(state["temperature"], state["temperature_target"], 0.35, 0.05),
        18,
        30,
    )
    state["humidity"] = clamp(
        move_toward(state["humidity"], state["humidity_target"], 2.4, 0.5),
        30,
        80,
    )
    state["light_level"] = clamp(
        move_toward(state["light_level"], state["light_target"], 4.8, 1.2),
        0,
        100,
    )
    state["soil_moisture"] = clamp(state["soil_moisture"] - random.uniform(0.2, 1.0), 0, 100)

    # 장치가 켜져 있으면 값에 조금 영향을 줍니다.
    if state["aircon_on"]:
        state["temperature"] = clamp(state["temperature"] - random.uniform(0.1, 0.28), 18, 30)
    if state["fan_on"]:
        state["humidity"] = clamp(state["humidity"] - random.uniform(-0.2, 0.6), 30, 80)
    if state["lamp_on"]:
        state["light_level"] = clamp(state["light_level"] + random.uniform(1.2, 3.0), 0, 100)

    trigger_random_event(state, conn)


def advance_simulation(conn: sqlite3.Connection) -> dict:
    """마지막 업데이트 시각을 보고 1초 단위로 필요한 만큼만 시뮬레이션합니다."""
    state = load_state(conn)
    last_updated = datetime.fromisoformat(state["last_updated"])
    now = datetime.now()
    elapsed_seconds = max(0, int((now - last_updated).total_seconds()))

    # 오랫동안 페이지를 안 열어도 한 번에 너무 많이 변하지 않도록 상한을 둡니다.
    tick_count = min(elapsed_seconds, 6)
    for _ in range(tick_count):
        advance_one_tick(state, conn)

    state["last_updated"] = now.isoformat(timespec="seconds")
    save_state(conn, state)
    return state


def fetch_recent_events(conn: sqlite3.Connection, limit: int = 6) -> list[dict]:
    rows = conn.execute(
        """
        SELECT message, created_at
        FROM events
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()

    events = []
    for row in rows:
        event_time = datetime.fromisoformat(row["created_at"])
        events.append(
            {
                "message": row["message"],
                "time": event_time.strftime("%H:%M"),
            }
        )
    return events


def build_dashboard_response(conn: sqlite3.Connection) -> dict:
    state = load_state(conn)
    return {
        "temperature": round(state["temperature"], 1),
        "humidity": round(state["humidity"]),
        "light_level": round(state["light_level"]),
        "soil_moisture": round(state["soil_moisture"]),
        "door_open": bool(state["door_open"]),
        "devices": {
            "lamp": bool(state["lamp_on"]),
            "aircon": bool(state["aircon_on"]),
            "fan": bool(state["fan_on"]),
        },
        "events": fetch_recent_events(conn),
    }


def toggle_device(conn: sqlite3.Connection, device_name: str) -> None:
    device_columns = {
        "lamp": "lamp_on",
        "aircon": "aircon_on",
        "fan": "fan_on",
    }
    column_name = device_columns.get(device_name)
    if not column_name:
        raise ValueError("Unknown device")

    state = load_state(conn)
    state[column_name] = 0 if state[column_name] else 1
    save_state(conn, state)
    device_label = {"lamp": "전등", "aircon": "에어컨", "fan": "선풍기"}[device_name]
    log_event(conn, f"{device_label}이(가) {'켜졌습니다' if state[column_name] else '꺼졌습니다'}.")


def set_all_devices(conn: sqlite3.Connection, value: bool) -> None:
    state = load_state(conn)
    state["lamp_on"] = 1 if value else 0
    state["aircon_on"] = 1 if value else 0
    state["fan_on"] = 1 if value else 0
    save_state(conn, state)
    log_event(conn, f"모든 장치를 {'ON' if value else 'OFF'} 상태로 바꿨습니다.")


def water_plant(conn: sqlite3.Connection) -> None:
    state = load_state(conn)
    state["soil_moisture"] = clamp(state["soil_moisture"] + random.uniform(14, 24), 0, 100)
    save_state(conn, state)
    log_event(conn, "화분에 물을 주어 토양 습도가 올라갔습니다.")


@app.route("/")
def home():
    return render_template("index.html", name=STUDENT_NAME, dashboard_title=DASHBOARD_TITLE)


@app.route("/api/status")
def api_status():
    with get_connection() as conn:
        advance_simulation(conn)
        return jsonify(build_dashboard_response(conn))


@app.route("/api/device/toggle", methods=["POST"])
def api_toggle_device():
    data = request.get_json(silent=True) or {}
    device_name = data.get("device", "")

    try:
        with get_connection() as conn:
            toggle_device(conn, device_name)
            return jsonify(build_dashboard_response(conn))
    except ValueError:
        return jsonify({"error": "unknown device"}), 400


@app.route("/api/device/all", methods=["POST"])
def api_set_all_devices():
    data = request.get_json(silent=True) or {}
    value = bool(data.get("value"))

    with get_connection() as conn:
        set_all_devices(conn, value)
        return jsonify(build_dashboard_response(conn))


@app.route("/api/plant/water", methods=["POST"])
def api_water_plant():
    with get_connection() as conn:
        water_plant(conn)
        return jsonify(build_dashboard_response(conn))


if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5013))
    app.run(host="0.0.0.0", port=port, debug=True)
else:
    init_db()
