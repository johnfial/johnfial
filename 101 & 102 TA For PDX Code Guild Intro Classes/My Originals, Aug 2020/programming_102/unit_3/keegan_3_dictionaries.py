'''
Unit 3 - Dictionaries

- One of the most powerful datatypes in Python
- Can be used to store large amounts of data
    and make working with that data easy
- Are collections of key:value pairs

'''

# dictionaries are defined using curly brackets

# blank dictionary
blank_dictionary = {}
# print(type(blank_dictionary)) # <class 'dict'>

# add key:value pairs
# keys are generally strings, but can be integers
# values can be ANY datatype, including other dictionaries
availabilities = {'Keegan':'Mon', 'Sarah':'Thu', 'Al':['Mon','Wed','Fri']}

# writing the same dictionary
# with key:value pairs on separate lines
availabilities = {
    # key: value,
    'Keegan': 'Mon',
    'Sarah': 'Thu',
    'Al': ['Mon','Wed','Fri']
}

# 'Unlocking' values using keys
# keys are passed into SQUARE brackets
employee_availability = availabilities['Al']
# print(employee_availability)

# print(availabilities)
# change the value at a particular key
availabilities['Keegan'] = ['Mon','Tue','Wed','Thu','Fri']
# print(availabilities)


# integers can be used as keys but
# Using integers as keys can be confusing with dictionaries
# because they look like lists. 
numbers = {1: 'one', 2: 'two'}
# print(numbers[1]) # this looks like a list reference because the key is an integer

# a good rule of thumb:
# if you see an integer in square brackets, it's probably a list
# if you see a string in square brackets, it's probably a dictionary


# print(availabilities['Tom']) # KeyError: 'Tom' - the key 'Tom' doesn't exist in the dictionary

availabilities['Tom'] = 'Tue' # add a value at the key of 'Tom'
# print(availabilities['Tom']) # Tue

# ------------------------ #

# remove key:value pairs from a dictionary
# keyword: del

# del dictionary_name[key_to_delete]
del availabilities['Sarah'] # delete the key:value pair at the key 'Sarah'
# print(availabilities)

# using a variable as a key
employee_name = 'Keegan'
# print(availabilities[employee_name]) # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# -------------------- #

# Dictionary methods

# dictionary_name.get(key, default_value_if_not_found)
# will return the value at the key if found,
# or the default value if not

# print(availabilities['George']) # KeyError
# print(availabilities.get('George', 'No value found for George')) # No value found for George
# print(availabilities.get('Keegan', 'No value found for Keegan')) # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# add items with .update(dictionary)
new_employees = {
    'John': 'Mon',
    'Yoko': 'Fri'
}

availabilities.update(new_employees)
# print(availabilities)

# remove items with .pop('key')
# pop() removes the value at the key and returns it
# removed_value = availabilities.pop('Keegan')
# print(availabilities)
# print(removed_value) # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


# ---------------------- #

# looping through dictionaries

# using for item in sequence, item will be the current key
for name in availabilities: # same as for name in availbilities.keys()
    # pull out each value using the name as a key
    avail = availabilities[name]

    message = f'name: {name}, availability: {avail}'
    # print(message)


# print(list(availabilities.values())) # list of values
for value in availabilities.values():
    message = f'availability: {value}'

    # print(message)

for item in availabilities.items():
    # print(item)
    # print(item[0], item[1])
    name = item[0] # grab the name at index 0
    avail = item[1] # grab the value at index 1
    message = f'name: {name}, availability: {avail}'
    # print(message)

# "unpack" the tuple for each item into TWO variables
for name, avail in availabilities.items():
    message = f'name: {name}, availability: {avail}'
    # print(message)


fruit_names = ['apple','banana','orange']
fruit_prices = [.75, .6, .33]

# blank dictionary
fruits = {}
for i in range(3):
    fruit_name = fruit_names[i]
    fruit_price = fruit_prices[i]

    fruits[fruit_name] = fruit_price

print(fruits)

# -------------------- #

# print a menu by looping through the dictionary
print('Menu:')
for fruit in fruits:
    print(f'{fruit} - ${fruits[fruit]:.2f}')


# ask the user which fruit they would like to buy
fruit_name = input('Which item would you like? ')

# get the price of the fruit if it exists
fruit_price = fruits.get(fruit_name, f'The following item is not in our inventory: {fruit_name}')

# ask the user how many they want
quantity = input(f'How many {fruit_name}s would you like? ')
quantity = int(quantity)

# calculate the total
total = quantity * fruit_price
# :.2f after a variable formats a float to two decimal places
result = f'{quantity} {fruit_name} @ ${fruit_price:.2f} ea - ${total:.2f}'

# print(result)