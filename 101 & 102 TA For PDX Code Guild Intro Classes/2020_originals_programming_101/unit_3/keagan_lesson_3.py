'''
Unit 3

- Operators
    - Arithmetic
    - Reassignment
    - Comparison
    - Logical
- Math module
- Datatype: Booleans
    - True/False
- Conditionals
'''

# Operators
# Characters and keywords that allow actions between data

# Arithmetic Operators (math)
x = 10
y = 6

# print(x + y) # 16 - addition
# print(x - y) # 4 - subtraction
# print(x * y) # 60 - multiplication
# print(x / y) # 1.6666666666666667 - Regular division
# print(x // y) # 1 - Floor division (cuts off the decimal without rounding)
# print(x ** y) # 1000000 - Exponentiation
# print(x % y) # 4 - Modulus - Remainder after division

# Reassignment Operators
x = 5 # assigning 5 to x
# print(x) # 5

x + 10 # this will not change the value of x
# print(x) # 5
# print(x + 10) # 15 - this still won't change x

# overwrite x with the result of x + 10
x = x + 10

x += 10 # x = x + 10
x -= 5 # x = x - 5
x *= 2 # x = x * 2
x /= 4 # x = x / 4
x //= 6 # x = x // 6
x **= 15 # x = x ** 15
x %= 2 # x = x % 2

# ------------------------------ #

# modulus is a wrap around operation
military_time = 18
twelve_hour_time = military_time % 12

# print(twelve_hour_time) # 6


# modulus is great for finding even/odd
# print(5437 % 2) # 1 - odd
# print(9832 % 2) # 0 - even


# ------------------------- #

# pretend this is the top of a file
import math # import the math module

interested = 20
drop_outs = 6
attendees = interested - drop_outs

# number of people per car
car_max = 4
# total cars needed, rounded up with math.ceil() (ceil = ceiling)
cars_needed = math.ceil(attendees / car_max)

percent = (attendees / interested) * 100

message = f'''
There were {interested} people interested in hiking.
{drop_outs} dropped out. Now there are {attendees} people going hiking.
Attendance: {percent}%
We will need {cars_needed} cars.'''

# print(message)

# ---------------- #
# Datatype: Boolean
# True / False

a = True
b = False

# print(a, b) # True False
# print(type(a), type(b)) # <class 'bool'> <class 'bool'>

# ------------------------ #

# Comparison Operators

x = 5
y = 5


# print(x == y) # True - equality
# print(x != y) # False - inequality - '!' means 'not'
# print(x < y) # False - less than
# print(x <= y) # True - less than or equal to
# print(x > y) # False - greater than
# print(x >= y) # True - greater than or equal to

# color = input('Enter a color: ')
# print('color' == 'blue')

# print('dog' > 'cat') # this works but it's comparing ASCII letter values, so be careful

# ----------------------- #

# Logical Operators
# and / or / not
# used to combine more than one comparison
# will always result in either True or False

# and - Returns True if BOTH sides are True
# print(1 == 1 and 2 == 2) # True
# print(1 == 1 and 3 == 5) # False
# print(True and True) # True
# print(True and False) # False

# or - Return True if ONE side is True
# print(1 == 1 or 2 == 2) # True
# print(1 == 1 or 3 == 5) # True
# print(True or True) # True
# print(True or False) # True
# print(False or False) # False

# not - Returns the reverse of the comparison
# print(1 == 1) # True
# print(not 1 == 1) # False
# print(not True) # False
# print(not False) # True

# many comparisons can happen at once
# print(((1==1) and (5<10)) or ((100 / 2 == 50) or (1 == 2))) # True
# print(not (((1==1) and (5<10)) or ((100 / 2 == 50) or (1 == 2)))) # False

# ------------------------------- #

# Conditional statements
# if / elif / else

# use conditionals to run code based on data values

# general structure
# if condition_a == True:
    # run this code block
    # a code block is all code
    # at a particular indentation level
# elif condition_b == True:
    # run the code
    # in THIS code block
# else:
    # run if condition_a
    # and condition_b are False

# as soon as one condition is True,
# all others are skipped

x = 10
y = 10

message = 'DEFAULT MESSAGE'

if x < y:
    message = 'x is less than y'
elif x > y:
    message = 'x is greater than y'
else: # else doesn't need a condition
    # else catches every other case
    message = 'x equals y'


# print(message)


message = 'NONE'

x = 7
y = 15

# comparisons can be combined
# if x < y and x == 5:
#     message = 'x is less than y and x equals 5'
# elif x < y and x > 10:
#     message = 'x is less than y and x is greater than 10'

# print(message)


# nested if / elif
if x < y:
    message = 'x is less than y. '
    
    if x == 5:
        message += 'x equals 5'
    elif x == 7:
        message += 'x equals 7'

# print(message)

# ----------------------------- #

import random # imports should be done at the top

# generate a random number between 1 and 100
random_number = random.randint(1, 100)

if random_number < 50:
    message = f'{random_number} is less than 50'
elif random_number > 50:
    message = f'{random_number} is greater than 50'
else:
    message = 'The random number is 50!'

# print(message)