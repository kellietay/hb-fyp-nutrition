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

import secrets

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
app.secret_key = secrets.APP_PASSWORD

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
    print(profile_list)

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
    
    input_date = request.args.get('inputdate', None)

    profile_list = []
    if session.get('userid',None):
        profile_list = User.query.get(session['userid']).profile

    notused, ref_obj, cal_obj, nutrient_dict, rec_obj, total_nutrients, inputdate, macro_dict, vitamin_dict, element_dict, percent_nutrients = refreshtable(profileid, input_date)
    
    #7: display the respective nutrients on the html
    return render_template('profile.html', profileid=profileid, 
                                            profiles=profile_list,
                                            profile_obj=notused,
                                            userid=userid, 
                                            ref_obj=ref_obj, 
                                            cal_obj=cal_obj, 
                                            nutrient_dict=nutrient_dict, 
                                            rec_obj=rec_obj, 
                                            total_nutrients=total_nutrients,
                                            input_date=inputdate,
                                            macro=macro_dict,
                                            vitamin=vitamin_dict,
                                            element=element_dict,
                                            percent=percent_nutrients)
    

def refreshtable(profileid = None, inputdate = None):

    if not profileid:
        profileid = request.args.get('profileid')
    
    if not inputdate:
        inputdate = request.args.get('inputdate', datetime.date.today())

    profile_obj = Profile.query.get(profileid)

    age = (datetime.date.today() - profile_obj.birthdate).days / 365

    ref_obj = Reference.query.filter(Reference.min_age < age).filter(Reference.max_age > age).first()

    cal_obj = Calorie.query.filter(Calorie.min_age < age).filter(Calorie.max_age > age).first()

    nutrient_dict = {'carbohydrates': 'Carbohydrates (g)', 
        'fiber': 'Total Fibre (g)', 
        'fat': 'Fat (g)', 
        'protein': 'Protein (g)', 
        'vitA' : 'Vitamin A (μg)', 
        'vitC' : 'Vitamin C (mg)', 
        'vitD' : 'Vitamin D (μg)',
        'vitE' : 'Vitamin E (mg)', 
        'vitB6' : 'Vitamin B6 (mg)', 
        'vitB12' : 'Vitamin B12 (μg)', 
        'thiamin' : 'Thiamin (mg)', 
        'riboflavin' : 'Riboflavin (mg)', 
        'niacin' : 'Niacin (mg)', 
        'folate' : 'Folate(μg)', 
        'calcium': 'Calcium (mg)', 
        'copper' : 'Copper (μg)', 
        'iron' : 'Iron (mg)', 
        'magnesium' : 'Magnesium (mg)', 
        'phosphorus' : 'Phosphorus (mg)', 
        'selenium' : 'Selemium (μg)', 
        'zinc' : 'Zinc (mg)', 
        'potassium' : 'Potassium (g)',
        'sodium' : 'Sodium (g)'}

    macro_dict = {'carbohydrates': 'Carbohydrates (g)', 
        'fiber': 'Total Fibre (g)', 
        'fat': 'Fat (g)', 
        'protein': 'Protein (g)'}

    vitamin_dict = {'vitA' : 'Vitamin A (μg)', 
        'vitC' : 'Vitamin C (mg)', 
        'vitD' : 'Vitamin D (μg)',
        'vitE' : 'Vitamin E (mg)', 
        'vitB6' : 'Vitamin B6 (mg)', 
        'vitB12' : 'Vitamin B12 (μg)', 
        'thiamin' : 'Thiamin (mg)', 
        'riboflavin' : 'Riboflavin (mg)', 
        'niacin' : 'Niacin (mg)', 
        'folate' : 'Folate(μg)'}

    element_dict = {'calcium': 'Calcium (mg)', 
        'copper' : 'Copper (μg)', 
        'iron' : 'Iron (mg)', 
        'magnesium' : 'Magnesium (mg)', 
        'phosphorus' : 'Phosphorus (mg)', 
        'selenium' : 'Selemium (μg)', 
        'zinc' : 'Zinc (mg)', 
        'potassium' : 'Potassium (g)',
        'sodium' : 'Sodium (g)'}

    rec_obj = Record.get_records_from_db(profileid, inputdate)

    total_nutrients = Record.calculate_total(rec_obj)
    
    percent_nutrients = {}

    for key, value in total_nutrients.items():
        
        if key == "calories":
            percent_nutrients[key] = round(total_nutrients[key]/cal_obj.__dict__["calories_modactive"]*100,1)
        
        elif value == 0 or not ref_obj.__dict__.get(key, None):
            percent_nutrients[key] = 0

        else:
            percent_nutrients[key] = round(total_nutrients[key]/ref_obj.__dict__[key]*100,1)

    return profile_obj, ref_obj, cal_obj, nutrient_dict, rec_obj, total_nutrients, inputdate, macro_dict, vitamin_dict, element_dict, percent_nutrients
                            

# @app.route('/profile/retrieve')
# @login_required
# def retrieve_table():

#     profileid = request.args.get('profileid')
#     input_date = request.args.get('inputdate')

#     profile_list = []
#     if session.get('userid',None):
#         profile_list = User.query.get(session['userid']).profile

#     notused, ref_obj, cal_obj, nutrient_dict, rec_obj, total_nutrients, inputdate, macro_dict, vitamin_dict, element_dict, percent_nutrients = refreshtable(profileid, input_date)
    
#     #7: display the respective nutrients on the html
#     return render_template('profile_date_ajax.html', profileid=profileid,
#                                             profiles=profiles_list,
#                                             profile_obj=notused,
#                                             userid=userid, 
#                                             ref_obj=ref_obj, 
#                                             cal_obj=cal_obj, 
#                                             nutrient_dict=nutrient_dict, 
#                                             rec_obj=rec_obj, 
#                                             total_nutrients=total_nutrients,
#                                             input_date=inputdate,
#                                             macro=macro_dict,
#                                             vitamin=vitamin_dict,
#                                             element=element_dict,
#                                             percent=percent_nutrients)

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


@app.route('/profile/getfoodlistfromapi')
@login_required
def getfoodlistfromapi():
    foodname = request.args.get("addfood")
    headers = {"x-app-id": secrets.NUTRITIONIX_ID,
                "x-app-key": secrets.NUTRITIONIX_KEY}
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



@app.route('/profile/addfood', methods = ['POST'])
@login_required
def addfood():
    foodname = request.form.get("inputfood","applesauce")
    profileid = request.form.get("profileid", 1)
    inputdate = request.form.get("inputdate", "2018-10-07")

    food_object = Food.query.filter(Food.food_name == foodname).first()

    if not food_object:

        print("{} does not exist in SQL. Creating Food".format(foodname))

        headers = {"x-app-id": secrets.NUTRITIONIX_ID,
                    "x-app-key": secrets.NUTRITIONIX_KEY,
                    "Content-Type": "application/json"}
        data = {"query": foodname }

        r = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients',
                    headers=headers,
                    json=data)

        json_data = json.loads(r.text).get("foods")[0]
        nutrient_data = {}

        for item in json_data.get("full_nutrients"):
            nutrient_data["attr_{}".format(item['attr_id'])] = item['value']

        altr_measures = {}
        if json_data.get("alt_measures"):
            for item in json_data.get("alt_measures"):
                altr_measures[item["measure"]] = item["serving_weight"]

            str_alt_measures = ", ".join(["{}:{}".format(key, value) for (key, value) in altr_measures.items()])
        else:
            str_alt_measures = ""

        test1 = Food(food_name = json_data.get("food_name"),
            brand_name = None,
            serving_qty = json_data.get("serving_qty"),
            serving_unit = json_data.get("serving_unit"),
            serving_weight_grams = json_data.get("serving_weight_grams"),
            calories = json_data.get("nf_calories", 0),
            carbohydrates = json_data.get("nf_total_carbohydrate", 0),
            fiber = json_data.get("nf_dietary_fiber", 0),
            fat = json_data.get("nf_total_fat", 0),
            protein = json_data.get("nf_protein", 0),
            vitA = nutrient_data.get("attr_320", 0),
            vitC = nutrient_data.get("attr_401", 0),
            vitD = nutrient_data.get("attr_328", 0),
            vitE = nutrient_data.get("attr_323", 0),
            vitB6 = nutrient_data.get("attr_415", 0),
            vitB12 = nutrient_data.get("attr_418", 0),
            thiamin = nutrient_data.get("attr_404", 0),
            riboflavin = nutrient_data.get("attr_405", 0),
            niacin = nutrient_data.get("attr_406", 0),
            folate = nutrient_data.get("attr_417", 0),
            calcium = nutrient_data.get("attr_301", 0),
            copper = nutrient_data.get("attr_312", 0),
            iodine = 0,
            iron =  nutrient_data.get("attr_303", 0),
            magnesium = nutrient_data.get("attr_304", 0),
            phosphorus = nutrient_data.get("attr_305", 0),
            selenium = nutrient_data.get("attr_317", 0),
            zinc = nutrient_data.get("attr_309", 0),
            potassium = json_data.get("nf_potassium")/1000,
            sodium = nutrient_data.get("attr_307", 0)/1000,
            chloride = 0,
            alt_measures = str_alt_measures)

        db.session.add(test1)
        db.session.commit()

        print(test1.food_id)

    else:
        print(food_object)
        print("FOOD IS FOUND. DONT MESS UP")

    newfood = Food.query.filter(Food.food_name == foodname).first()
    print(newfood)

    newrecord = Record(profile_id=profileid, 
                        food_id=newfood.food_id, 
                        date=inputdate,
                        serving_qty=0,
                        serving_unit=newfood.serving_unit,
                        serving_weight_grams=newfood.serving_weight_grams)

    db.session.add(newrecord)
    db.session.commit()

    print(newrecord.record_id)

    return render_template("record_ajax.html", item=newrecord)
    # need to replace this with the profile/retrieve


@app.route('/profile/updaterecords', methods=['POST'])
@login_required
def addrecord():
    recordid = request.form.get("recordid")
    newquantity = request.form.get("newquantity")
    profileid = request.form.get("profileid")
    inputdate = request.form.get("inputdate")
    updatetype = request.form.get("type")

    record_obj = Record.query.get(recordid)

    print(record_obj, recordid, newquantity, profileid, inputdate, updatetype)

    if record_obj and newquantity and updatetype == "update":
        record_obj.serving_qty = float(newquantity)
        db.session.commit()
        print("updated record")

    elif record_obj and updatetype == "delete":

        db.session.delete(record_obj)
        db.session.commit()
        print("deleted record")

    else:
        return "please check code"

    profile_list = []
    if session.get('userid',None):
        userid=session.get('userid',None)
        profile_list = User.query.get(session['userid']).profile

    notused, ref_obj, cal_obj, nutrient_dict, rec_obj, total_nutrients, inputdate, macro_dict, vitamin_dict, element_dict, percent_nutrients = refreshtable(profileid, inputdate)
    
    #7: display the respective nutrients on the html
    return render_template('profile_ajax.html', profileid=profileid, 
                                            profiles=profile_list,
                                            profile_obj=notused,
                                            userid=userid, 
                                            ref_obj=ref_obj, 
                                            cal_obj=cal_obj, 
                                            nutrient_dict=nutrient_dict, 
                                            rec_obj=rec_obj, 
                                            total_nutrients=total_nutrients,
                                            input_date=inputdate,
                                            macro=macro_dict,
                                            vitamin=vitamin_dict,
                                            element=element_dict,
                                            percent=percent_nutrients)


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
