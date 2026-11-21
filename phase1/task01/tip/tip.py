def dollors_to_float(d:str) -> float:
    return float(d.replace("$",""))
def percent_to_float(p:str) ->float:
    num = float(p.replace("%",""))
    return num / 100

def main():
    money = input("How much was the meal? \n")
    tip_percent = input("What percentage would you like to tip?\n")
    meal = dollors_to_float(money)
    rate = percent_to_float(tip_percent)
    res = meal * rate
    print(f"Leave ${res : .2f}")

if __name__ == "__main__":
    main()
