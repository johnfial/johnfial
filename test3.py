

# Define function to remove a number from passed list
def remove_all(numbers, target):
    new_list = [number for number in numbers if number != target]
    print(new_list)
    return new_list


test  =  [3, 3, 3, 4]


print(remove_all(test, 4))

test2 = remove_all(test, 4)

print(test2)