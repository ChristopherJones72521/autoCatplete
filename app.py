#!/usr/bin/Python

from flask import Flask
app = Flask(__name__)
app.run(host='0.0.0.0')
 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"
 
if __name__ == "__main__":
    app.run()