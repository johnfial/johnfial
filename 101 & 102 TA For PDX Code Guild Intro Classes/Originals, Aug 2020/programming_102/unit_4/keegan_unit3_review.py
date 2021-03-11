'''
Unit 3 Review

Dictionaries
'''

# curly brackets define a dictionary
fruit_prices = {}

# collections of key:value pairs
fruit_prices = {'apple':.6, 'banana':.7,'orange':.8}


# split key:value pairs onto separate lines
fruit_prices = {
    'apple':.6,
    'orange':.8,
    'banana':[.3,.1,.5],
}


# pull an item out of the dictionary
# by placing its key in square brackets []

fruit_name = 'apple'
apple_price = fruit_prices[fruit_name]
# print(apple_price)

fruit_name = 'banana'
banana_price = fruit_prices[fruit_name]
# print(banana_price) # [0.3, 0.1, 0.5]

# print(banana_price[1]) # 0.1 - second item of the list

# --------------- #

# change a value at a key
fruit_prices['banana'] = .75
# print(fruit_prices) # {'apple': 0.6, 'orange': 0.8, 'banana': 0.75}

# add value to a new key
fruit_prices['mango'] = .45
# print(fruit_prices) # {'apple': 0.6, 'orange': 0.8, 'banana': 0.75, 'mango': 0.45}

# remove a key:value pair
del fruit_prices['orange']
# print(fruit_prices) # {'apple': 0.6, 'banana': 0.75, 'mango': 0.45}

# dictionary methods

# if a key doesn't exist, Python will crash
# print(fruit_prices['watermelon']) # KeyError: 'watermelon'

# dictionary_name.get(key, default_value) will return
# the value at the key or the default value if the key doesn't exist

# print(fruit_prices.get('watermelon')) # None, by default
# print(fruit_prices.get('watermelon', 'No price for watermelon'))


# add key:value pair(s) with .update()

fruit_prices.update({'grapes':.8})
# print(fruit_prices)

new_fruits = {
    'watermelon': 1.0,
    'strawberry': .33
}
fruit_prices.update(new_fruits)
# print(fruit_prices)

# .pop(key) will remove an item at the key and return its value
removed_price = fruit_prices.pop('apple')
# print(fruit_prices)
# print(removed_price)

# .copy() returns a copy of a dictionary
# .clear() removes all items

# --------------------- #

# Looping through dictionaries

# print(fruit_prices.keys()) # dict_keys(['banana', 'mango', 'grapes', 'watermelon', 'strawberry'])
# print(list(fruit_prices.keys())) # ['banana', 'mango', 'grapes', 'watermelon', 'strawberry']

# for key in dictionary_name

# this will loop through the dictionary keys
# same as doing for key in fruit_prices.keys()
for fruit_name in fruit_prices:
    # get the value at the key
    price = fruit_prices[fruit_name]

    # print(fruit_name, price)

# for value in dictionary_name.values():
# print(fruit_prices.values()) # dict_values([0.75, 0.45, 0.8, 1.0, 0.33])
'''
for price in fruit_prices.values():
    print(price)
'''

total = 0
for price in fruit_prices.values():
    # get the sum of all prices
    total += price

# get the number of items in the dictionary
number_of_items = len(fruit_prices) # 5

average_price = total / number_of_items

# print(total, number_of_items, average_price)


# for item in dictionary_name.items()
# print(fruit_prices.items()) # dict_items([('banana', 0.75), ('mango', 0.45), ('grapes', 0.8), ('watermelon', 1.0), ('strawberry', 0.33)])

for item in fruit_prices.items():
    fruit_name = item[0]
    fruit_price = item[1]
    # print(item)
    # print(fruit_name, fruit_price)

# 'unpack' the values in the item into two variables
'''
for fruit_name, fruit_price in fruit_prices.items():
    print(fruit_name, fruit_price)
'''

# tuple/list unpacking
numbers = [1,2,3]
a, b, c = numbers # unpacking the numbers list into three variables
# print(f'a:{a}, b:{b}, c:{c}')



