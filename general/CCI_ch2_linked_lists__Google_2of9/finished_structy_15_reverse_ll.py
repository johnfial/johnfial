# status: complete! watched main video though...

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def reverse_list(head):
    # NOTE solution, two pointers, no? one iterating through, the other changing...
    # NOTE great one to use a whiteboard for and change the arrows!
    
    previous = None
    current = head
    next = current.next
    while current is not None:
        current.next = previous
        previous = current 
        current = next 
        try:
            next = current.next
        except: break
    # print(f'DONE while loop, current {current}, next: {next}, previous: {previous}.')
    
    head = previous
    # print(f'head: {head.val}')

    return head

def print_linked_list(head):
    printed_list = ''

    current = head
    while (current is not None):
        try:
            printed_list += f'{current.val} ~~~> '
            current = current.next
        except: break
    return printed_list

def main():
    # test_00:

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
    # # a -> b -> c -> d -> e -> f

    print(print_linked_list(a))
    reverse_list(a)
    print(print_linked_list(a))
    print(print_linked_list(f))

main()
# print_linked_list(a)


# reverse list

# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function
# should reverse the order of the nodes in the linked list # NOTE in-place and return the new head of the reversed linked list.

# reverse_list(a) # f -> e -> d -> c -> b -> a

# test_01:

# x = Node("x")
# y = Node("y")

# x.next = y

# # x -> y

# reverse_list(x) # y -> x

# test_02:

# p = Node("p")

# # p

# reverse_list(p) # p