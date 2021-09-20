from Graph import Graph

ex_adjacency_list = {
    0: [1],
    1: [2],
    2: [3,0],
    3: [2],
    4: [6], 
    5: [4], 
    6: [5],
    }

ex_adjacency_list = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': ['q'],
    'f': [],
    'q':[],
    'y':['z'],
    'z':[],
}
graph1 = Graph(ex_adjacency_list)
# graph1.depth_first_search('a')
# graph1.breadth_first_search('a')
# print(graph1.depth_first_recursion('a'))
# print(graph1.has_path_DFS_recursive('a', 'e'))
# print(graph1.has_path_BFS('y', 'z'))
print(graph1.has_path_DFS_recursive('a', 'q'))

# print(graph1.data)
# print(len(graph1.data))

# test = []
# print(f'len = {len(test)}')
# test.append(5)
# test.append(3)
# test.append(1)
# print(f'len = {len(test)}')
# print(test.pop())
# print(f'len = {len(test)}')
# print(test.pop())
# print(f'len = {len(test)}')
# print(test.pop())
# print(f'len = {len(test)}')
