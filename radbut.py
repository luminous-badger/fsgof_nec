#!/usr/bin/python

# From: https://www.geeksforgeeks.org/python-gui-tkinter/
# JM Sun  7 Jul 17:40:24 BST 2019

from Tkinter import *
master = Tk() 
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W) 
mainloop() 
