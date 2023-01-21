# https://adventofcode.com/2022/day/5

'''--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?'''

# https://adventofcode.com/2022/day/5

# STEP 1: convert the moves into a list of moves)

# # example:
example_moves = '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
example_moves = example_moves.split('\n')
print(example_moves)
list_of_moves = example_moves

# # actual:
# file_to_open = 'day5.txt'
# with open(file_to_open, 'r') as file:
#     input = file.read()
# list_of_moves = input.split('\n')
# print(len(list_of_moves))
# # actual list starts at line 11, so slice off index 0 through 10:
# list_of_moves =  list_of_moves[:10]
# # test print to see if it sliced properly
# print(list_of_moves[0:10])

for i in range(len(list_of_moves)):
    temp = list_of_moves[i]
    temp = temp.split(' ') # ['move', '1', 'from', '2', 'to', '1'] # len = 6, index 0 through 5
    # SUBTRACT 1, BECAUSE THE INPUT USES HUMAN NUMBERS, but we want an index
    temp = (int(temp[1]), int(temp[3])-1, int(temp[5])-1) # (number_to_move, stack_source, stack_dest)
    list_of_moves[i] = temp
    # print(temp, '<<<< (number_to_move, stack_source, stack_dest)')

print(list_of_moves)
    




# STEP 2: convert the first X lines into the lists

example_boxes = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 '''

# counter = 0
# for i in range(len(example_boxes)):
#     if example_boxes[i] == '[':
#         print(example_boxes[i+1])
#         counter += 1

# print(f'counter = {counter}')

# 2 create a practice list manually:
boxes_list = [
    ['Z', 'N'],
    ['M', 'C', 'D',],
    ['P']
]  # outer array from left to right, inner array: starting from bottom box, with top box as higher index
# boxes_list = [['N', 'Z', 'one'], ['D', 'C', 'M'], ['P', 'a', 'b']]

def rotate(array):
    # quicker -- lookup how to rotate a printed map/grid/array in python?
    
    # METHOD ONE -- # rotate try 1: -- https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    
    # temp_list = list(zip(*boxes_list[::-1]))
    # boxes_list = temp_list
    # print(boxes_list)

    # METHOD TWO

    # # rotate alternate way (opposite direction)
    # rotated = list(reversed(list(zip(*boxes_list))))
    rotated = list(zip(*boxes_list))[::-1]
    return rotated

# print(boxes_list)
# boxes_list = rotate(boxes_list)
# print(boxes_list)

# print the box output:
def print_output(boxes_list_input):
    for i in range(len(boxes_list_input)):
    
        line = ''
        for item in boxes_list_input[i]:
            line += f'[{item}]'
    line = f' '
    
    for i in range(len(boxes_list_input)):
        line += f' {i} '
    
    print(line)

# print_output(boxes_list)

# STEP 3: move the boxes!

print(boxes_list)
# convert the other lines into the moves... tuples in an array, maybe? then loop over the array? 
# use a STACK, which is just a list in python using only .pop() and .append()

'''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 '''
 
'''(number_to_move, stack_source, stack_dest)'''
(1, 2, 1)

print('*' * 50)

for move_index in range(len(list_of_moves)):

    # unpack
    move_tuple = list_of_moves[move_index]
    number_to_move, stack_source, stack_dest = move_tuple

    # loop over number
    for x in range(number_to_move):

        # pop one off source stack...
        temp_box = boxes_list[stack_source].pop()
        # ... append to dest stack
        boxes_list[stack_dest].append(temp_box)
        # print(boxes_list)

print(boxes_list)