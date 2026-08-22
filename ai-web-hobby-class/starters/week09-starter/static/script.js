// ===== 9주차: Teachable Machine 이미지 분류 (브라우저 AI) =====
// 5~8주: fetch → Python call_ai()
// 이번 주: tmImage.load() → model.predict() — Python 안 거침!

const MODEL_URL = window.TM_MODEL_URL || "";
const statusEl = document.getElementById("status");
const previewEl = document.getElementById("preview");
const resultEl = document.getElementById("result");
const btnPredict = document.getElementById("btn-predict");
const imageInput = document.getElementById("image-input");

let model = null;
let maxPredictions = 0;

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
        maxPredictions = model.getTotalClasses();
        statusEl.textContent = `모델 준비 완료! (클래스 ${maxPredictions}개)`;

        // ===== [🟡] 라벨명 자동 확인 — 주석 해제하면 콘솔(F12)에
        // 본인 모델의 실제 클래스명이 LABEL_KO 틀 형태로 출력됨.
        // metadata.json 직접 열어볼 필요 없이 그대로 복사해서 위 LABEL_KO 에 붙여넣고 값만 한글로 바꾸면 끝!
        // console.log("나의 LABEL_KO:\n" + JSON.stringify(
        //     Object.fromEntries(model.getClassLabels().map((name) => [name, name])),
        //     null, 4
        // ));
    } catch (err) {
        console.error(err);
        statusEl.textContent = "모델 로드 실패 — URL 끝의 / 와 공개 설정 확인";
    }
}

imageInput.addEventListener("change", () => {
    const file = imageInput.files && imageInput.files[0];
    if (!file) return;

    const url = URL.createObjectURL(file);
    previewEl.src = url;
    previewEl.classList.remove("hidden");
    btnPredict.disabled = !model;
    resultEl.textContent = "「분류하기」를 눌러 보세요!";
});

// ===== [🟢] 분류하기 =====
btnPredict.addEventListener("click", async () => {
    if (!model || btnPredict.disabled) {
        resultEl.textContent = "모델이 아직 없어요. MODEL_URL 을 확인하세요.";
        return;
    }

    // ===== [🟢] 분류 중에는 버튼을 잠가서 중복 클릭 방지 =====
    btnPredict.disabled = true;
    statusEl.textContent = "분류 중…";

    try {
        const prediction = await model.predict(previewEl);

        // 확률이 높은 순
        prediction.sort((a, b) => b.probability - a.probability);
        const top = prediction[0];

        // [🔴] 도전: 아래 주석을 해제하면 모든 클래스 확률 % 표시
        const lines = prediction.map(
            (p) => `${labelText(p.className)}: ${(p.probability * 100).toFixed(1)}%`
        );
        resultEl.textContent = lines.join("\n");

        // [🟢] 기본: 1등만 표시
        // resultEl.textContent = `결과: ${labelText(top.className)}`;
        statusEl.textContent = "분류 완료!";
    } catch (err) {
        console.error(err);
        statusEl.textContent = "분류 실패";
        resultEl.textContent = "오류가 났어요. 다시 시도해 주세요.";
    } finally {
        // 성공/실패 상관없이 완료되면 다시 클릭 가능하게
        btnPredict.disabled = false;
    }
});

loadModel().then(() => {
    if (model && previewEl.getAttribute("src")) {
        btnPredict.disabled = false;
    }
});
