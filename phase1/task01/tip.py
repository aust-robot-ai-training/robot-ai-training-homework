def a(b):
    b=float(b.replace("$",""))
    return b
def c(d):
    d=float(d.replace("%",""))/100
    return d
def main():
    user1=input()
    user2=input()
    end1=a(user1)
    end2=c(user2)
    tip=end1*end2
    print(f"${tip:.2f}")
main()