"""P02 | 小费计算器 (Tip Calculator)

读取餐费金额与希望支付的小费百分比，计算并输出小费金额。
"""


def dollars_to_float(d: str) -> float:
    """把 "$50.00" 这样的文本转换成浮点数 50.0。"""
    return float(d.strip().lstrip("$").replace(",", ""))


def percent_to_float(p: str) -> float:
    """把 "15%" 这样的文本转换成比例 0.15。"""
    return float(p.strip().rstrip("%")) / 100


def main() -> None:
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    tip = dollars_to_float(dollars) * percent_to_float(percent)
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()
