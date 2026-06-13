// ===== 5주차: 질문 입력 → fetch POST → Python call_ai() → AI 답 표시 =====
// 4주차: fetch('/api/check?q=...') → 이번 주: fetch('/api/chat', { method: 'POST' })

const questionInput = document.getElementById("question-input");
const replyEl = document.getElementById("reply");

// ===== [🟢] fetch POST → /api/chat → reply 표시 =====
async function askAi(question) {
    const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
    });
    const data = await res.json();
    replyEl.textContent = data.reply;
}

// ===== [🟢] 기본 질문 — question 빈 문자열이면 Python DEFAULT_QUESTION 사용 =====
document.getElementById("btn-default").addEventListener("click", () => {
    askAi("");
});

// ===== [🟡] 입력창 질문 보내기 =====
document.getElementById("btn-send").addEventListener("click", () => {
    const question = questionInput.value.trim();
    if (!question) {
        replyEl.textContent = "질문을 입력해 주세요!";
        return;
    }
    askAi(question);
});

questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        document.getElementById("btn-send").click();
    }
});

// ===== [🔴] 도전: 「생각 중…」 로딩 표시 =====
// async function askAi(question) {
//     const loadingEl = document.getElementById("loading");
//     loadingEl.classList.remove("hidden");
//     replyEl.textContent = "";
//     try {
//         const res = await fetch("/api/chat", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ question }),
//         });
//         const data = await res.json();
//         replyEl.textContent = data.reply;
//     } finally {
//         loadingEl.classList.add("hidden");
//     }
// }
