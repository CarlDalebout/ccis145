
"""
    input user desired ammount of cookies
    scale = user_amount / 48
    amount of sugar = 1.5 * scale
    amount of butter = 1 * scale
    amount of flour = 2.75 * scale

    print the amount of each ingrediant for the user

"""

def main():
    user_amount = int(input("how many cookies are you trying to make today: "))
    scale   = user_amount / 48
    sugar   = 1.5  * scale
    butter  = 1    * scale
    flour   = 2.75 * scale

    print(f"the amount of sugar you will need is {sugar} cups")
    print(f"the amount of butter you will need is {butter} cups")
    print(f"the amount of flour you will need is {flour} cups")

main()