"""
8주차 — 공공데이터 API 연동 스켈레톤

먼저 이 파일만 단독으로 실행해서 API 응답 구조를 눈으로 확인한 다음(3장),
필요한 값만 뽑는 가공 함수를 완성한다(4장).

    python opendata.py

# TODO 가 달린 부분만 직접 채운다. 함수 이름·시그니처는 바꾸지 않는다 —
# app.py의 /dashboard 라우트가 이 이름 그대로 가져다 쓴다.
"""
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
SAMPLE_PATH = Path(__file__).resolve().parent / "data" / "sample_air_quality.json"

# 등급 코드(khaiGrade) -> 사람이 읽는 문자열
GRADE_LABELS = {"1": "좋음", "2": "보통", "3": "나쁨", "4": "매우나쁨"}


def fetch_raw(sido="서울"):
    """공공데이터포털 API를 호출해 원본 JSON(dict)을 그대로 돌려준다."""
    api_key = os.environ.get("PUBLIC_DATA_API_KEY")

    # TODO: params 딕셔너리를 완성한다.
    # 필요한 키: serviceKey, returnType("json"), numOfRows, pageNo, sidoName, ver("1.3")
    params = {
        "serviceKey": api_key,
        # ...
    }

    # TODO: requests.get(API_URL, params=params, timeout=5)로 요청을 보내고
    # response.json()을 return 한다.
    raise NotImplementedError("fetch_raw를 완성하세요")


def parse_items(raw):
    """원본 JSON(dict)에서 측정소별로 필요한 값만 뽑아 리스트로 정리한다.

    반환 형태 예시:
        [{"station": "종로구", "pm10": 38, "pm25": 19, "grade": "보통"}, ...]
    """
    # TODO: raw["response"]["body"]["items"]에서 각 item마다
    #   station = item.get("stationName", "알 수 없음")
    #   pm10    = int(item.get("pm10Value") or 0)
    #   pm25    = int(item.get("pm25Value") or 0)
    #   grade   = GRADE_LABELS.get(item.get("khaiGrade"), "정보없음")
    # 를 뽑아 딕셔너리로 만들고, pm10 기준 내림차순 정렬해서 return 한다.
    raise NotImplementedError("parse_items를 완성하세요")


def load_sample():
    """샘플 JSON 파일을 읽어 parse_items와 같은 형태로 돌려준다."""
    with open(SAMPLE_PATH, encoding="utf-8") as f:
        return parse_items(json.load(f))


def fetch_air_quality(sido="서울"):
    """대시보드가 실제로 호출하는 함수.

    성공하면 (실시간 데이터, "live"), 실패하면 (샘플 데이터, "sample")을 돌려준다.
    이 함수는 절대로 예외를 밖으로 던지면 안 된다 — /dashboard가 죽지 않아야 한다.
    """
    try:
        raw = fetch_raw(sido)
        return parse_items(raw), "live"
    except Exception:
        return load_sample(), "sample"


if __name__ == "__main__":
    # 3장: 먼저 원본 JSON을 통째로 찍어서 구조를 눈으로 본다.
    print(fetch_raw())
