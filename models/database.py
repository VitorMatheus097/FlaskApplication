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

    def tryHeuristic(self, _word):
        return True
    
    def queryData(self, _word):
        cur = self.db.conn.cursor()
        
        _word = re.findall(r'[a-zéúíóáõãêûîôâç\-]*', _word.lower())[0]
        cur.execute("SELECT COUNT(1) FROM word WHERE wrd = '%s'" % _word)
        
        if (cur.fetchone()[0] == 0):
            return False
            # return self.tryHeuristic(_word)
        else:
            return True 
        
    