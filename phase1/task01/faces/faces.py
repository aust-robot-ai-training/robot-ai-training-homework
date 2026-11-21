def convert(text):
    """把 :) 换成 🙂，把 :( 换成 🙁，其余字符原样保留。"""
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    text = input()
    print(convert(text))


if __name__ == "__main__":
    main()
