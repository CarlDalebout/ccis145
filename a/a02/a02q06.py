"""
    A:
    grab the value from the user 
    check if the value from the user is greater then 9 and less then 51 
        if the value if greater then 9  and less then 51 print valid points
        else print invalid points

    B:
    check if the value from the user is greater then 9 and less then 51 
        if the value if greater then 9  and less then 51 print valid points
        else print invalid points

"""

def check_points_A(points):
    if points < 9:
        print("invalid points")
    else:
        if points > 51:
            print("invalid points")
        else:
            print("valid points")

def check_points_B(points):
    if points < 9:
        print("invalid points")
    elif points > 51:
        print("invalid points")
    else:
        print("valid points")

def main():
    points = int(input("please give me an amount of points between 9 and 51: "))
    check_points_A(points)
    check_points_B(points)

main()