from Queue import QueueNode, Queue


queue1 = Queue()
print(queue1.is_empty())
queue1.add(111)
queue1.add(222)
queue1.add(333)
print(queue1.is_empty())  # should return False
print(queue1.peek())  # should return next item ready...
queue1.remove()
print(queue1.peek())
queue1.remove()
print(queue1.peek())
print(queue1)
queue1.add(11)
queue1.add(21)
queue1.add(31)
print(queue1)
print('~~~~~~~~~working here~~~~~~~~~')
print(queue1.remove())
print(queue1)
print(queue1.remove())
print(queue1)
print(queue1.remove())
print(queue1)
