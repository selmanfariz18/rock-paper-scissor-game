from tkinter import *
#import tkinter as a
a=Tk()
a.title('Mobile')
a.geometry('400x200')


lbl=Label(a,text='At which point')
lbl.pack()

def printinput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

inputtxt=Text(a,height=1,width=14)
inputtxt.pack()


printbutton=Button(a,text='print',command=printinput)
printbutton.pack()

lbl = Label(a, text = "")
lbl.pack()

a.mainloop()
