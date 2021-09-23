
# needs BFS
# ...which uses a Queue
# so should use (node, distance) for each item in queue
# queue = list.pop(0) and list.append
# neighbors all have distance + 1, so .append([neighbor,dist+1])
# track visited...

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# https://structy.net/problems/shortest-path
# shortest path

# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.
# test_00:

# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# shortest_path(edges, 'w', 'z') # -> 2

# test_01:

# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# shortest_path(edges, 'y', 'x') # -> 1