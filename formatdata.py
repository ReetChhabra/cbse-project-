def settablenameformanipulating(name):
    global tablename
    tablename=name

#just pass all the information as named arguments the rest will be handled by the function
#Example: insertrecord(adminNo='984', name='Reet' ,age='12' etc)
#only pass data as a string even if it is an integer
def insertrecord( name, adminNo , adYear , passoutYear , cls , phoneNo , house , motherName , fatherName , age , dob , gender ):
    restr='INSERT INTO '+tablename+'(adminNo, name, cls, gender, fatherName, motherName, age, dob, house, phoneNo, adYear, passoutYear)'+" VALUES ({} ,'{}', {}, '{}', '{}', '{}', {}, '{}', '{}', {}, {}, '{}');".format(adminNo, name, cls, gender, fatherName, motherName, age, dob, house, phoneNo, adYear, passoutYear)
    return restr

#just pass what to select and a condition as named arguments
def queryfromtable(select, condition):
    restr='SELECT {} '.format(select)+'FROM {} '.format(tablename)+'WHERE {}'.format(condition)+';'
    return restr
