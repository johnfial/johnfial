# Lab 8 Password Generator
# https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab08-password_generator.md
# advanced opt. 2, ask the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().

# 2021_03_05

import string
import random

def generate_password(length=5):

    password = ''

    digits = string.digits
    letters = string.ascii_letters
    punctuation = string.punctuation
    characters = digits + letters + punctuation

    # TODO ADD SPACES

    # ask the user for the password length, then convert that string to an integer
    print('Welcome to password generator! (Note that this version does not include spaces at the present.)') 
    
    while len(password) < length:

        # randomly choose the next character, and add it io the password string
        next_character = random.choice(characters)
        password += next_character
    
    else:
        print(f'Your password: \n >>>>>>>>>> {password} <<<<<<<<<< \n It has already been cleared from program memory, and you will need to write it down or copy it! Close this program, clear all relevant caches, and/or restart for added security.')
    
    password = ""

generate_password(30)