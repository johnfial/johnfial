# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/

# TODO STATUS:    Working 2021 September
# ok brute force first solution, need to improve...

# https://www.bigocheatsheet.com/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 10.4 Sorted Search, No Size
# You are given an array-like data structure *Listy* which lacks a size method. It does, however
# have an elementAt(1) method that returns the element at index 1 in O(1) time. 
# If it is beyond the bounds of the data structure, it returns -1. 
# (For this reason, the data structure only supports positive integers.) 
# Given a Listy which contains sorted, positive integers, 
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.

# Hints: 320, 337, 348

class Listy():
    
    def __init__(self, data):
        self.data = list(data)
        print(f'new Listy() with self.data = {self.data}')

    def elementAt(self, target):
        # NOTE brute force:
        # iterate over each item looking for the target:
        # WRONG, this takes O(n) time, iterating over all items...
        try:
            for item in self.data:
                if item == target:
                    return self.data.index(target)
        except:
            return -1

ex = [1, 5, 15, 28, 99, 999,]
a = Listy(ex)
print(a.elementAt(15))
