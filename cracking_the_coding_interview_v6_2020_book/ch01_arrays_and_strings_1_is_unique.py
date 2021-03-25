# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Working 2021 Mar 25...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.1 
# Is Unique
# Implement an algorithm to determine if a string has all unique characaters. 
# What if you cannot use additional data structures? [other than string/OR/array]
# Hints: 44, 117, 132

def is_unique(input_string):
    print(f'is_unique() with input_string: {input_string}')
    seen_list = []

    input_string = input_string.lower().replace(' ', '').replace('.', '')
    # LOOKUP NOTE the better way to strip all non-letter characters... .strip() ???
    
    for letter in input_string:
        if letter not in seen_list:
            seen_list.append(letter)
            print(f'appending letter {letter}')
        else:
            print(f'letter {letter} already seen, returning False"')
            return False
    
    print('~~~~ SUCCESS, all characters new, returning True')
    return True
    



example_1 = 'this' # True
# is_unique(example_1)

example_2 = 'that' # False, repeats 't'
# is_unique(example_2)

example_3 = 'tesla... big mop'
is_unique(example_3)
















# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 