# 모던 프레임워크 지도 (선택 참고)

이 문서는 **정규 커리큘럼(weeks/)의 필수 내용이 아니다.**  
[tech-stack.md](tech-stack.md)의 「선택」 영역을 조금 더 풀어 쓴 **교사용 참고 자료**로,
학생 수준·시간 여유에 따라 **선택적으로** 소개할 때 쓴다.

> 서버·클라이언트·API·DB·도메인·IP 등 **더 아래층의 웹 개념**은 [web-concepts-guide.md](web-concepts-guide.md)로 따로 뺐다.

---

## 왜 정규 수업안에 넣지 않았나

[source-curriculum-map.md](source-curriculum-map.md)의 설계 원칙(중학생 대상 · 56시간 · 「기능을 다 가르치기」가 아니라 「웹 결과물에 필요한 워크플로우만」)에 따라,
본 과정은 **Vite + vanilla JS**를 표준 스택으로 고정했다.  
React/Next.js 「풀코스」는 시간·난이도상 정규 진도에 넣지 않되, **관심 있는 학생**을 위한 지도만 여기 남긴다.

---

## 프레임워크 지도 (한눈에)

| 스택 | 무엇인가 | 본 과정에서의 위치 |
|------|----------|---------------------|
| HTML/CSS/JS (vanilla) | 브라우저가 바로 이해하는 기본 언어 | **Phase1 표준** (Week3~6) |
| Vite + vanilla JS | 빌드 도구로 감싼 vanilla JS | **Phase2 표준** (Week7~) |
| React | 컴포넌트·상태 중심 UI 라이브러리 | 🔴 심화 — 관심 학생만 (Week7+ 이후 자율) |
| Next.js | React + 라우팅·배포가 통합된 프레임워크 | 🔴 심화 이상 — 캡스톤(Week11~13) 희망 학생만 |
| Vue / Svelte | React의 대안 프레임워크 | 참고용 — 본 과정 표준 아님 |

---

## 핵심 개념 지도 (교사 5~15분 설명용)

학생이 물어볼 때, 실습 없이 **개념만** 짚어줄 수 있도록 정리했다.

| 개념 | 한 줄 설명 |
|------|-----------|
| 컴포넌트(Component) | 버튼·카드처럼 **재사용 가능한 UI 조각** |
| 상태(State) | 화면이 기억하고 있다가 바뀌면 다시 그리는 값 (예: 클릭 횟수) |
| Props | 컴포넌트에 **넘겨주는 값** (예: 카드 제목) |
| 번들러(Bundler) | 여러 파일을 묶고 최적화해주는 도구 — **Vite가 이미 이 역할** |
| SSR(서버 렌더링) | 페이지를 서버에서 미리 그려서 보내는 방식 (Next.js가 지원, 개념만) |

> Week7에서 이미 「번들러가 왜 필요한가」는 다뤘다 — React를 몰라도 이 개념 지도는 자연스럽게 이어진다.

---

## 언제 도입해도 되는가 (학급 판단 기준)

| 학생 상황 | 추천 |
|-----------|------|
| Phase1(HTML/CSS)도 아직 벅참 | 프레임워크 언급 자제 — vanilla로 충분히 다지기 |
| Phase2 Starter Kit까지 무리 없이 완료 | React 맛보기 15~30분 (🔴 선택, 아래 데모 참고) |
| 캡스톤(Week11~13)에서 SPA 형태를 원함 | React + Vite 허용. 단 `CLAUDE.md`에 **범위를 명시**해 과확장 방지 |
| 대회·수상 실적으로 이미 React 경험 있음 | 자율 진행 허용, 단 학급 표준 결과물(README·CLAUDE.md 등)은 동일하게 유지 |

---

## React 맛보기 (선택 · 15~30분 미니 데모)

```
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

가장 작은 예시(카운터 버튼)만 보여줘도 충분하다:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      클릭 {count}번
    </button>
  );
}

export default Counter;
```

**설명 포인트:** `useState`가 방금 배운 「상태」개념을 코드로 표현한 것뿐 — vanilla JS로 변수+DOM 업데이트를 손으로 하던 것을, React가 대신 관리해준다.

---

## Next.js 관련 안내

- 이 과정에서는 **필수 아님**. 배포는 이미 6주차에 GitHub Pages/Vercel(정적 사이트)로 다뤘다.
- Next.js의 라우팅·SSR·API Routes는 **캡스톤에서 정말 필요한 학생**에게만 개별 안내.
- 「Next + Shadcn 풀코스」학습은 수업 시간이 아니라 **자율 학습**으로 유도.

---

## 상태관리 라이브러리 (Redux 등)

본 과정 범위 밖이다. 「컴포넌트가 많아지고 상태를 여기저기서 공유해야 할 때 필요해지는 것」정도만 개념으로 언급하면 충분하다 — 중학생 단일 미니앱 규모에서는 `useState`만으로도 대부분 해결된다.

---

## 배포 플랫폼 참고 (Week6 GitHub Pages/Vercel 외)

| 플랫폼 | 비고 |
|--------|------|
| GitHub Pages | 수업 표준 ① — 정적 사이트 |
| Vercel | 수업 표준 ② — 정적 + Next.js 등 프레임워크 배포도 지원 |
| Netlify | 대안. Vercel과 유사한 흐름 |
| Cloudflare Pages | 대안. 속도 강점, 설정은 Vercel과 유사 |

> 학급 표준은 **GitHub Pages 또는 Vercel 하나**로 유지 — 여러 플랫폼을 동시에 가르치지 않는다.

---

## 본 커리큘럼과의 접점

| 시점 | 접점 |
|------|------|
| Week7 | Vite + vanilla로 「번들러」개념 이미 도입 — React 맛보기의 전제 지식 |
| Week9~10 | 미니앱 MVP에서 상태가 복잡해지면 React 옵션을 **학생이 원할 때만** 고려 |
| Week11~13 | 캡스톤 심화에서 React/Next 선택적 사용 가능 (원본 커리큘럼 S24~26 Supabase 이벤트앱 대응) |

---

## 하지 않는 것 (설계 원칙 재확인)

- TypeScript 전면 도입
- 테스트 프레임워크(Jest 등) 정규 도입
- CI/CD 파이프라인 구성
- 모노레포·마이크로프론트엔드 등 대규모 아키텍처

→ 필요하면 **캡스톤 이후, 개별 자율 학습**으로 안내한다. 정규 4시간 수업 안에는 넣지 않는다.
