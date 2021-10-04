def build_graph(edges):

    graph = {}

    for source, dest in edges:

        # add each
        if source not in graph:
            graph[source] = []
        if dest not in graph:
            graph[dest] = []
        
        # append dest to source
        append = graph.get(source)
        append.append(dest)
        graph[source] = append

        # append source to dest
        append = graph.get(dest)
        append.append(source)
        graph[dest] = append        
        
    return graph


# test_00:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
graph_visual = {
    # component 1:
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'], 
    'm': ['k'], 
    'l': ['k'], 

    # component 2:
    'o': ['n'], 
    'n': ['o']}
graph = build_graph(edges)
print(graph)