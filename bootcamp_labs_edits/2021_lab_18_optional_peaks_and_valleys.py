##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab18-peaks_and_valleys.md
##############################################################################

# Step 1 Enter Data list
data = [3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13]
data_original = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]  # peaks 7, 9, 9, 16






data = [1, 2, 3, 8, 4, 5, ]

# hints:
# max(array) will return the highest #...
# for x in range (length list)
    # line_to_print += ' '

print(data)

max_height = max(data)
current_elevation = max(data)
for y in range(max_height):  # one print line for each up to the max height
    
    line = ''

    for x in range(len(data)):
        character = ' '
        if data[x] < current_elevation:
            character = ' '
        elif data[x] >= current_elevation:
            character = 'X'
        line += character

    print(f'current elevation is {current_elevation}, line y={y}: {line}')
    current_elevation -= 1










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

