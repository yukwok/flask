# --- initial comment
from flask import Flask

import random

random_number = random.randint(0, 9)
print(random_number)


app = Flask(__name__)

print(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!...</p>"


# @app.route("/")
# def in_homepage():
#     return "<p>Hello, World! i am in root.</p>"

#     # sdgdsgdsfg


# @app.route("/username/<name>/<int:age>")
# def age(name, age):
#     return f"<p>Hello, World! i am {name} in {age} years old.</p>"


# $ export FLASK_APP=hello
# $ flask run
#  * Running on http://127.0.0.1:5000/

# /Users/prog/Library/Python/3.8/bin

if __name__ == "__main__":
    app.run(debug=True)


# comments at the end
