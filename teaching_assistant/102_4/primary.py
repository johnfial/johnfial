# PRIMARY MODULE
# import secondary
from secondary import add

# run the say_hello function within the secondary module
# secondary.say_hello()


def main():
    # 'pass' allows a blank code block

    x = 5
    y = 10

    print(f'{x} + {y} = {add(x, y)}')


main()

