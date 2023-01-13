# https://adventofcode.com/2022/day/4
'''
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?'''

example_1 = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

# # example:
list_of_assignments = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
list_of_assignments = example_1.split('\n')
# print(list_of_assignments)  # ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

# actual:
file_to_open = 'day4.txt'
with open(file_to_open, 'r') as file:
    input = file.read()
list_of_assignments = input.split('\n')

count = 0           # part 1
overlap_at_all = 0  # part 2

for i in range(len(list_of_assignments)):

    # if i > 0: break  # for testing

    # for each pair of elves, 'temp' variable to convert to end results and increment counter(s)
    temp = list_of_assignments[i]
    temp = temp.split(',')
    # print(temp)
    
    # for a/b (range(2)), gets the range separated by '-' into a list of two sets, as "temp" variable...
    for x in range(2): 
        
        group_range = temp[x].split('-') # creates a two item list[]
        # print(group_range)

        # using num_current, iterates through the range creating a set {} with those numbers
        num_current = int(group_range[0])
        num_end = int(group_range[1])
        group_range = set()
        while num_current <= num_end:
            group_range.add(num_current)
            num_current += 1
        
        # place that group range back into the a/b half of the 'temp' variable
        temp[x] = group_range
        # print(f'<<< end group_range = {group_range}, print(type(group_range)) = {type(group_range)}')

    # --- Part One --- ...checks if one set overlaps...

    # print(temp[0],  type(temp[0]), '<<<< temp[0]', ">>>>> temp[1]", type(temp[1]), temp[1])    
    if (temp[0].issuperset(temp[1]) == True) or (temp[1].issuperset(temp[0]) == True):
        # print('~~~~COUNTER DING!')
        count += 1
    
    # --- Part Two --- 
    
    if (temp[0].isdisjoint(temp[1]) == False) or (temp[1].isdisjoint(temp[0]) == False):
        # print('~~~~COUNTER DING!')
        overlap_at_all += 1

    # set the temp back into the list, which is unnecessary for this problem, but could be useful
    list_of_assignments[i] = temp

# print(f'list_of_assignments {list_of_assignments}, and count={count}, overlap_at_all = {overlap_at_all}')
print(f'count={count}, overlap_at_all = {overlap_at_all}')



'''
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''