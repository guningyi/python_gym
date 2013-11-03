# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os
from tkinter import *
from tkinter import ttk
import sqlite3
import string
import tkinter as tk


class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
    self.createWidgets()
  def createWidgets(self): 
    top = self.winfo_toplevel()
    top.rowconfigure(0, weight = 1)
    top.columnconfigure(0,weight = 1)
    self.rowconfigure(0, weight = 1)
    self.columnconfigure(0, weight = 1)  
    self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton.grid(row = 0, column = 0, sticky=tk.N+tk.S+tk.E+tk.W)
  # search the file from the indicated path
  # it will retrun the set which include the all files contained in that path 
  def search_file(Path):
      p = str(Path)
      if p == "":
      	return []
      os.chdir(p)
      a = os.listdir(p)
      return a
      #print (a)
  
  def create_content_db():
      conn = sqlite3.connect("d:\\python_project\content.db")
      c = conn.cursor()
      try:
      	c.execute('''create table if not exists info(record blob)''')
      except c.Error:
      	print ("create table failed")
      	return
      conn.commit()
      c.close()
      return
  
  def write_record_to_db(value):
     listValue = list(value)
     listLen = len(listValue)
     print (listLen)
     conn = sqlite3.connect("d:\\python_project\content.db")
     c = conn.cursor()
     for i in range(1, listLen):
          var = listValue.pop()
          c.execute("insert into info values('%s')" % var)
          conn.commit()
     conn.close()
     return
  
  #return the set of the info form db
  def read_record_from_db():
     result = set()
     conn = sqlite3.connect("d:\\python_project\content.db")
     print("start to read content from info table")
     c = conn.cursor()
     c.execute('select * from info ')
     for row in c:
        result.add(row)
     return result
  
  def list_record_from_db():
     conn = sqlite3.connect("d:\\python_project\content.db")
     print("start to read content from info table")
     c = conn.cursor()
     c.execute('select * from info ')
     for row in c:
        print(row)
     return  


#if __name__ =="__main__":
app = Application()
app.master.title('Sample application')
app.mainloop() 

  #b = search_file("D:\\book")
  #result = set()
  #create_content_db()
  #write_record_to_db(b)
  #list_record_from_db()
  #result = read_record_from_db()
  #create_result_page(result)


