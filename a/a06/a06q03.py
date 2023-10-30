def capitalize_sentences(user_input): # a = 97 A = 65, z = 122 Z = 90
    ret = ""
    if(ord(user_input[0]) > 90):
        ret += chr(ord(user_input[0]) -32)
    else:
        ret += user_input[0]
    for index in range(1, len(user_input)):
        if(user_input[index-2] == '.' and ord(user_input[index]) > 90 ):
            ret += chr(ord(user_input[index]) - 32)
        else:
            ret += user_input[index]
    return ret

def main():
    user_input = input("please enter a string that has periods after the end of the sentence: ")
    print(capitalize_sentences(user_input))

main()