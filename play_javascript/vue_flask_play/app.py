from flask import Flask, render_template # needs lowercase then uppercase!
app = Flask(__name__)
print('test')
# BELOW COPIED FROM OTHER LAB
@app.route('/')
def index():
    return render_template('index.html')
print('test 2')