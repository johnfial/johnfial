
class Node(object):
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

def print_list(head):
    current = head
    while current.next is not None:
        print(current.val)
        current = current.next
    print(current.val)
    return