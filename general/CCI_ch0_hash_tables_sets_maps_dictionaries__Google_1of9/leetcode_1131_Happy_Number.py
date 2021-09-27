# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: No

# concepts: 
# # - recursion!
# - numbers

# don't know why this is in the sets/dicts section on leetcode?!?!

# NOTE general:
# https://en.wikipedia.org/wiki/Happy_number
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1131 Happy Number, solution: https://leetcode.com/problems/happy-number/solution/
def happy_number(n):

    # 1 get its digits
    integers = list(str(n))
    integers = [int(num) for num in integers]  # yay i remembered a simple list comprehension!

    # 2 get the sum of the squares of its digits
    sum_of_squares = 0
    for x in range( len( str(n) ) ):
        sum_of_squares += integers[x] ** 2
    
    # BASE CASE:
    if sum_of_squares == 1:
        print(f'found a happy number at n = {n}')  # debug print
        return True

    try:
        if happy_number(sum_of_squares) == True:
            return True
    except:
        print(f'final n={n} timed out!')  # debug print
        return False


# print(happy_number(1))
# print(happy_number(19))
print(happy_number(1111111111))
print(happy_number(14))


def happy_number_with_recursion_count_for_leetcode(n, count=1):

    # print(f'count = {count}')  # debug print
    count += 1
    if count >= 979999:  # TIMEOUT
        return False  # TIMEOUT

    # 1 get its digits
    integers = list(str(n))
    integers = [int(num) for num in integers]  # yay i remembered a simple list comprehension!

    # 2 get the sum of the squares of its digits
    sum_of_squares = 0
    for x in range( len( str(n) ) ):
        sum_of_squares += integers[x] ** 2

    # print(f'for integers = {integers}, sum_of_squares = {sum_of_squares}')  # debug print
    
    # BASE CASE:
    if sum_of_squares == 1:
        print(f'found a happy number at n = {n}')  # debug print
        return True

    try:
        if happy_number_with_recursion_count_for_leetcode(sum_of_squares, count) == True:
            return True
        else:
            return False
    except:
        print(f'n={n} timed out with count = {count}!')  # debug print
        return False


# print(happy_number_with_recursion_count_for_leetcode(123))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# leetcode_1131_Happy_Number
# Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:

# Input: n = 2
# Output: false

 

# Constraints:

#     1 <= n <= 231 - 1

