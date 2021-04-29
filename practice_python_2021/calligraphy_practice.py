# goal: make a random string of letters, numbers, or a random word list to practice calligraphy

import string
import random

# below @ https://pypi.org/project/english-words/ :
from english_words import english_words_set
english_list = list(english_words_set)

letters_upper = list(string.ascii_uppercase)
print(letters_upper)

def print_words(max=5):
        
    for i in range(max):
        integer = random.randint(0, 26)
        
        print(english_list[integer].upper())
        print(letters_upper[integer] * 5)


print_words(2)

# print(len(english_words_set)) # 25,000 words!
