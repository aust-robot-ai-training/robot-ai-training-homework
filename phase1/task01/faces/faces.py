def convert(text:str) -> str:
    text=text.replace(":)","\N{SLIGHTLY SMILING FACE}")
    text=text.replace(":(","\N{SLIGHTLY FROWNING FACE}")
    return text
def main():
    s=input()
    print(convert(s))
if __name__=="__main__":
    main()