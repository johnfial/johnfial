# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Working 2021 Mar 25...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.5 One Away 
# There are three types of edits that can be performed on string: insert a character, remove a character, or 
# replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# Hints: 23, 97, 130

def solution(string1, string2):
    # insert 
    if len(string1) == len(string2):
        printme = one_edit_replace(string1, string2)
        print(printme)
        return printme

    if len(string1) == len(string2) + 1:
        # string2 is longer by 1...
        return compare(string2, string1)

    if len(string1) + 1 == len(string2):
        # string1 is longer by 1...
        return compare(string1, string2)

    print('returning FALSE HERE!')
    return False

# 1 check length, route...
# 2 if SAME length, go to one_edit_replace() function
# function ABOVE: 
def one_edit_replace(string1, string2):
    
    # NOTE NOTE NOTE 
    # NOTE NOTE NOTE 
    # CONCEPT! 
    # NOTE NOTE NOTE 
    # NOTE NOTE NOTE :
    one_difference = False

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if one_difference: return False  # if it's already set to True, this is the 2nd, return FALSE
            one_difference = True  # else set to True
    return True

def compare(shorter, longer):
    c1 = 0
    c2 = 0
    while c1 < len(shorter) and c2 < len(longer):
        if shorter[c1] == longer[c2]:
            c1 += 1
            c2 += 1
        else:
            c1 += 2
            print(f'ELSE: c1 incremented by 2!')
    
    return True

# EXAMPLE:
#     pale, ple   --> True
#     pales, pale --> True
#     pale, bale  --> True
#     pale, bake  --> False

# print(solution('pale', 'ple'))
# print(solution('pales', 'pale'))
print(solution('bales', 'balez'))
# print(solution('pales', 'pal3z'))
# print(solution('pales', 'paleoooo'))
# solution('pale', 'bale')
# solution('pale', 'bake')




















# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 