def convert(time:str) -> float:
    hh,mm=time.split(":")
    return int(hh)+int(mm)/60
def main():
    t_str=input("What time is it?")
    t=convert(t_str)
    if 7.0<=t<=8.0:
        print("breakfast time")
    elif 12.0<=t<=13.0:
        print("lunch time")
    elif 18.0<=t<=19.0:
        print("dinner time")
if __name__=="__main__":
    main()