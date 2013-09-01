# -*- coding:gb18030 -*-
from html.parser import HTMLParser
import urllib.parse
import urllib.request
import os
import re
import sys
import json
import sqlite3



def main():
   conn = sqlite3.connect("d:\\python_project\sqliteTest1.db")
   c = conn.cursor()
   # Create table
   c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
   # Insert a row of data
   c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
   # Save (commit) the changes
   conn.commit()
   # We can also close the cursor if we are done with it
   c.close()


def read_db():
   conn = sqlite3.connect("d:\\python_project\sqliteTest1.db")
   c = conn.cursor()
   c.execute('select * from stocks order by price')
   for row in c:
      print(row)




if __name__ == '__main__':
    main()
    read_db()



