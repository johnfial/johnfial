##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab19-blackjack_advice.md
# NOTE do v2!
##############################################################################

card_values = {
    'A': 1,     
    '2': 2,     
    '3': 3,     
    '4': 4,     
    '5': 5,
    '6': 6,     
    '7': 7,     
    '8': 8,     
    '9': 9,     
    '10': 10,
    'J': 10,     
    'Q': 10,     
    'K': 10, 
    'AA': 11, #unnecessary now
    }

def generate_blackjack_advice(total_points):
    # 4 compare with simple if conditional their value to the <17, 17-21, 21, or >21 options
    # 5 print out the total point value
    # 6 and print the advice of what to do
    if total_points < 17:
        advice_output = f'Your total so far is {total_points}, and it is advised that you: Hit!'
    elif 16 < total_points < 21:
        advice_output = f'Your total so far is {total_points}, and it is advised that you: Stay!'
    elif total_points == 21:
        advice_output = f'Your total so far is {total_points}, exactly 21. Blackjack!'
    elif total_points > 21:
        advice_output = f'Your total so far is {total_points}: sorry, you already busted!'
    else: 
        advice_output = 'Error encountered!'
    return advice_output

def main():
    # Welcome message
    print('''Welcome to Blackjack v1.0! Please do not break or hack!
    Acceptable inputs are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.''')

    # 3 make a total variable and add all three of their inputs to it
    total_points = 0

    # 1 Ask user for three cards - three inputs # NOTE comment/uncomment sections 1/2 for testing
    # card_1 = input('Please input your first card: ').upper() # BUG UNALLOWED INPUT
    # card_2 = input('Please input your second card: ').upper()
    # card_3 = input('Please input your third card: ').upper()

    # 2 Then temporarily comment out those three inputs in order to more easily test with preset card values each time:
    card_1 = 'A'
    card_2 = 'J'
    card_3 = '5'

    if card_1 == 'A' or card_1 == 'A' or card_1 == 'A':
        print('we have an ace!')
        # total_points += 11

    total_points += card_values.get(card_1)
    total_points += card_values.get(card_2)
    total_points += card_values.get(card_3)

    print(generate_blackjack_advice(total_points))

main()









##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab19-blackjack_advice.md
##############################################################################
# Lab 19: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player 
# for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, 
# all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to 
# determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

# Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of both cards over 21. 
# Remember that you can have multiple aces in a hand. Try generating a list of all possible hand 
# values by doubling the number of values in the output whenever you encounter an ace. 
# For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you 
# account for the full range of possible values.
##############################################################################