# cracking the coding interview, V1.1, p.56
# The following code computes the product of a and b. What is its runtime?

# from Java:
def product(a, b = int):
    sum = 0
    c = 0
    while c < b: # performs one round of addition while counter at 0 is < the 2nd input number
        sum += a
        c += 1
    return sum

print(product(2, 10))
