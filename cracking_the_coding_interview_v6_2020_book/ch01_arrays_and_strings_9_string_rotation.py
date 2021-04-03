# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.6 String Rotation
# Assume you have a method isSubstring which checks if one word is a subscring of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to isSubstring (eg "waterbottle" is a rotation of "erbottlewat")
# Hints: 34, 88, 108

def isSubscring(source_string, test_string):
    if len(source_string) == len(test_string):
        
        # for loop... slice at certain point, append to 
        # check https://www.w3schools.com/python/python_ref_string.asp for how to splice at point, check for permutations of this within a loop...
        for position in (range(len(source_string))):
            test = source_string.split('a')
            print(test)

        
        # do this        
        print(source_string)
        return
    else:
        print('lengths do not match. return False')
        return False


source_example_1 = 'waterbottle'
test_example_1 = 'erbottlewat'

isSubscring(source_example_1, test_example_1)


source_example_2 = 'lollipops'
test_example_2 = ''
# isSubscring(source_example_2, test_example_2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 