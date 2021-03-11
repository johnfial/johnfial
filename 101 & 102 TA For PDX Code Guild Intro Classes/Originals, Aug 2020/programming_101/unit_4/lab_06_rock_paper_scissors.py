# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/rps.md

import random

print('Welcome to rock, paper, scissors v1.57386.52.20200903!')
user_choice = input('Please select your choice of rock, paper, or scissors: ')

options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)
print(f'The computer cast. . .: {computer_choice}') # firure out how to wait the text...

if user_choice == 'rock' and computer_choice == 'scissors':
    print('Your rock smashes feeble scissors and you win!')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('Nobody knows why paper wraps rock, but it does. You lose!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Nobody knows why paper wraps rock, but it does. You win!')
elif user_choice == 'paper' and computer_choice == 'scissors':
    print('You lose!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You cut and win!')
elif user_choice == 'scissors' and computer_choice == 'rock':
    print('Your scissors are broken to bits! You lose!')
elif user_choice == computer_choice:
    print('You tied! Statistically very likely but no less boring!')
else:
    print('Invalid entry!')


# It's kinda ugly. Other than the for loop (i think) that lets them play again (and could have a counter to keep score), how can I clean this up?
# Keegan Good:pdxcodeguild:  4:56 PM
# You could do nested ifs for each choice
# if user has rock
#     if computer has paper
#     if computer has scissors
# The final advanced version talks about using a dictionary and that's really the best way to simplify this one.
# https://hackernoon.com/how-to-approach-any-coding-problem-9230f3ad6f9 
# This article https://medium.com/@dannysmith/breaking-down-problems-its-hard-when-you-re-learning-to-code-f10269f4ccd5 uses Ruby instead of Python, but the process is the same for thinking about the problems (edited) 