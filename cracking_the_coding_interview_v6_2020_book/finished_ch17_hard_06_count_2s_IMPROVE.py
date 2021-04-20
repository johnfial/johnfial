# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Finished 20 April

# TODO Could validate integer input with 'try', could clean up nested for loop?

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 17.6 Count of 2s: Write a method to count the number of 2s that appear in all the numbers 
# between 0 and n (inclusive).

# EXAMPLE:
# Input:      25
# Output:     Output: 9 (2, 12, 20, 21, 22, 23, 24, 25. Note 22 counts twice.)
# Hints: 572, 611, 640


def count_twos(input_integer):
    
    # variables
    total_twos = 0
    full_number_list = []
    
    # validation
    if input_integer >= 0:

        for integer in range(0, input_integer+1):
            
            items_to_add = str(integer)
            for character in items_to_add:
                full_number_list.append(character)
        
        print(f'full_number_list of all numbers 0-{input_integer}: {full_number_list}. ')
        
        for number in full_number_list:
            if number == '2':
                total_twos += 1
        
        print(f'returning total_twos: {total_twos}.')
        return total_twos

    else:
        print('invalid input')
        return total_twos


print(count_twos(12))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 