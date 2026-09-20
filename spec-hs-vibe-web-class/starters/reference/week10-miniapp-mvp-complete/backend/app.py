import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_KEY"],
)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/items")
def list_items():
    res = supabase.table("guestbook").select("*").order("id", desc=True).limit(50).execute()
    return jsonify(res.data)


@app.post("/api/items")
def create_item():
    body = request.get_json(force=True, silent=True) or {}
    name = (body.get("name") or "").strip()[:50]
    message = (body.get("message") or "").strip()[:200]

    if not name or not message:
        return jsonify({"error": "name and message are required"}), 400

    res = supabase.table("guestbook").insert({"name": name, "message": message}).execute()
    return jsonify(res.data[0]), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
