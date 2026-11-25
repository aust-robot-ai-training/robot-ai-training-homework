def dollars_to_float(d: str) -> float:
    return float(d.removeprefix("$"))
def percent_to_float(p:str) -> float:
    return float(p.removesuffix("%"))/100
def main():
    meal=input("How much was the meal?")
    percent=input("What percentage would you like to tip?")
    money=dollars_to_float(meal)
    rate=percent_to_float(percent)
    tip=money*rate
    print(f"Leave ${tip:.2f}")
if __name__=="__main__":
    main()