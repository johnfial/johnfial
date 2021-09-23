# # # # # # # # # # # # # # # # # # # # #u # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Started/Finished 22 September 2021
# TODO: now figure out time complexity...
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

ex1 = [1, 7, 3, 4, ]

def get_product_of_all_ints_except_at_index(input_list):

    # Q: order matter?
    # Q: doubles allowed or not allowed? Wanted or unwanted?

    products = []

    for i in range(len(input_list)):
        # print(f'i = {i}')
        temp_list = input_list.copy()  # NOTE BUG this was important, because = in python makes the left side simply POINT to the right side's existence
        
        # 1 so pop out the number at that index, 
        temp_list.pop(i)
        product = 1
        
        # 2 multiply all the other numbers in the list
        while temp_list:
            product = product * temp_list.pop()
        
        # print(f'product for round {i} and temp_list {temp_list} : {product}')
        products.append(product)

    return products

ex2 = [5, 2, 1, 1, 9, 111, ]

print(get_product_of_all_ints_except_at_index(ex1))
print(get_product_of_all_ints_except_at_index(ex2))







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://www.interviewcake.com/question/python3/product-of-other-numbers
#  You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# For example, given:

#   [1, 7, 3, 4]

# your function would return:

#   [84, 12, 28, 21]

# by calculating:

#   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

# Here's the catch: You can't use division in your solution! 