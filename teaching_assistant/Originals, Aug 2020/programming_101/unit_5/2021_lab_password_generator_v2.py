# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Apr 2021 updating
# Lab 8 Password Generator newest version
# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/password_generator.md
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import string
import random

def generate_password(desired_length=5, desired_letters=5, desired_numbers=5, desired_punctuation=5):

    password = ''

    digits = string.digits
    letters = string.ascii_letters
    punctuation = string.punctuation
    characters = digits + letters + punctuation + ' '

    print('Welcome to password generator!') 
    
    v1:
    while len(password) < desired_length:
        # randomly choose the next character, and add it to the password string
        next_character = random.choice(characters)
        password += next_character
    v2: 
    # if desired_length > desired_letters + desired_numbers + desired_punctuation:
    #     # use minimum, then add random
    # elif desired_length < desired_length + desired_numbers + desired_punctuation:
    #     # ERROR, your length is wrong, add to it...
    else:
        print(f'Your password is: \n >>>>>>>>>> {password} <<<<<<<<<< \n It has already been cleared from this program\'s memory, and you will need to write it down or copy it! Close this program, clear all relevant caches, and/or restart for added security.')
    
    # This resets the variable to a blank password. May not be the most secure solution, but it's a start.
    password = ""

user_desired_length = 30  # input('Please enter your desired password length > ')
user_desired_length = int(user_desired_length)  # TODO fix invalid input
generate_password(user_desired_length)

# main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Password Generator

# Let's generate a ten-character password using a while loop and random.choice().
# The final result will be a string of random characters all on one line.

# Example output:
# Your password: Q45pA%x9PJ

# Extra Challenge 1
# Allow the user to choose how many characters the password will be.

# Extra Challenge 2
# Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. 
# Mix everything up using list(), random.shuffle(), and ''.join().

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
