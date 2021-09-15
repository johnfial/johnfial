# 8.9 Parens:
# Implement an algorithm to print all valid (e.g. properly opened and closed) cominations on n parentheses.

# EXAMPLE:
# Input: 3
# Output: 

# Hints: 138, 174, 187, 209, 243, 265, 295

def generate_parentheses(n):
    if n <= 0: 
        return
    if n == 1:
        return '()'
    
    while n > 1:
        print(f'n = {n}')
        return f'{generate_parentheses(n-1)}' + f'{generate_parentheses(n-2)}'

print(generate_parentheses(5))