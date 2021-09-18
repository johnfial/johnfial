# EXAMPLE GRAPH WITH TWO UNCONNECTED SECTIONS, three nodes and four nodes:
# 'left' side:
# 6 ~~> 5 ~~> 4 ~~> 6

# 'right' side:
# 0  ~~> 1 ~~> 2 <~~> 3
# 2  ~~> 0

ex_adjacency_list = {
    0: 1,
    1: 2,
    2: [3,0],
    3: 2,
    4: 6, 
    5: 4, 
    6: 5,
    }

# # # # 


class GraphDirected():

    class GraphNode():
        def __init__(self, data, name: str=''):
            self.id = 0
            self.data = data
            self.name = name
            self.children = None # NOTE unsure how to write this, p 106...
    
    def __init__(self, data):
        self.data = data
        for item in data:
            self.GraphNode(item)

    def depth_first_search(self):
        # NOTE:
        # recursive...
        # make a has_been_visited flag, otherwise will be infinite!
        pass
    def breadth_first_search(self):
        # use a queue!
        pass


class GraphUndirected():
    def __init__(self, data):
        pass

graph1 = GraphDirected([55, 11, 999, ])
print(graph1.data)
print(len(graph1.data))
