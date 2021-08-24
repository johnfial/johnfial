# midway through page: https://stackoverflow.com/questions/1839289/why-should-functions-always-return-the-same-type 
# this doc was from playing with object sizes in memory for algorithms, CS-ey interview stuff...

import sys  # 72
import datetime  # 72, but datetime.time = 408

()  # tuple 40!
''  # string 49!
[]  # list 56
{}  # dict 64!

print(sys.getsizeof(''))
print(sys.getsizeof([]))
print(sys.getsizeof(sys))
print(sys.getsizeof(datetime.time))