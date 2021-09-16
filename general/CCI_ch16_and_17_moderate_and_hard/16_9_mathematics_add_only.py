

# # # # # # # # 

# multiply via add
# 16.9
def multiply_without_asterisk(x, y):
    print(f'multiplying {x} and {y}')
    result = 0
    for i in range(y):
        result += x

    return result

x = 100
y = 3
print(multiply_without_asterisk(x,y))

