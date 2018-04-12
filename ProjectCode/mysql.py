import MySQLdb

from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="localhost", user="pi", passwd="raspberry", db="pi")

def insertReading(tagId,action):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y%m%d%H%M%S", localtime())
    cur.execute("""INSERT INTO readings (tagId, time, action) VALUES (%s, %s, %s)""",(tagId,currentTime,action))
    db.commit()
    cur.execute("SELECT name,surname FROM users WHERE id = (SELECT userId FROM cards WHERE tagId=%s LIMIT 1)",(tagId))
    row = cur.fetchone();
    db.close()
    if(row==None):
        return "Neznama karta"
    else:
        return unidecode(row[1]+", "+row[0])
