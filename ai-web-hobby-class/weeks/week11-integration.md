# 11주차 — 통합: Python + 텍스트 AI + 이미지 AI + 웹

**Phase:** 마무리 | **소요:** 60~90분

---

## 🟢 목표 (전원)

`app.py` + `index.html` — **챗봇·퀴즈·OX·(선택)TM** 메뉴로 이동, UI 통일.

---

## JS 핵심 개념 — 오늘 쓰는 코드 훑어보기

3주차부터 매주 `script.js`를 써 왔지만, 11주차는 **한 파일 안에 JS 패턴이 다 모이는 주**입니다.
새 문법을 배우기보다, **이미 쓰고 있던 4가지**를 이름 붙여 정리합니다.

| 패턴 | 하는 일 | `script.js` 실제 코드 |
|------|---------|----------------------|
| **DOM 선택** | 화면(HTML) 태그를 JS 변수로 가져오기 | `document.getElementById("question-input")` |
| **이벤트 리스너** | "누르면·입력하면" 실행할 함수 연결 | `btn.addEventListener("click", () => { ... })` |
| **fetch + async/await** | Python(Flask)에게 데이터 요청·응답 받기 | `const res = await fetch("/api/chat", {...}); const data = await res.json();` |
| **클래스·속성으로 화면 전환** | 탭을 누를 때마다 보이기/숨기기 | `panel.classList.toggle("active", isActive); panel.hidden = !isActive;` |

```javascript
// 메뉴(탭) 전환 — 4가지 패턴이 한 번에 들어있는 예
document.querySelectorAll(".tab").forEach((tab) => {       // 1) DOM 선택 (여러 개)
    tab.addEventListener("click", () => {                  // 2) 이벤트 리스너
        document.querySelectorAll(".panel").forEach((panel) => {
            const isActive = panel.id === `panel-${tab.dataset.tab}`;
            panel.classList.toggle("active", isActive);    // 4) 클래스로 전환
            panel.hidden = !isActive;
        });
    });
});
```

> **왜 Python이 아니라 JS인가?** 탭 전환은 서버에 물어볼 필요 없는 "화면만의 일"이라 JS가 즉시 처리합니다.
> 반대로 AI 답변처럼 서버(Python)가 계산해야 하는 일은 `fetch`로 물어봅니다 — 이게 3주차부터 배운 패턴 그대로입니다.

---

## 🟡 JS 실습 — 「지우기」 버튼 직접 추가하기

**목표:** 챗봇 탭에 버튼 하나 + `addEventListener` 하나를 **직접** 작성해서, 입력창과 답변을 초기화합니다. Python은 건드리지 않습니다 — 화면만의 일이기 때문입니다.

1. `templates/index.html` — `#panel-chat` 안 `.btn-row`에 버튼 추가

   ```html
   <button type="button" id="btn-clear" class="btn btn-secondary">지우기</button>
   ```

2. `static/script.js` — 위 4가지 패턴 중 **DOM 선택 + 이벤트 리스너**를 그대로 써서 완성

   ```javascript
   // 힌트: questionInput.value 를 빈 문자열로, replyEl.textContent 를 원래 안내문으로
   const btnClear = document.getElementById("btn-clear");
   btnClear.addEventListener("click", () => {
       // 여기를 채워보세요 (fetch 필요 없음!)
   });
   ```

3. 확인: 질문을 입력하고 답을 받은 뒤 「지우기」 클릭 → 입력창·답변이 원래대로 돌아오면 성공!

> 🔴 도전: 같은 방식으로 퀴즈 탭에도 「지우기」를 추가해 보세요. `subjectInput.value` 를 기본값(`{{ default_subject }}`)으로 되돌리면 완성입니다.

---

## 통합 체크리스트 (교사용 starter)

- [ ] `/api/chat` — Python AI
- [ ] `/api/generate-quiz` — Python AI
- [ ] `/api/check` — Python OX
- [ ] TM 섹션 — JS 이미지 AI
- [ ] `APP_TITLE`, footer `made by {{ name }}`

---

## 🟢🟡🔴 과제

### 🟢
1. [ ] 제목·푸터
2. [ ] 4메뉴 스크린샷

### 🟡
3. [ ] 챗봇 탭에 「지우기」 버튼 직접 추가 (JS 실습 — 위 섹션 참고)
4. [ ] 다크모드 CSS

### 🔴
5. [ ] 퀴즈 탭에도 「지우기」 추가 (JS 실습 도전 참고)
6. [ ] Replit **Deploy** → URL 받기

---

## 다음 주 (Week12)

- Deploy URL로 발표
