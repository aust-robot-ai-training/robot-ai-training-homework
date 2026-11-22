def convert(a):
    h,m=a.split(":")
    return int(h)+int(m)/60.0
def main():
    time=input("tell me")
    time1=convert(time)
    if 7.0<=time1<=8.0:
        print("breakfast time")
    elif 12.0<=time1<=13.0:
        print("lunch time")
    elif 18.0<=time1<=19.0:
        print("dinner time")
    else:
        print(" ")
main()
