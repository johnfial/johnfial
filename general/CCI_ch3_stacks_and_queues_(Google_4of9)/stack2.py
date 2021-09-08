# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# http://www.crackingthecodinginterview.com/solutions.html 
# TODO STATUS:    Working 2021 Sept 8...
# TODO SUBMITTED: 
# online @ https://youtu.be/wjI1WNcIntg?t=227 (Stack at 227s)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # TODO isEmpty()
    # peek/look/inspect
    # TODO make add/push
    # TODO make remove/pop
    # TODO test cases?

class Stack():
    
    Node = {}
    top = None
    
    def isEmpty(self):
        if self.top == None:
            return True
    
    def peek(self):
        return self.top.data

    def push(self, data: int):
        # create new node
        # new node  = top, top redefined
        # top points to node created
        print(data)
        pass

    def pop(self):
        # first get the data from top.data
        # top moves to top.next
        return self.data
