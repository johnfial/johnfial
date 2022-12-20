

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
# print(elves_calories)
print(max(elves_calories))
maximum = 0
print(maximum)
maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
print(maximum)
maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
print(maximum)
maximum += elves_calories.pop(elves_calories.index(max(elves_calories)))
print(maximum)
# 211107 IS WRONG, TOO HIGH

# REMEMBER ACTUAL DATA -- NOT EXAMPLE!
