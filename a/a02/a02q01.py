"""
    step one: get the cost of the food from the user
    step  1: calculate the tip_ammount by multiplying the food cost by 0.15
    step  2: calculate the sales_tax by multiplying the food cost by 0.07
    step  3: calculate the total of the food tip_ammount and the sales_tax
    step  4: print of the cost of the food
    step  5: print out the tip_ammount
    step  6: print out the sales_tax
    step  7: print out the total amount for the user to pay
"""

def main():
    food_cost = float(input("How much was the food: "))
    tip_ammount = food_cost * 0.15
    sales_tax = food_cost * 0.07
    total = food_cost + tip_ammount + sales_tax
    print(f"the cost of the food is:\t$", "%.2f" % food_cost)
    print(f"the cost of the tip is: \t$", "%.2f" % tip_ammount)
    print(f"the cost of the tax is: \t$", "%.2f" % sales_tax)
    print(f"the total for your outing is \t$", "%.2f" % total)

main()