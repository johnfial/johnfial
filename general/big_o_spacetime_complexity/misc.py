# misc big-o, from cracking the coding interview...

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# example 1:
def print_sum_and_product(array):
    sum = 0
    product = 0

    for num in array:
        sum += num
    for num in array:
        product *= num
    print(f'sum={sum} and product={product}')

# this is just O(n) where n is len(array), because two calls doesn't matter (we drop the O(2n))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# example 2:

# 

def print_pairs(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            print(f'array[i]={array[i]=} and array[j]={array[j]=}')

array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# ... but what's the runtime?
# two nested loops based on the length (call that n) of the array... n * n, basically, so n^2, right?
# 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# print_pairs(array_1)
print_sum_and_product(array_1)