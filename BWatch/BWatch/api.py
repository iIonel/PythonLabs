import requests

URL = "https://www.episodate.com/api/"
OMDb_URL = "https://www.omdbapi.com/"
KEY = 'b578a7b7'


def get_detail_seasons(name, episode, season):
    response = requests.get(URL+'show-details', { "q": name})
    json_response = response.json()
    all_episodes = json_response['tvShow']['episodes']

    for ep in all_episodes:
        curr_ep = ep['episode']
        curr_season = ep['season']

        if curr_season == season and curr_ep == episode:
            return True

    return False

def check_name_series(name):
    response = requests.get(OMDb_URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    if "Error" in json_response:
        return False
    return True


def get_imdb_link(name):
    response = requests.get(OMDb_URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    imdb_url = f"https://www.imdb.com/title/{json_response.get('imdbID')}/"
    return imdb_url


def total_series():
    response = requests.get(OMDb_URL, {"apikey": KEY, "type": 'series'})
    json_response = response.json()
    print(json_response)

def get_series_aprox_score():
    response = requests.get(URL, {"apikey": KEY})
    json_response = response.json()
    if "Error" in json_response:
        return False
    return True