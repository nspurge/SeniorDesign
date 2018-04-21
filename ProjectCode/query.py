#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import b64Image

image = b64Image.base64Image()

hostname = '71.66.232.181'
username = 'jarvis'
password = 'ironmanrules'
database = 'seniordesign'

##hostname = 'localhost'
##username = 'neal'
##password = 'password'
##database = 'seniordesign'

#tagId = '123456789'

def userSearch(tagId):
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
    cur = myConnection.cursor()

    sql = ("SELECT * FROM Users WHERE Rfid_Id = %s AND Deactivate = False")
    sql_data = (tagId)

    cur.execute(sql, sql_data)
    myConnection.commit()
    cur.fetchall()
    count = cur.rowcount

    myConnection.close()

    if(count == 1):
        print (count)
        return count
    else:
        print 'nothing'
        return 0
        
def doorOpen(tagId) :
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    cur = myConnection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = ("INSERT INTO Log (Rfid_Id, TimeStamp, EventDescription, EventImage)"
           " VALUES (%s, %s, %s, %s)")

    sql_data = (tagId, timestamp, 'Door Unlocked', image)
  
    cur.execute(sql, sql_data)
    myConnection.commit()

    myConnection.close()

def doorClose(tagId) :
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    cur = myConnection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = ("INSERT INTO Log (Rfid_Id, TimeStamp, EventDescription, EventImage)"
           " VALUES (%s, %s, %s, %s)")

    sql_data = (tagId, timestamp, 'Door Locked', image)

    cur.execute(sql, sql_data)
    myConnection.commit()

    myConnection.close()

def doNothing(tagId) :
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    cur = myConnection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = ("INSERT INTO Log (Rfid_Id, TimeStamp, EventDescription, EventImage)"
           " VALUES (%s, %s, %s, %s)")

    sql_data = (tagId, timestamp, 'Unauthorized Access Attempt', image)
    
    cur.execute(sql, sql_data)
    myConnection.commit()

    myConnection.close()
