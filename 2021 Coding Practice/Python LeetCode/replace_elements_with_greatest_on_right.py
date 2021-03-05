def replaceElements(arr: list[int]) -> list[int]:
    print(f'new arr is {arr} with len(arr) {len(arr)}')
    
    counter = 0
    output_array = []

    for num in arr:
        while counter < len(arr):
            # print(arr[counter])
            
            counter += 1
    
    for i in range(-1, -(len(arr)+1), -1):
        # loop through the array backwards
        # do an IF items from i to end of array are greater than arr[i]:
            # .append() to new_array
            # return new_array
            # else: 
                # return -1
        print(f'arr[{i}]: {arr[i]} ')

arr = [17, 18, 5, 4, 6, 1] # len = 6
replaceElements(arr)

arr_2 = [400]
# replaceElements(arr_2) # should return -1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
# Replace Elements with Greatest Element on Right Side

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

    # Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

    # Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

    # Constraints:
#     1 <= arr.length <= 104
#     1 <= arr[i] <= 105

    #    Hide Hint #1  
# Loop through the array starting from the end.
    #    Hide Hint #2  
# Keep the maximum value seen so far.