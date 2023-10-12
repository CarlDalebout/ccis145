def print_name():
    print("Carl Dalebout")

def get_major():
    major = input("what major are you: ")
    print("it looks like your major is", major)

def show_double(number):
    result = number * 2
    print(result)

def convert_cups_oz(cups):
    print(cups*8, "ozs")

def main():
    value = int(input("hello this is a program to convert cups to oz\nplease enter the amount of clups: "))
    convert_cups_oz(value)



main()