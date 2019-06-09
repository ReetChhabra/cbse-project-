import sqlite3
dbconnection=sqlite3.connect('students.db')
cursor=dbconnection.cursor()

def createtable(name):
    command='CREATE TABLE IF NOT EXISTS {} (adminNo INT, name VARCHAR(40), cls INT, gender VARCHAR(2), fatherName VARCHAR(40), motherName VARCHAR(40), address VARCHAR(60), age INT, dob VARCHAR(10), house VARCHAR(15), phoneNo INT, adYear INT, passoutYear VARCHAR(10));'.format(name)
    cursor.execute(command)


def command(string):
    cursor.execute(string)
    dbconnection.commit()

def fetchdata():
    resultlist= cursor.fetchall()
    return resultlist

def closedb():
    dbconnection.close()
