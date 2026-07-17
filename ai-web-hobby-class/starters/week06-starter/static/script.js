// ===== 6주차: 과목 입력 → fetch → Python build_quiz_prompt() → AI 퀴즈 표시 =====
// 5주차: fetch('/api/chat', POST) → 이번 주: fetch('/api/generate-quiz?subject=...')

const subjectInput = document.getElementById("subject-input");
const quizResultEl = document.getElementById("quiz-result");

// ===== [🟢] fetch GET → /api/generate-quiz → quiz 표시 =====
async function generateQuiz(subject) {
    const url = subject
        ? `/api/generate-quiz?subject=${encodeURIComponent(subject)}`
        : "/api/generate-quiz";

    const res = await fetch(url);
    const data = await res.json();
    quizResultEl.textContent = data.quiz;
}

// ===== [🟢] 퀴즈 생성 버튼 =====
document.getElementById("btn-generate").addEventListener("click", () => {
    const subject = subjectInput.value.trim();
    generateQuiz(subject);
});

subjectInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        document.getElementById("btn-generate").click();
    }
});

// ===== [🔴] 도전: 「퀴즈 만드는 중…」 로딩 표시 =====
// async function generateQuiz(subject) {
//     const loadingEl = document.getElementById("loading");
//     loadingEl.classList.remove("hidden");
//     quizResultEl.textContent = "";
//     try {
//         const url = subject
//             ? `/api/generate-quiz?subject=${encodeURIComponent(subject)}`
//             : "/api/generate-quiz";
//         const res = await fetch(url);
//         const data = await res.json();
//         quizResultEl.textContent = data.quiz;
//     } finally {
//         loadingEl.classList.add("hidden");
//     }
// }
