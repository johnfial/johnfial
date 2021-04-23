# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition

# TODO STATUS:    Started 22 April

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# xx: Valid parenthesis:
# Write a method to validate parenthesis within a string: i.e. that all are in order, matching, "balanced", etc.
# NOTE list.sort() does NOT help me, for obvious reasons...

example_1 = 'jello()' # valid
example_2 = 'jello()()' # valid
example_3 = 'jello(())'  # valid
example_4 = 'jello(()())'  # valid
example_5 = '(jello)()()' # valid

example_6 = ')jello(' # invalid, even though even...
example_7 = ')jello))' # invalid
example_8 = 'jello)' # invalid
example_9 = 'jello))((' # invalid

def validate_parentheses(input_string):
    parentheses_list = []
    if type(input_string) == str:

        for letter in input_string:
            if letter == '(' or letter == ')':
                parentheses_list.append(letter)

        
        if parentheses_list.count('(') == parentheses_list.count(')'):
            print('number of open( == )closed parentheses! first step!')
            # do more checking...
            # loop through the first, which must be '('
            # 2nd must be '(', starting a new check, OR ')', terminating that counter...
            # variable counter_current_parentheses ?

            print(f'parentheses_list: {parentheses_list}')
            current_open_parentheses_counter = 0

            # WORKING HERE # WORKING HERE # WORKING HERE # WORKING HERE # WORKING HERE 
            for counter in range(parentheses_list.count('(')):

                if parentheses_list[counter] == '(':
                    print('pass 2nd check! # do some work!')
                    if parentheses_list[counter+1] == ')':
                        print('MATCH! super balanced')
            # WORKING HERE # WORKING HERE # WORKING HERE # WORKING HERE # WORKING HERE 

        else: print('numbers do not match, odd number fails!')

    else:  # not a string...
        print('invalid datatype input!')
        return False

validate_parentheses(example_2)





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 