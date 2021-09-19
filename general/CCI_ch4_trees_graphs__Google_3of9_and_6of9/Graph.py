# EXAMPLE GRAPH WITH TWO UNCONNECTED SECTIONS, three nodes and four nodes:
# 'left' side:
# 6 ~~> 5 ~~> 4 ~~> 6

# 'right' side:
# 0  ~~> 1 ~~> 2 <~~> 3
# 2  ~~> 0

class GraphUndirected():
    def __init__(self, data):
        pass

ex_adjacency_list = {
    0: [1],
    1: [2],
    2: [3,0],
    3: [2],
    4: [6], 
    5: [4], 
    6: [5],
    }

# # # # 

class GraphDirected():

    # class GraphNode():
    #     def __init__(self, data, name: str=''):
    #         self.id = 0
    #         self.data = data
    #         self.name = name
    #         self.children = None # NOTE unsure how to write this, p 106...
    
    def __init__(self, data):
        self.data = data
        # for item in data:
        #     self.GraphNode(item)

    def depth_first_search(self, start_node):
        # depth first traversal
        # uses Stack(), because new nodes to explore in the future go on top of existing ones, and THAT node's neighbors go on the top of the stack.
        # NOTE from another series: # make a has_been_visited flag, otherwise will be infinite! ehh not with stack, will it?
        stack = [start_node, ]
        while len(stack) > 0:
            current = stack.pop()
            print(current)
            for neighbor in self.data[current]:
                stack.append(neighbor)
                # NOTE hint, 'process' node right when it ENTERS stack
    
    def depth_first_recursion(self, start_node):
        print(start_node)
        for neighbor in self.data[start_node]:
            self.depth_first_recursion(neighbor)
            # NOTE base case here has an empty node as a non-call line, but would this work in every case?

    def breadth_first_search(self, start_node):
        queue = [start_node]
        # NOTE commit to only remove by pop(0) removing from the FRONT
        # NOTE and pushing only via .append() to the end
        # NOTE that's the same as a queue FIFO !
        while len(queue) > 0:
            

        
        # Breadth first traversal Uses Queue(), because, we want first in first out to stay local...


ex_adjacency_list = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}
graph1 = GraphDirected(ex_adjacency_list)
# graph1.depth_first_search('a')
# graph1.depth_first_recursion('a')
graph1.breadth_first_search('a')


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