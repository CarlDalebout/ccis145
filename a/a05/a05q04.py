def encrypt_n(n = 1):
    string = input("Please give me a sting to encrypt: ")
    new_string = ""
    string_list = string.split()
    encrypted_string_list = ''
    for i in string_list:
        for j in i:
            if(ord(j) > ord('a') and ord(j) < ord('z') + n): #( 32 > 96 and 32 < 122)
                if(ord(j) + n > ord('z')):
                    new_char = chr((ord(j)) + n - 26)
                else:
                    new_char = chr((ord(j) + n))
                new_string += new_char
        encrypted_string_list += new_string
        print(new_string)

def decrypt_n(n = 1):
    string = input("please give me a string to decrypt: ")
    new_string = ""
    string_list = string.split()
    decrypted_string_list = ""
    for i in string_list:
        for j in i:
                if(ord(j)> ord('a') - n and ord(j) < ord('z')):
                    if(ord(j) - n) < ord('a'):
                        new_char = chr((ord(j)) - n + 26)
                    else:
                        new_char = chr((ord(j)) - n)

                    new_string += new_char
        decrypted_string_list += new_string
        print(new_string)

def main():
    roll_dice()
    # encrypt_n(2)
    # decrypt_n(2)

main()