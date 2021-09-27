# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    ACCEPTABLE solution, but poor in my opinion... could a) improve runtime and B) improve space
# TODO SUBMITTED: Yes, done
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Single Number

def single_num(nums):
    
    dic = {}
    
    # SPACE/TIME loops through nums once, O(n)
    for num in nums:
        # SPACE/TIME includes a dict. lookup...
        if dic.get(num) == None:
            dic[num] = 1
        else:
            dic[num] = (dic.get(num) + 1)
    
    # SPACE/TIME *THEN* iterates through entire dict... easiest spot to improve here!
    for item in dic.items():
        if item[1] == 1:
            return item[0]

    return False

print(single_num([2, 2, 1, ]))
print(single_num([ 4, 1, 2, 1, 2, ]))
print(single_num([ 1, ]))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
# Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1

 

# Constraints:

#     1 <= nums.length <= 3 * 104
#     -3 * 104 <= nums[i] <= 3 * 104
#     Each element in the array appears twice except for one element which appears only once.

