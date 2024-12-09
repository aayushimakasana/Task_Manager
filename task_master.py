from flask import Flask

app = Flask(__name__)

@app.route("/")
def task_master():
    return "<p>Hello and Welcome to Task Master!</p>"

