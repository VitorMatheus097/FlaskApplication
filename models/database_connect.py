import psycopg2
from app.models.database_config import config

class Connection:
    conn = None

    def __init__(self):
        try:
            params = config()
            self.conn = psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            
    def close(self):
        self.conn.close()