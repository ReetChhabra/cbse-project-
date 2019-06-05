import sqlite3
def startdb():
    global dbconnection
    global cursor
    dbconnection=sqlite3.connect('students.db')
    cursor=dbconnection.cursor()

def createtable(name):
    command='CREATE TABLE {} (adminNo INT, name VARCHAR(40), cls INT, gender VARCHAR(2), fatherName VARCHAR(40), motherName VARCHAR(40), age INT, dob VARCHAR(10), house VARCHAR(15), phoneNo INT, adYear INT, passoutYear VARCHAR(10))'.format(name)
    cursor.execute(command)

def command(string):
    cursor.execute(string)

def closedb():
    dbconnection.commit()
    dbconnection.close()
