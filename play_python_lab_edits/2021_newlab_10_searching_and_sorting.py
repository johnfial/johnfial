import math # Used for binary search on line ~65
# TODO runtime of searches?

    # LINKS:
    # https://en.wikipedia.org/wiki/Binary_search_algorithm
    # class eagle: https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/mob/11%20Stack%20and%20LinkedList.md

    # https://github.com/PdxCodeGuild/class_salmon/blob/main/1%20Python/labs/10%20Searching%20And%20Sorting.md

    # Lab 10: Searching and Sorting

    # Big-O Notation is a measure of the complexity of an algorithm, specifically how many steps an 
    # algorithm takes depending on the size of the input. For example, performing a linear search on a 
    # list of n elements takes, on average, n/2 steps, so we say a linear search is O(n). We throw away 
    # multiplicative and additive factors to characterize algorithms independently of the hardware it's 
    # running on. Big-O Cheat Sheet
    # Part 1 - Linear Search

    # Implement linear search, which simply loops through the given list and check if each element is 
    # equal to the value we're searching for. If it is, return the index at which it was found, otherwise, 
    # return a value indicating that it was not found.

    # Example run:

    #  I
    # [1, 2, 3, 4, 5, 6, 7, 8]
    #     I
    # [1, 2, 3, 4, 5, 6, 7, 8]
    #        I
    # [1, 2, 3, 4, 5, 6, 7, 8]

    # Stub:

    # def linear_search(nums, value):
    #   ...
    # # index 0  1  2  3  4  5  6  7
    # nums = [1, 2, 3, 4, 5, 6, 7, 8]
    # index = linear_search(nums, 3)
    # print(index) # 2

    # Part 2 - Binary Search

    # Implement binary search, which requires that a list is sorted and divides its search range in 
    # half each iteration until it finds its target.

    #     Begin by defining two indices: low and high. Initialize low as the lowest index in the list 
    # and high as the highest.

    #     Loop while low is less then high.

    #         For each iteration, calculate a third index mid which is in the middle between low and high
    #         If the element at mid is the one you're searching for, return it, otherwise check is the 
    # target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop.
    #         If it's greater, make low equal to mid and loop. If the loop terminates without returning, 
    # return a value indicating that it was not found.

    # Example run:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
def linear_search(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            print(f'linear_search(nums, target) found target={target} at index={i}')
linear_search(nums, 3)

print('~~~~~~~~~~~~~~~~~end linear_search()~~~')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# LAB 11 PART 2B BINARY SEARCH:
# from cracking the coding interview: https://www.youtube.com/watch?v=P3YID7liBug
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
def binary_search_iterative(nums, target):
    low = min(nums)
    high = max(nums)
    
    mid = nums[(math.floor(len(nums) / 2))-1]
    print(f'mid={mid}')
    
    while low < high:
        print(f'~~START WITH target {target} in nums=[{nums}], low: {low}, mid: {mid}, high: {high}')
        # 2 
        if mid == target:
            return mid
        # if target < mid, do this...
        if target < mid:
            high = mid
            print(f'target {target} in nums=[{nums}], low: {low}, mid: {mid}, high: {high}')
            break
        # if target > mid, do this...
        if target > mid:
            low = mid
            print(f'target {target} in nums=[{nums}], low: {low}, mid: {mid}, high: {high}')
            # don't i need to change high?
            break
        else:
            print('WTF why did this line run?!')
        
        # NOTE RESET MID, necessary lol...
        mid = (math.floor(low+high))
        print(f'mid={mid}')
        
    return  # index of target?

def binary_search_reursive(nums, target):
    print(f'binary_search_reursive(nums, target) running with nums: {nums} and target: {target}')

binary_search_iterative(nums, 3)
binary_search_reursive(nums, 3)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#  L        M           H
# [1, 2, 3, 4, 5, 6, 7, 8]
#  L  M     H
# [1, 2, 3, 4, 5, 6, 7, 8]
#     L  M  H
# [1, 2, 3, 4, 5, 6, 7, 8]

# Psuedocode:

# // A - the list
# // n - the length of the list
# // T - the value we're searching for
# function binary_search(A, n, T) is
#     L := 0
#     R := n − 1
#     while L ≤ R do
#         m := floor((L + R) / 2)
#         if A[m] < T then
#             L := m + 1
#         else if A[m] > T then
#             R := m - 1
#         else:
#             return m
#     return unsuccessful

# Stub:

# def binary_search(nums, value):
#   ...
# #       0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2

# Part 3 - Bubble Sort

# Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over 
# the list, comparing each number to the one next to it, and swapping them if needed.

# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped = false
#         for i := 1 to n - 1 inclusive do
#             /* if this pair is out of order */
#             if A[i - 1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap(A[i - 1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure

# Part 4 - Insertion Sort (optional)

# Implement insertion sort, which like bubble sort is also O(n^2), but is efficient at placing new 
# values into an already-sorted list.

# Psuedocode:

# i ← 1
# while i < length(A)
#     j ← i
#     while j > 0 and A[j-1] > A[j]
#         swap A[j] and A[j-1]
#         j ← j - 1
#     end while
#     i ← i + 1
# end while

# Part 5 - Quicksort (optional)

# Quicksort is one of the most efficient sorting algorithms. It works by swapping elements on either 
# side of a pivot value.

# Psuedocode:

# algorithm quicksort(A) is
#     quicksort_recursive(A, 0, length(A) - 1)

# algorithm quicksort_recursive(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort_recursive(A, lo, p)
#         quicksort_recursive(A, p + 1, hi)

# algorithm partition(A, lo, hi) is
#     pivot := A[lo + (hi - lo) / 2]
#     i := lo - 1
#     j := hi + 1
#     loop forever
#         do
#             i := i + 1
#         while A[i] < pivot
#         do
#             j := j - 1
#         while A[j] > pivot
#         if i ≥ j then
#             return j
#         swap A[i] with A[j]
