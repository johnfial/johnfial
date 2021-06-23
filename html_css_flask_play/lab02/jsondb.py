# https://github.com/PdxCodeGuild/class_salmon/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/mob/jsondb.py
import json

class JsonDB:
    def __init__(self, path='database.json'):
        print('hello from CLASS INIT!')
        self.path = path
        self.data = None
    
    def __str__(self) -> str:
        print('hello from the class __str__ function')
        return str(self.data)
    
    def load(self):
        with open(self.path, 'r') as file:
            self.data = json.loads(file.read())
        
    def save(self):
        with open(self.path, 'w') as file:
            file.write(json.dumps(self.data, indent=4, sort_keys=True))
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
    
    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
    
    def clear(self, key=None):
        if key is not None:
            del self.data[key]
        else:
            self.data = {}