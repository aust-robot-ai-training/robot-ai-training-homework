def convert(text: str) -> str:
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text


def main():
    text = input()
    print(convert(text))


if __name__ == '__main__':
    main()


