"""P03 | 银行问候语 (Home Federal Savings Bank)

根据问候语决定银行支付的金额：
以 hello 开头 -> $0；其余以 h 开头 -> $20；其他情况 -> $100。
比较前忽略开头的空白，并忽略字母大小写。
"""


def main() -> None:
    greeting = input("Greeting: ").strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
