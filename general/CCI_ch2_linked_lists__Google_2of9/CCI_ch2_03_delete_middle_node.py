# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 1.x

# CCI_ch2_03_delete_middle_node.py
# Delete Middle Node:
# Implement an algorithm to delete a node in the middle (i.e. NOT the first or last node,
# not necessarily the exact middle) of a singly linked list, given only access to that node.

# EXAMPLE:
# input: the node c from the linked list a -> b -> c -> d -> e -> f
# output : nothing returned, but the new list is a -> b -> d -> e -> f

# Hints: 72

# EXAMPLE:
# Input:
# Output:
# Hints: 


def remove_node(head, target_val):
    cur = head.next
    prev = head
    
    if prev.val == target_val:
        head = head.next
        return head
    
    while cur.val != target_val:
        cur = cur.next
        prev = prev.next
    
    # when it IS target_val:
    prev.next = cur.next    
    
    return head














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