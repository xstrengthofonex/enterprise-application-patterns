import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = os.path.join(BASE_DIR, 'people.db')

class DB(object):
    def __init__(self, database_url, **params):
        self.dbapi = sqlite3
        self.database_url = database_url
        self.params = params

    def connect(self):
        conn = self.dbapi.connect(self.database_url, **self.params)
        # conn.row_factory = sqlite3.Row
        return conn

db = DB(DATABASE_URL)