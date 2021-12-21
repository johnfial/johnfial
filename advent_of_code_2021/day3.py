# https://adventofcode.com/2021/day/3

# 1 input and modify file
file_to_open = 'day3.txt'
with open(file_to_open, 'r') as file:
    input = file.read()
output = input.split('\n')

output = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
output = output.split('\n')


print(output, len(output), type(output))

# https://adventofcode.com/2021/day/3
def power_consumption(input):
    
    # STEPS:
    # create a list of strings
    # loop through each position in all strings, finding MOST and LEAST common bit
    dict = {
        # i: count,
        '0_0': 0,
        '0_1': 0,
        '1_0': 0,
        '1_1': 0,
        '2_0': 0,
        '2_1': 0,
        '3_0': 0,
        '3_1': 0,
        '4_0': 0,
        '4_1': 0,
        '5_0': 0,
        '5_1': 0,
    }

    # TODO problematic
    for string in input:
        for x in range(len(string)):
            print(string[x])
            if string[x] == 0:
                dict[str(x) + '_0'] = dict[str(x) + '_0'] + 1
            elif string[x] == 1:
                dict[str(x) + '_1'] = dict[str(x) + '_1'] + 1
            else:
                print('wtf?!?!?')
    # count results
    most_freq = ''
    least_freq = ''
    for x in range(len(input[0])):
        if dict[str(x) + '_0'] > dict[str(x) + '_1']:
            most_freq += "0"
            least_freq += "1"
        else:
            most_freq += "1"
            least_freq += "0"
    print(f'{most_freq} and {least_freq} and dict {dict}')

    # take those two end results and convert to binary
    # multiply those two decimal numbers together

    return 

print(power_consumption(output))
print('*' * 20)




'''
# --- Day 3: Binary Diagnostic ---

# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010

# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

# So, the gamma rate is the binary number 10110, or 22 in decimal.

# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
'''