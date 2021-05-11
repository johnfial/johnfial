num = 1
if num < 3:
    num = str(num) # needed to add changing num to a string to concatenate below
    print(f'The number is ' + num) # LOOKUP CHANGE INT TO STRING
    print(f'{num} is less than three') #unsure why this breaks # {num} needed curly brackets
    print('thanks for playing!')

    # two other options:
    # print(f'The number is {num}') 
    # OR
    # print ('The number is ' + str(num))

# testing type and trying to remember syntax without looking online!
# num = 5
# print(type(num))
# print(num)

# num = str(num) #had to look online, dammit!
# print(type(num))
# print(num)