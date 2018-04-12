import base64

#base64 image function
def base64Image(path):
	image = open(path, 'rb')
	image_read = image.read()
	image_64_encode = base64.encodestring(image_read)

	return image_64_encode


#start main
from datetime import datetime
import mysql.connector

cnx = mysql.connector.connect(user='jarvis', password='ironmanrules', database='seniordesign')
cursor = cnx.cursor()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sql = ("INSERT INTO Log "
               "(TimeStamp, EventDescription, EventImage) "
               "VALUES (%s, %s, %s)")
sql_data = (timestamp, 'Door Opened', base64Image('IronManTest.png'))

# execute sql
cursor.execute(sql, sql_data)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
