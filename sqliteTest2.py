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
   c.execute('''create table if not exists ball (date text, record blob)''')
   # Insert a row of data
   c.execute("""insert into ball values ('2013036','[1,2,3,4,5,6,7]')""")
   c.execute("""insert into ball values ('2013035','[1,2,3,4,5,6,8]')""")
   # Save (commit) the changes
   conn.commit()
   # We can also close the cursor if we are done with it
   c.close()


def read_db():
   conn = sqlite3.connect("d:\\python_project\sqliteTest1.db")
   c = conn.cursor()
   c.execute('select * from ball order by date')
   for row in c:
      print(row)

if __name__ == '__main__':
    main()
    read_db()
