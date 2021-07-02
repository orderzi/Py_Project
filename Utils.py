import os
import mysql.connector
import datetime


cwd = os.getcwd()
scores_file = os.path.join(cwd,'Scores/Scores.txt')
scores_file_name = 'Scores.txt'
bad_return_code = -1

def db_connect(db_host, db_user, db_pass):
    flaskdb = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password=db_pass,
        database="flaskdb",
    )
    return flaskdb
db = db_connect('localhost','root','Wdcft5432!')
mycursor = db.cursor()

date = datetime.datetime.now()
sql = "INSERT INTO Scores (User,Scores,Date) VALUES (%s, %s, %s)"
val = ('Moti','91',date)

mycursor.execute(sql, val)
db.commit()

print(mycursor.rowcount, "record inserted.")