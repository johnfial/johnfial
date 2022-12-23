

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

day2_partial_1 = '''C Y
A Z
B X
C Y
B Y
C X
C Y
B X
B X
A Z
C X
B Y
B X
B X
A Z'''




# print(rps_list)
# print(len(rps_list))

# make a dict of the possibilities and points
rps_dictionary = {
}
p1 = {
    'A': 'rock', 
    'B': 'paper', 
    'C': 'scissors'}
p2 = {'X': 'rock', 
    'Y': 'paper', 
    'Z': 'scissors'}

# for item in p1:
    
#     total = 000
options = ['rock', 'paper', 'scissors']
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
        
print(rps_dictionary, '<<<<<<<<<< printing here')

player_1 = 0
player_2 = 0
day2_partial_1= '''A Y
B X
C Z'''
# input data to an easy format... list of tuples?
rps_list = day2_partial_1.split('\n') # ['A Y', 'B X', 'C Z']

i=0

for item in rps_list:
    
    temp = (item[0], item[2])
    print(temp)
    # printout = (rps_dictionary[1], rps_dictionary[1])
    
    rps_list[i] = temp
    
    i += 1

    print(player_1, player_2, f"<<<< end round {[i]}")

# print(rps_list)
# give each player points for what they play EACH round -- 1 rock, 2 paper, 3 scissors
# A and X rock, 1 
# B and Y paper, 2
# C and Z scissors, 3
# then give either 3 + 3 for draw, or 0/6 6/0 points for a winner


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

