# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
    if head == None: return None

    current = head
    i = 0
    while current != None:
        if i == index:
            return current.val
        current = current.next
        i += 1

def get_node_value_recursive(head, index):
    
    if head == None: return None

    if index == 0: 
        return head.val

    return get_node_value_recursive(head.next, index - 1)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

# print(get_node_value(a, 2)) # 'c'
print(get_node_value_recursive(a, 2)) # 'c'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://structy.net/problems/get-node-value
# get node value

# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.
# test_00:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 2) # 'c'

# test_01:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 3) # 'd'

# test_02:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 7) # None

# test_03:

# node1 = Node("banana")
# node2 = Node("mango")

# node1.next = node2

# # banana -> mango

# get_node_value(node1, 0) # 'banana'

# test_04:

# node1 = Node("banana")
# node2 = Node("mango")

# node1.next = node2

# # banana -> mango

# get_node_value(node1, 1) # 'mango'