# Lab 8 Password Generator
# https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab08-password_generator.md
# advanced opt. 2, ask the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().

import string
import random

# import ascii characters
digits = string.digits
letters = string.ascii_letters
punctuation = string.punctuation
# almost all possible characters here:
characters = digits + letters + punctuation

# ask the user for the password length, then convert that string to an integer
user_length_str = input('Note that this version does not include spaces at the present. Please type desired password length, in digits\n>: ') 
user_length_int =  int(user_length_str) # LEARNED, NOTE: must assign new variable, couldn't simply run the int() and leave the line otherwise clean
# advanced: fix so user must enter digits, and, if not, error code appears

#blank pw
password = ''

# run the loop
while len(password) < user_length_int:

# randomly choose the next character, and add it io the password string
    next_character = random.choice(characters)
    password += next_character

# print pw!
else:
    print(f'Your password is: \n{password}')