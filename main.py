import sqlfunctions as sql
import formatdata as format


sql.startdb()
sql.createtable('students')
format.settablenameformanipulating('students')
sql.command(format.insertrecord(adminNo='123', name='arpan', cls='12', gender='M', fatherName='Dilawar', motherName='Unknown', age='17', dob='2002/01/09', house='Ashoka', phoneNo='1234567890', adYear='2005', passoutYear='--'))
