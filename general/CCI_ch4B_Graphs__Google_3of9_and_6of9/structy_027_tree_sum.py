# STATUS: solved

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_sum(root):
    queue = [] #BFS
    sum = 0
    queue.insert(0, root)

    while queue:
        current = queue.pop()
        if current is not None:
            sum += current.val
            queue.insert(0, current.left)
            queue.insert(0, current.right)
    return sum



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
print(tree_sum(a))