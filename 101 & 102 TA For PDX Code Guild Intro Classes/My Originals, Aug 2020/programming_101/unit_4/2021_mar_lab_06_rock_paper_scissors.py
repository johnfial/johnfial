# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/rps.md

import random
import time

def game(rounds=999):
    print('Welcome to rock, paper, scissors 2021 v2.2.20210305!')
    
    current_round = 1
    user_wins = 0
    user_losses = 0
    
    while current_round <= rounds:
        print(f'''~~~~~~~~~~~~~~~~~~~~~~~ Round {current_round} of {rounds}: ''', end="")
    
        user_choice = input('Please type either: rock, paper, or scissors: ~~~~~~~~~~~~~~~~ > ')

        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        print(f'The computer casts. . .')
        time.sleep(1)
        print(f'. . .{computer_choice.upper()}! ', end="")
        # print()
        
        # firure out how to wait the text...

        if user_choice in options:
            if user_choice == 'rock':
                    if computer_choice == 'scissors':
                        print('Your rock smashes feeble scissors and you win!')
                        user_wins += 1
                    elif computer_choice == 'paper':
                        print('Nobody knows why paper wraps rock, but it does. You lose!')
                        user_losses += 1
            if user_choice == 'paper':
                    if computer_choice == 'rock':
                        print('Nobody knows why paper wraps rock, but it does. You win!')
                        user_wins += 1
                    elif computer_choice == 'scissors':
                        print('You lose!')
                        user_losses += 1
            if user_choice == 'scissors':
                    if computer_choice == 'paper':
                        print('You cut and win!')
                        user_wins += 1
                    elif computer_choice == 'rock':
                        print('Your scissors are broken to bits! You lose!')
                        user_losses += 1
            if user_choice == computer_choice:
                print('You tied! Statistically very likely but no less boring!')
        else:
            print('Invalid entry!')

        current_round += 1

    print(f'TOTALS: wins: {user_wins} losses: {user_losses}.') #  Win percentage: {user_wins/user_losses}')

game(4)

# It's kinda ugly. Other than the for loop (i think) that lets them play again (and could have a counter to keep score), how can I clean this up?
# Keegan Good:pdxcodeguild:  4:56 PM
# You could do nested ifs for each choice
# if user has rock
#     if computer has paper
#     if computer has scissors
# The final advanced version talks about using a dictionary and that's really the best way to simplify this one.
# https://hackernoon.com/how-to-approach-any-coding-problem-9230f3ad6f9 
# This article https://medium.com/@dannysmith/breaking-down-problems-its-hard-when-you-re-learning-to-code-f10269f4ccd5 uses Ruby instead of Python, but the process is the same for thinking about the problems (edited) 