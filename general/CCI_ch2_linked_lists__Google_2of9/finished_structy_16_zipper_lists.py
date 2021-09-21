# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Done, improve?
# TODO SUBMITTED: Finished
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Zipper Lists

class Node(object):
    def __init__(self, val) -> None:
        super().__init__()
        self.val = val
        self.next = None

def print_linked_list(head):
    printed_list = ''
    current = head
    while (current is not None):
        try:
            printed_list += f'{current.val} ~~~> '
            current = current.next
        except: break
    return printed_list

def zipper_lists(head_1, head_2):
    
    tail = head_1       # NOTE start at head_1, see following lines
    curr1 = head_1.next # NOTE
    counter = 1         # NOTE
    
    curr2 = head_2

    while curr1 is not None and curr2 is not None:
        if counter % 2 == 0:  # take node from list 1
            tail.next = curr1
            tail = curr1

            curr1 = curr1.next

            counter += 1
        if counter % 2 == 1:  # take node from list 2

            tail.next = curr2
            tail = curr2
            
            curr2 = curr2.next
            
            counter += 1
    
    # finish things here with remaining nodes
    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    print(print_linked_list(head_1))
    return head_1

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)  # a -> x -> b -> y -> c -> z




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://structy.net/problems/zipper-lists
# zipper lists

# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function
# should zipper the two lists together into single linked list by alternating nodes. If one of the
#  linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
#  The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.
# test_00:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# # a -> b -> c

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z

# test_01:

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # a -> b -> c -> d -> e -> f

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z -> d -> e -> f

# test_02:

# s = Node("s")
# t = Node("t")
# s.next = t
# # s -> t

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# one.next = two
# two.next = three
# three.next = four
# # 1 -> 2 -> 3 -> 4

# zipper_lists(s, one)
# # s -> 1 -> t -> 2 -> 3 -> 4

# test_03:

# w = Node("w")
# # w

# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# # 1 -> 2 -> 3 

# zipper_lists(w, one)
# # w -> 1 -> 2 -> 3

# test_04:

# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# # 1 -> 2 -> 3 

# w = Node("w")
# # w

# zipper_lists(one, w)
# # 1 -> w -> 2 -> 3