// ===== 11주차: 메뉴 전환 + 챗봇·퀴즈·OX(텍스트 AI) + 이미지 AI(TM) 통합 =====

// ---------- 메뉴(탭) 전환 ----------
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

// ---------- 메뉴 1: AI 챗봇 (5주차) ----------
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

// ---------- 메뉴 2: AI 퀴즈 (6주차) ----------
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

// ---------- 메뉴 3: OX 퀴즈 (4주차) ----------
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

// ---------- 메뉴 4: 이미지 AI — 웹캠 + Teachable Machine (9~10주차) ----------
const MODEL_URL = window.TM_MODEL_URL || "";

const statusEl = document.getElementById("status");
const resultEl = document.getElementById("result");
const webcamModeEl = document.getElementById("webcam-mode");
const webcamContainerEl = document.getElementById("webcam-container");
const btnPredict = document.getElementById("btn-predict");
const btnLive = document.getElementById("btn-live");

// 카메라 거부/미지원 시 대체 — 9주차 파일 업로드
const uploadModeEl = document.getElementById("upload-mode");
const imageInput = document.getElementById("image-input");
const previewEl = document.getElementById("preview");
const btnPredictUpload = document.getElementById("btn-predict-upload");

let model = null;
let webcam = null;
let liveMode = false; // 「지금 뭐야?」 켜져 있는 동안 true

// 본인 TM 클래스명에 맞게 수정
const LABEL_KO = {
    // "Class 1": "펜",
    // "Class 2": "가위",
};

function labelText(name) {
    return LABEL_KO[name] || name;
}

async function loadModel() {
    if (!MODEL_URL || MODEL_URL.includes("YOUR_MODEL_ID")) {
        statusEl.textContent = "⚠️ app.py 의 MODEL_URL 을 본인 TM 모델 주소로 바꿔 주세요.";
        resultEl.textContent = "Teachable Machine에서 모델 학습 → Share → 링크 복사 → MODEL_URL";
        return;
    }

    try {
        statusEl.textContent = "모델 불러오는 중…";
        model = await tmImage.load(MODEL_URL + "model.json", MODEL_URL + "metadata.json");
        statusEl.textContent = `모델 준비 완료! (클래스 ${model.getTotalClasses()}개)`;
        await setupWebcam();
    } catch (err) {
        console.error(err);
        statusEl.textContent = "모델 로드 실패 — URL 끝의 / 와 공개 설정 확인";
    }
}

async function setupWebcam() {
    try {
        const flip = true; // 거울 모드
        webcam = new tmImage.Webcam(300, 300, flip);
        await webcam.setup(); // 카메라 권한 요청
        await webcam.play();
        webcamContainerEl.appendChild(webcam.canvas);

        btnPredict.disabled = false;
        btnLive.disabled = false;
        statusEl.textContent = "웹캠 준비 완료! 「분류하기」를 눌러 보세요.";

        window.requestAnimationFrame(webcamLoop);
    } catch (err) {
        console.error(err);
        // 카메라 거부 / 카메라 없음 → 파일 업로드 모드로 전환
        webcamModeEl.classList.add("hidden");
        uploadModeEl.classList.remove("hidden");
        statusEl.textContent = "";
    }
}

function webcamLoop() {
    webcam.update();
    if (liveMode) {
        predictFrom(webcam.canvas);
    }
    window.requestAnimationFrame(webcamLoop);
}

async function predictFrom(source) {
    if (!model) return;

    const prediction = await model.predict(source);
    prediction.sort((a, b) => b.probability - a.probability);
    const top = prediction[0];

    resultEl.textContent = `결과: ${labelText(top.className)}`;
}

btnPredict.addEventListener("click", async () => {
    if (!webcam || !model) return;
    statusEl.textContent = "분류 중…";
    await predictFrom(webcam.canvas);
    statusEl.textContent = "분류 완료!";
});

btnLive.addEventListener("click", () => {
    liveMode = !liveMode;
    btnLive.textContent = liveMode ? "그만" : "지금 뭐야?";
    statusEl.textContent = liveMode ? "실시간 분류 중…" : "정지됨";
});

// 파일 업로드 대체 모드 (카메라 없을 때) — 9주차와 동일
imageInput.addEventListener("change", () => {
    const file = imageInput.files && imageInput.files[0];
    if (!file) return;

    previewEl.src = URL.createObjectURL(file);
    previewEl.classList.remove("hidden");
    btnPredictUpload.disabled = !model;
    resultEl.textContent = "「분류하기」를 눌러 보세요!";
});

btnPredictUpload.addEventListener("click", async () => {
    if (!model || btnPredictUpload.disabled) {
        resultEl.textContent = "모델이 아직 없어요. MODEL_URL 을 확인하세요.";
        return;
    }

    btnPredictUpload.disabled = true;
    try {
        await predictFrom(previewEl);
    } catch (err) {
        console.error(err);
        resultEl.textContent = "오류가 났어요. 다시 시도해 주세요.";
    } finally {
        btnPredictUpload.disabled = false;
    }
});

loadModel();
