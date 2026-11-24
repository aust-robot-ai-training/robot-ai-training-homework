"""P04 | 用餐时间 (Meal Time)

把 24 小时制时间换算成以小时为单位的浮点数，并判断属于哪一餐。
早餐 07:00-08:00，午餐 12:00-13:00，晚餐 18:00-19:00（均包含起点和终点）。
"""


def convert(time: str) -> float:
    """把 "7:30" 这样的时间转换成小时浮点数 7.5。"""
    hours, minutes = time.strip().split(":")
    return int(hours) + int(minutes) / 60


def main() -> None:
    value = convert(input("What time is it? "))
    if 7 <= value <= 8:
        print("breakfast time")
    elif 12 <= value <= 13:
        print("lunch time")
    elif 18 <= value <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()
