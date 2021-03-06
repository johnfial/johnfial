import json

# demonstrating how to go between json and a python dictionary
data = '{"name": "bob"}'
data = json.loads(data) # json string -> python dictionary
print(data['name']) # bob
data = json.dumps(data) # python dictionary -> json string
print(data)

# loads data from db.json, returns a dictionary
def load_database():
    with open('database.json', 'r', encoding='utf-8-sig', errors='ignore') as file:
        data = json.loads(file.read(), strict=False)
    return data

load_database()
print(load_database)