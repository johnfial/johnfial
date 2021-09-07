# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 16.1 The Heavy Pill:
# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of 1.1 grams. Given a scale that provides
# an exact measurement, how would you find the heavy bottle?
# NOTE You can only use the scale once!
# Hints: 186, 252, 319, 387

    # WHITEBOARD OUTSIDE:
    # The main solution I see is to measure a UNIQUE number of pills from each bottle -- I could leave one bottle unopened,
    # because if the scale result was exactly as expected, the heavy pill must be the unopened bottle. 

# Fortunately the 'heavy' pill weight is off by 0.1, a prime number (if decimal)!
# Also fortunately, I assume I have an unlimited number of pills per bottle.
# TODO STATUS:     Finished 13 May
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import random
import math

# # # # # # # # 
# variables
number_bottles = 20 # 20  # lower for testing
bottles_and_weights = []
prime_numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, ]  # You found a total of 20 prime numbers between 1-70:

# # # # # # # # 
# get the sum of the primes from 0 through the # of bottles.
sum_primes = sum(prime_numbers[0:number_bottles])

# # # # # # # # 
# generate the bottles and weights, using the index as the bottle number
for x in range(number_bottles):
    bottles_and_weights.append(1.0)

# # # # # # # # 
# make the heavy bottle
heavy_bottle = random.randint(0, number_bottles-1) # BUG: 1/number_bottles % chance of an IndexError...
bottles_and_weights[heavy_bottle] = 1.1

# print it out?   # need to have this accessible for checking, but hidden in the end
# print(f'the heavy_bottle is bottle # {heavy_bottle}. For reference this should use prime_numbers[{heavy_bottle}] which is {prime_numbers[heavy_bottle]} \n\n\n')

# # # # # # # # 
# weigh everything on the scale...
pills_total_weight = 0
for x in range(number_bottles):
    # x = index, remember, starting with [0]th bottle/prime, which is indeed bottle #1!
    # print(f'prime_numbers[{x}]={prime_numbers[x]}')
    print(f'for x={x} ... pills_total_weight = {pills_total_weight} ... adding weight: {bottles_and_weights[x] * prime_numbers[x]} ...')
    pills_total_weight += bottles_and_weights[x] * prime_numbers[x]


# # # # # # # # 
# ...then subtract the total weight of the pills
# SECRET SAUCE / ANSWER: one pill weighs 1.1g, and is multiplied by a *unique* prime number. 
# Divide the difference by primes until you find the single prime that fits perfectly. 
# Even with a thousand bottles, this should still work!
print(f'sum[primes]{sum_primes} - sum {pills_total_weight} # = {sum_primes - pills_total_weight}')
weight_difference = sum_primes - pills_total_weight
print('~~~')

# # # # # # # # 
for x in range(number_bottles):
    # These three prints helped me understand how to use the weight of the pill * prime number pills, rounded...
    # print('~~~')
    # print(weight_difference / prime_numbers[x])
    # print(round((weight_difference / prime_numbers[x]),3))
    # print(round((weight_difference / prime_numbers[x]),7))

    if round((weight_difference / prime_numbers[x]),3) == -0.100:
        print(f'Found "round((weight_difference / prime_numbers[x]),5) == -0.100" @ prime_numbers[{x}] = {prime_numbers[x]}. \nSo the heavy bottle is bottle #{x}!')

print(f'~~~~program ENDED~~~~~~~~~~')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 