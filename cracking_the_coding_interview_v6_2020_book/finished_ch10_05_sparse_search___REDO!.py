# 10.5 Given a sorted array of strings that is interspersed with empty strings, write a method to 
# find the location of a given string.

# Hints: 256

# NOTE STATUS: Finished quick, but could do this much cleaner with fewer nested loop/conditionals.

a = ['at', '', '', '', 'ball', '', '', 'cat', '', '', 'dad' '', '', ]

def sparse_search(a, term=''):
    for i in range(len(a)):
        
        if len(a[i]) > 0:
            print(a[i])
            if a[i] == term:
                print(f'index {i} for item {a[i]}')
                return i
                
print(sparse_search(a, 'ball'))