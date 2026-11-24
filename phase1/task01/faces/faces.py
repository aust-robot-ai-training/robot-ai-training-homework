"""P01 | 表情转换 (Making Faces)

把聊天文本里的 :) 换成 🙂，把 :( 换成 🙁，其余字符原样保留。
"""

SMILE = "🙂"
FROWN = "🙁"


def convert(text: str) -> str:
    """把 text 中的 :) 和 :( 分别替换成对应的表情符号。"""
    return text.replace(":)", SMILE).replace(":(", FROWN)


def main() -> None:
    text = input()
    print(convert(text))


if __name__ == "__main__":
    main()
