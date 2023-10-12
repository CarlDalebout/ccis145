import random
import sys

def roll_dice():
    dice_1 = 0
    dice_2 = 1
    while(dice_1  != dice_2):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(dice_1, dice_2, sep= "\t")

def even_or_odd(i):
    if(i % 2 == 0):
        print("even")
    else:
        print("odd")


def main():
    even_or_odd(random.randint(0, sys.maxsize))

main() 