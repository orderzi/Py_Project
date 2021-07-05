import os

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_DATABASE')
flask_url = os.environ.get('FLASK_URL')

MY_SQL_CRED = {
    "username": username,
    "password": password,
    "host": host,
    "database": database
}




