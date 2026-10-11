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


# TODO(🟡): 학사일정 도구 school_schedule(school_name, from_date, to_date)도 MCP 도구로 추가해 보자.


if __name__ == "__main__":
    mcp.run()  # 기본 transport = stdio
