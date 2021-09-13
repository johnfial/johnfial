# https://www.interviewcake.com/concept/python3/overlapping-subproblems?course=fc1&section=dynamic-programming-recursion
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Fibonnacci sequence:
# series where each number is the sum of the previous two numbers
# IE:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . . 

def fibbonacci(n):
    if n in [0, 1]:
        print(f'fib {n} found in base case [0, 1]')
        return n
    print(f'calculating fib({n})')
    return fibbonacci(n-1) + fibbonacci(n-2)

# print(fibbonacci(4))


memo = {}
def fib_with_memo(n):
    if n in [0, 1]:
        return n

    if n in memo:
        print(f'getting {n} from memo')
        return n

    result = fib_with_memo(n-1) + fib_with_memo(n-2)
    memo[n] = result
    return result

print(fib_with_memo(56))