# NOTE TODO UNDONE:
# undirected path problem where adjacency_list below:
adjacency_list = {
    'a': 'b',
    # etc, because edges are undirected, or two-way
}

class Graph():

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
            print(f'visiting: {current}')
            for neighbor in self.data[current]:
                stack.append(neighbor)
                # NOTE hint, 'process' node right when it ENTERS stack
    
    def depth_first_recursion(self, start_node):
        print(f'visiting: {start_node}')
        for neighbor in self.data[start_node]:
            self.depth_first_recursion(neighbor)
            # NOTE base case here has an empty node as a non-call line, but would this work in every case?
            # return neighbor

    def breadth_first_search(self, start_node):
        queue = [start_node]
        # NOTE commit to only remove by pop(0) removing from the FRONT
        # NOTE and pushing only via .append() to the end
        # NOTE that's the same as a queue FIFO !
        while len(queue) > 0:
            current = queue.pop(0)
            print(f'visiting: {current}')
            for neighbor in self.data[current]:
                queue.append(neighbor)
        
        # Breadth first traversal Uses Queue(), because, we want first in first out to stay local...

    def has_path_DFS_recursive(self, source, destination, path=[]):
        if path == []:
            path.append(source)
        # https://structy.net/problems/has-path
        # it's a-cyclic, so don't worry about infinite loop
        # but if not... make SURE to have visited=[] list!
        if source == destination:
            return True
        for neighbor in self.data[source]:
            path.append(neighbor)
            print(f'checking new path {path}')
            check = self.has_path_DFS_recursive(neighbor, destination, path)
            if check == True:
                return True
        return False
        # NOTE next step, pass in the path!
        

    def has_path_BFS(self, source, destination):
        queue = [source]
        while len(queue) > 0:
            current = queue.pop(0)
            if current == destination:
                return True
            for neighbor in self.data[current]:
                queue.append(neighbor)

        return False

