def main():
    name = list()
    name.append(input("Enter fist name:     "))
    name.append(input("Enter second name:   "))
    name.append(input("Enter third name:    "))
    name.append(input("Enter forth name:    "))
    name.sort(key=str.lower)
    print(f"The name in alphabetical are: {name}")

main()