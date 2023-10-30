def is_prime(x):
    if (x < 0):
        return False
    elif x in (0, 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

def main():
    value = int(input("please give me number to see if its prime: "))
    print(f"the number {value} is ", end= "")
    if(is_prime(value)):
        print("prime")
    else:
        print("not prime")

main()