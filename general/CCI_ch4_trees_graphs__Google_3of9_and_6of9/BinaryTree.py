# mostly https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def __str__(self) -> str:
        return f'{self.value} right: {self.right_child}, left: {self.left_child}'
    
    def insert_left(self, new_value):
        
        if self.left_child == None:
            # if no left child, just create node and add to current left_child
            self.left_child = BinaryTree(new_value)
        else: # (if self.left_child != None: )
            # if YES left_child, create new node and put in current left_child place... 
            new_node = BinaryTree(new_value)
            new_node.left_child = self.left_child
            # ...and then set the new node's left_child to THIS left node
            self.left_child = new_node
    
    def insert_right(self, new_value):
        if self.right_child == None:
            self.right_child = BinaryTree(new_value)
        else:
            new_node = BinaryTree(new_value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def DFS_pre_order(self): # DFS: Depth First Search
        print(self.value)

        if self.left_child:
            # print(f'self.left_child <<<<< value = {self.value}')
            self.left_child.DFS_pre_order()
        
        if self.right_child:
            # print(f'self.right_child >>>> value = {self.value}')
            self.right_child.DFS_pre_order()
    
    def DFS_in_order(self):
        if self.left_child:
            self.left_child.DFS_in_order()
        print(self.value)  # note where this is, between left and right recursive search...
        if self.right_child:
            self.right_child.DFS_in_order()

    def DFS_post_order(self):
        if self.left_child:
            self.left_child.DFS_post_order()
        if self.right_child:
            self.right_child.DFS_post_order()
        print(self.value)
    
    # def BFS(self):  # needs to import/implement the Queue structure, with .put() and .get()
    #     queue = Queue()
    #     queue.put(self)

    #     while not queue.empty():
    #         current_node = queue.get()
    #         print(current_node.value)

    #         if current_node.left_child:
    #             queue.put(current_node.left_child)
    #         if current_node.right_child:
    #             queue.put(current_node.right_child)

tree1 = BinaryTree('aaa')
# print(tree1)
tree1.insert_left('bbb')
# print(tree1)
tree1.insert_right('ccc')
# print(tree1.left_child.left_child.left_child)

# # # 

a = BinaryTree('aaa')
a.insert_left('bbb')
a.insert_right('ccc')

b = a.left_child
b.insert_right('ddd')

c = a.right_child
c.insert_left('e')
c.insert_right('f')

d = b.right_child
e = c.left_child
f = c.right_child

# a.DFS_pre_order()
a.DFS_in_order()
a.DFS_post_order()










