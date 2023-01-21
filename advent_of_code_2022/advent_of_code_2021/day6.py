# https://adventofcode.com/2021/day/6

# basically just the jacaloupe lab, little more complex

# 1 input and modify file
file_to_open = 'day6.txt'
with open(file_to_open, 'r') as file:
    input = file.read()
output = input.split(',')

# convert to integers
for i in range(len(output)):
    output[i] = int(output[i])

# # show input day6.txt
# print(output, len(output), type(output))

# https://adventofcode.com/2021/day/6
def lanternfish_reproduce(input, days=80):
    # for each lanternfish in list
    
    day = 0
    while day <days:
        temp = []
        for fish in input:

            # if # > 0, new is number minus 1
            if fish > 0:
                temp.append(fish-1)
            
            # if number == 0, then... number = 6, and append new 8
            if fish == 0:
                temp.append(6)  # old fish reset to 7
                temp.append(8)  # new fish        
        input = temp.copy()
        # print(f'After {day+1} days, input={input}, there are {len(input)} fish')
        print(f'After {day+1} days, there are {len(input)} fish')
        day += 1
        
    return input

lanternfish_reproduce(output)

example = [3,4,3,1,2,]
days = 18
# lanternfish_reproduce(example)

print('*' * 50)
def jackaloup_lab():
    population = [0,0]    # jackalope population
    year = 2000    # goes up 1

    while len(population) < 1000:

        # print(f'{year} is year, START of while loop...')

        # Increase age by 1 for each jack in population
        for i in range(len(population)):
            # print(f'A {age}-year old jack from list {population} ... ')
            # new_age = age
            population[i] += 1
            # print(f'... becomes a {i + 1}-year old jack from list {population}. ')

        year += 1

        # print(f'len(population) is {len(population)} and list is {population}')

        babies = []
        for x in population:
            if x > 3 and x < 9:
                # print(x)
                babies.append(0)

        # print(f'population is {(population)}')

        # Add babies to the main population
        population.extend(babies)

        # BELOW WAS THE DUMBER, MORE COMPLICATED WAY to kill off the elders. Worked <200, started to give list index errors greater than 300 or so...
        # for i in range(-1,-len(population),-1):
        #     # print(f'i is {i}')
        #     if population[i] > 10:
        #         population.pop(i)
        #         # population.remove(population[i])

        # ... But after letting us mull it over... Steve shared https://pythonexamples.org/python-remove-all-occurrences-of-item-from-list/
        # ...which reminded us of the 2 (or even 1) line version:
        while 11 in population:
            population.remove(11)

        # print(f'Year is {year}, len(babies) is {len(babies)}, len(population) is {len(population)}. End of while loop...')


    # # Final print
    print(f'Final JACKALOUP len(population) is {len(population)}, and year={year}!')

# print(jackaloup_lab())



'''
--- Day 6: Lanternfish ---

The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

So, suppose you have a lanternfish with an internal timer value of 3:

    After one day, its internal timer would become 2.
    After another day, its internal timer would become 1.
    After another day, its internal timer would become 0.
    After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
    After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

3,4,3,1,2

This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.

Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

To begin, get your puzzle input.

'''