

#################################################################
# 2022-12-01

print('*' * 50)

example = '''
2494
8013
1055
5425
9104
10665'''
# each elf inventory sep by newline
# so which elf is carrying the MOST calories? 

# create a list
# populate with each number
# 2d array?

calories_list = example.split('\n')

counter = -1
elves_calories = []

for calorie in calories_list:

    if calorie == '':
        elves_calories.append(0)
        counter += 1
        continue
    # print(elves_calories, calorie, '***aoeu') # ERROR HERE trying to add int of '', either remove this or...
    # print(calorie)
    elves_calories[counter] += int(calorie)
    # print(calorie)
# print(max(elves_calories))
# maximum = 0
# print(maximum)
# maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
# print(maximum)
# maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
# print(maximum)
# maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
# print(maximum)
# REMEMBER ACTUAL DATA -- NOT EXAMPLE!

################################################################################

# day 2 rock paper scissors

# make a dict of the possibilities and points
p1 = {
    'A': 'rock', 
    'B': 'paper', 
    'C': 'scissors'}
p2 = {'X': 'rock', 
    'Y': 'paper', 
    'Z': 'scissors'}

options = ['rock', 'paper', 'scissors']

# create english dictionary
rps_dictionary = {}
for perm1 in options:
    for perm2 in options:

        # give tie points
        if perm1 == perm2:
            rps_dictionary[(perm1, perm2)] = (3, 3)
        
        # if p1 wins, give 6, 0
        if (perm1 == 'scissors' and perm2 == 'paper' ) or (perm1 == 'rock' and perm2 == 'scissors') or (perm1 == 'paper' and perm2 == 'rock'):
            rps_dictionary[(perm1, perm2)] = (6, 0)
        # if p2 wins, give 0, 6
        if (perm2 == 'scissors' and perm1 == 'paper' ) or (perm2 == 'rock' and perm1 == 'scissors') or (perm2 == 'paper' and perm1 == 'rock'):
            rps_dictionary[(perm1, perm2)] = (6, 0)
# print(rps_dictionary, '<<<<<<<<<< printing here') # 
#   {('rock', 'rock'): (3, 3), ('rock', 'paper'): (6, 0), ('rock', 'scissors'): (6, 0), ('paper', 'rock'): (6, 0), ('paper', 'paper'): (3, 3), ('paper', 'scissors'): (6, 0), ('scissors', 'rock'): (6, 0), ('scissors', 'paper'): (6, 0), ('scissors', 'scissors'): (3, 3)} <<<<<<<<<< printing here
       
# initialize scores
player_1 = 0
player_2 = 0

# actual
file_to_open = 'input_2022_day2.txt'
with open(file_to_open, 'r') as file:
    input = file.read()
rps_list = input.split('\n')

# # example:
# day2_partial_1= '''A Y
# B X
# C Z'''
# rps_list = day2_partial_1.split('\n') # ['A Y', 'B X', 'C Z']

i=0
for item in rps_list:
    # temp indice counter to limit rounds:
    i += 1
    if i > 9:
        break
    
    # place the 'A' and 'Y' in indices 0 and 2 into a tuple of two strings
    temp = (item[0], item[2])
    # print(temp)

    # lookup each in the identical dictionaries ()
    translated = ((p1[temp[0]]),(p2[temp[1]]))
    print(translated)

    round_score = rps_dictionary[translated]
    player_1 += round_score[0]
    player_2 += round_score[1]
    
    # print(f'~~~ROUND {i}~~~\n~player_1 casts {translated[0]}, player 2 casts {translated[1]}, for scores of {round_score}.\n~Currently player_1 score: {player_1}, player_2 score: {player_2} <<<< end round {[i]}')
    

print(f'~~~FINAL SCORES: ~~~\nPlayer 1 = {player_1} and Player 2 = {player_2}')
# WRONG ANSWER
# Player 1 = 13755 and Player 2 = 1245
# 13755 IS TOO HIGH! #13749 too high as well


'''
For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
'''

