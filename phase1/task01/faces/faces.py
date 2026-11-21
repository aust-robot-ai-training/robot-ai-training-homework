def convert (text:str) -> str:
    res = text.replace(":)"," 🙂 ")
    res = res.replace(":(","🙁")
    return res

def main():
    s = input()

    print(convert(s))

if __name__ == "__main__":
    main()