n = int(input("give me a number: "))
i = 1
sum = 1
while(i < n):
    sum *= i
    print(i, "* ", end = "")
    i += 1

sum *= n
print(n, "=", sum)