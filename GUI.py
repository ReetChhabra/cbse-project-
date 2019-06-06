from tkinter import *
import variables as var
import main

def setdata():
    print(adminentry.get())
    var.adminno=adminentry.get()
    var.name=nameentry.get()
    var.cls=clsentry.get()
    var.gender=genderentry.get()
    var.fathername=fathernameentry.get()
    var.mothername=mothernameentry.get()
    var.age=ageentry.get()
    var.dob=dobentry.get()
    var.house=houseentry.get()
    var.phoneno=phonenoentry.get()
    var.adyear=adyearentry.get()
    var.passoutyear=passoutyearentry.get()
    main.intialize()
    main.enterdata()


root=Tk()
_adminno=IntVar()
_name=StringVar()
_cls=IntVar()
_gender=StringVar()
_fathername=StringVar()
_mothername=StringVar()
_age=IntVar()
_dob=IntVar()
_house=StringVar()
_phoneno=IntVar()
_adYear=StringVar()
_passoutyear=StringVar()


root.geometry('750x800')
root.title("SCHOOL MANAGEMENT")

label_0=Label(root,text="STUDENT RECORD",width=20,font=("bold",20))
label_0.place(x=200,y=53)

label_1=Label(root,text="ADMISSION NO.",width=20,font=("bold",12))
label_1.place(x=80,y=130)

addrecordbutton=Button(root, command=setdata, text='test')
addrecordbutton.pack()

adminentry=Entry(root,textvariable='_adminno')
adminentry.place(x=240,y=130)

label_2=Label(root,text="NAME",width=20,font=("bold",12))
label_2.place(x=68,y=180)

nameentry=Entry(root)
nameentry.place(x=240,y=180)

label_3=Label(root,text="FATHER'S NAME",width=20,font=("bold",12))
label_3.place(x=70,y=230)

fathernameentry=Entry(root)
fathernameentry.place(x=240,y=230)

label_4=Label(root,text="MOTHER'S NAME",width=20,font=("bold",12))
label_4.place(x=70,y=280)

mothernameentry=Entry(root)
mothernameentry.place(x=240,y=280)

label_5=Label(root,text="DATE OF BIRTH",width=20,font=("bold",12))
label_5.place(x=70,y=330)

dodentry=Entry(root)
dodentry.place(x=240,y=330)

label_6=Label(root,text="AGE",width=20,font=("bold",12))
label_6.place(x=70,y=380)

ageentry=Entry(root)
ageentry.place(x=240,y=380)

label_7=Label(root,text="ADDRESS",width=20,font=("bold",12))
label_7.place(x=70,y=430)

addressentry=Entry(root)
addressentry.place(x=240,y=430)

label_8=Label(root,text="PHONE NO.",width=20,font=("bold",12))
label_8.place(x=70,y=480)

phonenoentry=Entry(root)
phonenoentry.place(x=240,y=480)

label_9=Label(root,text="GENDER",width=20,font=("bold",12))
label_9.place(x=70,y=530)
var=IntVar()
Radiobutton(root,text="male",value=1,variable=var).place(x=235,y=530)
Radiobutton(root,text="female",value=2,variable=var).place(x=290,y=530)

label_10=Label(root,text="CLASS",width=20,font=("bold",12))
label_10.place(x=70,y=580)

list1=['1','2','3','4','5','6','7','8','9','10','11','12']
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your class')
droplist.place(x=240,y=580)

label_11=Label(root,text="ADMIN YEAR",width=20,font=("bold",12))
label_11.place(x=70,y=630)

adminyearentry=Entry(root)
adminyearentry.place(x=240,y=630)

label_12=Label(root,text="HOUSE",width=20,font=("bold",12))
label_12.place(x=70,y=680)

houseentry=Entry(root)
houseentry.place(x=240,y=680)

Button(root,text="SUBMIT",width=20,bg='brown',fg='white').place(x=300,y=730)


root.mainloop()
