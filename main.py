from os import system
import time

name = input('Enter your name: ')
last_name = input('Enter your surname: ')
certificate = bool(int(input('Do you have certificate? : \n'
                    '1 - avaliable \n'
                    '0 - not avaliable \n'
                    'Enter your answer only with number: ')))

ort = int(input('Enter your score on ORT: '))
english_level = input('Enter your English language proficiency level: \n'
                    '1 - Beginner\Elementary \n'
                    '2 - Pre-Intermediate \n'
                    '3 - Intermediate \n'
                    '4 - Upper-Intermediate \n'
                    '5 - Advanced \n'
                    '6 - Proficient \n'
                    'Enter your level: ')

clearScreen = system('cls')

def selectFaculty():
    faculities = print('Choose your faculity: \n'
                    '1 - Computer Engineering 2500$ \n'
                    '2 - Artificial Intelligence 2200$ \n'
                    '3 - Psychology 1900$ \n'
                    '4 - Journalism 1700$ \n'
                    '5 - International Relations 2200$ \n'
                    '6 - Law 1800$ \n'
                    '7 - Management 2200$ \n'
                    '8 - Medicine 3300$ \n')

    chosenProgram = int(input('Enter the number: '))

    facultyTuitionCosts = {
        1: ('Computer Engineering', 2500),
        2: ('Artificial Intelligence', 2200),
        3: ('Psychology', 1900),
        4: ('Journalism', 1700),
        5: ('International Relations', 2200),
        6: ('Law', 1800),
        7: ('Management', 2200),
        8: ('Medicine', 3300),
    }

    choice = facultyTuitionCosts[chosenProgram]

    if(choice[0] and 145 <= ort <= 155):
        percentage = round((choice[1] * 5) / 100)
        total = choice[1] - percentage
        print(f'Dear {name}{last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n'+
        f'The cost of your tuition with a 5% discount will be {total}$ per year.')

    elif(choice[0] and 156 <= ort <= 174):
        percentage = round((choice[1] * 10) / 100)
        total = choice[1] - percentage
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition with a 10% discount will be {total}$ per year.')

    elif(choice[0] and 175 <= ort <= 199):
        percentage = round((choice[1] * 25) / 100)
        total = choice[1] - percentage
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition with a 25% discount will be {total}$ per year.')

    elif(choice[0] and 200 <= ort <= 209):
        percentage = round((choice[1] * 50) / 100)
        total = choice[1] - percentage
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition with a 50% discount will be {total}$ per year.')

    elif(choice[0] and 210 <= ort <= 218):
        percentage = round((choice[1] * 75) / 100)
        total = choice[1] - percentage
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition with a 75% discount will be {total}$ per year.')

    elif(choice[0] and 219 <= ort <= 240):
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition with a 100% discount will be 0$ per year.')

    else:
        print(f'Dear {name} {last_name}, we congratulate you! You have been admitted to the {choice[0]} program at Ala-Too International University. \n' +
        f'The cost of your tuition will be {choice[1]}$ per year.')

def check_enrollment():
    if(certificate == False):
        print('You did not enroll because you do not own a certificate')
    elif(ort < 110):
        print('You did not enroll because your ORT score is not enough')
       

    elif(certificate == True and ort >= 110 and english_level == '1' or english_level == '2'):
        print('Take a one-year preparatory English language course (Foundation Course AIU) at the university.' +
        'Then next year, after completing that course, you will be able to enroll the university')

    else:
        print('Your applicant is recommended for admission to university')
        time.sleep(1)
        clearScreen = system('cls')
        selectFaculty()


check_enrollment()
