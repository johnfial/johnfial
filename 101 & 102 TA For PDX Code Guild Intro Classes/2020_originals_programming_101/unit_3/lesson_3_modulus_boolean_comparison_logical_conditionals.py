print('test')

x = 5
y = 3
print(x * y) # multiplication
print(x / y)
print(x // y) # cuts off the decimal without rounding
# ADVANCED, ROUND THIS
print(x**y)
print(x%y) # remainder , after division, rounded # MODULUS # wrap around operation

military_time = 18
twelve_hour_time = military_time % 12 #wraps around
print(twelve_hour_time)
# ADVANCED PM OR AM
# modulus great for finding even and odd % 2 if 1 - odd, if 0, even

# TOP TOP TOP TOP TOP TOPP
import math

irregular_number = 33.24
new = math.ceil(irregular_number)
print(new)

# reassign values...
x = 5
x = x + 10

# SHORTCUT TO REASSIGN THINGYS
x += 10 # same as x  = x + 10


# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
print('-----------------------------')
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 

# BOOLEANS ! 
# true / false

a = True
b = False
print(type(a))

# CHECX EQUALITY
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)

print('-----------------------------')

print(1 == 1 and 2 == 3)
print(True and True)


# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
print('-----------------------------')
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 
# ----------------------------- # 

# CONDITIONAL STATEMENTS
# if / elif / else
# run code based on data values

#if condition_a == True : 

    # do this code here, all code at an indentation level
    # all these comments are in one code block
#elif condition_b == True: # as many elifs as I want
    # run code here
#else: 
    # run if the above fail or are false


x = 10
y = 11
message = 'default'
if x < y:
    message = 'x is indeed less than y'
elif x > y:
    message = 'x is greater than y'
else:
    print('you broke it')

print(message)