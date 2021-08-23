# see https://www.bigocheatsheet.com/
# BIG-O notation
# any variable will do, not just n!
# combination = order does NOT matter, fewer possibilities
# permutation = order matters, more possibilites

# quiz to remember words 'constant/linear/polynomial/exponential' @ https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/e/quiz--comparing-function-growth
    # constant = K
        #  A function has "constant" growth if its output does not change based on the input, the nnnn. The easy way to identify constant functions is find those that have no nnnn in their expression anywhere, or have n0n^0n0n, start superscript, 0, end superscript. In this case, 1111 and 1000100010001000 are constant.
    # linear = Kn
        # A function has "linear" growth if its output increases linearly with the size of its input. The way to identify linear functions is find those where nnnn is never raised to a power (although n1n^1 n1n, start superscript, 1, end superscriptis OK) or used as a power. In this case, 3n3n3n3, n and (3/2)n(3/2)n(3/2)nleft parenthesis, 3, slash, 2, right parenthesis, n are linear.
    # polynomian Kn^X
        # A function has "polynomial" growth if its output increases according to a polynomial expression. The way to identify polynomial functions is to find those where nnnn is raised to some constant power. In this case, 2n32n^32n32, n, cubed and 3n23n^23n23, n, squared are polynomial.
    # exponential K ^ n
        # A function has "exponential" growth if its output increases according to an exponential expression. The way to identify exponential functions is to find those where a constant is raised to some expression involving nnnn. In this case, 2n2^n2n2, start superscript, n, end superscript and (3/2)n(3/2)^n(3/2)nleft parenthesis, 3, slash, 2, right parenthesis, start superscript, n, end superscript are exponential.

# https://www.youtube.com/watch?v=v4cd1O4zkGw
# 0(1) aka O(log n) = 
    # pidgeon transfer time, does note take longer with more input (n)
# O(n) == O(2n) == O(3n), etc, but O(n) is the notation...
    # This is a linear/quadratic relationship
    # In general, the internet is here. 
    # not too bad, takes slightly longer for more elements
# O(n log n)
    # 
# O(N^2)
    # this would be printing every single x + y pair, all permutations (order matters)
# O(2^n)
    # 
# O(n!)
    # The absolute worst

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

import random

# O(1)
def random_element(nums):
    index = random.randint(0, len(nums)-1)
    return nums[index]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

print(random_element(list1))

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# O(n)
def linear_search(nums, target):
    for num in nums:
        print(num)
        if num == target:
            print('found! ' + str(num))
    return  # an index, probably

# print(linear_search(list1, 5))

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

# O(n^2)
# SUPER inefficient, n^2, terrible!
def find_pair(nums, target):
    output = []
    for x in range(len(nums)):
        for y in range(len(nums)):
            # print(x, y)
            if x != y and nums[x] + nums[y] == target:
                output.append((nums[x], nums[y]))
    print(output)
    print(type(output[1]))
    return output

find_pair(list1, 5)
print(r'~~~~~~~~~~~~~~~')

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

# O(2^n)
    # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# O(n!)
    # The absolute worst