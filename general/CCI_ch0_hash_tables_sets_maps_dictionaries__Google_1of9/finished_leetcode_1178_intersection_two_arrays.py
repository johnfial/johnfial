# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : Yes, poor SPACE/TIME

# See followup!
    # Follow up:

    #     What if the given array is already sorted? How would you optimize your algorithm?
    #     What if nums1's size is small compared to nums2's size? Which algorithm is better?
    #     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# NOTE Concepts  :  
# - HashMap
# - Intersections / Sets
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def return_intersection(nums1, nums2):
    
    intersection = []

    for num in nums2:
        if num in nums1:
            intersection.append(num)
            nums1.remove(num)
    print(intersection)
    
    return intersection

# return_intersection([1, 2, 2, 1,],[2,2,])  # [2, 2]
return_intersection([4,9,5,],[9,4,9,8,4,])  # [4, 9]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
# Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

 

# Constraints:

#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000

 


