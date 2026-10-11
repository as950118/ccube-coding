import os
from datetime import datetime

import requests

BASE_URL = "https://open.neis.go.kr/hub"
TIMEOUT = 5  # 초. 응답이 없으면 무한정 기다리지 않는다.

# 나이스 급식 메뉴 뒤 괄호 숫자(알레르기 번호)의 공식 의미
ALLERGY_CODES = {
    1: "난류", 2: "우유", 3: "메밀", 4: "땅콩", 5: "대두", 6: "밀",
    7: "고등어", 8: "게", 9: "새우", 10: "돼지고기", 11: "복숭아", 12: "토마토",
    13: "아황산류", 14: "호두", 15: "닭고기", 16: "쇠고기", 17: "오징어",
    18: "조개류(굴, 전복, 홍합 등)", 19: "잣",
}


def _get(endpoint: str, **params):
    query = {"Type": "json", "pIndex": 1, "pSize": 5, **params}
    # 키는 코드에 적지 않고 환경 변수에서 읽는다. 없으면 샘플 모드(5건 제한)로 동작한다.
    api_key = os.environ.get("NEIS_API_KEY")
    if api_key:
        query["KEY"] = api_key
    try:
        return requests.get(f"{BASE_URL}/{endpoint}", params=query, timeout=TIMEOUT).json()
    except (requests.RequestException, ValueError):
        return {}


def get_school_code(school_name: str):
    """학교 이름 → (교육청코드, 학교코드, 학교이름). 못 찾으면 None. 같은 이름이 여럿이면 첫 결과."""
    res = _get("schoolInfo", SCHUL_NM=school_name)
    if "schoolInfo" not in res:
        return None
    row = res["schoolInfo"][1]["row"][0]
    return row["ATPT_OFCDC_SC_CODE"], row["SD_SCHUL_CODE"], row["SCHUL_NM"]


def get_meal(office_code: str, school_code: str, date: str | None = None):
    """급식 원문을 dict로 돌려준다(date는 YYYYMMDD, 생략하면 오늘). 급식이 없으면 None."""
    date = date or datetime.now().strftime("%Y%m%d")
    res = _get(
        "mealServiceDietInfo",
        ATPT_OFCDC_SC_CODE=office_code,
        SD_SCHUL_CODE=school_code,
        MLSV_YMD=date,
    )
    if "mealServiceDietInfo" not in res:
        return None

    rows = res["mealServiceDietInfo"][1]["row"]
    # 조식(1)·중식(2)·석식(3) 중 중식을 우선 사용한다.
    row = next((r for r in rows if r.get("MMEAL_SC_CODE") == "2"), rows[0])
    return {
        "date": date,
        "meal_name": row.get("MMEAL_SC_NM", ""),
        "menu": row["DDISH_NM"].replace("<br/>", "\n"),
        "calorie": row.get("CAL_INFO", ""),
        "nutrition": row.get("NTR_INFO", "").replace("<br/>", "\n"),
    }


def get_schedule(office_code: str, school_code: str, from_date: str, to_date: str):
    """기간(YYYYMMDD~YYYYMMDD)의 학사일정을 [{"date", "event"}] 리스트로 돌려준다. 없으면 빈 리스트.

    키 없이 쓰는 샘플 모드는 최대 5건만 돌려주므로 기간을 짧게(1~2주) 잡는다.
    """
    res = _get(
        "SchoolSchedule",
        ATPT_OFCDC_SC_CODE=office_code,
        SD_SCHUL_CODE=school_code,
        AA_FROM_YMD=from_date,
        AA_TO_YMD=to_date,
    )
    if "SchoolSchedule" not in res:
        return []
    return [
        {"date": row["AA_YMD"], "event": row["EVENT_NM"]}
        for row in res["SchoolSchedule"][1]["row"]
    ]
