# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/ # 1295
# TODO STATUS:    Finished
# TODO SUBMITTED: Yes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 




def findNumbers(nums: list[int]) -> int:
    answer = []
    for num in nums:
        int_as_str = str(num)
        if len(int_as_str) % 2 == 0:
            answer.append(int_as_str)
    
    print(f'len(answer) : {len(answer)}')
    return len(answer)

example_nums_1 = [12,345,2,6,7896] # output 2
example_nums_2 = [555,901,482,1771] # Output: 1 

findNumbers(example_nums_1)
print('space')
findNumbers(example_nums_2)
print('~~~~~FINISH!!!!~~~~~')

# Given an array nums of integers, return how many of them contain an even number of digits.
# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

 

# Constraints:

#     1 <= nums.length <= 500
#     1 <= nums[i] <= 10^5
