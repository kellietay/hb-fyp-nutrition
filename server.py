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
    profile_list = []
    if session.get('userid',None):
        profile_list = User.query.get(session['userid']).profile
    return render_template("homepage.html",profiles=profile_list)

@app.route("/login")
def login_page():
    """login"""
    return render_template("login.html")

@app.route('/verifylogin',methods = ['POST'])
def verifylogin():
    email = request.form.get('email')
    password = request.form.get('password')

    user_object = User.query.filter(User.email == email).first()

    if user_object:
        if user_object.password == password:
            session['userid'] = user_object.user_id
            session['fname'] = user_object.fname
            flash("login successful")
            return redirect('/')

        else:
            flash("Password is incorrect. Please try again")
            return redirect('/login')

    else:
        flash("Login does not exist. Please create account")
        return redirect('/register')

@app.route('/register')
def registration_form():
    """ register new users """
    return render_template("register.html")

@app.route('/add-user', methods = ['POST'])
def add_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    check_email = User.query.filter(User.email == email).first()
    
    if check_email:
        flash("Email already taken. Please try logging in")
        return redirect('/registration')

    else:
        new_user = User(fname=fname, lname=lname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("You have been added. Please login.")
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('userid', None)
    session.pop('fname', None)
    flash('You were logged out')

    return redirect('/')

@app.route('profile/'+session[userid]+'/<profilename>')
def profile(profilename)
    
    
    
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
