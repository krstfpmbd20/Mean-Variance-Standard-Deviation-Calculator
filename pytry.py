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

# command = ""
# started = False
# while True:
#     command = input('> ').lower()
#     if command == "start":
#         if started:
#             print('Car is already started.')
#         else:
#             started = True
#             print('Car started... Ready to go!')
#     elif command == "stop":
#         if not started:
#             print('Car is already stopped.')
#         else:
#             started = False
#             print('Car stopped.')
#     elif command == "help":
#         print('''start - to start the car
#         stop - to stop the car
#         quit - to exit''')
#     elif command == "quit":
#         print('Terminated.')
#         break
#     else:
#         print("I don't understand that...")

# def multiplication(x, y):
#     print("Answer is:", x * y)

# def addition(x, y):
#     print("Answer is:", x + y)

# def subtraction(x, y):
#     print("Answer is:", x - y)

# def division(x, y):
#     print("Answer is:", x / y)

# command = ""
# while True:
#     command = input('Enter a command: ').lower()
#     if command in ["add", "subtract", "multiply", "divide", "help"]:
#         if command == "help":
#             print('''add - to add two numbers
# subtract - to subtract two numbers
# multiply - to multiply two numbers
# divide - to divide two numbers
# quit - to exit''')
#         else:
#             x = int(input('Enter a number: '))
#             y = int(input('Enter another number: '))
#             if command == "add":
#                 addition(x, y)
#             elif command == "subtract":
#                 subtraction(x, y)
#             elif command == "multiply":
#                 multiplication(x, y)
#             elif command == "divide":
#                 division(x, y)
#     elif command == "quit":
#         print('Terminated.')
#         break
#     else:
#         print('Invalid command. Please enter "add", "subtract", "multiply", "divide", "help", or "quit".')

# def say_hi(string):
#     print(string)
#     print('Hi!')
#     print(string)
# say_hi('Hello, World!')

# password = input('Enter a password: ')
# password_length = len(password)
# conditions = []
# if password_length < 5:
#     conditions.append('Password must be at least 5 characters long.')
# if password.islower():
#     conditions.append('Password must contain at least one uppercase letter.')
# if password.isalpha():
#     conditions.append('Password must contain at least one number.')
# if not any(char in '!@#$%^&*()_+' for char in password):
#     conditions.append('Password must contain at least one special character (!@#$%^&*()_+).')
# if conditions:
#     for condition in conditions:
#         print(condition)
# else:
#     print('Password looks good.')

# sum = lambda x, y: x + y
# print(sum(5, 10)) 
  
# from functools import reduce
# list_store = [1, 2, 3, 4, 5]
# filtered = list(filter(lambda x: x % 2 == 0, list_store))
# print(filtered)
# reduced = reduce(lambda x, y: x + y, list_store)
# print(reduced)

# grades = [88, 75, 96, 55, 83]
# for grade in grades:
#     if grade >= 83:
#         print('A')
#     else:
#         print('F')

# students = set(['John', 'Mary', 'Steve', 'Anna', 'Lee'])
# students2 = set(['John', 'Mary', 'Lee'])

# print(students2.difference(students))

# lst = [1, 'two', 3, 'four', 5]
# def remove_strings(lst):
#     return [i for i in lst if not isinstance(i, str)]
# lst = remove_strings(lst)
# print(lst)

# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# print(np.dot(a, b))

# numbers = range(10)
# new_dict = {}
# for i in numbers:
#     if i % 2 == 0:
#         new_dict[i] = i ** 2
# {n ** 2 for n in numbers if n % 2 == 0}
# print(new_dict)

# lower_case = ['total', 'world', 'hello', 'goodbye_world']
# upper_case = [word.upper() for word in lower_case]
# print(upper_case)

# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# result = a * b
# result_str = ', '.join(map(str, result))
# print(result_str)

# import numpy as np
# np.array([1, 2, 3, 4])
# print(type(np.array([1, 2, 3, 4])))
# np.zeros(10, dtype=int)
# print(np.zeros(10, dtype=int))
# np.ones(10, dtype=int)
# print(np.ones(10, dtype=int))   
# np.random.randint(1, 10, 10)
# print(np.random.randint(1, 10, 10))
# np.random.normal(0, 1, (3, 4))
# print(np.random.normal(0, 1, (3, 4)))

# np.array = []
# for i in range(1, 11):
#     np.array.append(i)
# print(np.array)

# import numpy as np
# random = np.random.randint(1, 10, 10)
# print('Random Set: ', random)
# sorted_random = np.sort(random)
# print('Sorted Set: ', sorted_random)

# import numpy as np 
# random = np.random.randint(1, 10, 9) 
# print(random)  
# reshape = random.reshape(3, 3)
# print(reshape)
# reshape.sort(axis=1)
# print(reshape)

# import numpy as np
# v = np.arange(1, 11, 1)
# print(v)
# print(v[v < 3])

# set = []
# for i in range(1, 11):
#     set.append(i)
# print(set)

# word_list = ['hello', 'world', 'goodbye', 'what']
# remove_first_and_last = [word[1:-1] for word in word_list]
# print(remove_first_and_last)

# def FizzBuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# input = int(input())
# FizzBuzz(input)

# avg = []
# input = list(map(int, input().split()))
# avg.append(sum(input) / len(input))
# print(avg)

# def number_squared(n):
#     return n ** 2

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0, n):
#         print(number_squared(i))

# nums = [1, 2, 3, 4, 5]
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)

# import numpy as np
# import pandas as pd
# import seaborn as sns

# df = pd.read_csv('advertising.csv') 
# df = df.round() #rounds off the values in the dataframe to the nearest whole number.
# print(df.head())
# print(df.tail())
# print(df.info)
# print(df.describe)    
# print(df.isnull().values.any()) #returns true or false, false if there are no missing values.
# print(df.isnull()) #returns a dataframe of boolean values, true if there is a missing value, false if there is no missing value.
# print(df.isnull().sum()) #returns the number of missing values in each column. 

# import pandas as pd
# import seaborn as sns 

# df = sns.load_dataset('titanic')
# print(df[['sex', 'alone', 'survived']].head())
# print(df.index)

# import pandas as pd 
# import seaborn as sns
# import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
# df = pd.read_csv('titanic.csv')
# df.head()

# # available_datasets = sns.get_dataset_names()
# # print(available_datasets)

# # Plot histogram for the 'age' column
# plt.figure(figsize=(10, 6))
# n, bins, patches = plt.hist(df["age"], bins=20, edgecolor='black', alpha=0.7)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Count')

# # Annotate the bars with the count values
# for i in range(len(patches)):
#     plt.text(patches[i].get_x() + patches[i].get_width() / 2, patches[i].get_height(), str(int(n[i])), ha='center', va='bottom')

# plt.show()

# plt.boxplot(df['fare'])
# plt.show()
