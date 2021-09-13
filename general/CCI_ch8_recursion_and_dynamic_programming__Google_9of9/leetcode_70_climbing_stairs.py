# # https://leetcode.com/problems/climbing-stairs/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 









def stair_combinations(n):

    counter = 0

    for x in range(n):
        print(x)
        counter += 1
        pass
    
    print(f'final counter = {counter}')

n = 2

# stair_combinations(n)

# from https://leetcode.com/problems/climbing-stairs/discuss/1455588/Python-3-oror-Solution-with-Explanation-(faster-than-94.46-Memory-less-than-90.73) : 
def climb_stairs(n):
    if n in [1, 2]:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(30)) # don't go over 40 or so!

# 1 = 1
# 2 = 2 [1+1, 2]
# 3 = 3 [1+1+1, 1+2, 2+1]
# 4 = 5 [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]






# # https://leetcode.com/problems/climbing-stairs/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

 

# Constraints:

#     1 <= n <= 45

