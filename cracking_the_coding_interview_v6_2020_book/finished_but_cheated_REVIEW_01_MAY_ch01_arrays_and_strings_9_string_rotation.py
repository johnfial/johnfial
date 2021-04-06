# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Almost done 06 April, but saw solution...
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.6 String Rotation
# Assume you have a method isSubstring which checks if one word is a subssting of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to isSubstring (eg "waterbottle" is a rotation of "erbottlewat")
# Hints: 34, 88, 108

source_example_1 = 'waterbottle'

def isSubstring(source_string, test_string):
    
    # if it's not the same length, they can't be rotations, so don't even bother continuing
    if len(source_string) == len(test_string):
        
        # for loop... slice at certain point, append to 
        for x in range(len(source_string)):
            print(x)
            # https://www.w3schools.com/python/python_strings_slicing.asp
            # Here's a solution: https://www.geeksforgeeks.org/string-slicing-python-rotate-string/
        
            # TODO working here...
            a = source_string[x:]
            b = source_string[0:x]
            source_string_rotated = a + b
            print(source_string_rotated)

            # at every single iteration, check this:
            if source_string_rotated == test_string:
                print('they"re a rotation"')
                return True
            # otherwise loop again

        # at very end, if the loop didn't find anything......
        print('FAILED, NOT A ROTATION...')
        return False

    else:
        print('lengths do not match. return False')
        return False

source_example_1 = 'waterbottle'
test_example_1 = 'erbottlewat'
test_example_1 = 'wrbottlewat'

isSubstring(source_example_1, test_example_1)


source_example_2 = 'lollipops'
test_example_2 = ''
# isSubscring(source_example_2, test_example_2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 