# 왜 층을 나눴는가 (예시)

DB 종류가 바뀌거나(SQLite → 다른 DB) 화면이 바뀌어도(HTML → React), 나머지 코드를 다시 쓰지 않으려고 나눴다. `PostRepository`라는 약속만 지키면 어떤 저장 방식이든, 어떤 화면이든 갈아 끼울 수 있다.

# 오늘 막혔던 점 (예시)

`SqlitePostRepository`에서 `update` 메서드 이름을 실수로 `edit`로 지었더니 `Can't instantiate abstract class` 에러가 났다 — 추상 메서드 이름과 정확히 일치해야 한다는 걸 알게 됐다.

# 다음에 하고 싶은 것

- Repository를 하나 더 만들어서(예: JSON 파일 저장) 진짜로 몇 개까지 갈아 끼울 수 있는지 해보고 싶다
