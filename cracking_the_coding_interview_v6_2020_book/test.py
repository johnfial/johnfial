
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# p180 # 16.1 medium difficulty, swap numbers
# Write a method to swap two numbers in place (that is, without using any additional variables!).
# STATUS : done, confirm
a = 10
b = 20

def swap_numbers_in_place(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b  # returns the tuple

# print(a, b)
# print(swap_numbers_in_place(a, b))

a = 572
b = -23
# print(a, b)
# print(swap_numbers_in_place(a, b))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 16.6 is_smallest
# think I'm done, check for edge cases
index_a = 0
index_b = 0
list_a = [3, 73, 73, 83, 93, 2, 7777, ]
list_b = [1, 5, 9, 8, 57, 254, 30, ]

def find_smallest_difference(list_a, list_b):
    smallest_difference = 99999999999 # TODO does this work, need infinity, or what?
    for number_a in list_a:
        for number_b in list_b:
            temp_difference = abs( number_a - number_b )
            if temp_difference <= smallest_difference:
                smallest_difference = temp_difference
                print(f'new smallest difference: {smallest_difference} between {number_a} and {number_b}')
    return smallest_difference

# find_smallest_difference(list_a, list_b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 16.7 max_number of two, NOT using any legit comparisons...
def max_number(a, b):
    max_number = 0

    def compare_subfunction(a, b):
        if a > b: 
            return 1
        else: 
            return 0

    if compare_subfunction(a, b) == 1:
        print('line 59')
    return max_number

a = 50
b = 10
max_number(a, b)
