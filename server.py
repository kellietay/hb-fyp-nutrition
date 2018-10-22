"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, g, jsonify)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Profile, Reference, Food, Record, Calorie, connect_to_db, db

from sqlalchemy.sql import func

import datetime

from functools import wraps

import requests

from copy import deepcopy

import json

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('userid') is None:
            flash("The page you are trying to access requires a login. Please login.")
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

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
    return render_template("register.html");

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

@app.route('/profile/<userid>/<profileid>')
@login_required
def profile(userid, profileid):
    
    #1: retrieve profile id and birth date

    profile_obj = Profile.query.get(profileid)

    #2: use birthdate to calculate the correct Reference and Calorie tables

    age = (datetime.date.today() - profile_obj.birthdate).days / 365

    ref_obj = Reference.query.filter(Reference.min_age < age).filter(Reference.max_age > age).first()

    cal_obj = Calorie.query.filter(Calorie.min_age < age).filter(Calorie.max_age > age).first()

    #3: save the Reference and Calorie tables to the db



    #4: retrieve the Reference and Calorie tables and display on the html page

    nutrient_dict = {'carbohydrates': 'Carbohydrates (g)', 
        'fiber': 'Total Fibre (g)', 
        'fat': 'Fat (g)', 
        'protein': 'Protein (g)', 
        'vitA' : 'Vitamin A (μg)', 
        'vitC' : 'Vitamin C (mg)', 
        'vitD' : 'Vitamin D (mg)',
        'vitE' : 'Vitamin E (mg)', 
        'vitB6' : 'Vitamin B6 (mg)', 
        'vitB12' : 'Vitamin B12 (μg)', 
        'thiamin' : 'Thiamin (mg)', 
        'riboflavin' : 'Riboflavin (mg)', 
        'niacin' : 'Niacin (mg)', 
        'folate' : 'Folate(μg)', 
        'calcium': 'Calcium (mg)', 
        'copper' : 'Copper (μg)', 
        'iodine' : 'Iodine(μg)', 
        'iron' : 'Iron (mg)', 
        'magnesium' : 'Magnesium (mg)', 
        'phosphorus' : 'Phosphorus (mg)', 
        'selenium' : 'Selemium (μg)', 
        'zinc' : 'Zinc (mg)', 
        'potassium' : 'Potassium (g)',
        'sodium' : 'Sodium (μg)', 
        'chloride': 'Chloride (g)'}

    #5: retrieve the Records from the record db for this profile and today's date

    rec_obj = Record.get_records_from_db(profileid, "2018-10-07")

    total_nutrients = Record.calculate_total(rec_obj)
    

    #7: display the respective nutrients on the html
    return render_template('profile.html', profileid=profileid, 
                                            userid=userid, 
                                            ref_obj=ref_obj, 
                                            cal_obj=cal_obj, 
                                            nutrient_dict=nutrient_dict, 
                                            rec_obj=rec_obj, 
                                            total_nutrients=total_nutrients)
    

@app.route('/profile/retrieve')
@login_required
def retrieve_table():

    profileid = request.args.get('profileid')
    inputdate = request.args.get('inputdate')

    profile_obj = Profile.query.get(profileid)

    age = (datetime.date.today() - profile_obj.birthdate).days / 365

    ref_obj = Reference.query.filter(Reference.min_age < age).filter(Reference.max_age > age).first()

    cal_obj = Calorie.query.filter(Calorie.min_age < age).filter(Calorie.max_age > age).first()

    #3: save the Reference and Calorie tables to the db



    #4: retrieve the Reference and Calorie tables and display on the html page

    nutrient_dict = {'carbohydrates': 'Carbohydrates (g)', 
        'fiber': 'Total Fibre (g)', 
        'fat': 'Fat (g)', 
        'protein': 'Protein (g)', 
        'vitA' : 'Vitamin A (μg)', 
        'vitC' : 'Vitamin C (mg)', 
        'vitD' : 'Vitamin D (mg)',
        'vitE' : 'Vitamin E (mg)', 
        'vitB6' : 'Vitamin B6 (mg)', 
        'vitB12' : 'Vitamin B12 (μg)', 
        'thiamin' : 'Thiamin (mg)', 
        'riboflavin' : 'Riboflavin (mg)', 
        'niacin' : 'Niacin (mg)', 
        'folate' : 'Folate(μg)', 
        'calcium': 'Calcium (mg)', 
        'copper' : 'Copper (μg)', 
        'iodine' : 'Iodine(μg)', 
        'iron' : 'Iron (mg)', 
        'magnesium' : 'Magnesium (mg)', 
        'phosphorus' : 'Phosphorus (mg)', 
        'selenium' : 'Selemium (μg)', 
        'zinc' : 'Zinc (mg)', 
        'potassium' : 'Potassium (g)',
        'sodium' : 'Sodium (μg)', 
        'chloride': 'Chloride (g)'}

    #5: retrieve the Records from the record db for this profile and today's date

    rec_obj = Record.get_records_from_db(profileid, inputdate)

    total_nutrients = Record.calculate_total(rec_obj)
    

    #7: display the respective nutrients on the html
    return render_template('profile_ajax.html', profileid=profileid, ref_obj=ref_obj, cal_obj=cal_obj, nutrient_dict=nutrient_dict, rec_obj=rec_obj, total_nutrients=total_nutrients)
    



@app.route('/profile/new-profile')
@login_required
def newprofile():
    """form page to add new profile"""
    return render_template('newprofile.html')


@app.route('/profile/add-new-profile', methods = ['POST'])
@login_required
def addprofile():
    """ process post request to add new profile to db"""
    name = request.form.get('name')
    birthdate = request.form.get('birthdate')
    gender = request.form.get('gender')

    gender_bool = False

    if gender == 'Male':
        gender_bool = False
    elif gender == 'Female':
        gender_bool = True

    new_profile = Profile(name=name, birthdate=birthdate, gender=gender_bool, user_id=session.get('userid'))
    db.session.add(new_profile)
    db.session.commit()
    flash("New profile {} has been created".format(name))
    
    profile_obj = Profile.query.filter(Profile.name==name).filter(Profile.user_id==session.get('userid')).first()

    return redirect('/profile/{}/{}'.format(session['userid'], profile_obj.profile_id))


@app.route('/profile/<profileid>/addfood')
@login_required
def addfood(profileid):
    foodname = request.args.get("addfood")
    headers = {"x-app-id":"4df5cc3a",
                "x-app-key": "05fda724b6e208054c3a62bf6bab320f"}
    payload = {"query": foodname }

    r = requests.get('https://trackapi.nutritionix.com/v2/search/instant',
                headers=headers,
                params=payload)

    json_data = json.loads(r.text)

    lst=[]
    for item in json_data['common']:
        lst.append(item["food_name"])
        print(lst)

    return jsonify(lst)


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
