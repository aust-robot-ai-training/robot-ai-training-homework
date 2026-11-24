def main():
    s=input("Greeting:")
    s=s.strip().lower()
    if s.startswith("hello"):
        print("$0")
    elif s.startswith("h"):
        print("$20")
    else:
        print("$100")
if __name__=="__main__":
    main()