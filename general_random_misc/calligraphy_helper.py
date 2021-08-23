# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# I started practicing calligraphy, and wanted a file to give me random words to
# practice, plus random letters. So that's this!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import string
import random
from english_words import english_words_set  # from https://pypi.org/project/english-words/

import requests # for the word lookup below...

english_list = list(english_words_set)
# print entire word set: WARNING: 25,000 words!
# print(len(english_words_set))
# print(english_words_set)

letters_upper = list(string.ascii_uppercase)  # NOTE THE ORDER OF THE WORDS CHANGES EACH RUN...
# TODO add gui
# TODO add a word definition lookup... api is easiest way?
# print(letters_upper)

new_string = ''

def print_words(max=5):
        
    for i in range(max):
        random_int = random.randint(0, 5)
        random_word = random.randint(0, 25000)
        
        print(f'~~~~~~~~~~~~ PRACTICE #{i+1}/{max}: ~~~~~~~~~~~~~~')
        word = english_list[random_word].upper()
        print((word + ' ') * 6)
        print(letters_upper[random_int] * 20)
    print(f'~~~~~~~~~~~~ ALL DONE! ~~~~~~~~~~~~~~~~~~~')
    return word

# print_words(1) # change this
word_to_lookup = print_words(1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
example = [
    {'word': 'dice',
    'phonetics': [{'text': '/daɪs/', 'audio': 'https://lex-audio.useremarkable.com/mp3/dice_us_1.mp3'}], 
    'meanings': [
        {'partOfSpeech': 'verb',
        'definitions': [
            {'definition': 'Play or gamble with dice.',
            'synonyms': ['dice with', 'court', 'risk', 'not be afraid of', 'treat frivolously', 'make light of'],
            'example': 'prohibitions on all dancing and dicing'},
            {'definition': 'Cut (food or other matter) into small cubes.',
            'synonyms': ['chop', 'cut up', 'slice', 'dice', 'cube', 'mince'], 'example': 'dice the peppers'}]},
            {'partOfSpeech': 'noun', 'definitions': [{'definition': 'A small cube with each side having a different number of spots on it, ranging from one to six, thrown and used in gambling and other games involving chance.', 'example': "Gauss's guess was based on throwing a dice with one side marked ‘prime’ and the others all blank."}]}]}]
# print(example)
# print(type(example))
# print(example[0]['meanings'])

response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word_to_lookup}/') # , headers={'Accept': 'application/json'})
print(word_to_lookup) # DICE
# print(response) # <Response [200]>
# print(response.json()) # [{'word': 'dice', 'phonetics': [{'text': '/daɪs/', 'audio': 'https://lex-audio.useremarkable.com/mp3/dice_us_1.mp3'}], 'meanings': [{'partOfSpeech': 'verb', 'definitions': [{'definition': 'Play or gamble with dice.', 'synonyms': ['dice with', 'court', 'risk', 'not be afraid of', 'treat frivolously', 'make light of'], 'example': 'prohibitions on all dancing and dicing'}, {'definition': 'Cut (food or other matter) into small cubes.', 'synonyms': ['chop', 'cut up', 'slice', 'dice', 'cube', 'mince'], 'example': 'dice the peppers'}]}, {'partOfSpeech': 'noun', 'definitions': [{'definition': 'A small cube with each side having a different number of spots on it, ranging from one to six, thrown and used in gambling and other games involving chance.', 'example': "Gauss's guess was based on throwing a dice with one side marked ‘prime’ and the others all blank."}]}]}]
response_json_dict = response.json()
print(response_json_dict[0]['meanings'])













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
