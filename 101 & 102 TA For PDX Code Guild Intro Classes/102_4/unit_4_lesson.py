'''
Programming 102
Unit 4
'''

'''
Modules are just Python files.

As programs grow larger, it makes sense to break them up
into separate files (modules). Modules can be imported into
other modules using keyword 'import'
'''

# import the ENTIRE contents of a module into a single 
# keyword: import
# import <MODULE_NAME>
import random # 800+ lines of code
import string # 280+ lines of code

# module attributes are available using dot notation
letters = string.ascii_uppercase
random_number = random.randint(1, 100)
random_letter = random.choice(letters)

# print(random_letter, random_number, letters)

# ---------------------------------------------------------------------------- #

# import SPECIFIC ATTRIBUTES from a module
# keywords: from / import
# from <MODULE_NAME> import <ATTRTIBUTE_1>, <ATTRIBUTE_2>, ...

from string import ascii_uppercase # imports 1 line instead of 280+
from random import randint, choice # imports only randint() and choice() from random

letters = ascii_uppercase # shorten the variable name
random_number = randint(1, 100) # don't need random. anymore
random_letter = choice(letters)

# print(random_letter, random_number, letters)

# ------------------------------------------------------------------------- #

# import SPECIFIC ATTRIBUTES from a module and CHANGE THEIR VARIABLE NAME
# keywords: from / import / as
# from <MODULE_NAME> import <ATTRIBUTE_NAME> as <VARIABLE_NAME>, ...

from string import ascii_uppercase as letters
from random import choice as r_choice, randint as r_int

random_number = r_int(1, 100)
random_letter = r_choice(letters)

# print(random_letter, random_number, letters)

# ------------------------------------------------------------------------ #