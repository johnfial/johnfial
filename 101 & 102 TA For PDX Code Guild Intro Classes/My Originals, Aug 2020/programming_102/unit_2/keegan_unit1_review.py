'''
Unit 1 Review
'''

'''
Anatomy of an error message

File <FILENAME>.py, line number
    troublesome code (approximately)
                                   ^
ErrorType: Specific error message
'''

# handling errors
# keywords: try / except / else / finally



# dividend = 10

# divisor = input('Please enter the divisor: ')


# divisor = float(divisor) # program crashes if divisor cannot be converted

# try:
#     divisor = float(divisor)
# except ValueError:
#     # if there is a ValueError, run this code block
#     print(f'{divisor} cannot be converted to float!')
# else:
#     # if no error occured, run this block
#     quotient = dividend / divisor
#     print(f'{dividend} / {divisor} = {quotient}')
# finally:
#     # run this no matter what
#     print('Thanks for playing!')

# ----------------------------------- #

# while True: # while True will run until broken
#     number = input('Enter a decimal number: ')

#     try:
#         number = float(number)
#     except ValueError:
#         print(f'{number} is not a valid number')
#     else:
#         print(f'{number} converted successfully')
#         break # end the loop if a valid number is entered
#     finally:
#         print('Thanks!')

# print(10 / number) # by the time the user gets here, they're guaranteed to have entered a valid number

# --------------------------------------- #

# Raising an error
# color = input("Please enter a color: ")

# try:
#     if color == 'green':
#         raise ValueError(f"I don't like the color {color}")
# except ValueError as error: 
    # the message for the ValueError will be 
    # stored in the variable error because of the keyword 'as'
#     print(error)
# else:
#     print(f'I like the color {color}')
