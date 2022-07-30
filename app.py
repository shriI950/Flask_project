# flask 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is my first app!!! yay!"

app.run()