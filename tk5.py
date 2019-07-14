#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *
 
def clicked():
	lbl.configure(text="Button was clicked !!")

window = Tk()
 
window.title("FSGOF")
window.geometry('350x200')
 
lbl = Label(window, text="Fuzzy Set Goodness of Fit")
 
lbl.grid(column=0, row=0)
 
lbl2 = Label(window, text="Enter a File Name")
 
lbl2.grid(column=0, row=1)
 
combo = Combobox(window)

combo['values']= ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 )

combo.current(4) #set the selected item

combo.grid(column=0, row=90)
rad1 = Radiobutton(window,text='Y1', value=1)

rad2 = Radiobutton(window,text='Y4', value=2)

rad3 = Radiobutton(window,text='Y3', value=3)
rad4 = Radiobutton(window,text='Y4', value=4)

rad1.grid(column=0, row=1)

rad2.grid(column=0, row=2)

rad3.grid(column=0, row=3)
rad4.grid(column=0, row=4)

btn = Button(window, text="Run", command=clicked )
 
btn.grid(column=600, row=1100)

window.mainloop()
