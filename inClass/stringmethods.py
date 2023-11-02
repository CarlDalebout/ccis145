def main():
    letters = 0
    digits = 0
    spaces = 0
    lowercase = 0
    upercase = 0
    user_input = input("please give me a string to read: ")
   
    for i in range(len(user_input)):
        print(user_input[i])
        if(user_input[i].isnu):
            if(user_input[i].islower):
                letters += 1
                lowercase +=1
            elif(user_input[i].isupper):
                letters += 1
                upercase += 1
            elif(user_input[i].isspace):
                spaces += 1
        elif(user_input[i].isdigit):
            digits += 1

    print(f"[{user_input}]")
    print(f"there is {letters} letters")
    print(f"there is {digits} numbers")
    print(f"there is {spaces} spaces")
    print(f"there is {lowercase} lowercase letters")
    print(f"there is {upercase} uppercase letters")

main()