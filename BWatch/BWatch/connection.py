import psycopg2

def connect_db():
    """
    Trying connecting to the PostgreSQL database.
    """
    conn = psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="1234",
        port="5432"
    )
    return conn
