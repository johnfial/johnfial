# find factors where a**3 + b**3 = c**3 + d**3
# TODO what's the time complexity of this?
    # i believe it's n ^ 4. 

import timeit
# https://docs.python.org/3/library/timeit.html

def find_factors(n):

    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):                
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        if a**3 + b**3 == c**3 + d**3:
                            print('found it @', a, b, c, d)
                            # print(f'''
                            # a = {a}, a**3 = {a**3}
                            # b = {b}, b**3 = {b**3}
                            # c = {c}, c**3 = {c**3}
                            # d = {d}, d**3 = {d**3}, so...
                            # a**3 + b**3 = {a**3 + b**3} and c**3 + d**3 = {c**3 + d**3}
                            # ''')
    else:
        print('nstr')

n = 13 # first results are at n=13

# find_factors(n)

# y = timeit.timeit('find_factors(n)', number=10)
# print(y)

x = timeit.timeit('"-".join(str(n) for n in range(1000))', number = 100)
print(x)

