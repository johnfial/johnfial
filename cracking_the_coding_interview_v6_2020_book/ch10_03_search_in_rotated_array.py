# 10.3 Given a sorted array of n integers that has been rotated an unknown number of times,
# write code to find an element in the array. 
# You may assume that the array was originally sorted in increasing order.

# (Return the index in the original, sorted, un-rotated list.)

# Hints: 298, 310
# NOTE STATUS: Started

# EXAMPLE:
# Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# Output: 8 (the index of 5 in the array)

def find_in_array():
    # find the smallest #, that's the original first index
    # find the number, then shift...