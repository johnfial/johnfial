
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Exercise: 
# https://www.interviewcake.com/question/python3/delete-node?course=fc1&section=linked-lists

#  Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.

# The input could, for example, be the variable b below:

class LinkedListNode(object):

    def __repr__(self) -> str:
        return self.value

    def __init__(self, value):
        self.value = value
        self.next  = None
    
    def delete_node(self):
        next_node = self.next
        
        # how do you get the previous node, though?

        # take in next, set that as a temp variable
        # link the previous node to the next (temp variable)
        print(self)
        pass

def delete_node(input_node):
    # NOTE working here
    for node in node_list:
        if node.next = input_node.value:
            node.next = input_node.next
            return node.next


a = LinkedListNode('AAA')
b = LinkedListNode('BBB')
c = LinkedListNode('CCC')

a.next = b
b.next = c

b.delete_node()