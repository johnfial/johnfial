# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:    23 April 2021 started

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 06.

# Assume that no one can communicate the eye colors of others
# Assume that there is at least one blue-eyed person.

# Hints: 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Logic problem, nothing to code yet (but how long it'd take with starting #)

# 1 person? They'd leave on the first day, because the individual would see that everyone has 
# brown (etc.) eyes, know they have blue eyes, and leave.

# 2 people? More interesting. On the first day, neither would leave! Each would assume the OTHER 
# was the only blue-eyed person, and assume the other would leave on day 1. On day 2, after nobody left, 
# each would know his/her own eye color was blue, the OTHER person assumed as they did, and that their 
# own eyes were blue... BOTH would leave on the end of the SECOND day.

# ... so for 3 people would it be the same? Each of 3 would think that the two blue-eyed people were
# the only blue-eyed inhabitants. But, during the 2nd day, seeing that neither left, they would assume 
# that the others thought as they did, and leave... So end 2nd day, all 3 people would leave.
    # ... BUG ... wouldn't the whole island leave like this, then? Evene the brown (etc.) eyed people?!
    # Wouldn't person 4, seeing "all three blue-eyed people", see nobody leaves on day 1, assume he too
    # has blue eyes, and also leave?


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 