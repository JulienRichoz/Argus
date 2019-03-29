
import datetime
import MySQLdb

class StoreDB:

    def __init__(self):
        #init db
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="argus")
        self.cursor = self.db.cursor()
    
    def store(self, value):
        #get datetime
        date = datetime.datetime.now()
        #define format for date
        date.strftime('%Y-%m-%d %H:%M:%S')
        #prepare query to store vlaues
        sql = "INSERT INTO audio(date, intensity) VALUES(%s, %s)"
        #execute query
        self.cursor.execute(sql, (date, value))
        self.db.commit()