from application.app import app, db
import os

country_dict = {'Australia': 89, 'Canada': 33, 'United Kingdom': 46, 'United States': 78, 'India': 337}
#print(country_dict)

genre_dict = {'Sports Documentaries': 180, 'Independent Dramas': 384, 'Anime Dramas':452,
              'Children & Family Films': 783, 'Critically-acclaimed Independent Films': '875',
              'Critically-acclaimed Action & Adventure': 899, 'Steamy Thrillers': 972,
              'Sci-Fi & Fantasy': 1492, 'Korean Drama Movies': 1989,
              'Courtroom Dramas': 2748, 'Independent Thrillers': 3269, 'Romantic Films based on a book': 3830,
              'Sitcoms': 3903, 'Sci-Fi Dramas': 3916, 'Critically Acclaimed Films': 3979,
              'Animation': 4698, 'Indian Dramas': 5051, 'Bollywood Films': 5480, 'Documentaries': 6839,
              'Indian Comedies': 9942, 'Political Thrillers': 10504, 'Sci-Fi Thrillers': 11014,
              'Stand-up Comedy': 11559, 'Action Thrillers': 43048
              }

#print(genre_dict)

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


