def a(value):
    if value == 1:
        print("I")
    if value == 2:
        print("II")
    if value == 3:
        print("III")
    if value == 4:
        print("IV")
    if value == 5:
        print("V")
    if value == 6:
        print("VI")
    if value == 7:
        print("VII")
    if value == 8:
        print("VIII")
    if value == 9:
        print("IX")
    if value == 10:
        print("X")

def b(value):
    if value == 1:
        print("I")
    elif value == 2:
        print("II")
    elif value == 3:
        print("III")
    elif value == 4:
        print("IV")
    elif value == 5:
        print("V")
    elif value == 6:
        print("VI")
    elif value == 7:
        print("VII")
    elif value == 8:
        print("VIII")
    elif value == 9:
        print("IX")
    elif value == 10:
        print("X")

def main():
    value = int(input("please give me a value between 1 and 10: "))
    while value > 10 or value < 1:
        value = int(input("Error value is out of bounds\nplease give me a value between 1 and 10: "))
    a(value)
    b(value)

main()

"""
B:  I prefure the if-elif-else structure mainly becuase its far easier to write and manage 
    rather then the nested if-else statments
"""