import psycopg2


def connect_db():
    conn = psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="1234",
        port="5432"
    )
    return conn
