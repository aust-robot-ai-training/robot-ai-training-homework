def dollar_to_float(strs):
    return float(strs)    



def percent_to_float(strs2):
    return float(strs2) / 100


def main():
    strs = input('How much was the meal? :')
    strs2 = input('What percentage would you like to tip? :')
    result = dollar_to_float(strs=strs.strip('$')) * percent_to_float(strs2=strs2.strip('%'))
    print(f"Leave: ${result:.2f}")


main()