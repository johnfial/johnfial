class Solution():
    # @param A : integer
    # @param B : int
    # @return an integer
    m = 1
    n = 1
    gcd = 0

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def get_greatest_common_divisor(self):
        print(self)

        return self.gcd
    
    def __str__(self):
        return f'm: {self.m}, n: {self.n}'

Solution1 = Solution(565, 11)
print(Solution1.get_greatest_common_divisor())

# # https://www.interviewbit.com/problems/greatest-common-divisor/#
# # Greatest Common Divisor
    # Note:You only need to implement the given function. Do not read input, instead use the arguments to the function. 
    # Do not print the output, instead return values as specified. 
    # Still have a doubt? Checkout Sample Codes for more details.

# Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.

# Both m and n fit in a 32 bit signed integer.

# Example

    # m : 6
    # n : 9

    # GCD(m, n) : 3 

#     NOTE : DO NOT USE LIBRARY FUNCTIONS
