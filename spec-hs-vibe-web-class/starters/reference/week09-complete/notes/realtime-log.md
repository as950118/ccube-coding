# AI에게 준 프롬프트

목표: 이 Flask 게시판(app.py)에 실시간 채팅 기능을 추가하고 싶어.
요구사항: flask-socketio 사용, /chat은 로그인 필요하고 최근 30개 메시지를 DB에서 불러옴,
chat_messages 테이블에 저장, send_message -> new_message broadcast, 기존 라우트는 유지.
먼저 계획만 제안해줘.

# AI가 설명한 구조 요약

- `SocketIO(app)`을 만든 위치: `app.py` 상단, `app = Flask(__name__)` 바로 다음
- 서버가 메시지를 받는 이벤트 이름: `send_message` (`@socketio.on("send_message")`)
- 서버가 모든 접속자에게 방송하는 코드 줄: `emit("new_message", {...}, broadcast=True)`
- 브라우저 쪽에서 소켓 연결을 만드는 줄: `chat.html`의 `const socket = io();`
- `app.run(...)` → `socketio.run(app, ...)`로 바뀌었는가: 그렇다 (`if __name__ == "__main__":` 블록)

# 내가 직접 확인한 것 (두 브라우저로 테스트)

크롬 창 2개(하나는 시크릿 모드)로 각각 다른 계정 로그인 후 `/chat` 접속 → 한쪽에서 메시지를 보내니 다른 쪽에 새로고침 없이 바로 떴다. 서버를 껐다 켜도 이전 메시지가 남아 있는 것도 확인.

# 막혔던 점

처음엔 `app.run()`을 안 바꿔서 소켓 연결 자체가 안 됐다. `socketio.run(app, ...)`로 바꾸고 해결.

# 다음에 하고 싶은 것

접속 중인 인원 수를 화면에 표시하기
