import re
# 确保24小时制


# 转换时间
def convert(time):
    hours,min=map(int,time.split(':'))
    min=min/60
    return hours+min

# 主体函数
def main():
    if convert(time)>=7 and convert(time)<=8:
        print("breakfast time")

    elif convert(time)>=12 and convert(time)<=13:
        print("lunch time")

    elif convert(time)>=18 and convert(time)<=19:
        print("dinner time")

    else:
        print("It's not yet time")


if __name__=="__main__":
    # 是否为24小时制
    time=input("Please input time in 24-hour format (HH:MM): ")
    time=re.match('([01]?[0-9]|2[0-3]):[0-5][0-9]',time)
    if time==None:
        print("Invalid time format")

    else:
        # 正确格式执行函数
        time=time.group()
        main()
