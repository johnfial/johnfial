# https://leetcode.com/problems/4sum/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def ignore():
    class Solution:
        def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
            pass

    def fourSum(array, target):
        for num in array:
            print(target)

        answers = []
        a = 0
        b = 1
        c = 2
        d = 3
        if nums[a] + nums[b] + nums[c] + nums[d] == target:
            print(f'{nums[a]} + {nums[b]} + {nums[c]} + {nums[d]} == {target}')
            answers.append((nums[a], nums[b], nums[c], nums[d]))  # BUG gives it a tuple...
        
        print(answers)

def fourSum(array, target):
    answers = []    
    c = 0

    # NOTE TODO
    # the brute force (terrible 4^n as it is...) works, how do i get four distint #s out?

    for quad in range(len(array) ** 4):
        
        c += 1
        

    # for a in array:        
    #     for b in array:            
    #         for c in array:                
    #             for d in array:
    #                 if a + b + c + d == target:
    #                     print(f' found one with {a} + {b} + {c} + {d} == {target}')
    #                     answers.append([a, b, c, d])
    #                     c += 1
    
    print(f'c = {c}')
    print(answers)
    return answers

nums = [1, 0, -1, 0, -2, 2]
target = 0
# fourSum(nums, target)

# # example 2:
nums = [2, 2, 2, 2, 2, ]
target = 8
# fourSum(nums, target)

# # example 3:
nums = [1, 5, 3, 19, 2, -1, 7, 6, 12, -45, 0, 0, 1, 20, ]
target = 25
fourSum(nums, target)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # https://leetcode.com/problems/4sum/

# 18. 4Sum
# Medium

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

 

# Constraints:

#     1 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109