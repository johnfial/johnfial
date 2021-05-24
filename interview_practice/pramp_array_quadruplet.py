# https://www.pramp.com

# Array Quadruplet

# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet 
# that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an 
# array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

# Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return 
# the first one you encounter (considering the results are sorted).

# Explain and code the most efficient solution possible, and analyze its time and space complexities.

# Example:

# input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

# output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
#                      # whose sum is 20. Notice that there
#                      # are two other quadruplets whose sum is 20:
#                      # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
#                      # asked to return the just one quadruplet (in an
#                      # ascending order)

# Constraints:

#     [time limit] 5000ms

#     [input] array.integer arr
#         1 ≤ arr.length ≤ 100

#     [input] integer s

#     [output] array.integer
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

example_1 = [2, 7, 4, 0, 9, 5, 1, 3]
example_1_n = 20

def findArrayQuadruplet(array, s):

    quad_array = []  # ascending! ... or empty. return the FIRST possibility
    array.sort()
    print(array)

    sum = 0
    for i in range(len(array)-3):
        # NOTE ok start, but left off here... doesn't have to be consecutive, rather ANY four numbers...
        if array[i] + array[i+1] + array[i+2] + array[i+3] == s:
            print(f'found it with i {i}')
        print(f'i {i}, next loop...')



    return quad_array

findArrayQuadruplet(example_1, example_1_n)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Array Quadruplet

#     Any solution of more than O(N^3) is not efficient enough. Please rate your peer accordingly on the problem solving section.
#     If you peer can’t think of the any solution, encourage them to implement first a brute force solution and then optimize it.
#     If your peer can’t improve the naive solution, ask them how using sorting can improve the time complexity.
#     If still no progress, ask your peer to try first to solve the problem for a pair of integers instead of a quadruplet (i.e. find two numbers whose sum is s etc.). Then ask them to generalize that solution to a quadruplet.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Array Quadruplet

# The naive solution would be to consider every quadruplet in the input array and return the one (if exists) whose sum is s. This approach requires using 4 nested loops and its time complexity is O(N^4). This is quite inefficient and we can do better than that.

# We start by sorting the given array in ascending order and then for each pair (arr[i], arr[j]) in the array where (i < j), we check if a quadruplet is formed by current pair and a pair from a subarray arr[j+1...n-1]. So how do we find a complementing pair in the subarray arr[j+1...n-1]?

# What we want to do is to find two values in the subarray such that their sum equals to s - (arr[i], arr[j]). Let’s denote this value as r. Now, since we made sure to sort arr in an ascending order, the idea is to maintain the search space by keeping two indexes (low and high) that initially point to two end-points of the subarray. Then we loop until low is less than high and reduce the search space arr[low...high] at each iteration of the loop. We compare the sum of the values present at index low and high with r and increment low if the sum is less than r and decrement high if the sum is more than r. Finally, if the sum is equal to r, we found the desired pair.

# The quadruplet will then consist of the initial pair we found in the first step and the complementing pair we found in the subarray.

# Pseudocode:

# function findArrayQuadruplet(arr, s):
#     n = arr.length

#     # if there are fewer than 4 items in arr, by
#     # definition no quadruplet exists whose sum is s
#     if (n < 4):
#         return []

#     # sort arr in an ascending order
#     arr.sort()

#     for i from 0 to n - 4:
#         for j from i + 1 to n - 3:
#             # r stores the complementing sum
#             r = s - (arr[i] + arr[j])

#             # check for sum r in subarray arr[j+1…n-1]
#             low = j + 1, high = n - 1;

#             while (low < high):
#                 if (arr[low] + arr[high] < r):
#                     low++

#                 else if (arr[low] + arr[high] > r):
#                     high--

#                 # quadruplet with given sum found
#                 else:
#                     return [arr[i], arr[j], arr[low], arr[high]]

#     return []

# Time Complexity: we have three nested loops whose combined time complexity is O(N^3), where N is the size of arr. We also using sorting in the beginning and that’s additional O(N⋅log(N)). The total time complexity is still O(N^3) because O(N⋅log(N)) gets thrown away since in the asymptotic calculation it’s not material.

# Space Complexity: O(1) as we used only a constant amount of space throughout the algorithm.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 











# Australian Kevin's solution, 22 May 2021:

"""

[2, 7, 4, 0, 9, 5, 1, 3]
[0, 1, 2, 3, 4, 5, 7, 9] 20

"""

# I think the test case passed , but the complexity is very high, n! I think

def find_array_quadruplet(arr, s):
  arr.sort()
  if len(arr) < 4:
    return []
  
  for i in range(len(arr)):
    if arr[i] > s:
      continue
    has_three_sum = three_sum(arr[0:i] + arr[i+1:], s - arr[i])
    if has_three_sum:
      return sorted([arr[i]] + has_three_sum)
  return []
    
    
def three_sum(arr, s):
  for i in range(len(arr)):
    if arr[i] > s:
      continue
    has_two_sum = two_sum(arr[0:i] + arr[i+1:], s - arr[i])
    if has_two_sum:
      return [arr[i]] + has_two_sum
    

def two_sum(arr, s):
  dict = {}
  for number in arr:
    if number in dict:
      return [number, dict[number]]
    dict[s - number] = number
    
  return None


