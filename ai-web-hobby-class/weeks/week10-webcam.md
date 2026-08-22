# 10주차 — 웹캠 + TM (Flask 앱 안에서)

**Phase:** 이미지 AI | **소요:** 60~90min

---

## 🟢 목표 (전원)

같은 Flask 앱 — **웹캠** 켜고 TM 분류 결과 표시.

---

## JS 핵심 개념 — 오늘 쓰는 코드 훑어보기

9주차 파일 업로드 분류가 이번 주엔 **웹캠 실시간 분류**로 업그레이드됩니다. 새로 등장하는 JS 개념 3가지를 정리합니다.

| 패턴 | 하는 일 | `script.js` 실제 코드 |
|------|---------|----------------------|
| **비동기 함수 (`async`/`await`)** | 시간이 걸리는 작업(모델 예측)이 끝날 때까지 기다림 | `const prediction = await model.predict(source);` |
| **배열 정렬 (`.sort()`)** | 확률 높은 순으로 결과 줄 세우기 | `prediction.sort((a, b) => b.probability - a.probability);` |
| **애니메이션 루프 (`requestAnimationFrame`)** | 웹캠 화면을 초당 수십 번 계속 갱신 | `window.requestAnimationFrame(webcamLoop);` |

```javascript
// 웹캠 화면 갱신 루프 — 이 함수가 자기 자신을 계속 다시 부릅니다
function webcamLoop() {
    webcam.update();               // 웹캠 화면 최신 프레임으로
    if (liveMode) {                 // liveMode 가 true 인 동안만
        predictFrom(webcam.canvas); // 계속 분류
    }
    window.requestAnimationFrame(webcamLoop); // 다음 프레임에도 또 실행
}
```

> **`liveMode` 는 그냥 `true`/`false` 변수입니다.** 「지금 뭐야?」 버튼을 누르면 `liveMode = !liveMode`로 뒤집힐 뿐인데,
> 그 값 하나로 "1회만 분류"와 "계속 분류"가 갈립니다 — 버튼 하나, 변수 하나로 동작이 완전히 바뀌는 좋은 예입니다.

---

## 🟡 JS 실습 — 「초기화」 버튼 직접 추가하기

**목표:** 버튼 하나 + `addEventListener` 하나를 **직접** 작성해서, 실시간 분류를 끄고 결과를 원래대로 되돌립니다.

1. `templates/index.html` — `#webcam-mode` 안 `.btn-row`에 버튼 추가

   ```html
   <button type="button" id="btn-reset" class="btn btn-secondary">초기화</button>
   ```

2. `static/script.js` — 아래를 채워 완성 (모두 이미 쓰고 있는 변수들입니다)

   ```javascript
   // 힌트: liveMode 를 false로, btnLive 글자를 "지금 뭐야?"로, resultEl 을 안내문으로
   const btnReset = document.getElementById("btn-reset");
   btnReset.addEventListener("click", () => {
       // 여기를 채워보세요 — fetch 필요 없음, 위 JS 핵심 개념의 liveMode 변수를 그대로 씁니다
   });
   ```

3. 확인: 「지금 뭐야?」로 실시간 분류 중 「초기화」 클릭 → 분류가 멈추고 결과가 원래 문구로 돌아오면 성공!

> 🔴 도전: 업로드 모드(`#upload-mode`)에도 같은 「초기화」를 추가해 `preview` 이미지와 `image-input` 값을 지워보세요.

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] 웹캠 + 분류 1회
2. [ ] 결과 라벨 CSS

### 🟡
3. [ ] 「지금 뭐야?」 UI
4. [ ] 「초기화」 버튼 직접 추가 (JS 실습 — 위 섹션 참고)

### 🔴
5. [ ] 80% 이상일 때만 강조
6. [ ] 업로드 모드에도 「초기화」 추가 (JS 실습 도전 참고)

---

## 교사 메모

- 카메라 거부 → 9주 **파일 업로드**로 🟢
- Replit HTTPS OK

---

## 다음 주 (Week11)

- Python AI + TM + OX **전 통합**
