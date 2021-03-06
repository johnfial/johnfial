# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/
# TODO STATUS:    Working 2021 Mar 18: Finished, I think... 3 test cases work...
# TODO SUBMITTED: No

def distributeCandies(candyType):
    print(f'''Checking candyType: {candyType}, len(CandyType): {len(candyType)}, so MAX candies: {len(candyType)/2}.''')
    
    temp = []
    types_of_candies = 0
    max_candies = len(candyType) / 2
    
    for candy in candyType:
        if candy not in temp:
            temp.append(candy)
            types_of_candies += 1
    
    return types_of_candies

# Test cases:
candyType_1 = [1, 1, 2, 2, 3, 3]
# print(distributeCandies(candyType_1))
candyType_2 = [1, 1, 2, 3]
print(distributeCandies(candyType_2))
candyType_3 = [6, 6, 6, 6]
# print(distributeCandies(candyType_3))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/
# class Solution:
#     def distributeCandies(self, candyType: List[int]) -> int:
        
    # Distribute Candies

# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain
# weight, so she visited a doctor.

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her 
# candies very much, and she wants to eat the maximum number of different types of candies while still 
# following the doctor's advice.

# Given the integer array candyType of length n, return the maximum number of different types of 
# candies she can eat if she only eats n / 2 of them.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Example 1:
# Input: candyType = [1,1,2,2,3,3]
    # Output: 3
    # Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each 
    # type.

# Example 2:
# Input: candyType = [1,1,2,3]
    # Output: 2
    # Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], 
    # she still can only eat 2 different types.

# Example 3:
    # Input: candyType = [6,6,6,6]
    # Output: 1
    # Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Constraints:
#     n == candyType.length
#     2 <= n <= 104
#     n is even.
#     -105 <= candyType[i] <= 105



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #
# def name():
#     counter = 0
