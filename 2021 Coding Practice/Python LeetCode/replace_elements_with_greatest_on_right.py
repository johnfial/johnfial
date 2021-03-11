def replaceElements(arr: list[int]) -> list[int]:
    print(f'new arr is {arr} with len(arr) {len(arr)}')
    arr_len = len(arr) # saved as a variable because the array will change...
    counter = 0
    output_array = []
    highest_number = 0 # hmm...

    # I'd want to pop the first one off, then see if anything in there is greater than the first one (else -1), and if so, add THAT number to index of the NEW list... then at the end, return that list!
    while counter < arr_len:
        current_number = arr.pop(counter)
        for number in arr:
            if number > current_number:
                print(f'{number} is higher than {current_number}!')

        counter += 1
    print(f'arr {arr} and output_array {output_array}')
    
    if len(output_array) < 2:  # this might be 'edge case cheating' ...
        print('return -1!')
        return -1

    # # Commented out this try:
    # for i in range(-1, -(len(arr)+1), -1):  # loop through the array backwards
    #     # do an IF items from i to end of array are greater than arr[i]:
    #     # .POP off backwards, no?
    #         # .append() to new_array
    #         # return new_array
    #     print(f'arr[{i}]: {arr[i]} ')
    #     pass
    
arr = [17, 18, 5, 4, 6, 1] # len = 6
# replaceElements(arr)
arr_2 = [400]
arr_3 = [17, 18, 5, 4, 6, 1, 88, 5, 5, 13, 1, -5, 5, 1, 0] 

def find_highest_number(input_array, starting_index):
    highest_number_seen = -1
    counter = starting_index
    for num in range(len(input_array)):
        print(input_array[counter])
        if num > highest_number_seen:
            highest_number_seen = num
        counter =+ 1
    return highest_number_seen

print(find_highest_number(arr_3, 4))
# print(replaceElements(arr_2))
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