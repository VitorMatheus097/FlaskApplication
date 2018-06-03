from app.models.database_connect import Connection
import re

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
        
        _word = re.findall(r'[a-zéúíóáõãêûîôâç\-]*', _word.lower())[0]
        cur.execute("SELECT COUNT(1) FROM word WHERE wrd = '%s'" % _word)
        # cur.execute("SELECT COUNT(1) FROM word WHERE LOWER(wrd) LIKE REGEXP_REPLACE(LOWER('%s'), '[^a-zéúíóáõãêûîôâç\-]*', '', 'g')" % _word)
        
        return cur.fetchone()[0] != 0