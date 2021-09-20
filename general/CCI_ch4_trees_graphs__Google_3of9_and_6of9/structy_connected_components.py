# https://structy.net/problems/connected-components-count
# connected components count

# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

# NOTE below is from the class definition...
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

def connected_components_count(graph):
    connected_components_list = []    
    connected_components = 0
    
    to_visit = list(graph.keys())
    to_visit.sort()
    print(to_visit)
    for node in graph:
        if explore(graph, node) == True:
            connected_components += 1

    # while visited != to_visit:
    #     group = []
    #     for start_node in to_visit:
    #     TODO here
    #     connected_components_list.append(group)
    #     connected_components_list.sort()
    #     break

    # print(connected_components_list)
    # return len(connected_components_list)
    return connected_components

def explore(graph, current, visited=set()):
    if current in visited:
        return False
    
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)  # recursive DFS
    
    return True



graph1 = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5, 9],
  9: [99, 8],
  99: [9, ],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
} # -> 2

# print(connected_components_count(graph1))
print(connected_components_count(graph1))


def failed(graph):
    connected_components_list = []

    counter = 0
    for start_node in graph:
        temp_component = []
        temp_component.append(start_node)

        for destination in graph:
            counter += 1
            print(f'line 55 counter: {counter}, start_node: {start_node}, destination: {destination}')
            if (has_path_DFS_recursive(graph, start_node, destination) == True) and (destination not in temp_component):
                temp_component.append(destination)
                temp_component.sort()
                print(f'line 59 temp component: {temp_component}, start_node: {start_node}, destination: {destination}')


        # NOTE this is prob fine below:
        if (temp_component != []) and (temp_component not in connected_components_list):
            connected_components_list.append(temp_component)
            connected_components_list.sort()
            print(f'group added! current connected_components_list: {connected_components_list}...')
    
    return len(connected_components_list)