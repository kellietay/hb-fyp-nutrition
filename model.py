from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import jsonify
db = SQLAlchemy()

class User(db.Model):
    """ Users of nutrition website """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname =  db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "User user_id={} name={} {}".format(self.user_id, self.fname, self.lname)

class Profile(db.Model):
    """ profiles created by each user """

    __tablename__ = "profiles"

    profile_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    # dietary_id = db.Column(db.Integer, db.ForeignKey('dietaryreference.dietary_id'), nullable=False)
    # calorie_id = db.Column(db.Integer, db.ForeignKey('caloriereference.calorie_id'), nullable=False)
    name =  db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    #If Female = True, Male = False and no gender specified = null
    gender = db.Column(db.Boolean, nullable=False)

    #Define relationship between Profile and User
    user = db.relationship("User", backref=db.backref("profile",order_by=profile_id))
    # reference = db.relationship("Reference", backref=db.backref("profile", order_by=profile_id))
    # calorie = db.relationship("Calorie", backref=db.backref("profile",order_by=profile_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "profile id={} name = {}, birthdate = {}".format(self.profile_id, self.name, self.birthdate)


class Reference(db.Model):
    """ Reference table for Reccomended Daily Values """

    __tablename__ = "dietaryreference"

    dietary_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    min_age = db.Column(db.Float, nullable = False)
    max_age = db.Column(db.Float, nullable = True)

    #I = Infant, C = Child, M = Male, F = Female, P = Pregnant, L = Lactating
    gender = db.Column(db.String(1), nullable = True)

    #Setup nutrition data
    carbohydrates = db.Column(db.Float, nullable = False)
    fiber = db.Column(db.Float, nullable = True)
    fat = db.Column(db.Float, nullable = True)
    protein = db.Column(db.Float, nullable = False)
    vitA = db.Column(db.Float, nullable = False)
    vitC = db.Column(db.Float, nullable = False)
    vitD = db.Column(db.Float, nullable = False)
    vitE = db.Column(db.Float, nullable = False)
    vitB6 = db.Column(db.Float, nullable = False)
    vitB12 = db.Column(db.Float, nullable = False)
    thiamin = db.Column(db.Float, nullable = False)
    riboflavin = db.Column(db.Float, nullable = False)
    niacin = db.Column(db.Float, nullable = False)
    folate = db.Column(db.Float, nullable = False)
    calcium = db.Column(db.Float, nullable = False)
    copper = db.Column(db.Float, nullable = False)
    iodine = db.Column(db.Float, nullable = False)
    iron = db.Column(db.Float, nullable = False)
    magnesium = db.Column(db.Float, nullable = False)
    phosphorus = db.Column(db.Float, nullable = False)
    selenium = db.Column(db.Float, nullable = False)
    zinc = db.Column(db.Float, nullable = False)
    potassium = db.Column(db.Float, nullable = False)
    sodium = db.Column(db.Float, nullable = False)
    chloride = db.Column(db.Float, nullable = False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "dietary reference id={} min/max age = {}-{}, gender = {}".format(self.dietary_id, self.min_age, self.max_age, self.gender)


class Calorie(db.Model):
    __tablename__ = "caloriereference"

    calorie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #I = Infant, C = Child, M = Male, F = Female, P = Pregnant, L = Lactating
    gender = db.Column(db.String(1), nullable = True)
    min_age = db.Column(db.Float, nullable = False)
    max_age = db.Column(db.Float, nullable = True)
    calories_sedentary = db.Column(db.Float, nullable = False)
    calories_modactive = db.Column(db.Float, nullable = False)
    calories_active = db.Column(db.Float, nullable = False)

class Food(db.Model):
    """ Food previously added """

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
    """ see https://gist.github.com/mattsilv/95f94dd1378d4747fb68ebb2d042a4a6 
    for a sample response """

    food_name = db.Column(db.String, nullable=False)
    brand_name = db.Column(db.String, nullable=True)
    serving_qty = db.Column(db.Float, nullable=False)
    serving_unit = db.Column(db.String, nullable=False)
    serving_weight_grams = db.Column(db.Float, nullable=False)


    calories = db.Column(db.Float, nullable = False)
    carbohydrates = db.Column(db.Float, nullable = False)
    fiber = db.Column(db.Float, nullable = False)
    fat = db.Column(db.Float, nullable = True)
    protein = db.Column(db.Float, nullable = False)
    vitA = db.Column(db.Float, nullable = False)
    vitC = db.Column(db.Float, nullable = False)
    vitD = db.Column(db.Float, nullable = False)
    vitE = db.Column(db.Float, nullable = False)
    vitB6 = db.Column(db.Float, nullable = False)
    vitB12 = db.Column(db.Float, nullable = False)
    thiamin = db.Column(db.Float, nullable = False)
    riboflavin = db.Column(db.Float, nullable = False)
    niacin = db.Column(db.Float, nullable = False)
    folate = db.Column(db.Float, nullable = False)
    calcium = db.Column(db.Float, nullable = False)
    copper = db.Column(db.Float, nullable = False)
    iodine = db.Column(db.Float, nullable = False)
    iron = db.Column(db.Float, nullable = False)
    magnesium = db.Column(db.Float, nullable = False)
    phosphorus = db.Column(db.Float, nullable = False)
    selenium = db.Column(db.Float, nullable = False)
    zinc = db.Column(db.Float, nullable = False)
    potassium = db.Column(db.Float, nullable = False)
    sodium = db.Column(db.Float, nullable = False)
    chloride = db.Column(db.Float, nullable = False)
    alt_measures = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "food id={}  food name={}".format(self.food_id, self.food_name)


class Record(db.Model):
    __tablename__ = "records"

    record_id = db.Column(db.Integer, autoincrement=True, primary_key=True)    
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.profile_id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    serving_qty = db.Column(db.Float, nullable=False)
    serving_unit = db.Column(db.String, nullable=False)
    serving_weight_grams = db.Column(db.Float, nullable=False)

    #setup relationships
    food = db.relationship("Food", backref=db.backref("record"))
    profile = db.relationship("Profile", backref=db.backref("record"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "profile id ={}, food id={}, serving weight={}, date={}".format(self.profile_id, self.food_id, self.serving_weight_grams, self.date)

    @classmethod
    def convert_to_json(cls, lst):
        
        
        json_dict = self.__dict__
        json_dict.pop('_sa_instance_state')

    @classmethod
    def get_records_from_db(cls, profileid, user_def_date):
        return Record.query.filter(Record.profile_id == profileid).filter(Record.date==user_def_date).all()


    @classmethod
    def calculate_total(cls, rec_obj_list):

        total_list = {'calories': 0,
            'carbohydrates': 0, 
            'fiber': 0, 
            'fat': 0, 
            'protein': 0, 
            'vitA' : 0, 
            'vitC' : 0, 
            'vitD' : 0,
            'vitE' : 0, 
            'vitB6' : 0, 
            'vitB12' : 0, 
            'thiamin' : 0, 
            'riboflavin' : 0, 
            'niacin' : 0, 
            'folate' : 0, 
            'calcium' : 0, 
            'copper' : 0, 
            'iodine' : 0, 
            'iron' : 0, 
            'magnesium' : 0, 
            'phosphorus' : 0, 
            'selenium' : 0, 
            'zinc' : 0, 
            'potassium' : 0,
            'sodium' : 0, 
            'chloride': 0}

        if rec_obj_list != []:

            # For each record object
            for item in rec_obj_list:
                #Calculate the multiplier
                multiplier = (item.serving_qty * item.serving_weight_grams)/item.food.serving_weight_grams
                
                for key in total_list:
                    total_list[key] += round(item.food.__dict__.get(key,0) * multiplier, 2)

        return total_list

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///nutrition'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")