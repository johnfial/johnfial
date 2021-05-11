'''
Guess the Number!
ask user to guess the number
and display result
'''

secret = 5

# ask user to guess
guess = input('Guess number between 1 and 10\n>')

# convert
guess = int(guess)

#check if out of range
if guess < 1 or guess > 10:
    print('You must guess between 1 and 10.')
else:
    if guess == secret:
        result = 'You win!'
    elif guess > secret:
        result = 'too high!'
    elif guess < secret:
        result = 'too low!'
    print(result)
    print(f'The secret was: {secret}.')

# phrase "gate my code even further"
# always import at top!
