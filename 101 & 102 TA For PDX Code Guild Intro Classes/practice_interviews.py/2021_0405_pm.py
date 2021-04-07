##############################################################################
# # # # # # #
# 3 If you were given a log file, and wanted to check for the haw many entries appeared most frequently, what would you do?
# (see evernote)

##############################################################################
# 2 3D Space

##############################################################################

# 1 Make a function that takes in an integer and tells if it's a power of three.

def power_of_three(input_integer):
    '''
    Takes in an integer and return True if it is a power of 3, False otherwise.
    Examples of powers of 3: 1, 3, 9, 27, 81, etc...
    Remember that 3^1 is also written as 3**1.
    3^0 = 1 (any number to the power of 0 is = 1)
    3^1 = 3 (any number to the power of 0 is = 1)
    3^2 = 9  = 3 * 3
    3^3 = 27 = 3 * 3 * 3
    3^4 = 81
    . . .
    '''

    x = 0
    while 3 ** x <= input_integer:
        if 3**x == input_integer:
            return True
        x += 1
    return False

example_1 = 270
example_2 = 5
example_3 = 0
example_4 = 3
example_5 = 81

print(power_of_three(example_1))
print(power_of_three(example_2))
print(power_of_three(example_3))
print(power_of_three(example_4))
print(power_of_three(example_5))