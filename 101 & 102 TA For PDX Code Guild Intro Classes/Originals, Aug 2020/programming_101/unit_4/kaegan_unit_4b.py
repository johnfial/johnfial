# Loops!

# Loop a code block until a certain condition is met
# or until the loop is broken manually

animals = ['jaguar', 'ocelot', 'lynx', 'panther']

# for item in sequence:
# each subsequent item is stored in the item variable

# for readability, the item variable
# can be the singular version of the plural list name
for animal in animals:
    # loop this code block
    message = f'current animal: {animal}'
    # print(message)

# print('The loop has ended')

numbers = [45, 13, 33, 77, 5, 100]
for number in numbers:
    message = f'{number} squared is: {number ** 2}'
    # print(message)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    message = f'letter: {letter}'
    # print(message)
# print('keegan'[3]) # strings are also subscriptable (indices can be used)

# for x in range()

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    message = f'x: {x}'
    # print(message)

# built in function len(sequence) 
# will find the length of the sequence
animals_length = len(animals)
# print(animals_length) # 4

for index in range(animals_length):
    # print('index: ', index)
    animal = animals[index]
    message = f'index: {index}, animal: {animal}'
    # print(message)

# range(start, stop)
for x in range(50, 61):
    message = f'number: {x}'
    # print(message)

# range(start, stop, step)
for x in range(0, 10, 2):
    message = f'number: {x}'
    # print(message)

# count backwards from 10 to 0 by 1s
for x in range(10, -1, -1):
    message = f'number: {x}'
    # print(message)


# loop controls
# keywords: continue, break

for x in range(10):

    if x == 3 or x == 5:
        print(f'Skipping {x}')
        
        # go to the top of the loop
        continue
    

    if x == 8:
        print('Goodbye!')
        
        # end the loop
        break

    message = f'number: {x}'
    print(message)
