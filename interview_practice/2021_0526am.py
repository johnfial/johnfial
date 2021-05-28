##############################################################################

# always type out the goal/task!
# REVERSE THE ARRAY, then ideally, in place
# context for customer: array of products, want to sort in reverse order, for customer

import math
input_1 = [123, 55, 13, 999, 355, 789, 111, 15, ] # even, 8 len
input_odd = [123, 55, 13, 999, 355, 789, 111, 15, 950 ] # odd, 9 len
input_odd = [1, 2, 8,]

def reverse_array(input):
    # output_array = []
    # for i in range(-1, -len(input), -1):
    #     print(input[i])
    #     output_array.append(input[i])
    # print(output_array)
    # return output_array

    # NOW IN PLACE
    # odd vs even: odd middle doesn't change, even they do
    
    c = 0
    c_end = -1

    # NOTE play with this next line, also use i
    for i in range(math.floor(len(input) / 2)):
        temp = input[c_end]
        
        input[c_end] = input[c]
        input[c] = temp
        
        c+=1
        c_end-=1

    print(input)

    return input

reverse_array(input_1)
reverse_array(input_odd)




















##############################################################################