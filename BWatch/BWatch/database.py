from connection import connect_db


def insert_series(name, imdb, season, episode, date, score):
    connection = connect_db()
    last_episode = f"{season}, {episode}"

    query = "INSERT INTO SERIES (NAME, IMBD_LINK, LAST_EPISODE, LAST_DATE, SCORE) VALUES (%s, %s, %s, %s, %s);"

    with connection.cursor() as c:
        c.execute(query, (name, imdb, last_episode, date, score))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_series(name):
    connection = connect_db()
    query = "SELECT * FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        valid = c.fetchone()

    if valid is not None:
        return True
    return False


def delete_series(name):
    connection = connect_db()
    query = "DELETE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_score(name):
    connection = connect_db()
    query = "SELECT SCORE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        score = c.fetchone()
    return score


def update_score(name, score):
    connection = connect_db()
    query = "UPDATE SERIES SET SCORE = %s WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (score, name))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_snoozed(name):
    connection = connect_db()
    query = "SELECT SNOOZED FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        snoozed = c.fetchone()
    return snoozed


def update_snooze(name, flag):
    connection = connect_db()
    query = "UPDATE SERIES SET SNOOZED = %s WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (flag, name))

    connection.commit()
    print("\033[96mGood job!\033[92m")


def get_all_series():
    connection = connect_db()
    query = "SELECT NAME FROM SERIES WHERE SNOOZED = 0;"

    with connection.cursor() as c:
        c.execute(query)
        series = c.fetchall()

    return series


def get_episode(name):
    connection = connect_db()
    query = "SELECT LAST_EPISODE FROM SERIES WHERE NAME = %s;"

    with connection.cursor() as c:
        c.execute(query, (name,))
        episode = c.fetchone()

    return episode
