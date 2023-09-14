day = int(input("please enter a number 1-7 "));

# if(day == 1):
#     print("monday")
# else:
#     if(day == 2):
#         print("Tues")
#     else:
#         if(day == 3):
#             print("weds")
#         else:
#             if(day == 4):
#                 print("Thursday")
#             else:
#                 if(day == 5):
#                     print("Friday")
#                 else:
#                     if(day == 6):
#                         print("Sat")
#                     else:
#                         if(day == 7):
#                             print("Sun")
#                         else:
#                             print("error")

# match day:
#     case 1:
#         print("mon")
#     case 2:
#         print("tues")
#     case 3:
#         print("wed")
#     case 4:
#         print("thurs")
#     case 5:
#         print("fri")
#     case 6:
#         print("sat")
#     case 7:
#         print("sun")

def switch(day):
    if day == 1:
        return "mon"
    elif day == 2:
        return "tues"
    elif day == 3:
        return "wed"
    elif day == 4:
        return "thur"
    elif day == 5:
        return "fri"
    elif day == 6:
        return "sat"
    elif day == 7:
        return "sun"
    else:
        return "day is less then one or greated then 7"

print(switch(day))