# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Alexis" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Nathan" # write your name
    age = "46" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Elena" # write your name
    age = "42" # write your age

    return render_template('mother.html' , name = name , age = age)
# define the route to friends webpage
def friend():

    name = "Samuel" # write your name
    age = "16" # write your age

    return render_template('friend.html' , name = name , age = age)
@app.route("/friend")

app.run(debug=True)
