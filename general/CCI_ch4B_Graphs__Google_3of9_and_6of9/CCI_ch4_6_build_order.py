# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 October
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 4.6

# EXAMPLE:
# Input:      
# Output:     
# Hints: 



# Build Order: You are given a list of projects and a list of dependencies (a list of pairs, where the 
# second is dependent on the FIRST). (That is, the FIRST must be built FIRST). All of a project's dependencies
# must be built before the project. Find a build order that will allow the project to be built -- if there is no valid order, return an error.

# EXAMPLE
# Input:
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
# Output: f, e, a, b, d, c
# Hints: #26, #47, #60, #85, #725, #133


# TODO list:
# 1 build adjacency list
# 2 find_path
# 3 if no neighbors, build that first
# 4 add that to the built_list (basically a visited in path list)
# 5 return order

def build_order(projects, dependencies, build_order=[], graph={}):
    
    graph = {}  # NOTE remove this line!
    build_order = []  # NOTE remove this line!

    for project in projects:
        graph[project] = []

    for parent, child in dependencies:
        # print(f'parent {parent} must be built before child: {child}.')
        temp = graph.get(child)
        temp.append(parent)
        graph[child] = temp

    print(graph)    # {
        #     'a': ['f'], 
        #     'b': ['f'],
        #     'c': ['d'], 
        #     'd': ['a', 'b'], 
        #     'e': [], 
        #     'f': [`]}
    
    for item in graph:
        if graph[item] == []:
            build_order.append(item)

    print(f'build order: {build_order}')
    
    return build_order

build_order(projects, dependencies)