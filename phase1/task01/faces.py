def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text
def main():
    shuru=input()
    ct=convert(shuru)
    print(ct)
main()