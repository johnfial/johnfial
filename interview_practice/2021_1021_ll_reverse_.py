class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)

# create the list:
a = Node('a')
b = Node('b')
a.next = b
c = Node('c')
b.next = c
d = Node('d')
c.next = d

# TODO list in class itself, self.tail, reverse_list and print_list could be methods in class()
# more time on diagram! slooow down. timer!
# talk about perhipheral knowledge!

def reverse_list(head):
    # BUG if only 1-2 nodes
    # two edge cases return

    tail = head
    current = tail.next
    next = tail.next.next

    tail.next = None

    while next != None:
        # change current.next to tail
        current.next = tail

        # change all three variables
        tail = current
        current = next
        next = next.next

    # when current.next == None
    # update last change
    current.next = tail
    return current

# # # # 

def print_list(head):
    if head.next == None:
        print(head)
        return
    current = head
    while current.next != None:
        print(current.val)
        current = current.next
    print(current.val)
    return
print_list(d)
print('#' * 20)
reverse_list(a)
print(b.next)
print(a.next)
print_list(d)
