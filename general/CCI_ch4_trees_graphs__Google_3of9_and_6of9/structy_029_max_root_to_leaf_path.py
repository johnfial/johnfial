# STATUS: 

# max root to leaf path sum

# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

# You may assume that the input tree is non-empty.
# test_00:

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1

# max_path_sum(a) # -> 18

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    # start at root
    # visited list...
    # if node.left and node.right == None... it's a leaf, calc path, check...
    # 
    # recursive problem best
    # what's the base case? # NOTE the leaf node!
    print(-float('inf'))
    if root.left == None and root.right == None:
        return root.value
    pass



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
print(max_path_sum(a))

