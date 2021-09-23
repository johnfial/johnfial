# https://structy.net/problems/island-count
# 
# island count

# Write a function, islandCount, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. The function should return the 
# number of islands on the grid. An island is a vertically or horizontally
# connected region of land.
# test_00:

# TODO brainstorm:
# for each square, find neighbors with L
# add to group, same as 
# POSITION = row, column
# IF check if exists...

# if current posit is land
# IF land, explore DFS, MARK AS VISITED
# A) increment a count, AND ALSO B) add a 'name of island' 

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

# islandCount(grid); // -> 3

# test_01:

# const grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ];

# islandCount(grid); // -> 4