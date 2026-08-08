// ===== 8주차: 말풍선 채팅 UI + Python history =====
// 7주차: 답 1개 표시 → 이번 주: appendMessage() 로 쌓기

const chatLog = document.getElementById("chat-log");
const questionInput = document.getElementById("question-input");

// ===== [🟢] 말풍선 추가 — .bubble-user / .bubble-ai =====
function appendMessage(role, text) {
    const empty = chatLog.querySelector(".chat-empty");
    if (empty) empty.remove();

    const bubble = document.createElement("div");
    bubble.className = role === "user" ? "bubble bubble-user" : "bubble bubble-ai";
    bubble.textContent = text;
    chatLog.appendChild(bubble);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function renderHistory(history) {
    chatLog.innerHTML = "";
    if (!history || history.length === 0) {
        chatLog.innerHTML = '<p class="chat-empty">아직 대화가 없어요. 아래 질문을 보내 보세요!</p>';
        return;
    }
    history.forEach((msg) => appendMessage(msg.role, msg.text));
}

async function sendQuestion() {
    const question = questionInput.value.trim();
    if (!question) return;

    questionInput.value = "";
    appendMessage("user", question);

    const thinking = document.createElement("div");
    thinking.className = "bubble bubble-ai bubble-thinking";
    thinking.textContent = "생각 중…";
    chatLog.appendChild(thinking);
    chatLog.scrollTop = chatLog.scrollHeight;

    try {
        const res = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question }),
        });
        const data = await res.json();
        thinking.remove();

        // [🟡] history 가 있으면 전체 다시 그리기, 없으면 reply 만 추가
        if (data.history) {
            renderHistory(data.history);
        } else if (data.reply) {
            appendMessage("ai", data.reply);
        } else if (data.error) {
            appendMessage("ai", data.error);
        }
    } catch (err) {
        thinking.remove();
        appendMessage("ai", "오류가 났어요. Run 중인지 확인해 주세요.");
    }
}

document.getElementById("btn-send").addEventListener("click", sendQuestion);

// ===== [🟡] Enter 로 전송 =====
questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendQuestion();
    }
});

// ===== [🔴] 도전: /api/clear —— index.html 버튼 주석 해제 후 사용 =====
const clearBtn = document.getElementById("btn-clear");
if (clearBtn) {
    clearBtn.addEventListener("click", async () => {
        const res = await fetch("/api/clear", { method: "POST" });
        const data = await res.json();
        renderHistory(data.history);
    });
}
