// ===== 10주차: 웹캠 + Teachable Machine (브라우저 AI) =====
// 9주차: 사진 업로드 → model.predict()
// 이번 주: tmImage.Webcam 으로 카메라 켜기 → 같은 model.predict()!

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
let liveMode = false; // [🟡] 「지금 뭐야?」 켜져 있는 동안 true

// ===== [🟡] 클래스명 한글 매핑 (본인 모델 클래스에 맞게 수정) =====
const LABEL_KO = {
    // 예: Class 1: "펜", Class 2: "가위"
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
        const modelURL = MODEL_URL + "model.json";
        const metadataURL = MODEL_URL + "metadata.json";
        model = await tmImage.load(modelURL, metadataURL);
        statusEl.textContent = `모델 준비 완료! (클래스 ${model.getTotalClasses()}개)`;

        // ===== [🟡] 라벨명 자동 확인 — 주석 해제하면 콘솔(F12)에
        // 본인 모델의 실제 클래스명이 LABEL_KO 틀 형태로 출력됨.
        // metadata.json 직접 열어볼 필요 없이 그대로 복사해서 위 LABEL_KO 에 붙여넣고 값만 한글로 바꾸면 끝!
        // console.log("나의 LABEL_KO:\n" + JSON.stringify(
        //     Object.fromEntries(model.getClassLabels().map((name) => [name, name])),
        //     null, 4
        // ));

        await setupWebcam();
    } catch (err) {
        console.error(err);
        statusEl.textContent = "모델 로드 실패 — URL 끝의 / 와 공개 설정 확인";
    }
}

// ===== [🟢] 웹캠 켜기 — 실패하면 9주차 파일 업로드로 대체 =====
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
    webcam.update(); // 웹캠 화면 계속 갱신
    if (liveMode) {
        predictFrom(webcam.canvas);
    }
    window.requestAnimationFrame(webcamLoop);
}

// ===== [🟢] 분류 — 웹캠 프레임 또는 업로드된 이미지 공통 사용 =====
async function predictFrom(source) {
    if (!model) return;

    const prediction = await model.predict(source);
    prediction.sort((a, b) => b.probability - a.probability);
    const top = prediction[0];

    // [🔴] 도전: 아래 주석을 해제하면 모든 클래스 확률 % 표시
    const lines = prediction.map(
        (p) => `${labelText(p.className)}: ${(p.probability * 100).toFixed(1)}%`
    );
    resultEl.textContent = lines.join("\n");

    // [🟢] 기본: 1등만 표시
    // resultEl.textContent = `결과: ${labelText(top.className)}`;

    // [🔴] 확률 80% 이상일 때만 강조 (style.css 의 .result-high)
    resultEl.classList.toggle("result-high", top.probability >= 0.5);
}

// ===== [🟢] 「분류하기」 — 1회 분류 =====
btnPredict.addEventListener("click", async () => {
    if (!webcam || !model) return;
    statusEl.textContent = "분류 중…";
    await predictFrom(webcam.canvas);
    statusEl.textContent = "분류 완료!";
});

// ===== [🟡] 「지금 뭐야?」 — 누르면 계속 분류, 다시 누르면 정지 =====
btnLive.addEventListener("click", () => {
    liveMode = !liveMode;
    btnLive.textContent = liveMode ? "그만" : "지금 뭐야?";
    statusEl.textContent = liveMode ? "실시간 분류 중…" : "정지됨";
});

// ===== 파일 업로드 대체 모드 (카메라 없을 때) — 9주차와 동일 =====
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
