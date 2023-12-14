

def main():
    name_1 = input("Enter student name: ")
    gpa_1  = float(input("Enter GPA: "))
    name_2 = input("Enter student name: ")
    gpa_2  = float(input("Enter GPA: "))
    name_3 = input("Enter student name: ")
    gpa_3  = float(input("Enter GPA: "))


    filler = '-'
    print("\nStudent GPA Report:         ")
    print("Name", f"{'GPA' :>23}")
    print(f"{'' :{filler}>{29}}")

    if gpa_1 > gpa_2 and gpa_1 > gpa_3:
        print(f"{name_1 :<25}{gpa_1:.2f}")
        if gpa_2 > gpa_3:
            print(f"{name_2 :<25}{gpa_2:.2f}")
            print(f"{name_3 :<25}{gpa_3:.2f}")
        else:
            print(f"{name_3 :<25}{gpa_3:.2f}")
            print(f"{name_2 :<25}{gpa_2:.2f}")
    elif gpa_2 > gpa_1 and gpa_2 > gpa_3:
        print(f"{name_2 :<25}{gpa_2:.2f}")
        if gpa_1 > gpa_3:
            print(f"{name_1 :<25}{gpa_1:.2f}")
            print(f"{name_3 :<25}{gpa_3:.2f}")
        else:
            print(f"{name_3 :<25}{gpa_3:.2f}")
            print(f"{name_1 :<25}{gpa_1:.2f}")
    elif gpa_3 > gpa_1 and gpa_3 > gpa_2:
        print(f"{name_3 :<25}{gpa_3:.2f}")
        if gpa_1 > gpa_2:
            print(f"{name_1 :<25}{gpa_1:.2f}")
            print(f"{name_2 :<25}{gpa_2:.2f}")
        else:
            print(f"{name_2 :<25}{gpa_2:.2f}")
            print(f"{name_1 :<25}{gpa_1:.2f}")


main()