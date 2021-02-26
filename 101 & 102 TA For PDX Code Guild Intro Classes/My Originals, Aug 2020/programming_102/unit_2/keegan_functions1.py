'''
Unit 2

- Read, Evaluate, Print, Loop (REPL)
- Functions
'''

# REPL

'''
play_again = 'yes' # loop control
while play_again == 'yes':
    # loop this 
    # code block
    print("Welcome!")


    play_again = input('Do you want to play again? yes/no: ')
'''
# --------------------- #

'''
# no variable needed, just a boolean
while True:
    # loop this
    # code block
    print('Welcome!')

    # ask the user if they want to repeat the loop
    play_again = input('Do you want to play again? y/n: ')

    if play_again == 'n':
        print('Goodbye!')
        break # end the loop
    # elif play_again == 'y': # this is optional because the
    #     continue            # code will only break with 'n'
'''
# ------------------------------- #
'''
# blank color list
colors = []
while True:
    # ask the user for a color
    color = input('Please enter a color or "done" to quit: ')

    # end the loop if the user enters done
    if color == 'done':
        print(colors)
        break

    # nested REPL to ensure the color is not already in the list
    while color in colors:
        print(f'{color} is already in the list!')
        color = input('Please enter a color: ')

    # feedback on a positive input
    print(f'{color} was successfully added to the list!')

    # add the color to the list
    colors.append(color)

    # end the loop once the user has entered 3 colors
    if len(colors) == 3:
        print(colors)
        break
'''