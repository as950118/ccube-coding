// ===== 13주차 starter — Flask + SQLite 스마트홈 대시보드 =====
// fetch('/api/status') 로 서버 상태를 받고, 버튼은 POST API로 보냅니다.

const elements = {
    body: document.body,
    currentTime: document.getElementById("current-time"),
    darkModeButton: document.getElementById("dark-mode-button"),
    allOnButton: document.getElementById("all-on-button"),
    allOffButton: document.getElementById("all-off-button"),
    livingRoom: document.getElementById("living-room"),
    entranceRoom: document.getElementById("entrance-room"),

    lampButton: document.getElementById("lamp-button"),
    airconButton: document.getElementById("aircon-button"),
    fanButton: document.getElementById("fan-button"),
    waterButton: document.getElementById("water-button"),

    lampDevice: document.getElementById("lamp-device"),
    airconDevice: document.getElementById("aircon-device"),
    fanDevice: document.getElementById("fan-device"),
    doorPanel: document.getElementById("door-panel"),
    doorDevice: document.getElementById("door-device"),
    doorNote: document.getElementById("door-note"),

    temperatureCard: document.getElementById("temperature-card"),
    humidityCard: document.getElementById("humidity-card"),
    lightCard: document.getElementById("light-card"),
    plantDevice: document.getElementById("plant-device"),

    temperatureValue: document.getElementById("temperature-value"),
    temperatureStatus: document.getElementById("temperature-status"),
    humidityValue: document.getElementById("humidity-value"),
    humidityStatus: document.getElementById("humidity-status"),
    lightValue: document.getElementById("light-value"),
    lightStatus: document.getElementById("light-status"),
    soilValue: document.getElementById("soil-value"),
    soilFill: document.getElementById("soil-fill"),
    plantStatus: document.getElementById("plant-status"),
    plantNote: document.getElementById("plant-note"),
    plantIcon: document.getElementById("plant-icon"),

    lampSummary: document.getElementById("lamp-summary"),
    airconSummary: document.getElementById("aircon-summary"),
    fanSummary: document.getElementById("fan-summary"),
    doorSummary: document.getElementById("door-summary"),
    eventList: document.getElementById("event-list"),
};

let isDarkMode = false;

function updateClock() {
    const now = new Date();
    elements.currentTime.textContent = now.toLocaleTimeString("ko-KR", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
    });
}

function applyStatusChip(element, label, tone) {
    element.textContent = label;
    element.className = "mini-status " + tone;
}

function setDangerStyle(element, shouldHighlight) {
    element.classList.toggle("is-danger", shouldHighlight);
}

function getTemperatureState(temperature) {
    if (temperature >= 29) {
        return { label: "위험", tone: "danger" };
    }
    if (temperature <= 20) {
        return { label: "서늘함", tone: "warn" };
    }
    return { label: "정상", tone: "good" };
}

function getHumidityState(humidity) {
    if (humidity <= 35) {
        return { label: "건조", tone: "warn" };
    }
    if (humidity >= 70) {
        return { label: "높음", tone: "warn" };
    }
    return { label: "보통", tone: "good" };
}

function getLightState(lightLevel) {
    if (lightLevel < 34) {
        return { label: "어두움", tone: "warn" };
    }
    if (lightLevel < 68) {
        return { label: "보통", tone: "info" };
    }
    return { label: "밝음", tone: "good" };
}

function getPlantState(soilMoisture) {
    if (soilMoisture <= 20) {
        return {
            label: "물을 주세요",
            tone: "danger",
            note: "토양이 많이 말랐습니다. 물 주기 버튼을 눌러 주세요.",
            icon: "🥀",
            fill: "linear-gradient(90deg, #ef4444, #f97316)",
        };
    }
    if (soilMoisture <= 50) {
        return {
            label: "조금 건조",
            tone: "warn",
            note: "완전히 위험하진 않지만 조금 더 촉촉하면 좋습니다.",
            icon: "🌿",
            fill: "linear-gradient(90deg, #f59e0b, #facc15)",
        };
    }
    return {
        label: "건강",
        tone: "good",
        note: "토양 수분이 충분해서 식물이 건강합니다.",
        icon: "🪴",
        fill: "linear-gradient(90deg, #22c55e, #0ea5e9)",
    };
}

function setDeviceButton(buttonElement, isOn) {
    buttonElement.textContent = isOn ? "ON" : "OFF";
    buttonElement.classList.toggle("on", isOn);
    buttonElement.classList.toggle("off", !isOn);
}

function renderEvents(events) {
    elements.eventList.innerHTML = "";
    events.forEach((eventItem) => {
        const item = document.createElement("li");
        item.className = "event-item";
        item.innerHTML = `
            <span class="event-dot" aria-hidden="true"></span>
            <div>
                <strong>${eventItem.message}</strong>
                <span class="event-time">${eventItem.time}</span>
            </div>
        `;
        elements.eventList.appendChild(item);
    });
}

function renderDashboard(data) {
    const temperatureState = getTemperatureState(data.temperature);
    const humidityState = getHumidityState(data.humidity);
    const lightState = getLightState(data.light_level);
    const plantState = getPlantState(data.soil_moisture);

    elements.temperatureValue.textContent = data.temperature.toFixed(1) + "°C";
    applyStatusChip(elements.temperatureStatus, temperatureState.label, temperatureState.tone);
    setDangerStyle(elements.temperatureCard, temperatureState.tone === "danger");

    elements.humidityValue.textContent = data.humidity + "%";
    applyStatusChip(elements.humidityStatus, humidityState.label, humidityState.tone);
    setDangerStyle(elements.humidityCard, data.humidity <= 35);

    elements.lightValue.textContent = lightState.label;
    applyStatusChip(elements.lightStatus, lightState.label, lightState.tone);

    elements.soilValue.textContent = data.soil_moisture + "%";
    applyStatusChip(elements.plantStatus, plantState.label, plantState.tone);
    elements.plantNote.textContent = plantState.note;
    elements.plantIcon.textContent = plantState.icon;
    elements.soilFill.style.width = data.soil_moisture + "%";
    elements.soilFill.style.background = plantState.fill;
    setDangerStyle(elements.plantDevice, data.soil_moisture <= 20);

    const lampOn = data.devices.lamp;
    const airconOn = data.devices.aircon;
    const fanOn = data.devices.fan;

    setDeviceButton(elements.lampButton, lampOn);
    setDeviceButton(elements.airconButton, airconOn);
    setDeviceButton(elements.fanButton, fanOn);

    elements.lampDevice.classList.toggle("is-on", lampOn);
    elements.airconDevice.classList.toggle("is-on", airconOn);
    elements.fanDevice.classList.toggle("is-on", fanOn);
    elements.livingRoom.classList.toggle("is-lit", lampOn);
    elements.livingRoom.classList.toggle("is-cooling", airconOn);
    elements.livingRoom.classList.toggle("is-breezy", fanOn);

    elements.lampSummary.textContent = lampOn ? "ON" : "OFF";
    elements.airconSummary.textContent = airconOn ? "ON" : "OFF";
    elements.fanSummary.textContent = fanOn ? "ON" : "OFF";

    elements.doorPanel.textContent = data.door_open ? "열림" : "닫힘";
    elements.doorPanel.classList.toggle("on", data.door_open);
    elements.doorPanel.classList.toggle("off", !data.door_open);
    elements.doorDevice.classList.toggle("is-open", data.door_open);
    elements.doorSummary.textContent = data.door_open ? "열림" : "닫힘";
    elements.doorNote.textContent = data.door_open
        ? "현관문이 열려 있습니다. 출입 상태를 확인해 보세요."
        : "현관문이 닫혀 있습니다.";
    setDangerStyle(elements.entranceRoom, data.door_open);

    renderEvents(data.events || []);
}

// ===== 요청이 끝날 때까지(성공/실패 모두) 버튼을 잠가 중복 클릭 방지 =====
function withButtonLock(buttonElement, handler) {
    return async (...args) => {
        if (buttonElement.disabled) return;
        buttonElement.disabled = true;
        try {
            await handler(...args);
        } catch (err) {
            console.error(err);
        } finally {
            buttonElement.disabled = false;
        }
    };
}

async function fetchJson(url, options = {}) {
    const response = await fetch(url, options);
    if (!response.ok) {
        throw new Error("Request failed: " + response.status);
    }
    return response.json();
}

async function fetchStatus() {
    const data = await fetchJson("/api/status");
    renderDashboard(data);
}

async function toggleDevice(deviceName) {
    const data = await fetchJson("/api/device/toggle", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ device: deviceName }),
    });
    renderDashboard(data);
}

async function setAllDevices(value) {
    const data = await fetchJson("/api/device/all", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    renderDashboard(data);
}

async function waterPlant() {
    const data = await fetchJson("/api/plant/water", {
        method: "POST",
    });
    renderDashboard(data);
}

function toggleDarkMode() {
    isDarkMode = !isDarkMode;
    elements.body.classList.toggle("dark-mode", isDarkMode);
    elements.darkModeButton.textContent = isDarkMode ? "☀️ 라이트모드" : "🌙 다크모드";
}

elements.darkModeButton.addEventListener("click", toggleDarkMode);
elements.allOnButton.addEventListener("click", withButtonLock(elements.allOnButton, () => setAllDevices(true)));
elements.allOffButton.addEventListener("click", withButtonLock(elements.allOffButton, () => setAllDevices(false)));
elements.lampButton.addEventListener("click", withButtonLock(elements.lampButton, () => toggleDevice("lamp")));
elements.airconButton.addEventListener("click", withButtonLock(elements.airconButton, () => toggleDevice("aircon")));
elements.fanButton.addEventListener("click", withButtonLock(elements.fanButton, () => toggleDevice("fan")));
elements.waterButton.addEventListener("click", withButtonLock(elements.waterButton, waterPlant));

updateClock();
fetchStatus();

window.setInterval(updateClock, 1000);
window.setInterval(fetchStatus, 1000);
