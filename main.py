import sqlfunctions as sql
import formatdata as format
import variables as var

#always keep all the statements into functions even if its a single line
#statement as all other commands which are not in functions will automatically
#be run as the file is imported in the GUI file

def intialize():
    sql.createtable('students')

def enterdata():
    format.settablenameformanipulating('students')
    sql.command(format.insertrecord(adminNo=var.adminno, name=var.name, cls=var.cls, gender=var.gender, fatherName=var.fathername, motherName=var.mothername, address=var.address, age=var.age, dob=var.dob, house=var.house, phoneNo=var.phoneno, adYear=var.adyear, passoutYear=var.passoutyear))

def query():
    format.settablenameformanipulating('students')
    sql.command(format.queryfromtable(select='*', condition=format.formatconditionforquery(entryvalue=var.where,fieldname=var.fieldname)))
    resultlist=sql.fetchdata()
    for x in resultlist:
        print(x)


def test():
    format.settablenameformanipulating('students')
    print(format.queryfromtable(select='*', condition=format.formatconditionforquery(entryvalue=var.where,fieldname=var.fieldname)))
