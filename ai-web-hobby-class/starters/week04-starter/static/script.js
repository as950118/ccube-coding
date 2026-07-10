// ===== 4주차: O/X 버튼 → fetch → Python 이 정답 판정 =====
// 3주차: fetch('/api/add?a=...') → 이번 주: fetch('/api/check?q=...&answer=O')

const userAnswers = {};

// ===== [🟢] O/X 버튼 클릭 → fetch → 맞/틀 표시 =====
async function handleAnswer(card, answer) {
    const qIndex = card.dataset.index;
    const feedbackEl = card.querySelector(".feedback");

    const res = await fetch(`/api/check?q=${qIndex}&answer=${answer}`);
    const data = await res.json();

    feedbackEl.textContent = data.message;
    feedbackEl.classList.remove("correct", "wrong");
    feedbackEl.classList.add(data.correct ? "correct" : "wrong");

    userAnswers[qIndex] = answer;

    // ===== [🔴] 도전: 모든 문제 답하면 /api/score 호출 =====
    const totalQuestions = document.querySelectorAll(".question-card").length;
    if (Object.keys(userAnswers).length === totalQuestions) {
        await showScore(totalQuestions);
    }
}

// ===== [🔴] 도전: Python /api/score 로 총점 표시 =====
async function showScore(totalQuestions) {
    const answers = [];
    for (let i = 0; i < totalQuestions; i++) {
        answers.push(userAnswers[i] || "");
    }
    const res = await fetch(`/api/score?answers=${answers.join(",")}`);
    const data = await res.json();
    const panel = document.getElementById("score-panel");
    const text = document.getElementById("score-text");
    text.textContent = `총점: ${data.score} / ${data.total}`;
    panel.classList.remove("hidden");
}

document.querySelectorAll(".question-card").forEach((card) => {
    card.querySelectorAll(".btn-o, .btn-x").forEach((btn) => {
        btn.addEventListener("click", () => handleAnswer(card, btn.dataset.answer));
    });
});
