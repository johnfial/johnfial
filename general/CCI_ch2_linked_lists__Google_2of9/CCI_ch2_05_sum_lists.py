# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 2.05 Sum Lists:


# You have two numbers represented by a linked list, where each node contaions a single digit. 
# The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write
# a function that adds the two numbers and returns the sum as a linked list. (Cannot cheat and 
# just convert list to integer...)

# Hints: 7, 30, 71, 95, 109

# EXAMPLE 1
# Input:  7 ~~> 1 ~~> 6 + (5 ~~> 9 ~~> 2). Or in english, 617 + 295
# Output: 2 ~~> 1 ~~> 9. (The number 912)

# TODO STEPS:
# 1 make the linked lists
# 2 test: print out each
# 2 add to array until current = None
# 3 change array to int()
# 4 add numbers
# 5 create new linked list...
# 5a: create list() from sum IN REVERSE ORDER
# 5b: create node for each in list in range(len(list))
# 5c: link that node to next...
# 5d: return list!


# FOLLOW UP EXAMPLE: stored in forward order...
# EXAMPLE 2
# Input: (6 ~~> 1 ~~> 7) + (2 ~~> 9 ~~> 5). In engilsh: 617 + 295
# Output: 9 ~~> 1 ~~> 2. (The number 912)






















# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
#     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #

# Test cases:


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 