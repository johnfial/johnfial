# 10.7 
# Missing Integer:
# Given a file with 4 B non-negative integers, provide an algorithm to generate an integer that is not contained
# in the file. Assume you have 1GB of memory available for this task.

# FOLLOW UP: What if you only have 10MB of memry? Now assume that the values are
#  all DISTINCT and we now have no more than 1 B non-negative integers.

# Hints: 235, 524, 281


# Brainstorm
# first step is to ignore memory constraints, give a human-size number of integers, and generate a unique one
# figure out the big-O of this, good exercise for it!
# then work within increasingly restrictive memory constraints

data = [1, 5, 7, 9, 8, 2, 4, 5, 5, 5, 5, 6, 3, 5, 8, 7, 9, 15, 384, 967, 45, 50, ] # all positive!

def missing_int(input):
    print(len(input))

    # V1
    # 4,000,000,000 integers (4 B)
    # 1 GB memory

    # V2
    # 1,000,000,000 integers (1 B)
    # 10MB memory

    # FIRST TRY, WORKS BUT HOW'S THE MEMORY CONSTRAINTS? DOES IT PASS?
    print(f'starting loop...')
    for x in range(len(input)):
        if x == 0:
            pass
        elif x not in input:
            print(f'{x} not in data list!')
            print(f'adding {x} to the list')
            
            input.append(x)
            print(f'len(input) now = {len(input)}')
            return input
        else:
            print(f'{x} found in data list!')


missing_int(data)