// TODO 5: Render 배포 URL을 .env(VITE_API_URL)에 넣고, 여기서는 그 값만 읽어 쓴다
const API_URL = import.meta.env.VITE_API_URL;

const listEl = document.getElementById("list");
const formEl = document.getElementById("form");
const statusEl = document.getElementById("status");

function render(items) {
  // TODO 6: 내 데이터 모양에 맞게 화면에 그리기
  listEl.innerHTML = items
    .map((item) => `<li><strong>${escapeHtml(item.name)}</strong>${escapeHtml(item.message)}</li>`)
    .join("");
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

async function loadItems() {
  statusEl.textContent = "";
  try {
    const res = await fetch(`${API_URL}/api/items`);
    if (!res.ok) throw new Error(`API ${res.status}`);
    render(await res.json());
  } catch (err) {
    statusEl.textContent = `목록을 불러오지 못했습니다: ${err.message}`;
  }
}

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value.trim();
  const message = document.getElementById("message").value.trim();
  if (!name || !message) return;

  statusEl.textContent = "저장 중...";
  try {
    // TODO 7: 백엔드 POST /api/items 호출 (내 필드명에 맞게 body 수정)
    const res = await fetch(`${API_URL}/api/items`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, message }),
    });
    if (!res.ok) throw new Error(`API ${res.status}`);
    formEl.reset();
    statusEl.textContent = "";
    await loadItems();
  } catch (err) {
    statusEl.textContent = `저장에 실패했습니다: ${err.message}`;
  }
});

loadItems();
