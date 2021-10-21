# kevin long, group work, 13 oct 2021
# https://replit.com/@kevinelong/data-transformation#main.py

data = [
    {
        'id': '123',
        'name': 'widget',
        'price': 3.99,
    },
    {
        'id': '456',
        'name': 'gadget',
        'price': 400.51,
    },
]

expected = {
    '123': 
    {
        'id': '123',
        'name': 'widget',
    },
    '456':
    {
        'id': '456',
        'name': 'gadget',
    },
}

def transform(data_list, key_name):  
    # NOTE HINT key_name is a hint!
    # NOTE can solve in one line

    # we want for each object in the list
    # for key_name
    # an output object with each id as the key and the object as the pair
        # transform between outer list to outer dict

    data_objects = {}

    for object in data_list:
        # PART A 
        data_objects[object[key_name]] = object

        # PART B now after video:
        del object[key_name]
        
        # # PART B before video, lolz!:
        # temp_object = {}
        # for iterable_key in object:
        #     print(iterable_key)
        #     print('*')
        #     if iterable_key != key_name:
        #         temp_object[iterable_key] = object[iterable_key]
        # data_objects[object[key_name]] = temp_object

    
    return data_objects

# test 01:
# print(transform(data, 'id'))

# test 02:
print(transform(data, 'name'))

# NOTE
# If you finish then do the extra credit of removing the key_name from the inner object.
# Extra extra credit will be to be ready to answer the question: "Why would you want to do this? When would this be important?"
