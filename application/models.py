from application.app import app, db
import os
def movie_list(countrylist,genreid):
    import requests
    url = "https://unogsng.p.rapidapi.com/search"
    headers = {
        'x-rapidapi-key': os.environ["Rapid_key"],
        'x-rapidapi-host': os.environ["Rapid_host"]
    }

    querystring = {"countrylist": countrylist, "genrelist": genreid, "orderby":"rating", "type":"movie"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def series_list(countrylist,genreid):
    import requests
    url = "https://unogsng.p.rapidapi.com/search"
    headers = {
        'x-rapidapi-key': os.environ["Rapid_key"],
        'x-rapidapi-host': os.environ["Rapid_host"]
    }

    querystring = {"countrylist": countrylist, "genrelist": genreid, "orderby":"rating", "type":"series"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def country():
    import requests
    url = "https://unogsng.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-key': os.environ["Rapid_key"],
        'x-rapidapi-host': os.environ["Rapid_host"]
    }

    response = requests.request("GET", url, headers=headers)

    with open('countries.csv', 'w') as fd:
        #for chunk in response.iter_content(chunk_size):
        fd.write(response.text)

def genre():
    import requests
    url = "https://unogsng.p.rapidapi.com/genres"

    headers = {
        'x-rapidapi-key': os.environ["Rapid_key"],
        'x-rapidapi-host': os.environ["Rapid_host"]
    }

    response = requests.request("GET", url, headers=headers)

    with open('genre.csv', 'w') as fd:
        #for chunk in response.iter_content(chunk_size):
        fd.write(response.text)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))


db.create_all()
db.init_app(app)
