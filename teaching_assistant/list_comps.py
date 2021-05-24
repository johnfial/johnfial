
# list2 = [for x in range(3) print x]
import random
def pick_ticket():
    return [(random.randint(1,10), 'tupleB') for x in range(6) for x in range(3)]

print(pick_ticket())