const subjectInput = document.getElementById("subject-input");
const quizResultEl = document.getElementById("quiz-result");
const loadingEl = document.getElementById("loading");

async function generateQuiz(subject) {
    loadingEl.classList.remove("hidden");
    quizResultEl.textContent = "";

    try {
        const url = subject
            ? `/api/generate-quiz?subject=${encodeURIComponent(subject)}`
            : "/api/generate-quiz";
        const res = await fetch(url);
        const data = await res.json();
        quizResultEl.textContent = data.quiz;
    } finally {
        loadingEl.classList.add("hidden");
    }
}

document.getElementById("btn-generate").addEventListener("click", () => {
    generateQuiz(subjectInput.value.trim());
});

subjectInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        document.getElementById("btn-generate").click();
    }
});
