n = int(input("give me a number(1-20): "))

while(n > 0):
    j = 0
    while(j < n):
        print('*', end= '')
        j += 1
    print()
    n -= 1