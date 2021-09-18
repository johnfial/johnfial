# # # # # # # # 

# 16.9 Operations: Write methods to implement the multiply, subtract, and divide operations for 
# integers. The result of all of these are integers. You can use the add operator, but not minus, 
# times, or divide.

# A) multiply, easy
# B) subtract -- NOTE cheating? supposed to use bits?
# C) divide, NOTE stuck here

# # # # # # # # 


def multiply_via_add_only(x, y):
    print(f'multiplying {x} and {y}')
    result = 0
    for i in range(y):
        result += x

    return result

x = 100
y = 5
print(multiply_via_add_only(x,y))

# # # # # # # # 
def subtract_via_add_only(x, y):
    print(f'subtracting: {x} - {y}:')
     # NOTE cheating?
    result = x
    return x +- y
print(subtract_via_add_only(x, y))


# # # # # # # # 
def divide_via_add_only(x: int, y: int):
    print(f'dividing {x} / {y}:')
    result = x
    for i in range(y):
        result += -y
    return result

print(divide_via_add_only(x, y))
# # # # # # # # 
