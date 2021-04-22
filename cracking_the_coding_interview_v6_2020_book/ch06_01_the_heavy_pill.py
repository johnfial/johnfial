# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:     Started 21 Apr

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 16.1 The Heavy Pill:
# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of 1.1 grams. Given a scale that provides
# an exact measurement, how would you find the heavy bottle?

# You can only use the scale once!

# Hints: 186, 252, 319, 387

# WHITEBOARD OUTSIDE:
# The main solution I see is to measure a UNIQUE number of pills from each bottle -- I could leave one bottle unopened,
# because if the scale result was exactly as expected, the heavy pill must be the unopened bottle. 
# But how many pills



# Fortunately the 'heavy' pill weight is off by 0.1, a prime number (if decimal)!
# Also fortunately, I assume I have an unlimited number of pills per bottle.

# Let's practice some prime numbers:
def check_is_prime(input):

    known_primes = [1, 2, 3, 5, 7, 11, 13,]

    if input not in known_primes and type(input) == int:

        # print(f'Checking input integer {input}...', end='')

        for num in range(2, input-1):
            if input % num == 0:
                # print(f'Sorry! {input} is divisible by {num}, and therefore is not a prime number.')
                return False
        print(f'You did it! {input} is only divisible by itself and 1. It is therefore a prime number!')
        return True
    
    else:
        if input in known_primes:
            print(f'Indeed, {input} is a known prime number. Give me something more challenging!')
            return True
        else:
            print('invalid input')
            return False

def find_prime_numbers_through(ceiling):
    
    primes_found = []
    
    for number in range(1, ceiling):
        if check_is_prime(number) == True:
            primes_found.append(number)
    print(f'You found a total of {len(primes_found)} prime numbers between 1-{ceiling}: {primes_found}.')

        



# check_is_prime(24)
find_prime_numbers_through(3000)






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 