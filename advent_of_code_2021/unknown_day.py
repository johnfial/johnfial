# not sure which day, but day 7 was before and day 21 was next page... could be d21 actually?

from advent_of_code_2021.day21 import roll_dice


def function_name(input_here):
    die_current = 1
    something = None

    die_rolled_times = 0
    p1_posit = 0 #input
    p2_posit = 0 # input
    p1_score = 0
    p2_score = 0

    # check logic:
    if p1_posit >= 1000:
        output_3 = p2_score + die_rolled_times
    #elif ...
    # turn...
    while p1_score < 1000: # and p2_posit ...
        turn += 1
        if turn % 1 == 1:
            pass #p1 logic
        elif turn %1 == 0:
            pass #p2 logic
    die_rolled_times += 0 # something
    # roll_die (die_current)
    p1_posit = ((p1_posit + roll_dice()) % 10)
    p1_score + p1_posit


    return something