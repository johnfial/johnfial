# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This file is misc. notes from a) data structures lecture and b) Lab 11: Searching and Sorting
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# premature optimization = when you start optimizing what doesn't need it! 

# SETS
# good for overlap, 

# STACKS

stack = []
# print(stack)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    def pop(self):
        print('pop method!')
        (self.stack.append(123) * 5)
        self.stack.pop()

    def __str__(self):
        print('~~~~~~')
        return '~~~~~~~~~~~~~~~~~~~'

newstack = Stack
print(newstack)
print(newstack.pop())

# QUEUE

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Part 2 - Binary Search

# Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.

#     Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
#     Loop while low is less then high.
#         For each iteration, calculate a third index mid which is in the middle between low and high
#         If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop.
#         If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.

# Example run:

#  L        M           H
# [1, 2, 3, 4, 5, 6, 7, 8]
#  L  M     H
# [1, 2, 3, 4, 5, 6, 7, 8]
#     L  M  H
# [1, 2, 3, 4, 5, 6, 7, 8]
# Stub:

# def binary_search(nums, value):
#   ...
# #       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2


def binary_search(nums, target):
    for num in nums:
        if num == target:
            print(f'{num}=={target}==index: ')

binary_search(nums, 3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 