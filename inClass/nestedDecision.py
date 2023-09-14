amount1 = int(input("amount1: "))
amount2 = int(input("amount2: "))

if(amount1 > 10 and amount2 < 100):
    if(amount1 >= amount2):
        print("amount1 is larger")
    else:
        print("amount2 is larger")
else:
    print("input is not within the scope")