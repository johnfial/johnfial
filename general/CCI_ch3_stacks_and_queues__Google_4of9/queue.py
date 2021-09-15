# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# http://www.crackingthecodinginterview.com/solutions.html 
# TODO STATUS:    Working 2021 Sept 14...

# online @ https://youtu.be/wjI1WNcIntg?t=82 (Queue @ 82s)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# NOTE remember Queue is FIFO

class QueueNode():

    data = None
    next = None
    
    def __init__(self, data: int=None):
        self.data = data
        # NOTE what should go here, for next? or is this only in the Queue() class...?
        # self.next = QueueNode()  # nooooooooooope, recusion depth limit (in <1s!) hit at >495 times!

class Queue():

    head = QueueNode()  # remove from head...
    tail = QueueNode()  # add to the tail

    def is_empty(self): 
        if self.head.data == None:
            return True
        else:  # NOTE MOVE it saves 13 characters/bytes or 104 bits to put 'return False' on the same line...
            return False
        
    def peek(self): 
        return self.head.data  # BUG throws exception when head = none

    def add(self, data: int=None): 
        node = QueueNode(data)
        if self.tail != None:
            self.tail.next = node
        self.tail = node
        print(f'inside add(), self.head = {self.head}')
        if self.head == None:
            self.head = node

    
    def remove(self): 
        data = self.head.data
        self.head = self.head.next
        if self.head == None:  # NOTE why this check, and why set tail to None?
            self.tail = None
        return data


print('~~~~~~~~~working here~~~~~~~~~')
n1 = Queue()
print(n1)
n1.add(111)
n1.add(222)
print(n1.is_empty())
print(n1.peek())