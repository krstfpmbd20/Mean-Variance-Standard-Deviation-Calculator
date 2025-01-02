# ctrl / to comment out

# name = str(input('What is your name? '))
# age = int(input('How old are you? '))
# favorite_color = str(input('What is your favorite color? '))
# print(f'Hello, {name}, you are {age} years old and your favorite color is {favorite_color}.')

# birth_year = int(input('What year were you born? '))
# age = 2024 - birth_year
# print(f'You will be {age} years old in 2024.')

# pounds_weight = (input('Enter your weight in pounds: '))
# print(type(pounds_weight))
# kilograms_weight = int(int(pounds_weight) * 0.453592)
# print(type(kilograms_weight))
# print(f'Your weight in kilograms is: {kilograms_weight}')

# book_name = "\"The Alchemist's Secret\""
# print(book_name)

# def outer():
#     x = 5 
#     def inner():
#         return x * 2
#     return inner()
# print(outer())

# email = '''Dear Lee,

# You have been selected to join the 187 mobstaz.
# You are the chosen one.

# Sincerely,
# Codog
# '''
# print(email)

# name = "Kristof S. Pambid"
# print(name[-1:-16:-2])
# print(name[:2])

# def replace_second_occurrence(s, old, new):
#     parts = s.split(old, 2)
#     if len(parts) == 3:
#         return old.join(parts[:2]) + new + parts[2]
#     return s
# print(replace_second_occurrence('nnn', 'n', '1'))

# import math 

# x = -2.75
# print(math.ceil(x))

# try:
#     stochrsi = int(input('Enter stochrsi level: '))

#     if stochrsi > 80:
#         print('Overbought')
#     elif stochrsi < 20:
#         print('Oversold')
#     else:
#         print('Neutral')

# except ValueError:
#     print('Invalid input. Please enter an integer value.')

# try:
#     income = int(input('Enter your income: '))
#     credit = int(input('Enter your credit score: '))

#     high_income = (income >= 100000)
#     good_credit = (credit >= 700)
#     loan = 1000000

#     if high_income and good_credit:
#         print(f'You are qualified for a loan of {loan}.')
#     elif high_income or good_credit:
#         print(f'You are qualified for a loan of {loan/2}.')
#     else:
#         print('You are not qualified for a loan.')
# except ValueError:
#     print('Invalid input. Please enter an integer value.')

# temperature = int(input('Enter the temperature: '))
# if temperature > 30:
#     print('It\'s a hot day.')
# elif temperature < 10:
#     print('It\'s a cold day.')
# elif temperature < 30 and temperature > 10:
#     print('It\'s neither hot nor cold.')
# else:
#     print('Invalid input. Please enter an integer value.')

# name = input('Enter your name: ')
# length = len(name)
# if length < 3:
#     print('Name must be at least 3 characters long.')
# elif length > 50:
#     print('Name must be a maximum of 50 characters long.')
# else:    
#     print('Name looks good.')

# weight = int(input('Enter your weight: '))
# pounds_or_kilograms = input('(L)bs or (K)g: ')
# if pounds_or_kilograms.upper() == 'L':
#     weight_kg = weight * 0.453592
#     print(f'You are {weight_kg} kilos.')
# elif pounds_or_kilograms.upper() == 'K':
#     weight_lbs = weight / 0.453592
#     print(f'You are {weight_lbs} pounds.')
# else:
#     print('Invalid input. Please enter "L" for pounds or "K" for kilograms.')

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# import random

# secret_number = random.randint(1, 10)
# guess_count = 1
# while guess_count <= 3:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print(f'You won! The correct number was {secret_number}.')
#         break
# else:
#     print(f'You lost! The correct number was {secret_number}.')

command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started... Ready to go!')
    elif command == "stop":
        if not started:
            print('Car is already stopped.')
        else:
            started = False
            print('Car stopped.')
    elif command == "help":
        print('''start - to start the car
        stop - to stop the car
        quit - to exit''')
    elif command == "quit":
        print('Terminated.')
        break
    else:
        print("I don't understand that...")


