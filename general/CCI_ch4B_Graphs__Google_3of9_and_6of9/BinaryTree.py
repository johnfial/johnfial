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

class Tree(object):
    def __init__(self, data) -> None:
        self.data = data

    # def search(self, root):
    #     print(root, root.left, root.right)
    #     # stack = []
    #     # values_seen = []
    #     # stack.append(root)
    #     # 1 while stack is not empty
    #     # 2 append left/right
    #     # let current = stack.pop()
    #     # values_seen.append(current)

        

        return
