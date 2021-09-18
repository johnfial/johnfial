# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# http://www.crackingthecodinginterview.com/solutions.html 
# TODO STATUS:    Working 2021 Sept 14...

# online @ https://youtu.be/wjI1WNcIntg?t=82 (Queue @ 82s)
# see Stack_Queue_Notes.md
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# NOTE remember Queue is FIFO

class QueueNode():

    data = None
    next = None
    
    def __init__(self, data: int=None):
        self.data = data
        # NOTE what should go here, for next? or is this only in the Queue() class...?
        # self.next = QueueNode()  # nooooooooooope, recusion depth limit (in <1s!) hit at >495 times!

    def __repr__(self):
        return str(self.data)

class Queue():

    head = QueueNode()  # remove from head...
    tail = QueueNode()  # add to the tail
    size = 0

    def is_empty(self): 
        if self.head.data == None:
            return True
        else:  # NOTE it saves 13 characters/bytes or 104 bits to put 'return False' on the same line...
            return False
        
    def peek(self): 
        return self.head.data  # BUG to fix throws exception when head = none

    def add(self, data: int=None): 
        # NOTE add to the tail...
        node = QueueNode(data)
        if self.tail != None:
            self.tail.next = node
        self.tail = node
        if self.head.data == None:
            self.head = node
        self.size += 1
        # print(f'inside add(), data={data}, self.head = {self.head}. Node = {node}. self.tail={self.tail}')
    
    def remove(self):
        # BUG if try .remove on empty Queue...
        data = self.head.data
        self.head = self.head.next
        if self.head == None:  # NOTE why this check, and why set tail to None?
            self.tail = None
        self.size -= 1
        return data

    def __repr__(self):
        return f'QUEUE object w/ self.head: {self.head}, self.tail {self.tail}, Queue size: {self.size}'
