"""
    grab the length and width for the first rectangle
    grab the length for the second rectangle
    calculate the area of the first rectangle
    calculate the area of the second rectangle

    check if the the two rectangle is the same
        if so print they are the same and exit
    check if the area of the first is larger
        print that the first rectangle is larger
    check if the area of the second is larger
        print that the area of the second is larger
"""



def main():
    length_1 = int(input("please give me the length of the first rectangle: "))
    width_1  = int(input("please give me the width of the first rectangle: "))
    length_2 = int(input("please give me the length of the second rectangle: "))
    width_2  = int(input("please give me the width of the second rectangle: "))
    area_1 = length_1 * width_1
    area_2 = length_2 * width_2
    if area_1 == area_2:
        print("the area of both rectangles are the same")
    if area_1 > area_2:
        print("the area of the first rectangle is larger")
    if area_2 > area_1:
        print("the area of the second rectangle is larger")

main()