# BIG-O notation
# see https://www.bigocheatsheet.com/
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

import random

# O(1)
def random_element(nums):
    index = random.randint(0, len(nums)-1)
    return nums[index]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(random_element(list1))

# O(n)
def linear_search(nums, target):
    for num in nums:
        print(num)
        if num == target:
            print('found! ' + str(num))
    return  # an index, probably

# print(linear_search(list1, 5))

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

# O(n^2)
# SUPER inefficient, n^2, terrible!
def find_pair(nums, target):
    output = []
    for x in range(len(nums)):
        for y in range(len(nums)):
            # print(x, y)
            if x != y and nums[x] + nums[y] == target:
                output.append((nums[x], nums[y]))
    print(output)
    print(type(output[1]))
    return output

find_pair(list1, 5)
print(r'~~~~~~~~~~~~~~~')
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
