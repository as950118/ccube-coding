# 기술 스택 가이드

## 1. 개발 환경 (택 1)

| 도구 | 장점 | 단점 |
|------|------|------|
| **Replit** | 브라우저만, Secrets, 호스팅 | 무료 한도 |
| **CodePen** | HTML/CSS/JS 빠른 실습 | API는 프록시 필요 |
| **VS Code + Live Server** | 로컬 익숙해짐 | 설치 필요 |

**취미반 추천:** Replit (팀/교사 계정으로 템플릿 Fork)

---

## 2. AI API

| 서비스 | 용도 | 비고 |
|--------|------|------|
| OpenAI API | 챗봇, 퀴즈 생성 | GPT-4o-mini 등 저렴한 모델 |
| Google Gemini API | 동일 | 무료 티어 확인 |

### 보안
- API 키 → **Replit Secrets** 또는 **선생님 프록시**
- 학생 코드에 `sk-...` **직접 넣지 않기**

### 프록시 예시 (개념)
```
학생 fetch → /api/chat (선생님 서버) → OpenAI
```

---

## 3. 이미지 AI

| 도구 | 용도 |
|------|------|
| **Google Teachable Machine** | 2~5클래스 이미지 분류, URL export |
| TM JavaScript API | `tmImage.load()` + classify |

9~10주차 전용. 별도 API 키 불필요 (모델 URL만).

---

## 4. 호스팅 (11~12주)

| 서비스 | 용도 |
|--------|------|
| GitHub Pages | 정적 HTML 무료 호스팅 |
| Netlify / Vercel | drag & drop 배포 |
| Replit Deploy | 이미 Replit 사용 시 |

발표회 URL 공유용 — **필수 아님**, Replit 링크만으로도 OK

---

## 5. 피하는 것 (중학교 취미반)

- Python Flask/Django 풀스택
- Node 서버 직접 운영 (학생)
- SMS / Email 발송 API (스팸·비용·키)
- 딥러닝 프레임워크 (PyTorch 등)

**대안:** `mailto:` 링크로 「결과 보내기」 (11주 🔴)

---

## 6. 브라우저·권한

- Chrome 최신 권장
- 웹캠: **HTTPS** 또는 localhost (Replit OK)
- 카메라 거부 → 파일 업로드 대체

---

## 7. starter zip 규칙

```
week{N}-starter/
├── index.html
├── style.css
├── script.js      ← 🟢🟡🔴 주석
└── README.txt     ← 「🟢만 해도 OK」 3줄
```

- Week N starter = Week 1~(N-1) 기능 **포함**
- 파일명: `week05-starter.zip` 통일
