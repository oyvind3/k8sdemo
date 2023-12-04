import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    pod_name = os.getenv('HOSTNAME', 'localhost')
    return render_template("index.html", title="Hello from flask in kubernetes", pod_name=pod_name)
