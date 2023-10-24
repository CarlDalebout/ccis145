import random
def encrypt_n(n = 1):
    string = input("Please give me a sting to encrypt: ")
    new_string = ""
    string_list = string.split()
    encrypted_string_list = []
    for i in string_list:
        new_string = ""
        for j in i:
            if(ord(j) > ord('a') and ord(j) < ord('z') + n): #( 32 > 96 and 32 < 122)
                if(ord(j) + n > ord('z')):
                    new_char = chr((ord(j)) + n - 26)
                else:
                    new_char = chr((ord(j) + n))
                new_string += new_char
        encrypted_string_list += [new_string]
    print(str(encrypted_string_list))
    return encrypted_string_list

def decrypt_shift(string_list, shift_amount):
    string_list = string_list.split()
    decrypted_string_list = []
    for i in string_list:
        decrypted_string = ""
        for char in i:
            if(ord(char) > ord('a') - shift_amount  and ord(char) < ord('z')):
                if(ord(char) - shift_amount < ord('a')):
                    decrypted_char = chr((ord(char) - shift_amount) + 26)
                else:
                    decrypted_char = chr(ord(char) - shift_amount)
                decrypted_string += decrypted_char
        decrypted_string_list += [decrypted_string]
    return decrypted_string_list

def check_decryption(decrypted_string_list):
    
    file = open("wordlist.txt", "r")
    words = file.read().splitlines()
    found = True
    for decrypted_word in decrypted_string_list:
        for element in words:
            if(element != decrypted_word):
                found = False
    return found

def find_shift():
    found = False
    string = input("Enter your encrypted text: ")    
    for shift_amount in range(2, 25):
        if(check_decryption(decrypt_shift(string, shift_amount))):
            found = True   
            break 
    if(found):
        print("\nDecrypted text: ", end= '')
        for elements in decrypt_shift(string, shift_amount):
            print(elements, end= ' ')
        print("\nMethod used for decryption: ", shift_amount, "-character shift substituition", sep = '')
    else:
        print("\nDecryption failed")    


def main():
    amount = int(input("enter encrypte amount: "))
    encrypt_n(amount)
    find_shift()

main()