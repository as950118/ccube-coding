const API_URL = import.meta.env.VITE_API_URL;

const listEl = document.getElementById("list");
const formEl = document.getElementById("form");
const statusEl = document.getElementById("status");

function render(items) {
  listEl.innerHTML = items
    .map(
      (item) => `<li><strong>${escapeHtml(item.name)}</strong>${escapeHtml(item.message)}</li>`
    )
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
