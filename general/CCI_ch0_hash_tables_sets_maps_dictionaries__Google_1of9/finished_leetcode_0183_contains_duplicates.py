# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Solved, sets are nice!
# TODO SUBMITTED: Yes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Contains Duplicate
def dict_duplicate(array):
    
    hash_set = set()
    
    for item in array:
        if item in hash_set:
            return True
        else:
            hash_set.add(item)

    return False

print(dict_duplicate([1,2,3,1]))
# print(dict_duplicate([1,2,3,4]))
print(dict_duplicate([1,1,1,3,3,4,3,2,4,2]))
print(dict_duplicate(['aoeu', ' ', ' aoeu', 'aoeue', ]))




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

 

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109

