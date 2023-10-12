def min():
    value1 = int(input("please give me the first value: "))
    value2 = int(input("please give me the second value: "))
    if(value1 < value2):
        return value1
    else:
        return value2
    
def main():
    value = min()
    print(value)

main()