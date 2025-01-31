from tkinter import *
import variables as var
import main
import sqlfunctions as sql


main.intialize()

def setdata():
    print(adminentry.get())
    var.adminno=adminentry.get()
    var.name=nameentry.get()
    var.cls=_cls.get()
    var.gender=_gender.get()
    var.fathername=fathernameentry.get()
    var.mothername=mothernameentry.get()
    var.address=addressentry.get()
    var.age=ageentry.get()
    var.dob=dobentry.get()
    var.house=houseentry.get()
    var.phoneno=phonenoentry.get()
    var.adyear=adyearentry.get()
    var.passoutyear=passoutyearentry.get()
    main.enterdata()
    clearvalues()


def clearvalues():
    phonenoentry.delete(0,'end')
    adminentry.delete(0,'end')
    nameentry.delete(0,'end')
    _cls.set('')
    _gender.set('')
    fathernameentry.delete(0,'end')
    mothernameentry.delete(0,'end')
    addressentry.delete(0,'end')
    ageentry.delete(0,'end')
    dobentry.delete(0,'end')
    houseentry.delete(0,'end')
    adyearentry.delete(0,'end')
    passoutyearentry.delete(0,'end')

root=Tk()

_adminno=StringVar()
_name=StringVar()
_cls=StringVar()
_gender=StringVar()
_fathername=StringVar()
_mothername=StringVar()
_age=StringVar()
_dob=StringVar()
_house=StringVar()
_phoneno=StringVar()
_adyear=StringVar()
_passoutyear=StringVar()
_address=StringVar()


root.geometry('700x600')
root.title("SCHOOL MANAGEMENT")

label_0=Label(root,text="STUDENT RECORD",width=20,font=("bold",20))
label_0.place(x=200,y=53)

label_1=Label(root,text="ADMISSION NO.",width=20,font=("bold",12))
label_1.place(x=5,y=130)

adminentry=Entry(root,textvariable='_adminno')
adminentry.place(x=172,y=130)

label_2=Label(root,text="NAME",width=20,font=("bold",12))
label_2.place(x=280,y=130)

nameentry=Entry(root)
nameentry.place(x=490,y=130)

label_3=Label(root,text="FATHER'S NAME",width=20,font=("bold",12))
label_3.place(x=7,y=180)

fathernameentry=Entry(root)
fathernameentry.place(x=170,y=180)

label_4=Label(root,text="MOTHER'S NAME",width=20,font=("bold",12))
label_4.place(x=322,y=180)

mothernameentry=Entry(root)
mothernameentry.place(x=490,y=180)

label_5=Label(root,text="DATE OF BIRTH",width=20,font=("bold",12))
label_5.place(x=4,y=230)

dobentry=Entry(root, textvariable=_dob)
dobentry.place(x=170,y=230)

label_6=Label(root,text="AGE",width=20,font=("bold",12))
label_6.place(x=275,y=230)

ageentry=Entry(root, textvariable=_age)
ageentry.place(x=490,y=230)

label_7=Label(root,text="ADDRESS",width=20,font=("bold",12))
label_7.place(x=3,y=280)

addressentry=Entry(root, textvariable=_address)
addressentry.place(x=170,y=280)

label_8=Label(root,text="PHONE NO.",width=20,font=("bold",12))
label_8.place(x=300,y=280)

phonenoentry=Entry(root, textvariable=_phoneno)
phonenoentry.place(x=490,y=280)

label_9=Label(root,text="GENDER",width=20,font=("bold",12))
label_9.place(x=5,y=330)

genderlist=['M','F']
genderentry=OptionMenu(root, _gender, *genderlist)
genderentry.config(width=15)
genderentry.place(x=165,y=330)

label_10=Label(root,text="CLASS",width=20,font=("bold",12))
label_10.place(x=285,y=330)

classlist=['1','2','3','4','5','6','7','8','9','10','11','12']
c=StringVar()
droplist=OptionMenu(root,_cls,*classlist)
droplist.config(width=15)
droplist.place(x=485,y=330)

label_11=Label(root,text="ADMIN YEAR",width=20,font=("bold",12))
label_11.place(x=5,y=380)

adyearentry=Entry(root, textvariable=_adyear)
adyearentry.place(x=170,y=380)

label_12=Label(root,text="HOUSE",width=20,font=("bold",12))
label_12.place(x=285,y=380)

houseentry=Entry(root, textvariable=_house)
houseentry.place(x=490,y=380)

label_13=Label(root,text="PASS OUT YEAR",width=20,font=("bold",12))
label_13.place(x=5,y=430)

passoutyearentry=Entry(root, textvariable=_passoutyear)
passoutyearentry.place(x=170,y=430)

addrecordbutton=Button(root, command=setdata, text='Add Record')
addrecordbutton.place(x=315,y=460)

root.mainloop()
