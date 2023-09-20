flag = True

while(flag):
    s1 = float(input("Enter Test 1 score: "))
    s1 += float(input("Enter Test 2 score: "))
    s1 += float(input("Enter Test 3 score: "))
    print("the average score are", s1/3)

    if(input("keep going (y/n): ") == 'n'):
        flag = False 