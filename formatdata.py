def settablenameformanipulating(name):
    global tablename
    tablename=name

#just pass all the information as named arguments the rest will be handled by the function
#Example: insertrecord(adminNo='984', name='Reet' ,age='12' etc)
#only pass data as a string even if it is an integer
def insertrecord( name, adminNo , adYear , passoutYear , cls , phoneNo , house , motherName , fatherName , age , dob , gender , address):
    restr='INSERT INTO '+tablename+'(adminNo, name, cls, gender, fatherName, motherName, address, age, dob, house, phoneNo, adYear, passoutYear)'+" VALUES ({0} , '{1}', {2}, '{3}', '{4}', '{5}', '{6}' , {7}, '{8}', '{9}', {10}, '{11}', '{12}');".format(adminNo, name, cls, gender, fatherName, motherName, address, age, dob, house, phoneNo, adYear, passoutYear)
    return restr

#just pass what to select and a condition as named arguments
def queryfromtable(select, condition):
    restr='SELECT {} '.format(select)+'FROM {} '.format(tablename)+'WHERE {}'.format(condition)+';'
    return restr

def formatconditionforquery(fieldname, entryvalue):
    if fieldname == 'Admission Number' :
        return 'adminNo={}'.format(entryvalue)
    elif fieldname == 'Name' :
        return 'name LIKE %{}%'.format(entryvalue)
    elif fieldname == 'Father\'s name' :
        return 'fatherName LIKE \'%{}%\''.format(entryvalue)
    elif fieldname == 'Mother\'s name' :
        return 'motherName LIKE \'%{}%\''.format(entryvalue)
    elif fieldname== 'Class':
        return 'cls={}'.format(entryvalue)
    elif fieldname == 'Phone Number':
        return 'phoneNo LIKE \'%{}%\''.format(entryvalue)
    elif fieldname == 'Gender' :
        return 'gender = {}'.format(entryvalue)
    elif fieldname == 'Age' :
        return 'age = {}'.format(entryvalue)
    elif fieldname == 'Date of Birth' :
        return 'dob LIKE \'%{}%\''.format(entryvalue)
    elif fieldname == 'Address' :
        return 'address LIKE \'%{}%\''.format(entryvalue)
    elif fieldname == 'House' :
        return 'house LIKE \'%{}%\''.format(entryvalue)
    elif fieldname == 'Admission Year' :
        return 'adYear={}'.format(entryvalue)
    elif fieldname == 'Passout Year' :
        return 'passoutYear = {}'.format(entryvalue)




#settablenameformanipulating('students')
#print(queryfromtable('Name', 'Name=\'nametosearch\''))
