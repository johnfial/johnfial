

# testing a tabata timer...
import time
def tabata_timer():

    for x in range(240):
        print(x)
        time.sleep(.1)
        if x % 20 == 0:
            print('rest!')
        if x % 30 == 0:
            print('work!')

tabata_timer()
