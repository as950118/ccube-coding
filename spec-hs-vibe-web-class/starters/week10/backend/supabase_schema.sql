-- TODO 1: 내 미니앱에 맞는 테이블 이름·컬럼으로 바꾼 뒤, Supabase 대시보드 SQL Editor에서 실행
create table if not exists items (
  id bigint generated always as identity primary key,
  name text not null,
  message text not null,
  created_at timestamptz not null default now()
);

-- RLS는 켜두고 정책은 만들지 않는다: 프론트/anon 키로는 아무것도 못 하게 막고,
-- 백엔드(Render)의 SUPABASE_SERVICE_KEY만 (RLS를 우회해) 접근하게 한다.
alter table items enable row level security;
