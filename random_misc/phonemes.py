# dict keys = Heb letters; dict values = list of phonemes
# Is it best to cycle through this in the order of the dictionary, or in the order of the phonemes list?
    # K: I think in the order of the phonemes list

phonemes = ['d', 'a', 'f']
dictionary = {
	"א": ["", "a", "'", "o", "i"],
    "ד": ["d"],
    "פ": ["f", "ph", "p"], 
    'abc': ['q', 'b',]
}

def word_combos(phonemes):
    combinations = []  # this will be a list of LISTS of strings
    for x in range(10):
        temp = '.' * len(phonemes)
        combinations.append(temp)
    
    # for phoneme...
    for phoneme in phonemes:
        i = 0
        temp_combination = []
    
        for phoneme_list in dictionary.values():  # this is but one way to lookup the keys by value, cycle through all the values in the dict (not the most efficient...)
            # for each value, append it to a temporary list of strings?
        #
            if phoneme in phoneme_list:
                # for 
                # temp_combination.append()
                print(phoneme, phoneme_list)

        i += 1  # increment counter to index the main letter

    print('~~~~~~~~~~')
    print(combinations)
    return combinations

# # 
# Trying to get output to look like this: 
# length of the output is == the length of the input phonemes
    # combos = 
    # 	['d', 'a.1', 'f']
    # 	['d', 'a.2', 'f']
    # 	['d', 'a.3', 'f']
    # 	['d', 'a.4', 'f']

word_combos(phonemes)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 





input_list = ['a', 'b', 'd', 'e',]
def letter_permutations(input_list):
    for letter in input_list:
        for letter2 in input_list:
            print(letter, letter2)

# letter_permutations(input_list)

'''
['ד']
['א', 'ה', 'ע', '']
['פ']

['d']
['a.1', 'a.2', 'a.3', 'a.4']
['f']

'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Dictionary Methods

# Python has a set of built-in methods that you can use on dictionaries.
# Method 	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary