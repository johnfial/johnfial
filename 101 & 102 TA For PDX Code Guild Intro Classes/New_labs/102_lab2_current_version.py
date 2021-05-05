# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab2.md
# STATUS: 2.1 and 2.2 done, 2.3 REPL is ok but some bugs and could be prettier
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 2.1
# Create a function called sum_numbers which will take in a single parameter, numbers, which will be passed a list of numbers as an argument when the function is called.
# The function will return the sum of all the numbers in the list.
# Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
# Sum: 53


def sum_numbers(input_list):
    sum_total = 0
    for num in input_list:
        sum_total += num
    return sum_total


example_1 = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]  # sum 51
example_2 = [5, 10, 5, 15, 25, 35 ]
print(sum_numbers(example_2))

# # # # 2.1 took ~2-3 minutes (including file setup)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 










# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def remove_all(numbers, target=10):
    
    while target in numbers:
        print('removing...')
        numbers.remove(target)
    
    print(f'new numbers {numbers}')
    return numbers

example_list = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
target_1 = 4
remove_all(example_list, target_1)

# Create a function called remove_all which takes in two parameters, numbers & target.

# The numbers parameter will be passed a list of numbers and the target parameter will be 
# passed the number to remove from the list.
# The function will return a new list containing only the numbers that are not the target number.

# Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

# Remove: 4
# Numbers: [5, 2, 10, 5, 8, 10]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2.1

# Create a function called sum_numbers which will take in a single parameter, numbers, which will be passed a list of numbers as an argument when the function is called.

# The function will return the sum of all the numbers in the list.

# Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

# Sum: 51

# 2.2

# Create a function called remove_all which takes in two parameters, numbers & target.

# The numbers parameter will be passed a list of numbers and the target parameter will be passed the number to remove from the list.

# The function will return a new list containing only the numbers that are not the target number.

# Numbers: [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

# Remove: 4
# Numbers: [5, 2, 10, 5, 8, 10]

# 2.3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def repl_loop_list_builder():
    '''
    Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter 
    them one at a time. Add each number to a list.

    Once the user enters 'done', ask the user to define the target number for the remove_all function.

    Call the functions using the values the user provides.
    '''

    user_generated_list = []
    user_input = input('give me an integer (whole) number, or type "done" to finish: > ')    

    while user_input != 'done':
        try:
            # convert to int/float
            user_number = int(user_input)
            
            # add to list:
            user_generated_list.append(user_number)
        except:
            print('invalid number')

        user_input = input('give me an integer (whole) number, or type "done" to finish: > ') 
    
    # when user_input == 'done':        
    print(f'your user_generated_list is: {user_generated_list}')
    
    target_number = input('give me a target integer (whole) number to remove from your list >')
    # # # # # 
    # could improve the error handling here with user input...
    try:
        target_number = int(target_number)
    except:
        print('invalid number')
    
    user_generated_list = remove_all(user_generated_list, target_number)
    sum_numbers(user_generated_list)
    print(f'sum of your numbers list is {sum_numbers(user_generated_list)}')
    print(f'new user_generated_list without target_number {target_number} is: {user_generated_list}')

    print('goodbye!')
    print('**********************************')

    return

repl_loop_list_builder()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter 
# them one at a time. Add each number to a list.

# Once the user enters 'done', ask the user to define the target number for the remove_all function.

# Call the functions using the values the user provides.

# Enter a number or 'done' to quit:
# > 4

# Enter a number or 'done' to quit:
# > 5

# Enter a number or 'done' to quit:
# > 4

# Enter a number or 'done' to quit:
# > 7

# Enter a number or 'done' to quit:
# > 4

# Enter a number or 'done' to quit:
# > 9

# Enter a number or 'done' to quit:
# > done

# Enter a number to remove it from the list: 4

# You entered [4, 5, 4, 7, 4, 9]

# The sum of the numbers is 28

# After removing all the 4s
# The numbers are [5, 7, 9]