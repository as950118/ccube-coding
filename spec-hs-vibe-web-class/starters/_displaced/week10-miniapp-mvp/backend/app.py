import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

# TODO 1: Supabase 프로젝트를 만들고, SUPABASE_URL / SUPABASE_SERVICE_KEY를
#         .env(로컬)과 Render 환경변수(배포)에 등록한 뒤 아래 두 줄이 동작하는지 확인
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_KEY"],
)

TABLE_NAME = "items"  # TODO 2: 내 미니앱에 맞는 테이블 이름으로 바꾸기 (예: posts, guestbook)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/items")
def list_items():
    # TODO 3: TABLE_NAME에서 최신순으로 목록을 가져오기
    res = supabase.table(TABLE_NAME).select("*").order("id", desc=True).limit(50).execute()
    return jsonify(res.data)


@app.post("/api/items")
def create_item():
    body = request.get_json(force=True, silent=True) or {}

    # TODO 4: 내 데이터 모양에 맞게 필드를 검증하고 insert 하기
    # 예: name, message 두 필드가 비어있지 않은지 확인
    name = (body.get("name") or "").strip()[:50]
    message = (body.get("message") or "").strip()[:200]

    if not name or not message:
        return jsonify({"error": "name and message are required"}), 400

    res = supabase.table(TABLE_NAME).insert({"name": name, "message": message}).execute()
    return jsonify(res.data[0]), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
