# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Started late at night...
# TODO SUBMITTED: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.4 Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing
# and non-letter characters.

# EXAMPLE:
# Input:      Tact Coa
# Output:     True (permutations: "taco cat", "atco cta" etc.)
# Hints: 106, 121, 134, 136


def palindrome_permutation(input_here):
    print(len(input_here))
    input_list = list(input_here)
    input_list.reverse()
    new_string = str(input_list)
    print(new_string)
    print(input_here)

example1 = 'tact coa'
palindrome_permutation(example1)

# count number of each letter in string
# optional: strip out punctiation, non-letters, etc, and lowercase() it
# 












# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 