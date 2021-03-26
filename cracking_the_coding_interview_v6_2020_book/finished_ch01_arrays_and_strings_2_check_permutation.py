# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Working 2021 Mar 25...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.2
# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other. 
# Hints: 1, 84, 122, 131


# Test cases:
example_1 = 'melissa'
example_2 = 'bobby'
example_3 = 'salimes'

def permutation_checker(input_1, input_2):
    print(f'welcome to permutation_checker(), input input_1: {input_1} and input_2: {input_2}.')
    compare1 = []
    compare2 = []

    if len(input_1) == len(input_2):
        for i in range(len(input_1)):
            compare1.append(input_1[i])
            compare2.append(input_2[i])
        
        compare1.sort()
        compare2.sort()

        print(f'comparing sorted strings {compare1} and {compare2}')
        if compare1 == compare2:
            print(f'~~~Congratulations! input input_1: {input_1} and input_2: {input_2} are permutations of each other! ~~~')
            return True
        else:
            print('~~~Sorry! Not permutations. Ending. ~~~~~')
            return False


    else:
        print(f'Sorry, the lengths of the strings do not match, so they cannot possibly be permutations. \n ~~~Goodbye.~~~')
        return False



permutation_checker(example_1, example_3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Title


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
#     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #
























# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 