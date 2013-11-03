# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os
from tkinter import *
from tkinter import ttk

 
# search the file from the indicated path
# it will retrun the set which include the all files contained in that path 
def searchFile(Path):
    p = str(Path)
    if p == "":
    	return []
    os.chdir(p)
    a = os.listdir(p)
    print (a)




win =Tk()
win.title('HunterXGUI')
#win.geometry('200x160')
mainframe=ttk.Frame(win,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)



button = Button(win, text='list file',relief='groove',bg='yellow', fg='red',command=searchFile)
button.pack()
button.configure(width=10,height=2)
var=StringVar()
Label(win,text='search key word', bg='green',fg='red').grid(column=3, row=1, sticky=W)
entry = ttk.Entry(mainframe,width=7,textvariable = var)
entry.grid(column=2, row=1, sticky=(W, E))
for child in mainframe.winfo_children(): child.grid_configure(padx=5,  pady=5)
win.mainloop()
