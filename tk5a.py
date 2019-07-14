#!/usr/bin/python3

'''
See:
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
https://riptutorial.com/tkinter/example/29714/place--
'''

from tkinter import *
from tkinter.ttk import *

rownum = 0
 
def clicked():
	lbl.configure(text="Button was clicked !!")

window = Tk()
 
window.title("FSGOF")
window.geometry('350x400')
 
lbl = Label(window, text="Fuzzy Set Goodness of Fit")
 
lbl.grid(column=0, row=rownum)
print('R:', rownum)
rownum += 1
 
lblfilla = Label(window, text="")
 
lblfilla.grid(column=0, row=rownum)
print('R:', rownum)
rownum += 1
 
lbl2 = Label(window, text="Enter a File Name")
 
lbl2.grid(column=0, row = rownum )
print('R:', rownum)
rownum += 1

combofn = Combobox(window)
combofn['values']= ( 'IndiaResistdata2006.csv', 'cs2k.csv' )
combofn.current(0) #set the selected item
combofn.grid(column=0, row = rownum )
print('R:', rownum)
rownum += 1

lblfillb = Label(window, text="")
 
lblfillb.grid(column=0, row = rownum)
print('R:', rownum)
rownum += 1

lbl3 = Label(window, text="Enter number of X-Columns")
 
lbl3.grid(column=0, row = rownum )
print('R:', rownum)
rownum += 1
 
combo = Combobox(window)

combo['values']= ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 )

combo.current(4) #set the selected item

combo.grid(column=0, row = rownum )
print('R:', rownum)
rownum += 1

lblfillc = Label(window, text="")
 
lblfillc.grid(column=0, row = rownum)
print('R:', rownum)
rownum += 1

lbl3 = Label(window, text="Choose Y-Column")
 
lbl3.grid(column=0, row = rownum )
print('R:', rownum)
rownum += 1
 
rad1 = Radiobutton(window,text='Y1', value=1)
rad2 = Radiobutton(window,text='Y4', value=2)
rad3 = Radiobutton(window,text='Y3', value=3)
rad4 = Radiobutton(window,text='Y4', value=4)

rad1.grid(column=0, row = rownum )
rownum += 1
rad2.grid(column=0, row = rownum )
rownum += 1
rad3.grid(column=0, row = rownum )
rownum += 1
rad4.grid(column=0, row = rownum )
rownum += 1
print('R:', rownum)

'''
'''

lblfilld = Label(window, text="")
 
lblfilld.grid(column=0, row = rownum)
print('R:', rownum)
rownum += 1

btn = Button(window, text="Run", command=clicked )
 
btn.grid(column=0, row = rownum)

window.mainloop()
