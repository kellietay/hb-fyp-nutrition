"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Profile, Reference, Food, Record, Calorie, connect_to_db, db

from sqlalchemy.sql import func


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
    """Homepage"""
    return render_template("homepage.html")

@app.route("/login")
def login_page():
    """login"""
    return render_template("login.html")

@app.route('/verifylogin',methods = ['POST'])
def verifylogin():
    email = request.form.get('email')
    password = request.form.get('password')

    User_object = User.query.filter(User.email == email).first()

    if User_object:
        if User_object.password == password:
            session['userid'] = email
            flash("login successful")
            return redirect('/')

        else:
            flash("Password is incorrect. Please try again")
            return redirect('/login')

    else:
        flash("Login does not exist. Please create account")
        return redirect('/registration')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
