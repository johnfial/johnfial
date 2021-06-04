# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# I started practicing calligraphy, and wanted a file to give me random words to
# practice, plus random letters. So that's this!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import string
import random

from english_words import english_words_set  # from https://pypi.org/project/english-words/

english_list = list(english_words_set)
# print entire word set: WARNING: 25,000 words!
# print(len(english_words_set))
# print(english_words_set)

letters_upper = list(string.ascii_uppercase)  # NOTE THE ORDER OF THE WORDS CHANGES EACH RUN...
# TODO add gui
# TODO add a word definition lookup... api is easiest way?
# print(letters_upper)

def print_words(max=5):
        
    for i in range(max):
        random_int = random.randint(0, 5)
        random_word = random.randint(0, 25000)
        
        print(f'~~~~~~~~~~~~ PRACTICE #{i+1}/{max}: ~~~~~~~~~~~~~~')
        print((english_list[random_word].upper() + ' ') * 6)
        print(letters_upper[random_int] * 20)
    print(f'~~~~~~~~~~~~ ALL DONE! ~~~~~~~~~~~~~~~~~~~')

print_words(5) # change this

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# poetry naturally flows out when practicing calligraphy, so here's some random stuff:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

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
