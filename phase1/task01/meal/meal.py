def convert(time:str) -> float:
    hh,mm = time.split(":")
    hour = int(hh)
    min = int(mm)
    return hour + min / 60

def main():
    t = input(" What time is it? ")
    time_num = convert(t)
    if 7.0 <= time_num <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_num <= 13.0:
        print("lunch time")
    elif 18.0 <= time_num <= 19.0:
        print("dinner time")


if __name__ == "__main__":
    main()