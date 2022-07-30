# flask 

from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "This is my first app!!! yay!"

def rootPage():
    return "This is my root page!"

def introPage():
    return 'This is Intro page'
app.run()