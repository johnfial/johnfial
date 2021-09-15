# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# http://www.crackingthecodinginterview.com/solutions.html 
# TODO STATUS:    Working 2021 Sept 14...

# online @ https://youtu.be/wjI1WNcIntg?t=227 (Stack at 227s)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# NOTE remember Stack is LIFO

class StackNode():
    
    data = None
    next = None

    def __init__(self, data=None):
        self.data = data

    def __str__(self) -> str:
        return str(self.data)

class Stack():

    top = StackNode()
    size = 0
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def peek(self):
        # NOTE she's ignoring null pointer checks...
        return self.top.data

    def push(self, data: int):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        # NOTE she ignored null pointer checks
            # i.e. if top is null, throw exception, etc...
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1 
        return popped_data


# newstack = Stack()
# newstack.push(55)
# newstack.push(5511)
# print(newstack.top)
# print(newstack.top.next)
# print(newstack.top.next.next)
# print(newstack.top.next.next.next)
# newstack.push(333)
# print(newstack.top)
# print(newstack.size)
# newstack.pop()
# print('~~~~~~~~~working here~~~~~~~~~')
# print(newstack.top)
# print(newstack.size)


