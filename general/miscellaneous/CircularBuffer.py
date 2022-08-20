
print('test')

######################################################################

print('#' * 20)

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity  # check that the variable shouldn't be inside the list!
        self.tail = -1
        self.head = 0
        self.size = 0
        
    def Enqueue(self, item):
        if self.size == self.capacity:
            print('Error: Queue is full!')
            raise ValueError
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item
            self.size += 1
    # NOTES
    # queue/enqueue/push at tail (right), move tail right +1
    # pop/dequeue at head (left), then move head + 1
    # https://towardsdatascience.com/circular-queue-or-ring-buffer-92c7b0193326
    
    def Dequeue(self):
        # remove one from head, clear current head# NO , remove item from TAIL, clear tail. then move tail?
        if self.size == 0: 
            print('error, size 0!')
            return
        value = self.queue[self.head] 
        # self.head += 1
        self.head = (self.head + 1) % self.capacity  # WHY?
        self.size -= 1
        return value
        
    def display_all(self):
        if self.size == 0:
            print(f'Queue is empty')
            
        else:
            print(f'CircularQueue with size={self.size}: --> ', end='')
            index = self.head
            
            for i in range(self.size):
                print(f'--> {self.queue[index]} ', end='')
                index = (index + 1) % self.capacity
        print(flush=True)    
            
    def peek(self):
        
        index = self.head
        print(f'head: {self.queue[index]}, and tail: {self.queue[self.tail]}, and size: {self.size}')

newRing = CircularQueue(5)
newRing.Enqueue(10)
newRing.Enqueue(20)
newRing.Dequeue()
newRing.display_all()
newRing.Enqueue(30)
newRing.Enqueue(40)
newRing.display_all()
newRing.Enqueue(50)
newRing.Enqueue(60)
newRing.Enqueue(600)
newRing.Enqueue(6000)
newRing.display_all()




######################################################################
