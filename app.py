from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a simple python web app running on Flash framework!"