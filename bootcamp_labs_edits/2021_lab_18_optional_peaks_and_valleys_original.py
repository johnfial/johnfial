##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab18-peaks_and_valleys.md
##############################################################################

# Step 1 Enter Data list
data = [3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13]
# peaks 7, 9, 9, 16
# valleys

# Step 2 Make a peak function
# Which checks if the number is both greater than index(num-1) AND index(num+1)
def check_peaks(data_input):
    peaks = []
    counter = 0
    try: # try works because at the end of the list, there's an index error
        for i in data_input:
            if data_input[counter-1] < data_input[counter] > data_input[counter+1]:
                # print(i)
                peaks.append(data_input[counter])
                counter += 1
            else:
                counter += 1
    except:
        pass

    # .print(peaks)
    return peaks


# Step 3 Then a valley function
# Which checks if the number is both less than index(num-1) AND index(num+1)
def find_valleys(data_input):

    valleys = []
    counter = 0

    try: # try works because at the end of the list, there's an index error
        for i in data_input:
            if data_input[counter-1] > data_input[counter] < data_input[counter+1]:
                valleys.append(data_input[counter])
                counter += 1
            else:
                counter += 1
    except:
        pass
    return valleys


# Step 4 Then a combined function (or something like that) to make them into a single list -- NOT sorted, right?
def peaks_and_valleys(peaks,valleys):
    peaks_and_valleys = peaks + valleys
    peaks_and_valleys.sort()
    return peaks_and_valleys

peaks = check_peaks(data)
# print(f'peaks are at {peaks}')
valleys = find_valleys(data)
# print(f'valleys are at {valleys}')
# print(f'sorted peaks and valleys are at {peaks_and_valleys(peaks,valleys)}')




def print_xs(data_input):

    height = max(data_input)

    print(f'len(data1) is {len(data_input)}')
    print(f'height is {height}')

    # THIS LINE RUNS TOTAL TIMES FOR HEIGHT, ONE PRINT STATEMENT PER HEIGHT OF DATA
    # LINE = ONE PRINT STATEMENT, FOR ENTIRE X AXIS
    # FOR EACH LINE IN 
    
    # vertical
    for x in range (len(data_input)):
        line = '' # '0' + ('X' * x) + '0'
        for y in range(height):
            print((height - data_input[x]) * '0')

        # print('X' * data_input[x])

    
    # mattew's code similar:
    # for y in data_input:
    #     # print(i)
    #     print('X' * y)


data = [] # overwrites top of file
data1 = [3,4,5]
data2 = [1, 2, 3, 6, 2]
print_xs(data1)


# ***************************** WORKING FROM HERE *****************************




# Step 5 V2 DRAW THE X'S ...

# don't think as print statement
# think as x-y axis!











# ***************************** ^^^^^^^^^ TO HERE ****************************


# Step 6 V3 POUR WATER ONTO HILLS... # 6a Basically... for each valley. take the difference between it and the nearest peak (control for edge possibilites), and calculate the width (index) and height (numbers) and use that to calculate water...



















print('    >> PROGRAM ENDED <<    ')
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab18-peaks_and_valleys.md
##############################################################################

# Lab 18: Peaks and Valleys

# Define the following functions:

#     peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#     valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

#     peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# Visualization of test data:
# Data 	1 	2 	3 	4 	5 	6 	7 	6 	5 	4 	5 	6 	7 	8 	9 	8 	7 	6 	7 	8 	9
# Index 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20
# POI 							P 			V 					P 			V 			

# Example I/O:

#                                                       X                 X
#                                                    X  X  X           X  X
#                               X                 X  X  X  X  X     X  X  X
#                            X  X  X           X  X  X  X  X  X  X  X  X  X
#                         X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
#                      X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                   X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# >>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]

# Version 2 (optional)

# Using the data list above, draw the image of X's above.
# Version 3 (optional)

# Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

#                                                   X  O  O  O  O  O  X
#                                                X  X  X  O  O  O  X  X
#                           X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
#                        X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
#                     X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
#                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#         X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

