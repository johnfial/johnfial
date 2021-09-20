# find island size
# store as min size
# IF min = 1, return that right away?!
# 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://structy.net/problems/minimum-island

# minimum island

# Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.
# test_00:

# const grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ];

# minimumIsland(grid); // -> 2

# test_01:

# const grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ];

# minimumIsland(grid); // -> 1

# test_02:

# const grid = [
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
# ];

# minimumIsland(grid); // -> 9