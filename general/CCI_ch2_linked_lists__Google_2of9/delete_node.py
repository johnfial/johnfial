# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Exercise: 
# https://www.interviewcake.com/question/python3/delete-node?course=fc1&section=linked-lists

# Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.

# The input could, for example, be the variable b below:

# from LinkedList import LinkListNode, LinkedList
from LinkedListNode import print_linked_list, Node

a = Node('AAA')
b = Node('BBB')
a.next = b
c = Node('CCC')
b.next = c
d = Node('DDD')
c.next = d

b.delete_node()
# should now be a > c > d


def delete_node(input_node):
    # NOTE working here
    input_node.data = input_node.next  # ???
    # previous = input_node.next   