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

def linked_list_find(head, target):
    if head == None: return False
    current = head

    try:
        while current.val != None:
            if current.val == target: 
                return True
            current = current.next

    except:
        return False

def linked_list_find_recursive(head, target):
    if head == None: return False
    if head.val == target: return True

    current = head
    return linked_list_find_recursive(head.next, target)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

# print(linked_list_find(a, "d")) # True
print(linked_list_find_recursive(a, 'd'))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# https://structy.net/problems/linked-list-find
# linked list find

# Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
# The function should return a boolean indicating whether or not the linked list contains the target.
# test_00:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linkedListFind(a, "c") # True

# test_01:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linkedListFind(a, "d") # True

# test_02:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linkedListFind(a, "q") # False

# test_03:

# node1 = Node("jason")
# node2 = Node("leneli")

# node1.next = node2

# # jason -> leneli

# linkedListFind(node1, "jason") # True

# test_04:

# node1 = Node(42)

# # 42

# linkedListFind(node1, 42) # True

# test_05:

# node1 = Node(42)

# # 42

# linkedListFind(node1, 100) # False