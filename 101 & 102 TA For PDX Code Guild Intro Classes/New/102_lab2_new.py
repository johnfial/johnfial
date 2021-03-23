# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab2.md
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def square_the_numbers(input_list):
    print(f'start function square_the_numbers(input_list) with input_list = {input_list}')
    
    counter = 0

    for num in input_list:
        
        print(f'num: {num} changing to num*num: {num * num}')
        num_squared = num * num
        input_list[counter] = num_squared
        counter += 1
    print(input_list)
    return input_list

example_1 = [5, 4, 3]
# print(square_the_numbers(example_1))

example_2 = [70, 97, 56, 20, 82, 15, 19, 15, 87, 11]
# print(square_the_numbers(example_2))

# # # # 2.1 took ~5 minutes (including file setup)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 2.2:
def filter_numbers(input_list, max_number=10):
    '''
    Takes in a list of numbers and a maximum number. The function will return a new list containing only the numbers below the maximum.
    
    Example: 
    
    numbers list: [44, 28, 97, 25, 91, 78, 90, 76, 75, 58]
    maximum number: 50.

    Returns list: [44, 28, 25]
    '''
    print(f'input_list: {input_list}, max_number: {max_number}')
    
    for num in input_list:

        if num > max_number:
            input_list.remove(num)
            print(f'num {num} removed! new list is : {input_list}')
    
        print(f' num: {num} @ line 48')
    
    return input_list

example_list_1 = [44, 28, 97, 25, 91, 78, 90, 76, 75, 58]
maximum_number_1 = 50
# print(filter_numbers(example_list_1, maximum_number_1))
# @ 15 min (10min here on 2.2), almost done, pop index out of range error ...
# @ 21 min (15min here on 2.2), still skipping over items...



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 2.3
def repl_loop():
    '''
    Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter them one at a time. Add each number to a list.
    Once the user enters 'done', pass the user's list into both functions and display the results.
    '''

    user_generated_list = []
    user_input = input('give me an integer (whole) number, or type "done" to finish: > ')    

    while user_input != 'done':
        print('test')

        try:
            # convert to int/float
            user_number = int(user_input)
            
            # add to list:
            user_generated_list.append(user_number)
        except:
            print('invalid number')

        user_input = input('give me a number, or type "done" to finish: > ')  

    if user_input == 'done':       
        print('goodbye')
        print(user_generated_list)

        print(square_the_numbers(user_generated_list))
        print('**********************************')
        print(filter_numbers(user_generated_list))

        return


repl_loop()
# @ 30 min (10min here on 2.3), mostly done



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2.1

# Create a function called square_the_numbers which takes in the list of numbers and returns a list of those numbers all raised to the power of 2.

# Numbers: [70, 97, 56, 20, 82, 15, 19, 15, 87, 11]

# Numbers squared: [4900, 9409, 3136, 400, 6724, 225, 361, 225, 7569, 121]

# 2.2

# Create a function called filter_numbers which takes in a list of numbers and a maximum number. 
# The function will return a new list containing only the numbers below the maximum.

# Numbers: [44, 28, 97, 25, 91, 78, 90, 76, 75, 58]

# The maximum is 50.
# The numbers below the maximum are [44, 28, 25]

# 2.2

# Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter them one at a time. Add each number to a list.

# Once the user enters 'done', pass the user's list into both functions and display the results.

# Enter a number or 'done' to quit:
# > 26

# Enter a number or 'done' to quit:
# > 93

# Enter a number or 'done' to quit:
# > 48

# Enter a number or 'done' to quit:
# > 65

# Enter a number or 'done' to quit:
# > 37

# Enter a number or 'done' to quit:
# > 103

# Enter a number or 'done' to quit:
# > done

# You entered [26, 93, 48, 65, 37, 103]

# Those numbers to the power of 2 are: [676, 8649, 2304, 4225, 1369, 10609]

# The maximum is 50.
# The numbers below the maximum are [44, 28, 25]