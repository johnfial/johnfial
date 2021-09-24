# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Started late at night...
# TODO SUBMITTED: 
# NOTE 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.4 Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing
# and non-letter characters.

# EXAMPLE:
# Input:      Tact Coa
# Output:     True (permutations: "taco cat", "atco cta" etc.)
# Hints: 106, 121, 134, 136


from string import ascii_letters



def make_dict():
    dict = {}
    from string import ascii_letters
    # print(ascii_letters)
    
    dict[' '] = 0
    for letter in ascii_letters:
        dict[letter] = 0

    # print(dict)
# make_dict()
# 0 make dict of lettrs and ' '
letters_dict = {
    ' ': 0, 
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
    'y': 0, 'z': 0, 
    }

def solution(string, letters_dict):

    # 1 strip,     # strip leading / trailing stuff whitespace,     # .lower()
    string.lower()
    string.strip(' !@#$%^&*()}{/=\\?+|-_:1230456789')

    # 2 for each letter in string, increment dict counter
    for letter in string:
        letters_dict[letter] = (letters_dict.get(letter) + 1)
    # letters_dict[' '] = 0  # reset this, doesn't matter

    # final check: dict is allowed to have ONE odd number (or 0), the rest must be even (or 0) -> return True
    odd_characters = 0

    for (key, value) in letters_dict.items():
        if value % 2 != 0:
            print(f'KEY: {key} with value {value} triggered this!')
            odd_characters += 1
    
    if odd_characters == 0 or odd_characters == 1: return True 
    else: return False

    

example1 = 'tact coa'
# palindrome_permutation(example1)
# print(solution(example1, letters_dict))
example2 = 'joh nonh jqoo'
print(solution(example2, letters_dict))
# print(solution(example1, letters_dict))
# print(solution(example1, letters_dict))











# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #

def palindrome_permutation(input):
    
    # TODO 1 strip casing, strip whitespace
    # input = ''  # TODO remove this
    input = input.strip().strip('!@#$%^&*()}{[]/=\\-_|+ ?').lower()
    illegal_characters = '!@#$%^&*()}{[]/=\\-_|+ ?'  # TODO add rest...
    input_list = list(input)
    # print(input_list)
    for character in input_list:
        if character in illegal_characters:
            input_list.remove(character)
    # print(input_list)
    

    # TODO 2 if same = .reverse return True
    test_list = input_list.copy()
    test_list.reverse()
    print(test_list)
    
    if input_list == test_list:
        print(f'palindrome!!!')
        return True
    
    
    return False



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 