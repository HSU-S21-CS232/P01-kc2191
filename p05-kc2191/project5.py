from flask import Flask
import os

#tell flask what app to run
os.environ["FLASK_APP"] = "project5.py"
app = Flask(__name__)

#base route (home page)
@app.route('/')
def home():
    return '<h1>Hello, World! </h1>'

@app.route('/about')
def about():
    return '<h1>About Me</h1><p>My name is Kevin </p>'