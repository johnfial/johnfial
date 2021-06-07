# midway through page: https://stackoverflow.com/questions/1839289/why-should-functions-always-return-the-same-type 
# this doc was from playing with object sizes in memory for algorithms, CS-ey interview stuff...

import sys

''  # string 49!
()  # tuple 40!
[]  # list 56
{}  # dict 64!

print(sys.getsizeof(''))
print(sys.getsizeof([]))