# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Created 12 April
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 6.10 One in 1000 soda bottles is poisoned:

# Whiteboarding/meditation note:
# Here's the simple ~28d solution figured out before reading the hints (meditating)
    # Round 1:
# Day 1 break them into 10 groups of 100 bottles, test 100 drops on each strip
# Day 8 one of those groups is positive, and we now have 9 good strips left
    # Round 2:
# Day 8 break the 100 suspect sodas into 9 groups of 11 + 12 (8 of 11, 1 of 12), test via 9 strips
# Day 15 one strip shows a group of 11 (or 12) with the poisoned soda, now 8 good strips left
    # Round 3:
# Day 15 break the 12 (conservatively) suspect sodas across the 8 remaining strips: 4 strips have 2 soda drop each, the other 4 strips have one soda each
# Day 22 50/50 shot here you found the individual soda, otherwise use 2 more strips to test between the two suspect sodas
    # 50: poisoned soda found!
    # ~50% go to bonus round 4!:
        # Day 29 test both suspect sodas on two of the 7 remaining strips
        # Day 36 poisoned soda found!

# variables BS:
sodas_suspect = 1000
sodas_negative = 0
sodas_positive = 0
test_strips_negative = 0

sodas_dictionary = {}

sodas_suspect = 10  # TESTING ONLY: overwrite the other to use a smaller number

for i in range(10):
    sodas_dictionary[i] = False
# make the one True item...
import random
positive_soda = random.randint(1, 1000)
positive_soda = 5
sodas_dictionary[positive_soda] = True



print(sodas_dictionary)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 