# print(f"{num:,}")

def main():
    amount = float(input("Enter the amount in USD: "))
    EUR = amount * (85.79 / 100.5)
    GBP = amount * (75.13 / 100.5)
    JPY = amount * (11120.5 / 100.5)

    print(f"${amount:,.2f}", "USD is equivalent to: \n")
    print(f"${EUR:,.2f}", "EUR")
    print(f"${GBP:,.2f}", "GBP")
    print(f"${JPY:,.2f}", "JPY")

main()