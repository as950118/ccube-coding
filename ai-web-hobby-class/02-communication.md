# 채팅·이메일 운영 가이드

## 1. 채널 역할

| 채널 | 대상 | 용도 | 톤 |
|------|------|------|-----|
| **카카오톡 / 밴드** | 학부모 | 수업 전·후 짧은 안내 | 3~5줄 |
| **디스코드 / 클래스룸** | 학생 | starter, #질문, #자랑 | 친근·짧게 |
| **이메일** | 학부모 (+학생) | 주 1회 Weekly Letter | 1페이지 |

> **채팅 = 지금 확인**, **이메일 = 나중에 다시 읽기**  
> 같은 내용을 두 번 길게 쓰지 않기

---

## 2. 디스코드 채널 구성 (예시)

| 채널 | 용도 |
|------|------|
| `#공지` | starter 링크, 이번 주 🟢 목표 (읽기 전용) |
| `#질문` | 에러 스크린샷, 「이 줄이 뭐예요?」 |
| `#자랑` | 과제·꾸민 화면 (선택) |

**규칙 (1주차 공지):**
- 채팅은 **안내·질문**용
- 과제 **대신 해주기**는 안 됨
- 밤 10시 이후 답변 안 해도 됨 (교사)

---

## 3. 발송 타이밍 (수업이 수요일인 경우)

| 시점 | 채널 | 내용 |
|------|------|------|
| **화요일 저녁** | 카톡 | 내일 수업 + starter 링크 |
| **수요일 수업 직후** | 카톡 + 디스코드 | 오늘 요약 + 선택 과제 🟢 |
| **목요일 (선택)** | 디스코드 | 「🟢 해본 사람 🙋」 |
| **일요일 18:00** | 이메일 | Weekly Letter (예약 발송 권장) |

**이메일은 주 1회** — 매일 보내지 않기

---

## 4. 메시지 3종 로테이션

교사 부담을 줄이려면 **템플릿 3종**만 주차·링크·🟢 2줄만 바꿉니다.

| 종류 | 파일 |
|------|------|
| 수업 전 | [messages/chat-before-class-template.md](messages/chat-before-class-template.md) |
| 수업 후 | [messages/chat-after-class-template.md](messages/chat-after-class-template.md) |
| 부드러운 리마인드 | [messages/chat-reminder-template.md](messages/chat-reminder-template.md) |
| 주간 이메일 | [messages/email-weekly-letter-template.md](messages/email-weekly-letter-template.md) |
| 1주차 orientation | [messages/email-week0-orientation.md](messages/email-week0-orientation.md) |

---

## 5. 매 메시지에 넣을 한 줄

다음 수업 전 카톡·수업 후 카톡·Weekly Letter **모두**에 아래 중 하나 포함:

> ❗ 과제 안 해도 다음 수업 starter로 같이 시작해요!

잊지 않게 **매주 1번** 반복합니다.

---

## 6. FAQ 고정 답변 (핀/공지)

| 질문 | 답변 |
|------|------|
| 과제 필수인가요? | 선택입니다. starter 매주 드립니다. |
| 집 PC 없어요 | 수업에서 🟢까지 완료합니다. |
| 에러가 나요 | #질문에 스크린샷 — 안 해도 다음 주 OK |
| API 키는? | 수업용은 선생님이 관리합니다 |

전체: [appendix/faq.md](appendix/faq.md)

---

## 7. 피해야 할 표현

- 「과제 안 낸 학생 ~」 (공개 압박)
- 「다음 주 못 따라옵니다」
- 「Level 3까지 필수」

---

## 8. Google Drive 링크 운영

```
AI웹반/
├── Week01/starter.zip
├── Week02/starter.zip
...
└── FAQ.pdf
```

- **항상 같은 폴더 구조** → 메시지는 링크만 교체
- starter 파일명 규칙: `week05-starter.zip` (통일)
