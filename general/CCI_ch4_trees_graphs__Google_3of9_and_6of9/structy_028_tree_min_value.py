# STATUS: solved

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_min_value(root):
    queue = [] #BFS
    queue.insert(0, root)

    if (root.val):
        min_value = root.val
    else:
        return None

    while queue:
        current = queue.pop()
        print(f'visiting {current}')
        if current is not None and (current.val < min_value):
            min_value = current.val
        if current is not None:
            queue.insert(0, current.left)
            queue.insert(0, current.right)
    return min_value



a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(tree_min_value(a))