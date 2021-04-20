# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:     finished 20 apr?
# think I'm done, check for edge cases

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 16.6 is_smallest

# EXAMPLE:
# Input:      
# Output:     
# Hints: 

index_a = 0
index_b = 0
list_a = [3, -73, 73, 83, 93, 2, 7777, ]
list_b = [1, 5, 9, 8, 57, 254, 30, ]

def find_smallest_difference(list_a, list_b):
    
    # variables:
    smallest_difference = 99999999999 # TODO does this work, need infinity, or what?
    
    for number_a in list_a:
        
        for number_b in list_b:
            
            # am I sure I want to take the absolute value?
            temp_difference = abs( number_a - number_b )
            
            if temp_difference < smallest_difference:
                smallest_difference = temp_difference
                print(f'new smallest difference: {smallest_difference} between {number_a} and {number_b}')
    
    return smallest_difference

find_smallest_difference(list_a, list_b)











# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   # Failed Attempts:  #   #   #   #   #   #   #   #   #   #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 