

list1 = [1, 2, 3, 5, ]
def find_max(list_input):

    max_list = max(list_input)
    return max_list

print(find_max(list1))

def find_min(list_input):
    return (min(list_input))

print(find_min(list1))

def combined_function(list_input):
    
    c = []
    c.append(find_max(list_input))
    c.append(find_min(list_input))
    
    print(c)
    return c



print(combined_function) 