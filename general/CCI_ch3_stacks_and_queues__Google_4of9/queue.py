# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# http://www.crackingthecodinginterview.com/solutions.html 
# TODO STATUS:    Working 2021 Sept 8...

# online @ https://youtu.be/wjI1WNcIntg?t=82 (Queue @ 82s)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# NOTE remember Queue is FIFO

class Node():
    data = None
    next = None
    
    def __init__(self, data):
        self.data = data

class Stack():

    head = None
    tail = None


