

# https://github.com/PdxCodeGuild/class_salmon/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/13%20Flask%20Forms.md

from flask import Flask  # needs lowercase then uppercase!
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hullo Middle-Earth!'

app.run(debug=True)

