from application.app import app
from flask import request
from application.models import WorkItem, db, SubTask, User
from sqlalchemy.exc import IntegrityError
from flask_jwt import jwt_required, JWT, current_identity

# Import your models here
#from application.models import User
from application.models import movie_list
from application.models import series_list


def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.query.filter_by(id=user_id).first()


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user


jwt = JWT(app, authenticate, identity)


@app.route("/")
def home():
    return {"Status": "Success"}, 200

@app.route("/signup", methods=["POST"])
def signup():
    params = request.authorization
    try:
        user = User(**params)
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return {"Status": "Error", "result": "User already exists"}, 400
    return {"Status": "Success", "result": "User created"}

# Write your API endpoints here
@app.route("/movie", methods=["Get"])
def get_movie_list():
    print(request.args)
    country = request.args["countrylist"]
    # method 1
    try:
        genre = request.args["genreid"]
    except KeyError:
        genre  =None


    # Method 2
    #genre = request.args.get("genreid", None)


    #genre = request.args["genreid"]
    print(type(country))
    m_list = movie_list(country, genre)
    print(type(m_list["results"]))
    l = []
    for i in m_list["results"]:
        print(i["title"], ',', i["imdbrating"],',',  i["year"])
        new_dict = {'title': i["title"], 'imdbrating': i["imdbrating"], 'year': i["year"]}
        l.append(new_dict)
    print(type(l))
    print(l)
    movies = {'results':l}
    return movies
# l

@app.route("/series", methods=["Get"])
def get_series_list():
    print(request.args)
    country = request.args["countrylist"]
    try:
        genre = request.args["genreid"]
    except KeyError:
        genre  =None

#    genre = request.args["genreid"]
    print(type(country))
    s_list = series_list(country, genre)
    print(type(s_list["results"]))
    l = []
    for i in s_list["results"]:
        print(i["title"], ',', i["imdbrating"],',',  i["year"])
        new_dict = {'title': i["title"], 'imdbrating': i["imdbrating"], 'year': i["year"]}
        l.append(new_dict)
    print(type(l))
    print(l)
    series = {'results': l}
    return series
