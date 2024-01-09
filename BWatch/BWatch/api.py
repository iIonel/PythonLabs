import requests


URL = "https://www.episodate.com/api/"
OMDb_URL = "https://www.omdbapi.com/"
KEY = 'b578a7b7'
Youtube_KEY ='AIzaSyCpZSN2RFQK20d0xiSS73BLDJZ2mKNL-SY'


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


def get_rating_series(id):
    response = requests.get(URL + 'show-details', {"q": id})
    json_response = response.json()
    rating = json_response['tvShow']['rating']
    return rating

def get_series_aprox_score(rating):
    response = requests.get(URL+'most-popular', {"page": 1})
    json_response = response.json()
    series = json_response['tv_shows']
    all_series = []

    for s in series:
       id = s['id']
       if int(rating) == int(float(get_rating_series(id))):
            all_series.append(s['name'])

    return all_series

def id_series(name):
    response = requests.get(URL + 'most-popular', {"page": 1})
    json_response = response.json()
    series = json_response['tv_shows']

    for s in series:
        if s['name'] == name:
            return s['id']

def get_new_episodes(name, episode, season):
    id = id_series(name)
    response = requests.get(URL + 'show-details', {"q": id})
    json_response = response.json()
    if 'episodes' in json_response['tvShow']:
        all_episodes = json_response['tvShow']['episodes']
        new_episodes = []

        for ep in all_episodes:
            curr_ep = int(ep['episode'])
            curr_season = int(ep['season'])
            curr_date = ep['air_date']

            if curr_season > season or (curr_season == season and episode < curr_ep):
                new_episodes.append({'date':curr_date,'season':curr_season,'episodes':curr_ep})
        return new_episodes





