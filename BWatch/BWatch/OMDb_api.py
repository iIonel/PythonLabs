import requests

KEY = 'b578a7b7'
URL = "https://www.omdbapi.com/"


def get_total_seasons(name):
    response = requests.get(URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    if json_response.get("totalSeasons") is not None:
        return json_response.get("totalSeasons")
    else:
        return max(int)


def check_name_series(name):
    response = requests.get(URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    if "Error" in json_response:
        return False
    return True


def get_imdb_link(name):
    response = requests.get(URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    imdb_url = f"https://www.imdb.com/title/{json_response.get('imdbID')}/"
    return imdb_url


def get_series_aprox_score():
    response = requests.get(URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    if "Error" in json_response:
        return False
    return True
