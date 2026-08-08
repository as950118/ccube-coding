import requests

SERVER_URL = "http://172.30.1.53:5001"

class ChatMessage:
    def __init__(self, student_id, message):
        self.student_id = student_id
        self.message = message
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "message": self.message
        }
    def send(self, server_url):
        try:
            response = requests.post(
                server_url + "/api/messages",
                json=self.to_dict(),
            )
            result = response.json()
            print("상태 코드:", response.status_code)
            print("서버 응답:", result["message"])

            return result["messages"]
        except:
            print("오류발생!")

chat1 = ChatMessage(
    "son",
    "안녕하세요!!1"
)
chat1.send(SERVER_URL)
