from Heap import MinHeap


a_list = [5, 1, 3, 3, 99, 2, 98, ]
a = MinHeap(a_list)
print(a)
a.heapify_down()
a.heapify_up()
print(type(a))
print(a)
# NOTE not working yet, heapify at least...