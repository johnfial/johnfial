'''
Unit 4 - Modules

# Also known as: Python files

Once our programs get a little larger,
it helps to break them up into smaller pieces
or multiple files.

These files are modules
Modules can be imported into each other
'''

import random
import string
import math
import sys

# import module_name 
# import the entire contents of a module

# module_name.attribute_name
# module attributes are accessed with a dot
random.randint(1,100)
all_letters = string.ascii_letters
random.choice(all_letters)

# ----------------- #

# import SPECIFIC attributes from a module
# from module_name import attribute_name

from random import choice, randint
from string import ascii_letters

# since the attributes are imported directly,
# the module_name. isn't necessary

random_letter = choice(ascii_letters)
random_number = randint(1,100)
# print(random_letter, random_number)

# ------------- #

# import SPECIFIC attribute with a CUSTOM variable name
# from module_name import attribute_name as variable_name
from string import ascii_letters as all_letters

# this can be done, but the variable names chc
# and rndnt are less readable than choice and randint (opinion)
from random import choice as chc 
from random import randint as rndnt

random_letter = chc(all_letters)
random_number = rndnt(1,100)
# print(random_letter, random_number)

# --------------------- #

# combining complex imports

'''
from module_name import (
    attribute_name as variable_name,
    attribute_name as variable_name,
    attribute_name as variable_name,
)
'''

from random import (
    choice as chc,
    randint as rndnt
)

from string import (
    ascii_lowercase as lowercase,
    ascii_uppercase as uppercase
)
