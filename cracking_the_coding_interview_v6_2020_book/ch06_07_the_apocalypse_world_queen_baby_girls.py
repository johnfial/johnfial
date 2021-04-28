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

# Whiteboarded this, very fun!

def main(input_generations, parents):

    generation_number = 0
    initial_births = parents / 2  # 1000 in my example, also 1000 maximum (ideal) girls
    new_births = initial_births
    total_girls = 0
    total_boys = 0

    birth_rate = 0.5



    for x in range(1,input_generations+1):
        
        generation_number += 1
        
        new_girls = new_births * birth_rate
        total_girls += new_girls

        new_boys = new_births * birth_rate
        total_boys += new_boys

        gender_ratio = total_boys / total_girls
        
        print(f'SUMMARY: Generation {generation_number}, new_girls: {new_girls}, .new_boys: {new_boys}, total_girls: {total_girls}, total_boys: {total_boys}, gender_ratio: {gender_ratio}.')
        # print(f'{percentage*100}% of babies born were girls, so {new_births} new_births * {percentage * 100}% = {new_births * percentage} girls and {new_births * percentage} boys.')

        new_births = 

main(2, 2000)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 