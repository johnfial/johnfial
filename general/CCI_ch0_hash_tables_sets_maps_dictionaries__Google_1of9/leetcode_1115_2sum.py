# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Two Sum


def two_sum(nums, target):
    c1 = -1
    c2 = 0

    # for combo in range(len(nums) ** 2):
    #     print(f'trying combo {combo}')
        
    #     if nums[c1] + nums[c2] == target:
    #         return [c1, c2]
    #     if c1 == c2:
    #         pass
    #     c1 += 1
    #     c2 += 1

    y = nums[0]
    for x in range(len(nums)):
        if nums[x] == target - y:
            print(f'nums[{x}] - {y} == target: {target}')
            return [x, 0]

# print(two_sum([2,7,11,15],9))
# print(two_sum([3,2,4,],6))
# print(two_sum([3,3,],6))
print(two_sum([3,9,94, 8, 5, 2, 7, 78, 78, 45, 12, 45, 56, 89, 1,5, 4, 2, 1, ],7))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

 

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?