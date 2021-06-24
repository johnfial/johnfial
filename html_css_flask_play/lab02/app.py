# https://github.com/PdxCodeGuild/class_salmon/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/13%20Flask%20Forms.md
# https://github.com/PdxCodeGuild/class_salmon/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/mob/04%20Flask%20Todo%20List.md

from flask import Flask, render_template, request  # needs lowercase then uppercase!
app = Flask(__name__)
from jsondb import JsonDB

# @app.route('/')
# def index():
#     return r'''
#     <title>
#     Title here!
#     </title>
#     <center>Hullo Middle-Earth!</center>
#     !
#     '''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # contact_name = request.form['input_text']
        # print(contact_name)
        # name = f"{request.form} + 'aoeu'"
        return request.form
    else:
        name = 'bob'
        temperature = 97
        nums = [1, 2, 3]  
        return render_template('index.html', name=name, temperature=temperature, nums=nums)
        #   remember this needs to be in /templates/

database = JsonDB('database.json')
database.load()
# print(database)
# x = database.get('x', 0)
# x += 1
# database.set('x', x)
database_dict = database.get('todos')
print(type(database_dict))
print(database_dict)
# print(len(x))
# database.save()
# print(database)

# app.run(debug=True)