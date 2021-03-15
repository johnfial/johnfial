# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
# NOTE STATUS: Looks good, done I think, could certainly be shorter
# Submitted: No...

def sortArrayByParity(A):
    print(f'~~~started with array: A {A}')
    
    odd = []
    even = []
    
    for num in A:
        if num % 2 == 0:
            print('even:', end='')
            print(num)
            even.append(num)
        else:
            print('odd:', end='')
            print(num)
            odd.append(num)
    
    A = []
    A.extend(even)
    A.extend(odd)
    
    print(f'new array: A {A}')
    
    return A


a_1 = [3, 1, 2, 4] # expected: [2, 4, 3, 1] ... also acceptable: [4,2,3,1], [2,4,1,3], and [4,2,1,3]
sortArrayByParity(a_1)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
    # followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Note:

#     1 <= A.length <= 5000
#     0 <= A[i] <= 5000

