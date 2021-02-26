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
