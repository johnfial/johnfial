
# number = input('give me a number please! : ')
# print(type(number))
# number = float(number)

# print(type(number))
# print(number + 60)

print('0*' * 10)

for x in range(5):
    message = f'x: {x}'
    print(message)

'''
Programming 101 Review
'''

'''Unit 1'''

# Comments

# single line comments are intiated with a pound sign #

'''
Multi-line
comments use triple
quotes
'''

"""
Multi-line with 
double quotes
"""

'''
Comments

organize code
explain code
exclude code
'''

# ---------------- #

# print(data) # built in function to display data to terminal

# print('hello') # hello

# print('hello', 1, 3.14, [1,2,3]) # multiple values can be passed

# -------------------- #

# Datatype: String - 'str'

# print(type('hello')) # <class 'str'>

# strings are textual data. Sequences of characters
# surrounded by quotes

'hello'
'12345'
"   h e l l o "
'3.1415'
'$%^&*()'
'''
multi
line
string
'''

# print('''multi
# line
# string''')

# ----------------- # 

# String concatenation - adding (smooshing) strings together

# print('x' + '*' + 'y' + '=' + 'z') # x*y=z
# print('hello' + ' ' + 'world!') # hello world

# print('1+1=' + 2) # Can only concatenate strings to other strings. TypeError: can only concatenate str (not "int") to str

# print('a' - 'b') # Cannot subtract strings - TypeError: unsupported operand type(s) for -: 'str' and 'str' 
# print('5' * 5) # 55555
# print('5' * '5') # this won't work: TypeError: can't multiply sequence by non-int of type 'str'

# print a border around a string
# print('-*-' * 4)
# print('hello world!')
# print('-*-' * 4)

# ----------------------- #

# Methods - functions that manipulate the data
# to which they are attached with a dot .

# data.method_name()

# <class 'str'>
# print('hello'.upper()) # HELLO
# print('HELLO'.lower()) # hello
# print("i DoN'T lIkE SPAM".capitalize()) # I don't like spam

# ---------------------- #

# Escape characters

# allow special characters to be placed within a string
# allow 'illegal' characters to placed within a string

# escape characters are denoted by a backslash \

# print quotes in a string
# using mismatched quotes
# print("My name is 'Keegan'")
# print('My name is "Keegan"')

# using escape characters
# print('My name is \'Keegan\'')
# print("My name is \"Keegan\"")

# print('hello\n\nworld') # newline - \n
# print('hello\tworld') # horizontal tab - \t

'''Unit 2'''

# variables

# named pieces of data
# variable_name = some_value
number = 99
name = 'Gill Bates'

# print(number) # 99
# print(name) # Gill Bates

# variable become the datatype they store
# print(type(number)) # <class 'int'>
# print(type(name)) # <class 'str'>

'''
Variable names

- must start with a letter or underscore
- cannot start with a number
- can only contain alpha-numeric characters and underscores
    - A-z, 0-9, and _
- are case sensitive
    - age, Age, and AGE are different variables
'''

# best practice with variable names
# is to use underscore-separated lowercase words

variable_name = 'proper variable name'

# class SomeClassName: # TitleCase is used for classes
# PI = 3.14 # all caps are generally used for global variables

name = 'Keegan'
city = 'Portland'

# print('Hello ' + name + '! Today in ' + city + ' it is smokey')

# print('Next year: ' + (2020 + 1)) # Error
# print('Next year: ' + str(2020 + 1)) # Next year: 2021

# ------------------------- #

# f-string - format Python expressions into strings

# f-strings are denoted with an f in front of the opening quote
# expressions are placed within the string using curly brackets {}

message = f'Hello {name}! Today in {city} it is smokey.'
# print(message) # Hello Keegan! Today in Portland it is smokey.

message = f'Next year: {2020 + 1}'
# print(message) # Next year: 2021 - integers don't have to be converted to str

# -------------------------------- #

# input(prompt_message) - display the prompt message
# and wait for the user to hit enter
# name = input('Enter your name: ') # store the user's response in a variable 'name'
# print(name)

# REMEMBER! input() ALWAYS returns a string!
# number = input('Enter a number: ')
# print(type(number)) # <class 'str'>

# str(data) # convert data to a string
# int(data) # convert data to an integer

# number = int(number) # convert input to int
# print(type(number)) # <class 'int'>

# number = float(number) # convert input to float
# print(type(number)) # <class 'float'>

# ------------------------------- #

'''
Unit 3
'''

# Operators

# Arithmetic operators
x = 5
y = 6

# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # standard division - returns a float - 0.8333333333333334
# print(x // y) # floor division - always rounds down - 0
# print(x ** y) # exponentiation
# print(x % y) # remainder of division

# print(10 % 4) # 2
# print(9 % 2) # 1

# Reassignment Operators

x = 5
x + 10 # this won't change x
# print(x) # 5
# print(x + 10) # 15 - still doesn't change x

# z = x + 10 # store the result in a different variable
x = x + 10 # this will change x to 15
# print(x) # 15

x += 10 # x = x + 10
x -= 10 # x = x - 10
x *= 10 # x = x * 10
x /= 10 # x = x / 10
x **= 10 # x = x ** 10
x //= 10 # x = x // 10
x %= 10 # x = x % 10

# ---------------------- #

# Datatype: Boolean - True / False
a = True
b = False

# Booleans in Python are Capitalized
# a = true # invalid - looks for a variable called true
# b = false # invalid - looks for a variable called false

# ---------------------- #

# Comparison operators - return booleans
x = 5
y = 5

# print(x == y) # True - equality
# print(x != y) # False - inequality - '!' mean 'not'
# print(x < y) # False - less than
# print(x <= y) # True - less than or equal to
# print(x > y) # False - greater than
# print(x >= y) # True - greater than or equal to

# strings can be compared to strings
word1 = 'cat'
word2 = 'cat'
# print(word1 == word2) # True

# cannot compare strings to integers
# print('cat' < 2) # ERROR! - TypeError: '<' not supported between instances of 'str' and 'int'
# -------------------------- #

# Logical Operators
# keywords: and / or / not

# and - returns True if BOTH sides are True
# print(True and True) # True
# print(True and False) # False
# print(x < y and x == 5) # False
# print(x == 5 and y == 5) # True

# or - return True if ONE side is True
# print(True or False) # True
# print(False or False) # False
# print(x == 2 or y == 5) # True
# print(x == 1 or y == 4) # False

# not - return the opposite of the result
# print(x == 5) # True
# print(not x == 5) # False

# ------------------------- #

# Conditional statements
# keywords: if / elif / else

# if some_condition == True:
#     # run this
#     # code block
# elif some_other_condition == True:
#     # run this
#     # code block
# else:
#     # run this if all others are False

x = 10
y = 10

if x < y:
    message = 'x is less than y'
elif x > y:
    message = 'x is greater than y'
else: # else doesn't require a condition
    message = 'x equals y'

# print(message)

'''
Unit 4
'''

# Datatype: List

# lists are 'ordered' and 'changeable' sequences
# of items. Items are separated by commas and lists
# are surrounded by square brackets []

blank_list = []
# print(type(blank_list)) # <class 'list'>

numbers = [1, 2, 3] # list of numbers
colors = ['red', 'green', 'blue'] # list of strings


# list items can be ANY datatype
jumble = [1.1, 6, 'green', [1, 2, 3], True]
# print(jumble) # [1.1, 6, 'green', [1, 2, 3], True]

# since lists are 'ordered' we can reference
# their items using the item's position in the list
# an item's position is called its index

# list indices start at 0
# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue
# print(colors[3]) # index too far right - IndexError: list index out of range

# negative indices can be used
# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red
# print(colors[-4]) # index too far left - IndexError: list index out of range

# change a value at an index:
colors[1] = 'burgundy'
# print(colors) # ['red', 'burgundy', 'blue']


# add items to a list:

# add lists together
colors2 = ['yellow', 'turquoise']
colors += colors2 # colors = colors + colors2
# print(colors) #['red', 'burgundy', 'blue', 'yellow', 'turquoise']

# add an item to the end of a list
colors.append('mauve')
# print(colors) # ['red', 'burgundy', 'blue', 'yellow', 'turquoise', 'mauve'] 

# add an item at a given index
colors.insert(2, 'brown')
# print(colors) # ['red', 'burgundy', 'brown', 'blue', 'yellow', 'turquoise', 'mauve']

# remove items from a list:

# keyword: del
del colors[4] # remove yellow
# print(colors) # ['red', 'burgundy', 'brown', 'blue', 'turquoise', 'mauve']

# remove the first occurance of an item
colors.remove('blue')
# print(colors) # ['red', 'burgundy', 'brown', 'turquoise', 'mauve']

# must remove items that exist
# colors.remove('pink') # ValueError: list.remove(x): x not in list

# remove an item at a given index
colors.pop(2) # remove the item at index 2
# print(colors) # ['red', 'burgundy', 'turquoise', 'mauve']

colors.sort()# sort a list in place
colors.sort(reverse=True) # sorts reversed
# print(colors)

# colors = colors.sort() # .sort() doesn't RETURN a sorted list
# print(colors) # None
# print(colors[0])  # TypeError: 'NoneType' object is not subscriptable

sorted_colors = sorted(colors) # sorted() returns a sorted list
sorted_colors = sorted(colors, reverse=True) # sort descending
# print(sorted_colors) # ['burgundy', 'mauve', 'red', 'turquoise']

# ---------------------------------- #

# for loops

# for item in sequence
for color in colors:
    message = f'current color: {color}'
    # print(message)

for number in [1, 2, 3, 4, 5]:
    message = f'number: {number}, number squared: {number ** 2}'
    # print(message)

# for x in range()

# range(stop)
for x in range(5):
    message = f'x: {x}'
    # print(message)

# range(start, stop)
for x in range(5, 10):
    message = f'x: {x}'
    # print(message)

# range(start, stop, step)
for x in range(0, 10, 2):
    message = f'x: {x}'
    # print(message)

# count down from 10 by 1
for x in range(10, -1, -1):
    message = f'x: {x}'
    # print(message)

# loop controls
# keywords: continue, break

for x in range(10):
    if x == 5:
        # print('skipping 5...')
        continue # go to the top of the loop

    if x == 8:
        # print('goodbye')
        break # end the loop

    # print(x)

# --------------------- #

'''Unit 5'''
# while loop

# while some_condition == True:
#     # run this 
#     # code block

i = 0
while i < 10:
    # print(i)

    i += 1 # change i so that the loop will end


i = 0
while i < 10:
    # print(i)

    if i == 5:
        # print('the loop was broken')
        break

    i += 1
else:
    # this code block will run 
    # only if the loop ends
    # 'naturally'

    # loops end naturally when their condition becomes False
    message = 'The loop ended naturally'
    # print(message)


for color in colors:
    # print(color)
    if color =='red':
        break
else:
    message = 'all colors printed'
    # print(message)