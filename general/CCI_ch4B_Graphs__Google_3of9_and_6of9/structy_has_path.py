# takes in dict with adjacency list + 2 nodes
# return boolean if path between

# from Graph import Graph

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def has_path_DFS_recursive(graph, source, destination, visited=[]):
    # NOTE because this is a directed (and therefore cyclic) graph, 
    # it REQUIRES a visited list
    if source == destination:
        return True
    
    for neighbor in graph[source]:
        if neighbor not in visited:
            visited.append(neighbor)
            if has_path_DFS_recursive(graph, neighbor, destination, visited) == True:
                return True
    return False

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



