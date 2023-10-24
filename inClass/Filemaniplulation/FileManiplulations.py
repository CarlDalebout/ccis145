def main():
    file_out = open("numbers/numbers.txt", 'w')
    file_out.write(f"{56}\n")
    file_out.write(f"{100}\n")
    file_out.write(f"{14}\n")
    file_out.close()

    file_in = open("numbers/numbers.txt", 'r')
    a = int(file_in.readline().strip())
    b = int(file_in.readline().strip())
    c = int(file_in.readline().strip())
    file_in.close()
    
    if(a > b):
        a, b = b, a 
    if(a > c):
        a, c = c, a
    if(b > c):
        b, c = c, b

    file_out = open("numbers/numbers.txt", 'w')
    file_out.write(f"{a}\n")
    file_out.write(f"{b}\n")
    file_out.write(f"{c}\n")
    file_out.close()

main()





# file_out_negative = open("numbers/negative_numbers.txt", "w")
# # file_test = open(r"c:\\Docs||number.txt") how to open a folder in windows
# for i in range(1, 21):
#     file_out_positive.write(f"{i} \n")
#     file_out_negative.write(f"{-i} \n")

# file_out_positive.close()
# file_out_negative.close()

# file_in = open("numbers/positive_numbers.txt", "r")

# sum = 0
# numbers = file_in.readlines()
# for element in numbers:
#     sum += int(element.strip())
#     print(int(element.strip()))
# print(sum)
# # if(file_in.readline() != ""):

# file_in.close()
