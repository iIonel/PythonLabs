from connection import connect_db


def insert_series(name, imdb, season, episode, date, score):
    """
    Insert a TV Show into the database.

    Args:
        name (str): The TV Show name.
        imdb (str): The IMDb link.
        season (int): The last season.
        episode (int): The last episode.
        date (str): The last date watched.
        score (float): The user's score.
    """
    connection = connect_db()
    last_episode = f"{season}, {episode}"

    query = "INSERT INTO SERIES (NAME, IMBD_LINK, LAST_EPISODE, LAST_DATE, SCORE) VALUES (%s, %s, %s, %s, %s);"

    with connection.cursor() as c:
        c.execute(query, (name, imdb, last_episode, date, score))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_series(name):
    """
    Check if a TV Show exists in the database.

    Args:
        name (str): The TV Show name.

    Returns:
        bool: True/False if TV Show exists in database.
    """
    connection = connect_db()
    query = "SELECT * FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        valid = c.fetchone()

    return valid is not None


def delete_series(name):
    """
    Delete a TV Show from the database.

    Args:
        name (str): The Tv Show name.
    """
    connection = connect_db()
    query = "DELETE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_score(name):
    """
    Get the score of a TV Show.

    Args:
        name (str): The Tv Show name.

    Returns:
        int: Returning the score of the TV Show.
    """
    connection = connect_db()
    query = "SELECT SCORE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        score = c.fetchone()

    return score


def update_score(name, score):
    """
    Update the score of a TV Show.

    Args:
        name (str): The Tv Show name.
        score (float): The my new score.
    """
    connection = connect_db()
    query = "UPDATE SERIES SET SCORE = %s WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (score, name))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_snoozed(name):
    """
    Get the snooze status of a TV Show.

    Args:
        name (str): The Tv Show name.

    Returns:
        int: Returing snooze status of the TV Show.
    """
    connection = connect_db()
    query = "SELECT SNOOZED FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        snoozed = c.fetchone()

    return snoozed


def update_snooze(name, flag):
    """
    Update the snooze status of a TV Show.

    Args:
        name (str): The Tv Show name.
        flag (int): Update new snooze status (0: nsnoozed, 1: snoozed).
    """
    connection = connect_db()
    query = "UPDATE SERIES SET SNOOZED = %s WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (flag, name))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_all_series():
    """
    Get a list of all TV Show with snoozed 0.

    Returns:
        list: Returning list of Tv Shows with snoozed 0.
    """
    connection = connect_db()
    query = "SELECT NAME FROM SERIES WHERE SNOOZED = 0;"

    with connection.cursor() as c:
        c.execute(query)
        series = c.fetchall()

    return series


def get_episode(name):
    """
    Get the last episode of a TV Show.

    Args:
        name (str): The Tv Show name.

    Returns:
        tuple: Returning my last episode.
    """
    connection = connect_db()
    query = "SELECT LAST_EPISODE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        episode = c.fetchone()

    return episode
