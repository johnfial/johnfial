# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# if there's an ID with incremented numbers AND nothing has been deleted, the easiest way is to % 2 the ID 
# if not:
    #  one way is to iterate through the nodes and increment a counter
    # another is to add the node count to the LinkedList implementation, then add/remove count appropriately
    # 

    # NOTE LOOKUP: how can I make my datatype iterable in Python?

from  linked_list import LinkListNode, LinkedList

def is_even_or_odd(ll):
    # NOTE working here
    for node in ll:
        print(node)

        pass

n1 = LinkListNode(111) # id: 1
n2 = LinkListNode(222) # id: 2
n3 = LinkListNode(333) # id: 3
n4 = LinkListNode(444) # id: 4
n5 = LinkListNode(555) # id: 5
n6 = LinkListNode(666)
n7 = LinkListNode(777)

ll = LinkedList(n1) # 1 ~>>
ll.link(n1, n2) # 1 ~>> 2
ll.link(n2, n3) # 1 ~>> 2 ~>> 3
ll.link(n3, n4) # 1 ~>> 2 ~>> 3 ~>> 4
ll.link(n4, n5) # 1 ~>> 2 ~>> 3 ~>> 4 ~>> 5

is_even_or_odd(ll)










# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1

# Linked List Length Even or Odd?
# Basic Accuracy: 56.34% Submissions: 37300 Points: 1

# Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd() which contains head of the linked list and check whether the length of linked list is even or odd.

# Input:
# The input line contains T, denoting the number of testcases. Each testcase contains two lines. the first line contains N(size of the linked list). the second line contains N elements of the linked list separated by space.

# Output:
# For each testcase in new line, print "even"(without quotes) if the length is even else "odd"(without quotes) if the length is odd.

# User Task:
# Since this is a functional problem you don't have to worry about input, you just have to  complete the function isLengthEvenOrOdd() which takes head of the linked list as input parameter and returns 0 if the length of the linked list is even otherwise returns 1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 103
# 1 <= A[i] <= 103

# Example:
# Input:
# 2
# 3
# 9 4 3
# 6
# 12 52 10 47 95 0

# Output:
# Odd
# Even

# Explanation:
# Testcase 1: The length of linked list is 3 which is odd.
# Testcase 2: The length of linked list is 6 which is even.