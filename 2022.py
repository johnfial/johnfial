

#################################################################
# 2022-12-01

print('*' * 50)

example = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
# each elf inventory sep by newline
# so which elf is carrying the MOST calories? 

# create a list
# populate with each number
# 2d array?

print_output = example.split('\n')
print(print_output)

counter = -1
elves_calories = []

for item in print_output:

    if item == '':
        elves_calories.append(0)
        counter += 1
    print(elves_calories, item, '***aoeu') # ERROR HERE trying to add int of '', either remove this or...
    print(item)
    elves_calories[counter] += int(item)
    print(item)
print(elves_calories)