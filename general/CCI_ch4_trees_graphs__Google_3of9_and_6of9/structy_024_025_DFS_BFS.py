# status solved

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
    stack = []
    values_seen = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if current is not None:
            values_seen.append(current.val)
            print(current.val)
            stack.append(current.right)
            stack.append(current.left)
    return values_seen

def breadth_first_values(root):
    queue = []
    values_seen = []
    queue.insert(0, root)

    while queue:
        current = queue.pop()
        if current is not None:
            values_seen.append(current.val)
            queue.insert(0, current.left)
            queue.insert(0, current.right)

    return values_seen

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# print(depth_first_values(a))
# print(breadth_first_values(a))