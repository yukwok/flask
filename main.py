# --- initial comment
from flask import Flask

app = Flask(__name__)

# print(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!...</p>"


@app.route("/")
def in_homepage():
    return "<p>Hello, World! i am in root.</p>"


@app.route("/username/<name>/<int:age>")
def age(name, age):
    return f"<p>Hello, World! i am {name} in {age} years old.</p>"


# $ export FLASK_APP=hello
# $ flask run
#  * Running on http://127.0.0.1:5000/

# /Users/prog/Library/Python/3.8/bin

if __name__ == "__main__":
    app.run(debug=True)
