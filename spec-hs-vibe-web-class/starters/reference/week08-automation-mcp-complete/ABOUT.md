# 자동화 입문 · 커맨드 · 서브에이전트 · MCP (교사 참고 · 완성 예시, 보관됨)

> ⚠️ **보관됨(displaced):** 8주차는 이제 [../week08-complete/](../week08-complete/)(공공데이터 API · 대시보드)입니다. 이 폴더는 참고용으로만 보관합니다.

**수업안:** [../../../weeks/_displaced/week08-automation-mcp.md](../../../weeks/_displaced/week08-automation-mcp.md)

학생용 starter는 [../../_displaced/week08-automation-mcp/](../../_displaced/week08-automation-mcp/) 입니다.  
이 폴더는 **조교·교사 참고용**이며, 수업 중 학생에게 통째로 배포하지 않습니다.

## 이 예시에 대해

[week07-complete](../week07-complete/)의 Starter Kit에 이어서, `.claude/commands/commit.md`
커스텀 커맨드와 CLAUDE.md 보강, `notes/automation-log.md` 기록 예시를 추가했습니다.
실제 MCP 서버 연결(Context7 등)은 로컬 도구 설정이 필요해 텍스트로만 안내합니다.

## 파일

```
week08-complete/
├── ABOUT.md
├── .claude/
│   └── commands/
│       └── commit.md        ← 커스텀 커맨드 예시
└── notes/
    └── automation-log.md    ← 기록 예시
```

> CLAUDE.md 보강 예시는 [week07-complete/CLAUDE.md](../week07-complete/CLAUDE.md)에
> "## 커맨드" 섹션을 추가하는 형태로 안내합니다 (아래 확인 포인트 참고).

## 확인 포인트

- `.claude/commands/commit.md`: 「무엇을 하는 커맨드인지」가 프롬프트 안에 명확한가?
- CLAUDE.md: 커맨드 사용법이 한 줄 이상 추가되었는가?
  ```markdown
  ## 커맨드
  - /commit — 변경사항을 요약해 커밋 메시지를 제안하고 커밋까지 실행
  ```
- automation-log.md: 오늘 만든 커맨드(+선택: MCP·서브에이전트 체험)가 기록되어 있는가?
