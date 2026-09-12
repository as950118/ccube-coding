create table if not exists guestbook (
  id bigint generated always as identity primary key,
  name text not null,
  message text not null,
  created_at timestamptz not null default now()
);

-- RLS 켜두고 정책은 만들지 않는다: anon/authenticated 키로는 아무것도 못 하게 막고,
-- 백엔드(Render)의 SERVICE_KEY만 (RLS를 우회해) 접근하게 한다.
-- 이게 3단 분리("DB는 백엔드만 직접 만진다")의 핵심 포인트.
alter table guestbook enable row level security;
