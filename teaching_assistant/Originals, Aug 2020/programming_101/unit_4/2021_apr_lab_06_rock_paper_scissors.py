# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/rps.md

import random
import time

def rock_paper_scissors():
    print('Welcome to rock, paper, scissors 2021 v2.3.20210429!')

    current_round = 1
    user_wins = 0
    user_losses = 0

    while True:
        print(f'''Round {current_round}: ''', end="")

        choices_list = ['rock', 'paper', 'scissors', 'quit']

        print('Please type from the following four choices: ')
        for choice in choices_list:
            print(choice)
        user_choice = input('~~~~~~~~~~~~~~~~ input > ')


        if user_choice in choices_list:
            if user_choice == 'quit':
                break
            
            computer_choice = random.choice(choices_list[0:2]) # slice off the 'quit' choice!
            print(f'The computer casts. . .')
            time.sleep(1)
            print(f'{computer_choice.upper()}! ') # , end="")

            if user_choice == 'rock':
                    if computer_choice == 'scissors':
                        print('Your rock smashes feeble scissors and you win!')
                        user_wins += 1
                        current_round += 1
                    elif computer_choice == 'paper':
                        print('Nobody knows why paper wraps rock, but it does. You lose!')
                        user_losses += 1
                        current_round += 1
            if user_choice == 'paper':
                    if computer_choice == 'rock':
                        print('Nobody knows why paper wraps rock, but it does. You win!')
                        user_wins += 1
                        current_round += 1
                    elif computer_choice == 'scissors':
                        print('You lose!')
                        user_losses += 1
                        current_round += 1
            if user_choice == 'scissors':
                    if computer_choice == 'paper':
                        print('You cut and win!')
                        user_wins += 1
                        current_round += 1
                    elif computer_choice == 'rock':
                        print('Your scissors are broken to bits! You lose!')
                        user_losses += 1
                        current_round += 1
            if user_choice == computer_choice:
                print('You tied! Statistically very likely but no less boring!')
                current_round += 1
        else:
            print('Invalid entry!')

    # BUG division by 0 if they don't play...
    print(f'TOTALS: wins: {user_wins} losses: {user_losses}.') # Win percentage: {user_wins/user_losses}')

rock_paper_scissors()
