"""
    grab a number from the user between 1-7
    check if the user has provided an invalid value
        if the value is wrong grabe another value from the user
    check if the value from the user is 1
        if the value is equal to 1 print monday
    check if the value from the user is 2
        if the value is equal to 2 print tuesday
    check if the value from the user is 3
        if the value is equal to 3 print wednesday
    check if the value from the user is 4
        if the value is equal to 4 print thursday
    check if the value from the user is 5
        if the value is equal to 5 print friday
    check if the value from the user is 6
        if the value is equal to 6 print saturday
    check if the value from the user is 7
        if the value is equal to 7 print sunday
"""

def main():
    value = int(input("Please give me a value between 1 and 7: "))
    while value > 7 or value < 1:
        value = int(input("Error value is out of range 1 and 7\nPlease give me a value between 1 and 7: "))
    if value == 1:
        print("monday")
    if value == 2:
        print("tuesday")
    if value == 3:
        print("wednesday")
    if value == 4:
        print("thursday")
    if value == 5:
        print("friday")
    if value == 6:
        print("saturday")
    if value == 7:
        print("sunday")

main()