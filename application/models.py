def movie_list(countrylist,genreid):
    import requests
    url = "https://unogsng.p.rapidapi.com/search"
    headers = {
        'x-rapidapi-key': "a967acffecmsh5456f5c23c3b388p16cdb5jsnd021e4b13a88",
        'x-rapidapi-host': "unogsng.p.rapidapi.com"
    }

    querystring = {"countrylist": countrylist, "genrelist": genreid, "orderby":"rating", "type":"movie"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def series_list(countrylist,genreid):
    import requests
    url = "https://unogsng.p.rapidapi.com/search"
    headers = {
        'x-rapidapi-key': "a967acffecmsh5456f5c23c3b388p16cdb5jsnd021e4b13a88",
        'x-rapidapi-host': "unogsng.p.rapidapi.com"
    }

    querystring = {"countrylist": countrylist, "genrelist": genreid, "orderby":"rating", "type":"series"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()



