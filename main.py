from os import system
# from threading import Timer

name = input('Enter your full name: ')
certificate = input('Do you have certificate? : \n'
                    '0 - not avaliable \n'
                    '1 - avaliable \n'
                    'Enter your answer: ')
ort = int(input('Enter your score on ORT: '))
english_level = input('Enter your English language proficiency level: \n'
                        '1 - A1 \n'
                        '2 - A2 \n'
                        '3 - B1 \n'
                        '4 - B2 \n'
                        '5 - C1 \n'
                        '6 - C2 \n'
                        'Enter your level: ')

clearTerminal = system('cls')

def faculity_func():
    faculities = print('Choose your faculity: \n'
                    '1 - Computer Engineering 2500$ \n'
                    '2 - Artificial Intelligence 2200$ \n'
                    '3 - Psychology 1900$ \n'
                    '4 - Journalism 1700$ \n'
                    '5 - International Relations 2200$ \n'
                    '6 - Law 1800$ \n'
                    '7 - Management 2200$ \n'
                    '8 - Medicine 3300$ \n')

    faculities_choice = int(input('Enter the number: '))

    faculities_prices = {
        1: ('Computer Engineering', 2500),
        2: ('Artificial Intelligence', 2200),
        3: ('Psychology', 1900),
        4: ('Journalism', 1700),
        5: ('International Relations', 2200),
        6: ('Law', 1800),
        7: ('Management', 2200),
        8: ('Medicine', 3300),
    }

    choice = faculities_prices[faculities_choice]

    if(choice[0] and 145 <= ort <= 155):
        percentage = round((choice[1] * 5) / 100)
        sum = choice[1] - percentage
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 5% discount will be {sum}$ per year.')
    elif(choice[0] and 156 <= ort <= 174):
        percentage = round((choice[1] * 10) / 100)
        sum = choice[1] - percentage
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 10% discount will be {sum}$ per year.')
    elif(choice[0] and 175 <= ort <= 199):
        percentage = round((choice[1] * 25) / 100)
        sum = choice[1] - percentage
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 25% discount will be {sum}$ per year.')
    elif(choice[0] and 200 <= ort <= 209):
        percentage = round((choice[1] * 50) / 100)
        sum = choice[1] - percentage
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 50% discount will be {sum}$ per year.')
    elif(choice[0] and 210 <= ort <= 218):
        percentage = round((choice[1] * 75) / 100)
        sum = choice[1] - percentage
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 75% discount will be {sum}$ per year.')
    elif(choice[0] and ort >= 219):
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition with a 100% discount will be {sum}$ per year.')
    else:
        print(f'Dear {name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. The cost of your tuition will be {choice[1]}$ per year.')

def check_things():
    if(certificate == '0'):
        print('You did not enroll because you do not own a certificate')
    elif(ort < 110):
        print('You did not enroll because your ORT score is not enough')
    elif(certificate == '1' and ort >= 110 and english_level == '1' or english_level == '2'):
        print('Take a one-year preparatory English language course (Foundation Course AIU) at the university.' +
        'Then next year, after completing that course, you will be able to enroll the university')
    else:
        print('Your applicant is recommended for admission to university')
        faculity_func()


check_things()
# clearTerminal = system('cls')

# def clearScreen():
#     return system('cls')

# delay_clear = Timer(1, clearScreen)
# delay_clear.start()