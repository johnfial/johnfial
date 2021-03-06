# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
# TODO STATUS:    Working 2021 Mar 25...
# TODO SUBMITTED: yes,     # Runtime: 32 ms, Memory Usage: 14.1 MB
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def merge(nums1, m, nums2, n): # nums1/2 are the arrays, m and n are the numbers initialized
    c1 = 0 # counter 1 for nums1
    c2 = 0 # counter 2 for nums2
    while c1 < m+n: # used to be while c1 < m:, but...
        # ... after failing example 2, writing the commented out section "if m==0:" for it and example 3, ...
        # ... STILL failing example 4, i realized writing for that edge case was silly... and saw the obvious: to continue the loop while counter 1 was < m+n TOGETHER...
        # ... not just m, as the instructions clearly state that nums1 has the space/length for m+n...

        # NOW EDIT THIS COMMENT IN A DAY OR TWO SO IT'S MORE CLEAR TO MY FUTURE SELF!
        try:
            print(f'c1 is {c1} and nums1: {nums1}')
            print(f'nums1[c1]: {nums1[c1]}, and nums2[c2]: {nums2[c2]}.')
            nums1[c1+m] = nums2[c2]
        except:
            print('excepted')
            pass
        c1 += 1
        c2 += 1
    # if m == 0: # i don't like this writing for only one edge case, bad philosophy...
    #     print('m == 0, so...:')
    #     nums1[m] = nums2[m]

    nums1.sort()
    print(nums1)

# # example 1:      
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# merge(nums1, 3, nums2, 3) # expected [1,2,2,3,5,6]
# # example 2: 
# nums1 = [1]
# nums2 = []
# merge(nums1, 1, nums2, 0)
# # example 3:
# nums1 = [0]
# nums2 = [1]
# merge(nums1, 0, nums2, 1) # expected: [1]
# example 4:
nums1 = [0,0,0,0,0]
nums2 = [1,2,3,4,5]
merge(nums1, 0, nums2, 5) # Expected: [1,2,3,4,5]



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

# Example 1:
    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # Output: [1,2,2,3,5,6]
# Example 2:
    # Input: nums1 = [1], m = 1, nums2 = [], n = 0
    # Output: [1]

# Constraints:
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[i] <= 109

