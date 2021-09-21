import math

def log_of(n, count=-1) -> int:
    '''
    This will count the depth (log) of the recursive calls to find the log2^n...
    '''
    if n == 0: return count
    n = math.floor(n/2)
    count += 1
    return log_of(n, count)

# print(math.log(32, 2))  # (log x, base y)
print(log_of(4))  
print(log_of(512))

