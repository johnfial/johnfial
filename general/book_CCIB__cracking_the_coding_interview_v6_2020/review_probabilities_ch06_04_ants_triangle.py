# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:    23 April 2021 started

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 06.4 Ants on a Triangle
# There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them)
# if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being 
# equally likely to be chosen, and that they walk at the same speed. 

# EXTRA: What's the probability of collision with n ants of an n-vertex polygon?

# Ants, ants, marching up and down again...

# Hints: 157, 195, 296

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def ant_polygon_probability(n):
    # Possibility of no collisions: 2 out of 2*n
    # Collisions: (1 - ( 2 / (2*n) ))

    print(f'Total possibilites for n={n} vertices: 2*n = {2**n}.')

    no_collisions = 2 / (2**n)
    print(f'possibilites for NO collisions 2 / (2*n): {no_collisions}')

    collisions = 1 - (no_collisions)
    print(f'possibilites of collisions: 1 - (2 / (2*n)) : {collisions} ')
    print(2/6)

ant_polygon_probability(3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 