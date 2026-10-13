from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello CART 351!</h1>'

@app.route("/about")
def about():
    return '<h1 style="color:purple">About Cart 351!</h1>'

@app.route("/bio")
def bio():
    return '<h1 style="color:blue; background-color:powderblue; text-decoration: wavy underline; font-family: verdana">hey!</h1><p>bye</p>'

@app.route("/user/<name>")
def user_profile(name):
    return f"<h2>This is <span style='color:orange; text-decoration: underline'>{name}'s</span> profile page</h2>"

@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    # we will use templates soon!
    return f"<h2>the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"

@app.route("/cat/<name>")
def cat_name(name):

    if name.endswith("y"):
        remove_y= name[0:-1]
        new_name = remove_y + "iful"
        return f"ur cat's name is now {new_name}"
    else:
        new_name= name + "y"
        return f"<h1> <span style = 'color:blue'>ur cat's name is now {new_name}</h1>"

app.run()

