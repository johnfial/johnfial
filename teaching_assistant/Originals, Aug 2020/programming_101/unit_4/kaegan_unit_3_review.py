'''
Unit 3 

- Operators
    - arithmetic
    - reassignment
    - comparison
    - logical (and/or/not)
- Datatype: Boolean
    - True / False
- Conditionals
    - if / elif / else
'''
# assign values to variables
# with the assignment operator =
x = 11
y = 3

# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # regular division (returns a float)
# print(x // y) # floor division ("cuts off the decimal" or "always rounds down")
# print(x ** y) # exponentiation
# print(x % y) # remainder after division


# getting both the quotient without decimals and the remainder
quotient = x // y
remainder = x % y

# print(quotient, remainder)

# ------------------------- #

x = 5
# x * 5 # won't change the value stored in x
# print(x * 5) # this will print the result, but won't save it
# print(x) #5

# set a new variable with the result
z = x * 5
# print(x) # 5
# print(z) # 25

# if the old value of x doesn't matter,
# it can be overwritten
x = x * 5 # this will overwrite x with the new value
# print(x) # 25
# print(x * 5) # 125

# Reassignment operators
# combine the assignment and arithmetic operators

x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
x //= 5 # x = x // 5
x **= 5 # x = x ** 5
x %= 5 # x = x % 5

# ------------------------- #

# Datatype: Boolean
# True / False

a = True
b = False

# Booleans in Python must be capitalized
# a = true # this tries to use 'true' as a variable name


# Truthiness / Falsiness

# Just like int(), float(), str() we have bool()
# which will convert the value to a boolean

# any datatype that has value is considered "Truthy"
# any datatype that has NO value is considered "Falsey"

# Truthy
# print(bool(1)) # True
# print(bool('Hello')) # True
# print(bool([1,2,3])) # True

# Falsey
# print(bool(0)) # False
# print(bool('')) # False
# print(bool([])) # False

# x = ""
# if x: # if statement using Truthiness
#     print('x has value')
# else:
#     print('x has no value')

# -------------------------------- #

# Comparisons

# Comparisons MUST have two sides
# print(x < ) # SyntaxError

x = 5
y = 5

# print(x == y) # equality
# print(x != y) # inequality - '!' means 'not'
# print(x < y) # less than
# print(x <= y) # less than or equal
# print(x > y) # greater than
# print(x <= y) # greater than or equal


# ------------------------ #

# Logical operators
# and / or / not
# combine the results of two or more comparisons

x = 3
y = 10

# and - Returns True if BOTH sides are True
# print(x < 10 and x == 3) # True
# print(x > 10 and x == 3) # False
# print(True and True)
# print(False and True) #  False

# or - Return True if ONE side is True
# print(x < 10 or x == 4) # True
# print(x > 10 or x == 4) # False
# print(True or False) # True
# print(False or False) # False

# not - Return the opposite
# print(x == 3) # True
# print(not x == 3) # False

# print(not True) # False
# print(not False) # True

# logical comparisons must have two sides
x = 9

# print(x < 10 and 5) # this is illegal logical comparisons need two sides
# print(x < 10 and x < 5)

# print(1 < x < 10) # check if a number is between two others
# print(x > 1 and x < 10) # same as line 151

# ----------------------- #

# Conditionals
# if / elif / else
# Run code only when a certain condition is True

x = 19

if x < 10:
    # run this code block
    # if x < 10
    message = 'x is less than 10'
elif x > 10:
    # run this code block
    # if x > 10
    message = 'x is greater than 10'
else:
    # run the code block in else
    # if all other conditions are False
    message = 'x equals 10'

# print(message)
