def dollars_to_float(d):
    """去掉开头的 $，转成浮点数，例如 "$50.00" -> 50.0。"""
    return float(d.replace("$", ""))


def percent_to_float(p):
    """去掉结尾的 % 并除以 100，例如 "15%" -> 0.15。"""
    return float(p.replace("%", "")) / 100


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()
