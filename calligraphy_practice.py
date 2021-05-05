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
        integer = random.randint(0, 25)
        
        print((english_list[integer].upper() + ' ') * 6)
        print(letters_upper[integer] * 20)


print_words(4)

# print(len(english_words_set)) # 25,000 words!

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Random poems:
# One minute to go, one life to share
# The road hard to walk is so often bare

# The farmer's ocean breeze wanes with a sneeze
# An onion's pungent trail bites the eyes like hail
# Green nails growing sharp
# wraps over the ancient bark

# # # # #

# I had a dream, and not of ice cream

# On an island, high tide, 
# Wanted to swim, my friend, lots of pride
# Girls there, too, avoiding our chase
# I said "swim later on, no need for now's haste!"

# But the dream changed its scene

# You were there too, son, 
# Amid feelings all over,
# That's the power they hold
# Help break free of our molds.

# # # # #
