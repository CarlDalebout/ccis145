def print_date(date):
    while(len(date) != 10 or date[2] != '/' or date[5] != '/'):
        date = input("invalid format please give me a correct date in the from mm/dd/yyyy: ")
    
    if(date[6] != '-'):
        year = int(date[6])*1000 + int(date[7])*100 + int(date[8])*10 + int(date[9])
    while(year < 0 or year > 9999):
        date = input("invalid year please give me a correct date int he form mm/dd/yyyy: ")
        year = int(date[6])*1000 + int(date[7])*100 + int(date[8])*10 + int(date[9])

    leap_year = False
    if(year % 100 == 0 and year %400 == 0):
        leap_year = True
    elif(year % 100 != 0 and year % 4 == 0):
        leap_year = True
    else:
        leap_year = False

    if(date[0] != '-'):
        month = int(date[0])*10 + int(date[1])
    while(date[0] == '-' or month > 12):
        date = input("invalid month please give me a correct date in the form mm/dd/yyyy: ")
        month = int(date[0])*10 + int(date[1])
    
    if(date[3] != '-'):
        day = int(date[3])*10 + int(date[4])
    while(date[3] == '-' or day < 0):
        date = input("invalid day please give me a correct date in the form mm/dd/yyyy: ")
        day = int(date[3])*10 + int(date[4])

    if(month == 1 and day <= 31):
        print(f"January {day}, {year}")
    elif(month == 2 and leap_year == False and day <= 28):
        print(f"February {day}, {year}")
    elif(month == 2 and leap_year == True and day <= 29):
        print(f"February {day}, {year}")
    elif(month == 3 and day <= 31):
        print(f"March {day}, {year}")
    elif(month == 4 and day <= 30):
        print(f"April {day}, {year}")
    elif(month == 5 and day <= 31):
        print(f"May {day}, {year}")
    elif(month == 6 and day <= 30):
        print(f"June {day}, {year}")
    elif(month == 7 and day <= 31):
        print(f"July {day}, {year}")
    elif(month == 8 and day <= 31):
        print(f"August {day}, {year}")
    elif(month == 9 and day <= 30):
        print(f"September {day}, {year}")
    elif(month == 10 and day <= 31):
        print(f"October {day}, {year}")
    elif(month == 11 and day <= 30):
        print(f"November {day}, {year}")
    elif(month == 12 and day <= 31):
        print(f"December {day}, {year}")
    else:
        date = input("invalid day please give me a correct date in the form mm/dd/yyyy: ")
        print_date(date)


def main():
    date = input("please give me a data in the form mm/dd/yyyy: ")
    print_date(date)

main()