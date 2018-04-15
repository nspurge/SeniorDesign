#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import read
import b64Image

#tagId = read.readTag()
tagId = '123456789'

#filename = '/home/pi/Desktop/SeniorDesign/ProjectCode/Images/' + datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg")
image = b64Image.base64Image()

##hostname = '71.66.232.181'
##username = 'jarvis'
##password = 'ironmanrules'
##database = 'seniordesign'

hostname = 'localhost'
username = 'neal'
password = 'password'
database = 'seniordesign'

def userSearch():
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
    cur = myConnection.cursor()

    sql = ("SELECT * FROM Users WHERE Rfid_Id = %s")
    sql_data = (tagId)

    cur.execute(sql, sql_data)
    myConnection.commit()
    cur.fetchall()
    count = cur.rowcount

    myConnection.close()

    if(count == 1):
        return count
        print (count)
    else:
        return 0
        print 'nothing'

def doorOpen() :
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    cur = myConnection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = ("INSERT INTO Log (Rfid_Id, TimeStamp, EventDescription, EventImage)"
           " VALUES (%s, %s, %s, %s)")

    sql_data = (tagId, timestamp, 'Door Unlocked', image)

#    print (sql)
#    print (sql_data)
  
    cur.execute(sql, sql_data)
    myConnection.commit()

    myConnection.close()

def doorClose() :
    import MySQLdb
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

    cur = myConnection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = ("INSERT INTO Log (Rfid_Id, TimeStamp, EventDescription, EventImage)"
           " VALUES (%s, %s, %s, %s)")

    sql_data = (tagId, timestamp, 'Door Locked', image )

#    print (sql)
#    print (sql_data)
    
    cur.execute(sql, sql_data)
    myConnection.commit()

    myConnection.close()



