from tkinter import *

def resulttextboxui(resultlist):
    root=Tk()
    root.geometry('1200x450')
    root.title('Query Results')

    scrollbar=Scrollbar(root)
    textboxheight=len(resultlist)

    resulttext=Text(root, yscrollcommand=scrollbar.set, width=200, height=textboxheight)
    resulttext.pack()
    for record in resultlist:
        resulttext.insert(INSERT, str(record)+'\n')


    root.mainloop()

def displayresult(result):
    fhandle=open('result.txt','a+')
    for x in range(len(result)):
        outresult=str(result[x])+'\n'
        fhandle.write(outresult)
    fhandle.close()
