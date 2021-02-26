'''
Unit 4 Review

- Datatype: list
- random module (random.choice())
- for item in sequence
- for x in range()
- loop controls:
    - continue
    - break
'''

# lists are 'ordered' and 'changeable' sequences of items

# items are comma separated and surrounded by square brackets

blank_list = []
# print(type(blank_list)) # <class 'list'>

fruits = ['apple', 'banana', 'pear'] # list of strings

# placing items on multiple lines
fruits = [
    'pear', # commas are required
    'apple',
    'banana',
]
# print(fruits) 

# list items can be any datatype
jumble = [1, True, 'moose', 3.14, [1, 2, 3]]
# print(jumble)

# ------------------ #

# because lists are 'ordered' items can be 
# referenced using their position in the list

# an item's position is called its 'index'

# list indices start at 0
# print(fruits[0]) # pear
# print(fruits[1]) # apple
# print(fruits[2]) # banana
# print(fruits[3]) # Too far right! - IndexError: list index out of range

# negative indices start at the last item and work left
# print(fruits[-1]) # banana - starts at -1 because there's no -0
# print(fruits[-2]) # apple
# print(fruits[-3]) # pear
# print(fruits[-4]) # Too far left! - IndexError: list index out of range


# change the value at index 2 to 'mango'
fruits[2] = 'mango'

# index in a variable
to_change = 1
fruits[to_change] = 'peach'

# print(fruits) # ['pear', 'peach', 'mango']


# adding items
# list_name.append(item) - will add the item to the end of the list
fruits.append('grape')
# print(fruits) # ['pear', 'peach', 'mango', 'grape']

# list_name.insert(index, item) - will add the item at the index
fruits.insert(2, 'watermelon')
# print(fruits) # ['pear', 'peach', 'watermelon', 'mango', 'grape']

# lists can be added together
fruits_2 = ['cherry', 'plum']
fruits += fruits_2 # fruits = fruits + fruits_2
# print(fruits) # ['pear', 'peach', 'watermelon', 'mango', 'grape', 'cherry', 'plum']

# removing items
# keyword: del
# del list_name[index] - will remove the item at the index
del fruits[1] # delete peach
# print(fruits) # ['pear', 'watermelon', 'mango', 'grape', 'cherry', 'plum']

# add duplicate to show remove()
fruits.append('watermelon')
# print(fruits) # ['pear', 'watermelon', 'mango', 'grape', 'cherry', 'plum', 'watermelon']

# list_name.remove(item) - will remove the first instance of the item from the list
# removed_fruit = fruits.remove('watermelon')
# print(removed_fruit)
# print(fruits) # ['pear', 'mango', 'grape', 'cherry', 'plum', 'watermelon']

# list_name.pop(index) - remove the item at the index
removed_fruit = fruits.pop(3)
# print(removed_fruit)
# print(fruits)

# list_name.sort() will sort the list
numbers = [8, 4, 67, 34, 12, 99, 101, 134]
# numbers.sort()
# print(numbers) # [4, 8, 12, 34, 67, 99, 101, 134]

colors = ['yellow','grey','teal','fuscia','burgundy']
colors.sort() 
# print(colors) # ['burgundy', 'fuscia', 'grey', 'teal', 'yellow']

# sort in reverse
numbers.sort(reverse=True)
# print(numbers) # [134, 101, 99, 67, 34, 12, 8, 4]

colors.sort(reverse=True)
# print(colors) # ['yellow', 'teal', 'grey', 'fuscia', 'burgundy']

# list_name.count(item) will count the occurances of the item in the list
# print(fruits.count('watermelon')) # 2

# --------------------------------------- #
# print(random.randint(1,100)) # random module doesn't exist here
# import the random module
import random

random_fruit = random.choice(fruits)
# print(random_fruit) # print a random fruit

# ------------- #

# Loops
# code blocks that are repeated until a certain condition is met


# for item in sequence
for fruit in fruits:
    # loop this code block
    message = f'fruit: {fruit}'
    # print(message)

# strings are sequences too
word = 'hello'
for letter in word:
    message = f'letter: {letter}'
    # print(message)


# for item in range()

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    message = f'x: {x}'
    # print(message)


# blank list
squares = []
for x in range(10):
    x_squared = x ** 2 # square of x
    squares.append(x_squared) # add to list

# print(squares)

fruits.append('kiwi')
# len(sequence) will return the length of the sequence as an integer
fruits_length = len(fruits) 
# print(fruits_length) # 7

for index in range(fruits_length):
    # get the fruit at the current index
    fruit = fruits[index]

    message = f'index: {index}, fruit: {fruit}'
    # print(message)

# loop controls
# keywords: continue, break

for x in range(10):
    if x > 2 and x < 6:
        # print('spam')

        # go to the top of the loop
        continue

    if x == 8:
        # print('goodbye')
        
        # end the loop
        break

    # print(x)


words = ['Hello', 'my', 'name', 'is', 'Keegan!']

sentence = ''
for word in words:
    sentence = sentence + word + ' '

# print(sentence) # Hello my name is Keegan!

