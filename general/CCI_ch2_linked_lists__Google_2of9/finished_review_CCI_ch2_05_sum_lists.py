# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : Done -- but it ain't pretty!
# NOTE Concepts  :  
# - Linked Lists
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 2.05 Sum Lists:

# You have two numbers represented by a linked list, where each node contaions a single digit. 
# The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write
# a function that adds the two numbers and returns the sum as a linked list. (Cannot cheat and 
# just convert list to integer...)

# Hints: 7, 30, 71, 95, 109

# EXAMPLE 1
# Input:  (7 ~~> 1 ~~> 6) + (5 ~~> 9 ~~> 2). Or in english, 617 + 295
# Output: (2 ~~> 1 ~~> 9). (The number 912)


# FOLLOW UP EXAMPLE: What if now the output should be in normal forward order?
# EXAMPLE 2
# Input: (6 ~~> 1 ~~> 7) + (2 ~~> 9 ~~> 5). In engilsh: 617 + 295
# Output: 9 ~~> 1 ~~> 2. (The number 912)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# 1 make the linked lists

from LinkedListNode import Node, print_linked_list

a1 = Node(7)
a2 = Node(1)
a1.next = a2
a3 = Node(6)
a2.next = a3

b1 = Node(5)
b2 = Node(9)
b1.next = b2
b3 = Node(2)
b2.next = b3

def add_wierd_lists(head1, head2):
    
    if head1 == None and head2 == None: return None  # or return Node(0) ? 
    
    # 2 test: print out each
    # 2 add to array until current = None
    array1 = ''
    array2 = ''

    runner = head1
    while runner != None:
        array1 += str(runner.val)
        runner = runner.next
    array1 = array1[::-1]

    runner = head2
    while runner != None:
        array2 += str(runner.val)
        runner = runner.next
    array2 = array2[::-1]

    # solving for single None head (which should 'add 0' and thus still output the other list)
    if head1 == None: array1 = 0
    if head2 == None: array2 = 0

    # 3 change array to int()
    int1 = int(str(array1))
    print(int1)
    int2 = int(str(array2))
    print(int2)

    # 4 add numbers
    sum = int1 + int2

    # 5 create new linked list...
    # 5a: create list() from sum IN REVERSE ORDER
    # 5b: create node for each in list in range(len(list))
    # 5c: link that node to next...
    reverse_sum = list(str(sum))
    reverse_sum.reverse()
    print(reverse_sum)

    global head    
    head = Node(reverse_sum[0])
    second = Node(reverse_sum[1])
    head.next = second # links first to 2nd
    for x in range(len(reverse_sum)):
        try:
            # NOTE This works for 3 digits, pretty sure something isn't right for 4+ digits (overwriting variables)
            third = Node(reverse_sum[x+2])  # makes 3rd
            second.next = third  # links 2nd to 3rd
            fourth = Node(reverse_sum[x+3]) # makes 4th
            third.next = fourth # links 3rd to 4th
        except:
             break

    # 5d: return list!

    return head

print(add_wierd_lists(a1, b1))
print_linked_list(head)
print(head.next)
print(add_wierd_lists(a1, None))






















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