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

# for part 2:
strategy_lookup = {
    # ('opponent', 'goal'): 'play',
    ('rock', 'X'): 'scissors',
    ('rock', 'Y'): 'rock',
    ('rock', 'Z'): 'paper',
    ('paper', 'X'): 'rock',
    ('paper', 'Y'): 'paper',
    ('paper', 'Z'): 'scissors',
    ('scissors', 'X'): 'paper',
    ('scissors', 'Y'): 'scissors',
    ('scissors', 'Z'): 'rock',
}

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
            rps_dictionary[(perm1, perm2)] = (0, 6)
        
        # add the values of 1/2/3 for r/p/s:
        # print(rps_dictionary[(perm1, perm2)], 'newline', (perm1, perm2))
        temp_scores = rps_dictionary[perm1, perm2]

        # brute force way...
        if perm1 == 'rock':
            temp_scores = (temp_scores[0] + 1 , temp_scores[1])
        if perm1 == 'paper':
            temp_scores = (temp_scores[0] + 2 , temp_scores[1])
        if perm1 == 'scissors':
            temp_scores = (temp_scores[0] + 3 , temp_scores[1])
         

        if perm2 == 'rock':
            temp_scores = (temp_scores[0], temp_scores[1] + 1 )
        if perm2 == 'paper':
            temp_scores = (temp_scores[0], temp_scores[1] + 2 )
        if perm2 == 'scissors':
            temp_scores = (temp_scores[0], temp_scores[1] + 3 )
         
        # better way to just add (1, 2, or 3) to the player's index, but not sure how to code this...
        # print(options.index(perm1), '<<<options.index')
        # temp_scores = rps_dictionary[(perm1, perm2)]
        # temp_roll = (perm1, perm2)
        # for x in range(2):
        #     print(x)
        #     hand = options.index(player)
        #     if hand == 0:
        #         temp_scores

        rps_dictionary[(perm1, perm2)] = temp_scores

# print(rps_dictionary) # 
#   {('rock', 'rock'): (3, 3), ('rock', 'paper'): (6, 0), ('rock', 'scissors'): (6, 0), ('paper', 'rock'): (6, 0), ('paper', 'paper'): (3, 3), ('paper', 'scissors'): (6, 0), ('scissors', 'rock'): (6, 0), ('scissors', 'paper'): (6, 0), ('scissors', 'scissors'): (3, 3)} <<<<<<<<<< printing here
       
# initialize scores
opponent = 0
you = 0

# # example:
day2_partial_1= '''A Y
B X
C Z'''
rps_list = day2_partial_1.split('\n') # ['A Y', 'B X', 'C Z']

# actual
file_to_open = 'input_2022_day2.txt'
with open(file_to_open, 'r') as file:
    input = file.read()
rps_list = input.split('\n')

i=0
for item in rps_list:

        # temp indice counter to limit rounds:
    # i += 1
    # if i > 9:
    #     break
    
        # place the 'A' and 'Y' in indices 0 and 2 into a tuple of two strings
    temp = (item[0], item[2])

    ### START OPTIONAL PART 1/2 PATH
    #### LOGIC FOR PART 1 OF 2 ###

        # lookup each in the identical dictionaries ()
    translated = ((p1[temp[0]]),(p2[temp[1]]))
    
    #### LOGIC FOR PART 2 OF 2 ###, COMMENT OUT FOR PART 1:
    
        # send a tuple of the (opponent's move, goal) into the strategy_lookup dict:
    strategy_input = (translated[0], item[2])
    translated_part_2 =  (translated[0], strategy_lookup[strategy_input])    #     print(translated_part_2)

    ### END OPTIONAL PART 1/2 PATH (below calculation is the same for both parts)
    round_score = rps_dictionary[translated_part_2]
    opponent += round_score[0]
    you += round_score[1]

    # print(f'~~~ROUND {i}~~~\n~opponent casts {translated[0]}, you cast {translated[1]}, for scores of {round_score}.\n~Currently opponent score: {opponent}, you score: {you} <<<< end round {[i]}')
    

print(f'~~~FINAL SCORES: ~~~\ opponent = {opponent} and you = {you}')

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

