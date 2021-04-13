# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Unfinished... 5-20 more min?
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.6
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the 
# string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters a-z.

# Hints: 92, 110

def compress_string(input_string):
    
    # .lower() it
    input_string = input_string.lower()
    
    # two counter? i and i+ 1, start at 0 and 1?
    c1 = 0
    c2 = 1

    while c1 < len(input_string)-1:
        
        # if counters are the same, increment letter counter
        print(f'{input_string[c1]} + {input_string[c2]}')
        if input_string[c1] == input_string[c2]:
            print('yes')

            # replace:
            # while loop? then at end, replace range of counters by # seen
        
        c1 += 1
        c2 += 1

    print(input_string)
    return input_string

example_1 = 'aAbBcCcCccccczZZZfF'
compress_string(example_1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 