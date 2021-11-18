

def print_recursive(x):
    if x == 0:
        return
    print(x)
    x -= 1
    return print_recursive(x)


print_recursive(10)