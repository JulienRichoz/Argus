import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="argus")

cur = db.cursor()

cur.execute("SELECT * FROM trafic")

for row in cur.fetchall():
    print(row[0])
    print(row[1])
db.close()
