# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/
# NOTE STATUS: No, still
# Submitted: no...


def removeElement(nums: list[int], val: int) -> int:
    print(f'~~~START~~~ nums now {nums}, removing all entries of val {val}')
    # for num in nums:
    #     if num == val:
    #         nums.pop()
    
    counter = 0
    nums_temp = []
    
    for num in nums:
        print(f'~~~num: {num} ')
        if num != val: # if it's a legit number:
            print(f'legit num {num}!')
            counter += 1
        else:
            nums_temp.append(num)
            nums.remove(num) # Q does this return the value? A no, returns nothing
    
    nums.extend(nums_temp) # add the popped numbers to the end
    
    print(f'nums now {nums}')
    return counter



nums_1 = [3,2,2,3]
val_1 = 3 # Output: 2, nums = [2,2]
nums_2 = [0,1,2,2,3,0,4,2]
val_2 = 2 # Output: 5, nums = [0,1,4,0,3]

print(removeElement(nums_1, val_1))
# print(removeElement(nums_2, val_2))

print('~~~finish~~~')
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/
# Remove Element

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

 
# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]
# Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.

 

# Constraints:

#     0 <= nums.length <= 100
#     0 <= nums[i] <= 50
#     0 <= val <= 100

