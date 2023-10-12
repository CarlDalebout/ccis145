
def main():
    n = int(input("please give me a number (3-20): "))
    while(n < 3 or n > 20):
        n = int(input("please give me a number (3-20): "))
    n_2 = n-2
    print("*" * n)
    for i in range(n_2):
        print("*", " " * n_2, "*", sep = "")
    print("*" * n)

main()