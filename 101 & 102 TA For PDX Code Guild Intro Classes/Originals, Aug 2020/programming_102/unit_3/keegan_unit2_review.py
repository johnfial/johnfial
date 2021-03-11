# remember function(parameter, parameter2=DEFAULT_VALUE!)

import random
import doctest # for testing in docstrings
'''
Unit 2 Review

# Read, Evaluate, Print, Loop (REPL)
# functions
'''

# REPL

'''
again = 'yes'
while again == 'yes':
    # loop some code

    # ask the user if they want to play again, lowercase their answer
    again = input('Do you want to play again? yes/no: ').lower()
'''

'''
# using True instead of a comparison in the while condition
while True:
    # loop some code

    again = input('Do you want to play again? yes/no: ').lower().replace(' ', '')

    if again == 'yes':
        print("Okay let's play again")
        continue
    elif again == 'no':
        print('Goodbye')
        break
'''

'''
while True:
    number = int(input('Please enter a number between 50 and 100 or done to exit: '))

    # break the loop if the user enters done
    if number == 'done':
        break

    # nested REPL to ensure proper data entry
    while number < 50 or number > 100:
        print('Out of range!')
        number = int(input('Please enter a number between 50 and 100: '))

    print(f'{number} is between 50 and 100')
'''

# --------------------- #

'''
# blank list to store numbers
numbers = []

# REPL with a for loop
for i in range(5):
    number = float(input('Enter a number: '))

    # add the number to the list
    numbers.append(number)

    print(f'{number} added to the list')

print(numbers)
'''

# ------------------- #

# Functions

# named blocks of code that run only when called
# functions can take in data and return data after it's manipulated
# Typically designed for one task
# once defined they can be called as many times as needed
'''
# keyword def will define a function
def function_name(parameter1, parameter2=default_value):
    # this block will run 
    # when the function is called

    # parameters are empty variables waiting for data
    # unless they have default values

    # perform operations using the parameters

    return manipulated_parameters

# call the function
function_name(argument1) # this will use parameter2's default value
function_name(argument1, argument2) # this will overwrite parameter2's default
'''

def add(a, b):
    result = a + b
    return result # this variable result only exists inside the function

# print(add(1,2))
result = add(5,6) 

# print(result)


# parameters can have default values
def add_to_list(colors, color='blue'):
    colors.append(color)
    return colors

colors = []
add_to_list(colors) # add the default value 'blue' to the list
# print(add_to_list(colors, 'purple')) # overwrite the default value for color

# catch the return value in a variable called colors
colors = add_to_list(colors, 'red')
# print(colors)


# --------------- #
'''
def absolute_value(num):
    # if the number is negative, flip the signQ
    if num < 0:
        num *= -1

    return num


# print(absolute_value(-14)) # 14
# print(absolute_value(99))
numbers = []

# create a list of 10 numbers between -100 and 100
for i in range(10):
    number = random.randint(-100, 100)
    numbers.append(number)

positives = []
for number in numbers:
    # get the absolute value of the number and add it to the list
    positives.append(absolute_value(number))

print(numbers)
print(positives)
'''

def multiply(a,b):
    '''
    return the sum of two numbers a and b
    
    # write tests into a docstring
    >>> multiply(5,5)
    23
    
    '''
    return a * b

# print(multiply(5, 6))


# doctest.testmod(name='multiply_test', verbose=True) # call the doctest