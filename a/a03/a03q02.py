
def main():
    value = int(input("please give me a value between 0 and 36: "))
    while value > 36 or value < 0:
        value = int(input("Error value is out of bounds\nplease give me a value between 0 and 36: "))
    if value > 28:
        if value % 2 == 0:
            print("the pocket is red")
        else:
            print("the pocket is black")
    elif value > 18:
        if value % 2 == 0:
            print("the pocket is black")
        else:
            print("the pocket is red")
    elif value > 10:
        if value % 2 == 0:
            print("the pocket is red")
        else:
            print("the pocket is black")
    elif value > 0:
        if value % 2 == 0:
            print("the pocket is black")
        else:
            print("the pocket is red")
    else:
        print("the pocket is green")

main()