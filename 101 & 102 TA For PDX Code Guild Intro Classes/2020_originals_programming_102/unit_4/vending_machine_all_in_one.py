inventory = {
    'crackers': .5,
    'cookies': .75,
    'mints': .1,
}

def display_inventory():
    '''
    Display the inventory in a nice way
    '''
    print('Inventory')
    print('---------')
    # loop through the inventory dictionary and print each item
    for product, price in inventory.items():
        print(f'{product} - ${price:.2f}')


def get_total(quantity, price_per):
    '''
    Return the result of quantity * price_per
    '''
    return quantity * price_per

def main():
    # display the inventory
    display_inventory()

    # ask the user which product they want
    product = input('Enter the name of the product you want: ')

    # ensure the product is in the inventory
    # If the user enters something invalid, .get returns False
    # not False is True, so the loop will run
    
    while not inventory.get(product, False): # same as while product not in inventory
        print(f'invalid product: {product}')
        product = input('Enter the name of the product you want: ')

    # if the user has exited the above while loop,
    # they have entered a valid key for the dictionary
    product_price = inventory[product]

    # ask how many they want
    quantity = input(f'Enter the number of {product} you want: ')
    
    # ensure the user enters an integer
    while not quantity.isdigit():
        print('Invalid choice')
        quantity = input(f'Enter the number of {product} you want: ')

    # Once a valid number has been entered
    # convert to integer
    quantity = int(quantity) # this will break if quantity can't be converted

    # calculate the total
    total = get_total(quantity, product_price)

    # use :.2f to format prices to two decimal places
    result = f'{quantity} {product} @ ${product_price:.2f} each: ${total:.2f}'

    print(result)

# if the file is run directly, run main()
if __name__ == '__main__':
    main()