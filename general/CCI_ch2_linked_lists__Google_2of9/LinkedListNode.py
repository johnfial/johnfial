class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def print_linked_list(head):
    if head == None: return None
    current = head
    array = []
    while current != None:
        print(current.val)
        array.append(current.val)
        current = current.next
    print(f'entire linked list: {array}')
    return array