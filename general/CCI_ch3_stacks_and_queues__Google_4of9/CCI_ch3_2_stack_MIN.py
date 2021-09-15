
# 3.2 Stack Min
# How would you design a stack which, in addition to push and pop, has a function min which returns
# the minimum element? Push, pop, and min should all operatie in O(1) (ie constant) time.
# Hints: 27, 59, 78


from Stack import StackNode, Stack

# in addition to Stack functions...
# brute force: 
    # stack obj has property 'min' which stores the min data. each pop and push checks...
    # push: if new.data is > self.min, let self.min = new.data
        # otherwise no change
    # pop: if popped element is = min
        # 
        # NOTE problem I'm running into is this might require a full list of all pushed elements...
        # OR to re-iterate over the whole stack when an element is popped (push is easy though)
    # min() function simply returns self.min ...

class Stack():
    min = 0
    def min_element(self):
        return min

array = [12, 555, 6549, 55, 99999, ]