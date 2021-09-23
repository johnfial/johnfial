# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/

def moveZeroes(nums: list[int]) -> None:
    counter = 0 # pointer #1
    temp_0s = [] # temp list to store the 0s... could also use a variable, but am not sure how to do it without another list or variable

    for i in range(len(nums)): # this means it's a two-pointer solution, and I switched from "for num in nums:"
        print(f'current i {i} in nums {nums} with counter {counter}') 
        if nums[counter] == 0:
            print(f'found a 0! nums{counter}')
            nums.pop(counter)
            temp_0s.append(0)
            counter -= 1 # since we're popping off an item, we need to DECREASE the counter before the main loop increases it
        counter += 1

    nums.extend(temp_0s)
    print(nums)

arr = [0,1,0,3,12] # expected [1, 3, 12, 0, 0]
arr_2 = [0, 0, 1] # expected [1, 0, 0]
moveZeroes(arr_2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
#    Hide Hint #1  
# In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. 
# However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, 
# first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
#    Hide Hint #2  
# A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.