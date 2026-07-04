// ===== 3주차: fetch 로 Python API 와 대화 =====
// 포켓몬 배틀: fetch('/attack?skill=...') → 이번 주: fetch('/api/add?a=...&b=...')

// ===== [🟢] 더하기 — fetch → Python add() → 화면 표시 =====
async function calculateAdd() {
    const a = document.getElementById("num-a").value;
    const b = document.getElementById("num-b").value;

    const res = await fetch(`/api/add?a=${a}&b=${b}`);
    const data = await res.json();

    const resultEl = document.getElementById("result");
    resultEl.textContent = `${a} + ${b} = ${data.sum}`;

    // ===== [🔴] 도전: data.error 가 있으면 메시지 표시 =====
    // if (data.error) {
    //     resultEl.textContent = data.error;
    //     resultEl.classList.add("error");
    //     return;
    // }
}

document.getElementById("btn-add").addEventListener("click", calculateAdd);

// ===== [🟡] 도전: 빼기 — subtract API 완성 후 주석 해제 =====
async function calculateSub() {
    const a = document.getElementById("num-a").value;
    const b = document.getElementById("num-b").value;
    const res = await fetch(`/api/sub?a=${a}&b=${b}`);
    const data = await res.json();
    document.getElementById("result-sub").textContent = `${a} - ${b} = ${data.diff}`;
}
document.getElementById("btn-sub").addEventListener("click", calculateSub);
