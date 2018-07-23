from app.models.database_connect import Connection
import re
import nltk
import string

class DataBase:
    db = None

    def __init__(self):
        try:
            self.db = Connection()
        except (Exception) as error:
            print(error)
    
    def kill(self):
        self.db.close()

    def tryHeuristic(self, _word, lower_word):
        cur = self.db.conn.cursor()
        
        cur.execute("SELECT word_mapped FROM word_map WHERE LOWER(word) = '%s'" % lower_word)
        words = cur.fetchall()

        if not words:
            words.append((_word,))
            return [(-1, words)]
        else:
            return [(0, words)]

    def makeNgrams(self, text):
        tokens = nltk.word_tokenize(text)
        return nltk.ngrams(tokens, 3)
    
    def queryData(self, ngram):
        cur = self.db.conn.cursor()

        _word = ngram[2]

        if (_word.isdigit() or _word in string.punctuation): 
            return [(1, [_word if _word in string.punctuation else ' ' + _word])]
        
        lower_word = re.findall(r'[a-zéúíóáõãêûîôâç\-]*', _word.lower())[0]
        cur.execute("SELECT COUNT(1) FROM word WHERE LOWER(wrd) = '%s'" % lower_word)
        
        if (cur.fetchone()[0] == 0):
            return self.tryHeuristic(_word, lower_word)
        else:
            return [(1, [_word if _word in string.punctuation else ' ' + _word])] 
        
    