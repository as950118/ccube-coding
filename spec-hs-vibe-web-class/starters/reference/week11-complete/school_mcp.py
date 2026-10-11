# 실습 2. 내 코드를 MCP 서버로 만들기
# 같은 neis.py를 이번에는 Claude Code(남이 만든 하네스)에 꽂는다.
#
# 연결: claude mcp add school -- <파이썬 절대경로> <이 파일 절대경로>
# 확인: Claude Code 안에서 /mcp
#
# ⚠️ MCP 서버는 표준 입출력(stdio)으로 Claude Code와 대화한다. 이 파일에서 print()를 쓰면 대화가 깨진다.
from mcp.server import MCPServer

import neis

mcp = MCPServer("school")


# 함수 이름·인자 타입·docstring이 그대로 "도구 설명서"가 된다 (step5의 TOOLS 딕셔너리를 손으로 쓸 필요가 없다)
@mcp.tool()
def school_meal(school_name: str, date: str) -> str:
    """나이스(NEIS) 공식 데이터에서 학교의 급식(중식) 메뉴를 조회한다. date는 YYYYMMDD."""
    school = neis.get_school_code(school_name)
    if school is None:
        return "학교를 찾지 못했습니다. 정확한 학교 이름(예: 서울과학고등학교)이 필요합니다."
    meal = neis.get_meal(school[0], school[1], date)
    if meal is None:
        return f"{school[2]}의 {date} 급식 정보가 없습니다. (주말·방학·휴업일일 수 있음)"
    return f"[{school[2]} {date} {meal['meal_name']}]\n{meal['menu']}\n칼로리: {meal['calorie']}"


@mcp.tool()
def school_schedule(school_name: str, from_date: str, to_date: str) -> str:
    """나이스(NEIS) 공식 데이터에서 학교의 학사일정(시험·행사·휴일)을 조회한다. 날짜는 YYYYMMDD, 한 번에 최대 5건이라 기간을 1~2주로 짧게 잡는다."""
    school = neis.get_school_code(school_name)
    if school is None:
        return "학교를 찾지 못했습니다. 정확한 학교 이름(예: 서울과학고등학교)이 필요합니다."
    events = neis.get_schedule(school[0], school[1], from_date, to_date)
    if not events:
        return f"{school[2]}의 {from_date}~{to_date} 학사일정이 없습니다."
    return f"[{school[2]} 학사일정]\n" + "\n".join(f"{e['date']} {e['event']}" for e in events)


if __name__ == "__main__":
    mcp.run()  # 기본 transport = stdio
