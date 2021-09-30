# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : Works -- now improve!
# NOTE Concepts  : Linked Lists
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 2.7 Given two singly linked lists, determine if the two lists intersect. Return the intersecting
# node. Intersection is based on REFERENCE, not value -- if the Kth node of the first linked list is
# exactly the exact same node (by reference) as the Jth node of the second, they are intersecting.
# SO not if both have 'cat' or 123, rather, if the node itself is identical.
# I think this MUST mean that the entire rest of the lists are identical, because one cannot have a different
# node.next pointer than the other...

# Hints: 20, 45, 55, 65, 76, 93, 111, 120, 129

# 1 build it!

from LinkedListNode import Node, print_linked_list

def create_lists():  # heads: a, l, one
    # a -> b -> c -> d -> e -> f
    global a 
    a = Node("aaa")
    b = Node("bbb")
    c = Node("ccc")
    d = Node("ddd")
    e = Node("eee")
    global f
    f = Node("fff")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # # # # # # # # # # 

    # l -> m -> n -> o -> p -> c -> d -> e -> f
    global l
    l = Node("lll")
    m = Node("mmm")
    n = Node("nnn")
    o = Node("ooo")
    p = Node("ppp")
    l.next = m
    m.next = n
    n.next = o
    o.next = p
    p.next = c

    # # # # # # # # # # 

    # one -> two -> three -> four
    global one
    one = Node(1)
    two = Node(2)
    one.next = two
    three = Node(3)
    two.next = three
    global four
    four = Node(4)
    three.next = four

    # # # # # # # # # # 

create_lists()

def has_intersection(headA, headB):
    if headA == None or headB == None: return False

    runner = headA
    comparison = []
    # 0 NOTE ideally, the linked lists would have a size attribute allowing us to add the smaller one first:

    # 2 add one list to array
    while runner is not None:
        comparison.append(runner)
        runner = runner.next

    # 3 runner for second list checks if node in array, if yes return True
    runner = headB
    while runner is not None:
        if runner in comparison: return True
        runner = runner.next

    return False

# print_linked_list(a)
# print_linked_list(l)
print(has_intersection(a, l))  # True
print(has_intersection(a, one))  # False

# one -> two -> three -> four -> f
four.next = f
print(has_intersection(a, one))  # True













# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
#     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #

# Test cases:


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 