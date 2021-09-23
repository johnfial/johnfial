# https://www.enjoyalgorithms.com/blog/move-all-the-zeroes-to-the-end
# Move zeroes to end of an array

# Given an array of n elements filled with several integers, some being zeroes,
# write a program to move all the zeroes to the end.

def move_zeroes(input_list):
    
    # this solution pops off all zeroes, putting them in a temp array,
    # and extends the original by the # of zeroes popped
    
    # SPACE/TIME:
    # the O() for the loop is O(n) elements in the list, and i think thi .append() and .pop(i) and O(1),
    # and am not sure about the .extend() method's big-O...
    # So I think the final is O(n) ...

    temp_zeroes = []
    
    c = 0
    while c < len(input_list):
        if input_list[c] == 0:
            print(f' num = {input_list[c]}, c={c}')
            temp_zeroes.append(input_list.pop(c))
            c -= 1
        c += 1


    input_list.extend(temp_zeroes)
    return input_list

ex1 = [4, 8, 6, 0, 2, 0, 1, 15, 12, 0, ]
ex2 = [0, 3, 5, 9, 0, 0, 23, 2, ]
ex3 = [0, 0, 0, 0, 44, 3, 5, 9, 0, 0, 23, 2, ]

# print(move_zeroes(ex1))
# print(move_zeroes(ex2))
print(move_zeroes(ex3))