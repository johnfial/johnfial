import json

def load_json_data(filename):
    with open(filename, 'r', encoding='cp1252') as file:
        print(file)
        print(type(file))
        print('~~~~~')
        data = json.loads(file.read())
    return data

def save_json_data(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data))
    return

# database filename here:
data = load_json_data('database.json')
print(type(data))
print(data)

# data = {}
# save_json_data('database.json', data)
