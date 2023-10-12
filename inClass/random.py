import random

def roll_dice():
    dice_1 = 0
    dice_2 = 1
    while(dice_1  != dice_2):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(dice_1, dice_2, sep= "\t")

def main():
    roll_dice()

main()