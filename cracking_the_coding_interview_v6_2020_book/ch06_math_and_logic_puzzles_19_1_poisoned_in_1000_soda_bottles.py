# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Created 12 April
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 6.10 One in 1000 soda bottles is poisoned:

# Whiteboarding/meditation note:

# variables BS:
sodas_suspect = 1000
sodas_negative = 0
sodas_positive = 0
test_strips_negative = 0

sodas_dictionary = {}

sodas_suspect = 10  # TESTING ONLY: overwrite the other to use a smaller number

for i in range(10):
    sodas_dictionary[i] = False

print(sodas_dictionary)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 