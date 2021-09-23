class MinHeap():
    # see an example at bottom of https://www.programiz.com/dsa/priority-queue
    
    capacity = 10
    size = 0
    # Gayle's Java example:
    # def ensure_extra_capacity() if size == capacity, data = copy. . .
    # unnecessary with python's dynamic lists by default...
    
    data = []
    
    def __init__(self, data: list):
        self.data = data
    def __str__(self):
        return str(self.data)

    # use an array to implement!
    # formulas for parent/child, where index = i :
    # parent = i-2 / 2          (round up!)
    # left = 2i + 1
    # right = 2i + 2
    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1
    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2
    def get_parent_index(self, child_index):
        return (child_index - 1) / 2 # BUG modulus needed?
    
    # has children
    def has_left_child(self, index):
        return (self.get_left_child_index(index) < self.size)
    def has_right_child(self, index):
        return (self.get_right_child_index(index) < self.size)
    def has_parent(self, index):
        return (self.get_parent_index(index) >= 0)
    
    # get data of parent/children
    def left_child(self, index):
        return self.data[self.get_left_child_index(index)]
    def right_child(self, index):
        return self.data[self.get_right_child_index(index)]
    def parent(self, index):
        return self.data[self.get_parent_index(index)]
    
    def peek(self):
        if self.size == 0:
            raise Exception
        else:
            return self.data[0]
    
    def poll(self):  # actually takes out an item
        if self.size == 0:
            raise Exception()
        else: 
            item = self.data[0]
            self.data = self.data[self.size - 1]
            self.size -= 1 
            self.heapify_down()
            return item

    def add_item(self, item):
        # self.ensure_capacity(), unnecessary
        self.data[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size -1
        
        while (self.has_parent(index) and self.parent(index) > self.data[index]):
            self.swap(self.get_parent_index(index), index) # BUG need to implement swap?
            index = self.get_parent_index(index)

        # while hasParent(index) and parent(index) > data[index]:
            # swap(getParentIndex(index), index) # can you do this in python?
            # index = getParentIndex(index)

        pass
    def heapify_down(self):
        index = 0
        while (self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index(index)  # 50/50 guess
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            if self.data[index] < self.data[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)  # NOTE BUG swap
            index = smaller_child_index

