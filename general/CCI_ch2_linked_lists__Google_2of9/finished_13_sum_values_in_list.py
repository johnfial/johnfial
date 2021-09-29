# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head=None):
  sum = 0
  
  if head == None: return sum
  current = head

  while True:
    sum += current.val
    current = current.next
    try:
      if current.next == None:
        sum += current.val
        break
    except:
      break
    
  return sum


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19

print(sum_list(None))

# https://structy.net/problems/sum-list

# sum list

# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.
# test_00:

# a = Node(2)
# b = Node(8)
# c = Node(3)
# d = Node(-1)
# e = Node(7)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# # 2 -> 8 -> 3 -> -1 -> 7

# sum_list(a) # 19

# test_01:

# x = Node(38)
# y = Node(4)

# x.next = y

# # 38 -> 4

# sum_list(x) # 42

# test_02:

# z = Node(100)

# # 100

# sum_list(z) # 100

# test_03:

# sum_list(None) # 0