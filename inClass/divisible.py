number = int(input("please give me a number: "))

if(number%11 == 0 and number%5 == 0 and number%3 == 0):
    print(number, "is devisable by 3, 5, 11")
elif(number%11 == 0 and number%5 == 0):
    print(number, "is devisable by 5 and 11")
elif(number%11 == 0 and number%3 == 0):
    print(number, "is devisable by 3 and 11")
elif(number%11 == 0):
    print(number, "is devisable by 11")
elif(number%5 == 0 and number%3 == 0):
    print(number, "is devisable by 3 and 5")
elif(number%5 == 0):
    print(number, "is devisable by 5")
elif(number%3 == 0):
    print(number, "is devisable by 3")
else:
    print(number, "is not desiable by 3, 5, or 11")