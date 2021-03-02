
# NOTE, this is their very confusing one...

def removeDuplicates(nums):
    temp_array = []
    duplicate_array = []
    i = 0
    for num in nums:
        if num not in temp_array:
            temp_array.append(num)
        else: 
            print(f'duplicate num found, num: {num} @ i: {i} ')
            temp_number = nums.pop(i)
            duplicate_array.append(temp_number)
            print(f'popped temp_number: {temp_number}')
        i += 1
    print(nums)
    # print(duplicate_array)
    return len(temp_array) # but not nums, as it should be modified within the class Solution

# aoeu
# WORKS LOCALLY BUT DOESN'T MODIFY IN PLACE, especially with their class-based judging system...
# def removeDuplicates(nums):
        # temp_array = []
        # for num in nums:
        #     if num not in temp_array:
        #         temp_array.append(num)
        # # temp_array.sort() # needed?
        # nums = temp_array
        # print(nums)
        # return len(temp_array)

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

example_1 = [1,1,2] 
example_2 = [0,1,2,3,4]
# removeDuplicates(example_2)
print(removeDuplicates(example_1))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 26 https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
