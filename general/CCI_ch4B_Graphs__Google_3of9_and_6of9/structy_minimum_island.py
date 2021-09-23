def minimum_island(grid):
    
    visited = set()
    island_sizes = float('inf')
    island_sizes = []

    for row in range(len(grid)-1):
        for column in range(len(grid[row])-1):
            print(f'entering @ row, col: {row, column}')
            size = explore_size(grid, row, column, visited)
            print(f'adding island of size {size} with posit {row, column}')
            if size >= 1:
                island_sizes.append(size)
    
    return min(island_sizes)

def explore_size(grid, row, column, visited):
    
    row_inbounds = (0 <= row) and (row <= len(grid)-1)
    col_inbounds = (0 <= column) and (column <= len(grid[0])-1)
    print(f'entering @ row, col: {row, column} with row_inbounds, col_inbounds: {row_inbounds, col_inbounds}')
    if not row_inbounds or not col_inbounds:
        return 0

    if grid[row][column] == 'W': return 0

    # store the posit as a nice string, check if in set
    position = str(row) + ',' + str(column)
    if position in visited:
        print(f'visited {position} already')
        return 0
    visited.add(position)
    print(position)

    # NOTE explore neighbors:
    # if we made it here, now explore neighbors, and by default we are on land
    # also note if this were diagonal, we'd have eight combinations...
    size = 1
    size += explore_size(grid, row-1, column  , visited)
    size += explore_size(grid, row  , column-1, visited)
    size += explore_size(grid, row+1, column  , visited)
    size += explore_size(grid, row  , column+1, visited)

    return size

grid01 = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
grid02 = []

grid03 = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimum_island(grid03))



# minimum island

# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.
# test_00:


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