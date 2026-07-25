const MODEL_URL = window.TM_MODEL_URL || "";
const statusEl = document.getElementById("status");
const previewEl = document.getElementById("preview");
const resultEl = document.getElementById("result");
const btnPredict = document.getElementById("btn-predict");
const imageInput = document.getElementById("image-input");

let model = null;

// 본인 TM 클래스명에 맞게 수정
const LABEL_KO = {
    "Class 1": "클래스 1",
    "Class 2": "클래스 2",
};

function labelText(name) {
    return LABEL_KO[name] || name;
}

async function loadModel() {
    if (!MODEL_URL || MODEL_URL.includes("YOUR_MODEL_ID")) {
        statusEl.textContent = "⚠️ app.py 의 MODEL_URL 을 본인 TM 모델 주소로 바꿔 주세요.";
        return;
    }

    try {
        statusEl.textContent = "모델 불러오는 중…";
        model = await tmImage.load(MODEL_URL + "model.json", MODEL_URL + "metadata.json");
        statusEl.textContent = `모델 준비 완료! (클래스 ${model.getTotalClasses()}개)`;
    } catch (err) {
        console.error(err);
        statusEl.textContent = "모델 로드 실패 — URL 끝의 / 와 공개 설정 확인";
    }
}

imageInput.addEventListener("change", () => {
    const file = imageInput.files && imageInput.files[0];
    if (!file) return;
    previewEl.src = URL.createObjectURL(file);
    previewEl.classList.remove("hidden");
    btnPredict.disabled = !model;
});

btnPredict.addEventListener("click", async () => {
    if (!model) return;
    statusEl.textContent = "분류 중…";
    const prediction = await model.predict(previewEl);
    prediction.sort((a, b) => b.probability - a.probability);
    const lines = prediction.map(
        (p) => `${labelText(p.className)}: ${(p.probability * 100).toFixed(1)}%`
    );
    resultEl.textContent = lines.join("\n");
    statusEl.textContent = "분류 완료!";
});

loadModel();
