import requests

#Config links
URL = "https://www.episodate.com/api/"
OMDb_URL = "https://www.omdbapi.com/"
KEY = 'b578a7b7'


def get_detail_seasons(name, episode, season):
    """
    Get details about a specific season / episode.

    Args:
        name (str): The Tv Show name.
        episode (int): The Episode number.
        season (int): The Season number.

    Returns:
        bool: True/False if the episode exists.
    """
    response = requests.get(URL + 'show-details', {"q": name})
    json_response = response.json()
    all_episodes = json_response['tvShow']['episodes']

    for ep in all_episodes:
        curr_ep = ep['episode']
        curr_season = ep['season']

        if curr_season == season and curr_ep == episode:
            return True

    return False


def check_name_series(name):
    """
    Check Tv Show name, if it exists.

    Args:
        name (str): The Tv Show name.

    Returns:
        bool: True/False if the name exists on IMDb.
    """
    response = requests.get(OMDb_URL, {"apikey": KEY, "t": name})
    json_response = response.json()

    if "Error" in json_response:
        return False

    return True


def get_imdb_link(name):
    """
    Get IMDb link for a specific Tv Show.

    Args:
        name (str): The Tv Show name.

    Returns:
        str: The IMDb link.
    """
    response = requests.get(OMDb_URL, {"apikey": KEY, "t": name})
    json_response = response.json()
    imdb_url = f"https://www.imdb.com/title/{json_response.get('imdbID')}/"
    return imdb_url


def get_rating_series(id):
    """
    Get the rating of a TV Show.

    Args:
        id (str): The ID of the TV Show.

    Returns:
        float: The rating of the TV Show.
    """
    response = requests.get(URL + 'show-details', {"q": id})
    json_response = response.json()
    rating = json_response['tvShow']['rating']
    return rating


def get_series_aprox_score(rating):
    """
    Get TV shows with a similar rating.

    Args:
        rating (float): The rating to compare.

    Returns:
        list: A list of TV Shows with similar ratings.
    """
    response = requests.get(URL + 'most-popular', {"page": 1})
    json_response = response.json()
    series = json_response['tv_shows']
    all_series = []

    for s in series:
        show_id = s['id']
        if int(rating) == int(float(get_rating_series(show_id))):
            all_series.append(s['name'])

    return all_series


def id_series(name):
    """
    Get the ID of a TV Show.

    Args:
        name (str): The Tv Show name.

    Returns:
        str: The ID of the TV show.
    """
    response = requests.get(URL + 'most-popular', {"page": 1})
    json_response = response.json()
    series = json_response['tv_shows']

    for s in series:
        if s['name'] == name:
            return s['id']


def get_new_episodes(name, episode, season):
    """
    Get new episodes of a TV Show.

    Args:
        name (str): The Tv Show name.
        episode (int): The Episode number.
        season (int): The Season number.

    Returns:
        list: A list of dictionaries with information for new episodes.
    """
    show_id = id_series(name)
    response = requests.get(URL + 'show-details', {"q": show_id})
    json_response = response.json()

    if 'episodes' in json_response['tvShow']:
        all_episodes = json_response['tvShow']['episodes']
        new_episodes = []

        for ep in all_episodes:
            curr_ep = int(ep['episode'])
            curr_season = int(ep['season'])
            curr_date = ep['air_date']

            if curr_season > season or (curr_season == season and episode < curr_ep):
                new_episodes.append({'date': curr_date, 'season': curr_season, 'episodes': curr_ep})

        return new_episodes
