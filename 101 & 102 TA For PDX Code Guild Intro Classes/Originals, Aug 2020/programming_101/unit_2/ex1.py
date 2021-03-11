Street = input('Input street name and number: ')
City = input('Enter city: ')
State = input('enter full state name: ')
Zip = input('Enter ZIP Code: ')

# puts the string together here
address = f'''
{Street},
{City}, {State} {Zip} #advanced, could add a +five digit check here and stuff
'''

# Prints it with correct title punctuation!
print(address.title())