# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 October
# TODO SUBMITTED : 
# NOTE Concepts  :  
# - 
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 3.6 Animal Shelter:

# An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis. 
# People must adopt either the oldest anmial or whether they would prefer a dog or a cat
# (and will receive the oldest animal of that type). 
# They cannot select which specific animal they would like. 
# Create the data structures to maintain this system and implement operations such as 
# enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.

# Hints: 22, 56, 56

import datetime
class ShelterQueue(object):
    class Node():
        def __init__(self) -> None:
            date_added = datetime.datetime.now
    
    dog_linked_list = []
    cat_linked_list = []

    # edge cases: empty linked lists

    def dequeueDog(self):
        dog = self.dog_linked_list.pop(0)
        return dog
    def dequeueCat(self):
        cat = self.cat_linked_list.pop(0)
        return cat
    
    def dequeueAny(self):

        # NOTE very important to test datetime > < operators
        compare_dog = self.dog_linked_list.peek()
        compare_cat = self.cat_linked_list.peek()

        if compare_cat == None and compare_dog == None: 
            return None        
        elif compare_dog == None:
            return compare_cat
        elif compare_cat == None:
            return compare_dog

        if compare_cat.date_added >= compare_dog:
            compare_cat = self.cat_linked_list.pop(0)
            return compare_cat
        elif compare_cat.date_added < compare_dog:
            compare_dog = self.dog_linked_list.pop(0)
            return compare_dog



