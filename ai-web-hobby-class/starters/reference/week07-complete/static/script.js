// ===== 7주차: 탭 전환 + 챗봇(/api/chat) + 퀴즈(/api/generate-quiz) =====
// [🔴] OX 탭 버튼 주석 해제 후 /api/check 도 동작합니다

// ---------- 탭 전환 ----------
document.querySelectorAll(".tab").forEach((tab) => {
    tab.addEventListener("click", () => {
        const target = tab.dataset.tab;

        document.querySelectorAll(".tab").forEach((t) => {
            t.classList.toggle("active", t === tab);
            t.setAttribute("aria-selected", t === tab ? "true" : "false");
        });

        document.querySelectorAll(".panel").forEach((panel) => {
            const isActive = panel.id === `panel-${target}`;
            panel.classList.toggle("active", isActive);
            panel.hidden = !isActive;
        });
    });
});

// ---------- 탭 1: AI 챗봇 (5주차) ----------
const questionInput = document.getElementById("question-input");
const replyEl = document.getElementById("reply");

async function askAi(question) {
    const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
    });
    const data = await res.json();
    replyEl.textContent = data.reply;
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

// ---------- 탭 2: AI 퀴즈 (6주차) ----------
const subjectInput = document.getElementById("subject-input");
const quizResultEl = document.getElementById("quiz-result");

async function generateQuiz(subject) {
    const url = subject
        ? `/api/generate-quiz?subject=${encodeURIComponent(subject)}`
        : "/api/generate-quiz";
    const res = await fetch(url);
    const data = await res.json();
    quizResultEl.textContent = data.quiz;
}

document.getElementById("btn-generate").addEventListener("click", () => {
    generateQuiz(subjectInput.value.trim());
});

subjectInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        document.getElementById("btn-generate").click();
    }
});

// ---------- [🔴] 탭 3: OX 퀴즈 (4주차) ----------
document.querySelectorAll(".question-card").forEach((card) => {
    card.querySelectorAll(".btn-o, .btn-x").forEach((btn) => {
        btn.addEventListener("click", async () => {
            const qIndex = card.dataset.index;
            const answer = btn.dataset.answer;
            const feedbackEl = card.querySelector(".feedback");

            const res = await fetch(`/api/check?q=${qIndex}&answer=${answer}`);
            const data = await res.json();

            feedbackEl.textContent = data.message;
            feedbackEl.classList.remove("correct", "wrong");
            feedbackEl.classList.add(data.correct ? "correct" : "wrong");
        });
    });
});
