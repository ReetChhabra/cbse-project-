from tkinter import *
import variables as var
import main

def query():
    var.where=queryentry.get()
    var.fieldname=_fieldname.get()
    print(_fieldname.get(),queryentry.get())
    main.test()

root= Tk()
root.geometry('400x600')
root.title('Query DB')

_fieldname=StringVar()
_where=StringVar()

fieldlist=['Admission Number','Name','Father\'s name','Mother\'s name','Phone Number',
'Class','Gender','Age','Date of Birth','Address','House','Admission Year','Passout Year']

fieldnamedroplist=OptionMenu(root, _fieldname, *fieldlist)
fieldnamedroplist.config(width=20)
fieldnamedroplist.pack()

queryentry=Entry(root, textvariable=_where)
queryentry.pack()

querybutton=Button(root, command=query, text='Query')
querybutton.pack()

root.mainloop()
