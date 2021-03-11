# https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_2/exercise_1.md

def counting():

    again = 'yes'
    counter = 0

    while again == 'yes':
        again = input('Play again? yes/no: ')
        counter += 1

    if again == 'no' or 'done':
        print(f'The loop ran {counter} times. Goodbye.')

    else:
        print('Input error!')
        # break # ERROR break outside loop

counting()


# site solution:

    # # create a counter variable to
    # # to count loop iterations
    # counter = 0

    # # begin a REPL
    # while True:
    #     # count the current iteration
    #     counter += 1

    #     # ask the user if they want the run the loop again?
    #     again = input('Again? yes/no: ')

    #     # if the user enters 'no'
    #     if again == 'no':
    #         # tell the user how many times the loop ran
    #         print(f'The loop ran {counter} times.')

    #         # end the loop
    #         break
