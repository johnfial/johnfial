# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:    23 April 2021 started

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 06.7 The Apocalypse (brief type)
# The world queen is concerned about the birth rate, and wants all families to keep birthing until they have one baby girl.
# Assume the odds of M/F is 50%. Assume they immedately stop with a girl. No twins or anything like that.

# What will the gender ratio of the new generation be?

# Hints: 154, 160, 171, 188, 201

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# First let's print out the % of 50% halving...

def main(input_generations):
    
    percentage = 100
    sum = 0

    for x in range(1,input_generations+1):
        new_generation = (percentage / 2)
        percentage = percentage - new_generation
        sum += new_generation
        print(f'{percentage} and {new_generation} and sum {sum}')

main(7)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 