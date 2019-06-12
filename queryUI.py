from tkinter import *
import variables as var
import main

def query():
    var.resultto=_resultto.get()
    var.where=queryentry.get()
    var.fieldname=_fieldname.get()
    main.query()

root= Tk()
root.geometry('400x600')
root.title('Query DB')


_fieldname=StringVar()
_where=StringVar()
_resultto=StringVar()

label=Label(root, text='Search by field', font=('bold',12))
label.pack()

fieldlist=['Admission Number','Name','Father\'s name','Mother\'s name','Phone Number',
'Class','Gender','Age','Date of Birth','Address','House','Admission Year','Passout Year']

fieldnamedroplist=OptionMenu(root, _fieldname, *fieldlist)
fieldnamedroplist.config(width=20)
fieldnamedroplist.pack()

queryentry=Entry(root, textvariable=_where)
queryentry.pack()

resulttolabel=Label(root, text='Output to:')
resulttolabel.pack()

resultolist=['Text File','Text Box']
resulttodroplist=OptionMenu(root, _resultto, *resultolist)
resulttodroplist.config(width=10)
resulttodroplist.pack()

querybutton=Button(root, command=query, text='Query')
querybutton.pack()

root.mainloop()
