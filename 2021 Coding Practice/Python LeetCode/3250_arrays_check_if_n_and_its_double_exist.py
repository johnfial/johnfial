# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

def checkIfExist(arr: list[int]) -> bool:
    ''' test '''
    # print(arr)
    counter = 0
    for num in arr:
        for num2 in arr:
            # print(f'counter {counter} num {num} and num2 {num2}')
            counter += 1
            
            if num == num2 * 2 or num2 == num * 2:
                if num != 0:
                    print(f'~~~~double found with num{num} and num2 {num2} ~~~~')
                    return True
                elif num == num2 == 0:
                    print(f'~~~~double found with num{num} and num2 {num2} ~~~~')
                    return True
    print('~~~~~~~~~~~FALSE~~~~~~~~~~~~')
    return False



arr_1 = [10, 2, 5, 3]
# checkIfExist(arr_1)

arr_2 = [7, 1, 14, 11]
# checkIfExist(arr_2)

arr_3 = [3, 1, 7, 11]
# checkIfExist(arr_3)

arr_4 = [-2,0,10,-19,4,6,-8]
# checkIfExist(arr_4)

arr_5 = [0, 0] # expected TRUE!
checkIfExist(arr_5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Check If N and Its Double Exist

# Given an array arr of integers, check if there exists two integers N and M 
    # such that N is the double of M ( i.e. N = 2 * M).

# More formally, check if there exists two indices i and j such that :

#     i != j
#     0 <= i, j < arr.length
#     arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

# Example 2:

# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

# Example 3:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

 

# Constraints:

#     2 <= arr.length <= 500
#     -10^3 <= arr[i] <= 10^3

#    Hide Hint #1  
# Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].

#    Hide Hint #2  
# On each step of the loop check if we have seen the element 2 * arr[i] so far or arr[i] / 2 was seen if arr[i] % 2 == 0.