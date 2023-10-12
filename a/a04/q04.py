

def main():
    n = int(input("please give me a number: "))
    i = 2
    prime = True

    while(i < n):
        if(n%i == 0):
            prime = False
            print(n, "%", i, "=", n%i)
            break
        i += 1

    if(prime == True):
        print("Prime!")
    else:
        print("Not Prime!")


main()
