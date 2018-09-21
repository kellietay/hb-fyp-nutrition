from sqlalchemy import func
from model import User, Profile, Reference, Food, Record, Calorie, connect_to_db, db
from server import app
import datetime

REFLIST = []

def load_dietaryreference():
    Reference.query.delete()

    for row in open("seed_data/u.reference.csv"):
        row = row.rstrip().split(",")

        if len(row) == 28:

            # gender, min_age, max_age, calories, carbohydrates, fiber, fat, protein, vitA, vitC, vitD, vitE, vitB6, vitB12, thiamin, riboflavin, niacin, folate, calcium, copper, iodine, iron, magnesium, phosphorus, selenium, zinc, potassium, sodium, chloride = row.split(",")

            for i in range(0,28):
                if row[i] == "":
                    row[i] = None

            reference = Reference(min_age = row[1],
                gender = row[0],
                max_age = row[2],
                carbohydrates = row[3],
                fiber = row[4],
                fat = row[5],
                protein = row[6],
                vitA = row[7],
                vitC = row[8],
                vitD = row[9],
                vitE = row[10],
                vitB6 = row[11],
                vitB12 = row[12],
                thiamin = row[13],
                riboflavin = row[14],
                niacin = row[15],
                folate = row[16],
                calcium = row[17],
                copper = row[18],
                iodine = row[19],
                iron = row[20],
                magnesium = row[21],
                phosphorus = row[22],
                selenium = row[23],
                zinc = row[24],
                potassium = row[25],
                sodium = row[26],
                chloride = row[27])

            db.session.add(reference)

        else:
            print('error, row only has {} for gender {}, min_age {}'.format(len(row), row[0], row[1]))
            break

    db.session.commit()


def load_caloriereference():
    Calorie.query.delete()

    for row in open("seed_data/u.calorie.csv"):
        row = row.rstrip().split(",")

        for i in range(0,len(row)):
            if row[i] == "":
                row[i] = None

        calorie = Calorie(gender=row[0],
            min_age=row[1],
            max_age=row[2],
            calories_sedentary=row[3],
            calories_modactive=row[4],
            calories_active=row[5])

        db.session.add(calorie)

    db.session.commit()

def load_user():
    User.query.delete()

    kellie = User(fname="Kellie",
        lname="Tay",
        email="kellie@gmail.com",
        password="password")
    
    paul = User(fname="Paul",
        lname="Ng",
        email="paul@gmail.com",
        password="password")

    db.session.add_all([kellie, paul])

    db.session.commit()

def load_profile():
    Profile.query.delete()

    kellie1 = Profile(user_id=1,
        dietary_id=1,
        calorie_id=1,
        name="Matthew",
        birthdate= "2016-08-06",
        gender=False)

    db.session.add(kellie1)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    # Import different types of data
    load_dietaryreference()
    load_caloriereference()
    load_user()
    load_profile()