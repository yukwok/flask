# --- initial comment
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# $ export FLASK_APP=hello
# $ flask run
#  * Running on http://127.0.0.1:5000/

# /Users/prog/Library/Python/3.8/bin
