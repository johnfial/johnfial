'''
Unit 2
-Variables
-F-strings
-Input
-Integers/Floats (numbers)
'''

# So far we've just been printing our results, but we really want to store them, that's wdat varuables are for
# name the varable to describe the data it holds!

first_name = 'John'
# print(first_name)

greeting = 'Hello, '
city = 'Portland'
number_type = 4

message_a = greeting + first_name + '!'
message_b = 'Today in ' + city + ' it is sunny!'
# print(message_a + ' ' +  message_b)

# -----------------

# formatted strings!
# they allew python *expressions* to be placed within strings and printed!
# initiated before an 'f' before opening quotes
# then expressions are placed in curly brackets

# expression is just python code!

# now with f strings
# message = f'Hello, {first_name}! Today in {city} it is sunny!'
# # print(message)


# message = 'My favorite number is:' + favorite_number
# there's a str(string) function that just converts the interger or number into a text string
favorite_number = 10
message=f'My favorite number is: {favorite_number + 10}'
# print(message)

# -----------------
instrument = 'cello'
# print(type(instrument))


# -----------------
# -----------------
# -----------------

# INPUT!!!

# input displays a prompt message and waits for user input

# print('running!')
# capture user's entry in a variable
# first_name = input("Enter you name: ")
# print(first_name)

# print(number, type(number))

# -----------------

player_1 = input('Enter the name of player 1: ')
instrument_1 = input('Enter the name of player 1\'s instrument: ')


player_2 = input('Enter the name of player 2: ')
instrument_2 = input('Enter the name of player 2\'s instrument: ')

message = f'''
Band Practice!
    {player_1} - {instrument_1}
    {player_2} - {instrument_2}
'''

print(message)






