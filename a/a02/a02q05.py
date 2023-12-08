A_score = 90
B_score = 80
C_score = 70
D_score = 60


def main():
    score = int(input("Please give me the score the student got: "))
    if score >= A_score:
        print('Your grade is A.')
    else:
        if score >= B_score:
            print('Your grade is B.')
        else:
            if score >= C_score:
                print('Your grade is C.')
            else: 
                if score >= D_score:
                    print('Your grade is D.')
                else:
                    print('Your grade is F.')

main()