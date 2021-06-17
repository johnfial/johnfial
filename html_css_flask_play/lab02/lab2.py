# @ https://github.com/PdxCodeGuild/class_armadillo/blob/master/3%20Flask/labs/lab02_flask_todo.md
# flask notes @ https://github.com/PdxCodeGuild/class_eagle/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/12%20Flask.md

import json
from flask import Flask
app = Flask(__name__)

def load_json_data():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_json_data(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data))
    return

@app.route('/')
def index():
    return 'Hullo Middle-Earth!'

# app.run(debug=True)

# database filename here:
data = load_json_data()
print(type(data))
print(data)

# data = {}
# save_json_data('database.json', data)
