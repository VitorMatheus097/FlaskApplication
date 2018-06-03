from app.models.database_connect import Connection

class DataBase:
    db = None

    def __init__(self):
        try:
            self.db = Connection()
        except (Exception) as error:
            print(error)
    
    def kill(self):
        self.db.close()

    def queryData(self, _word):
        cur = self.db.conn.cursor()

        cur.execute("SELECT COUNT(1) FROM word where wrd = '%s';" % _word)
        return cur.fetchone()[0] != 0