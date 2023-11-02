import random

def clean_data(text_name):
    cleaned_list = list()
    file_in = open(text_name, 'r')
    data_list = file_in.readlines()
    for element in range(len(data_list)):
        data_list[element] = data_list[element].replace("\n", '')
        data_list[element] = data_list[element].replace(":", '')
        data_list[element] = data_list[element].replace(".", '')
        data_list[element] = data_list[element].replace(",", '')
        data_list[element] = data_list[element].replace("'", '')
        data_list[element] = data_list[element].replace("-", '')
        data_list[element] = data_list[element].replace("?", '')
        data_list[element] = data_list[element].replace("(", '')
        data_list[element] = data_list[element].replace(")", '')
    for element in range(len(data_list)):
        data_list[element] = data_list[element].split()
        
    return data_list


def encrypt_word(user_input_list, cleaned_list):
    encrypt_word_list = list()
    # [hello], [world]
    for element in user_input_list:
        page = 0
        line = 0
        word = 0
        found = False
        for lines in cleaned_list:
            for words in lines:
                # print(f"looking for {element} in line {line}")
                if words == "Page":
                    page += 1
                    line  = 0
                if words == element:
                    if(not found):
                        found = True
                        # print(f"the word {element} is located at page: {page}, line: {line}, word: {word}")
                        encrypt_word_list += [[page, line, word]]
                    elif(found and random.randint(1, 4) == 1):
                        encrypt_word_list.pop()
                        # print(f"replaceing location of {element} with new location page: {page}, line: {line}, word: {word}")
                        encrypt_word_list += [[page, line, word]]
                word += 1
            line += 1
            word = 0
        if(not found):
            # print(f"the word {element} was not found")
            encrypt_word_list += [["?", "?", "?"]]
    return encrypt_word_list

def decrypt_word(user_input_list, cleaned_list):
    decrypt_word_list = list()
    for element in user_input_list:
        # print(f"element[0]: {element[0]}, element[2]: {element[2]}, element[4]: {element[4]}")
        page = 0
        line = 0
        word = 0
        found = False
        for lines in cleaned_list:
            for words in lines:
                if words == "Page":
                    page += 1
                    line  = 0
                if(page == int(element[0]) and line == int(element[1]) and word == int(element[2])):
                    found = True
                    # print(lines)
                    decrypt_word_list += [lines[word]]
                word += 1
            line += 1
            word  = 0
        if(not found):
            decrypt_word_list += ["unknown"]
    return decrypt_word_list

def main():
    text_name = "book1.txt"
    cleaned_list = clean_data(text_name)
    # print(cleaned_list)
    # print(cleaned_list[5][2])
    while(True):
        user_input = int(input("what would you like to do (1) Encrypt Message, (2) Decrypt Message, (3) Exit: \n"))
        while(user_input > 3 or user_input < 1):
            (print("!!!Invalid inputer!!!"))
            user_input = int(input("what would you like to do (1) Encrypt Message, (2) Decrypt Message, (3) Exit: \n"))

        if(user_input == 1):
            user_input = input("please give me a string to encrypt: ")
            user_input_list = user_input.split()
            # print(user_input_list)
            encrypted_user_input = encrypt_word(user_input_list, cleaned_list)
            print(encrypted_user_input)
        elif(user_input == 2):
            user_input = input("please give me a string to decrypt: ")
            user_input_list = user_input.split()
            temp_list = list()
            for element in user_input_list:
                # print(element)
                temp_list += [element.split(".")]
            user_input_list = temp_list
            # print(user_input_list)
            decrypted_user_input = decrypt_word(user_input_list, cleaned_list)
            print(decrypted_user_input)
        else:
            break

main()