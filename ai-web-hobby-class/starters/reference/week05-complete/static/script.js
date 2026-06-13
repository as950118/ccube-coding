const questionInput = document.getElementById("question-input");
const replyEl = document.getElementById("reply");
const loadingEl = document.getElementById("loading");

async function askAi(question) {
    loadingEl.classList.remove("hidden");
    replyEl.textContent = "";

    try {
        const res = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question }),
        });
        const data = await res.json();
        replyEl.textContent = data.reply;
    } finally {
        loadingEl.classList.add("hidden");
    }
}

document.getElementById("btn-default").addEventListener("click", () => askAi(""));

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
