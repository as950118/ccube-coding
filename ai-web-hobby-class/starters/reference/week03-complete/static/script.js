async function calculateAdd() {
    const a = document.getElementById("num-a").value;
    const b = document.getElementById("num-b").value;

    const res = await fetch(`/api/add?a=${a}&b=${b}`);
    const data = await res.json();
    showResult(`${a} + ${b} = ${data.sum}`, data.error);
}

async function calculateSub() {
    const a = document.getElementById("num-a").value;
    const b = document.getElementById("num-b").value;

    const res = await fetch(`/api/sub?a=${a}&b=${b}`);
    const data = await res.json();
    showResult(`${a} - ${b} = ${data.diff}`, data.error);
}

function showResult(text, error) {
    const resultEl = document.getElementById("result");
    resultEl.textContent = error || text;
    resultEl.classList.toggle("error", Boolean(error));
}

document.getElementById("btn-add").addEventListener("click", calculateAdd);
document.getElementById("btn-sub").addEventListener("click", calculateSub);
