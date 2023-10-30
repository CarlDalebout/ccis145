import random

def get_computer_choice():
    return random.randint(1,3)

def check_game_state(user_input, computer_input):
    if(user_input == computer_input):
        return 3
    elif(user_input == 1 or computer_input == 1):
        if(user_input == 2 or computer_input == 2):
            return 2
        elif(user_input == 3 or computer_input == 3):
            return 0
    elif(user_input == 2 or computer_input == 2):
        if(user_input == 3 or computer_input == 3):
            return 1

def main():
    user_input = int(input("please give me a number between 1-3 (1: rock, 2: paper, 3: scissors): "))
    while(user_input < 1 or user_input > 3):
        user_input = int(input("please give me a number between 1-3 (1: rock, 2: paper, 3: scissors): "))
    if(user_input == 1):
        print("\nYou picked Rock\n")
    elif(user_input == 2):
        print("\nYou picked Paper\n")
    elif(user_input == 3):
        print("\nYou picked Scissors\n")

    computer_choice = get_computer_choice()
    if(computer_choice == 1):
        print("The computer picked Rock\n")
    elif(computer_choice == 2):
        print("The computer picked Paper\n")
    elif(computer_choice == 3):
        print("The computer picked Scissors\n")
    

    game_state = check_game_state(user_input, computer_choice)
    if(game_state == 0):
        print("The Rock Smashes Scissors")
    elif(game_state == 1):
        print("The Scissors Cut Paper")
    elif(game_state == 2):
        print("The Paper Covers Rock")
    else:
        print("the game needs to get played again")
        main()
    
main()