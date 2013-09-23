# -*- coding:gb18030 -*-
from html.parser import HTMLParser
import urllib.parse
import urllib.request
import os
import re
import sys
import json
import sqlite3

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)        
        
    def handle_starttag(self, tag, attrs):
        # here we redefine the function that could handle start tag in html file.
        if tag == 'em':
            # judge the attribute of tag <a>
            for name,value in attrs:
                if name == 'class':
                    print(value)


            
def parse_page(strUrl):
    source = urllib.request.urlopen(strUrl).read()
    handler = MyParser()
    handler.feed(str(source))

def package_json(flag, value):
    print(ok)

def add_to_page(json, value):
    print(ok)

def add_list_to_page(value):
    print(ok)

def create_double_ball_db():
    print("create the double ball db!")
    conn = sqlite3.connect("d:\\python_project\double_record.db")
    c = conn.cursor()
    c.execute(''' create table if not exists record1(record blob)''')
    conn.commit()
    c.close()

def write_record_to_ball_db(value):
   conn = sqlite3.connect("d:\\python_project\double_record.db")
   c = conn.cursor()
   c.execute("""insert into record1 values ('value')""")
   conn.commit()
   conn.close()


def read_record_from_ball_db():
   conn = sqlite3.connect("d:\\python_project\double_record.db")
   c = conn.cursor()
   c.execute('select * from record1 ')
   for row in c:
      print(row)
    

def get_serial_number(strUrl):
    print("start to get serial number")
    source = urllib.request.urlopen(strUrl).read()
    start = 0
    List = []
    while True:
        startPos = source.find(str.encode('td align'), start)
        print(startPos)
        if startPos == -1:
            break
        key = source[startPos+10: startPos+16]
        print(key)
        pattern=str.encode('center')
        if key == pattern:
            print("key == pattern")
            serial_number=source[startPos+64:startPos+70]
            print(serial_number)
            return serial_number
        
    
    

def parse_page_find_method(strUrl):
    source = urllib.request.urlopen(strUrl).read()
    start=0
    List=[]
    while True:
        #(strUrl)#debug serial number
        startPos= source.find(str.encode('<em'), start)
        print(startPos)
        if startPos == -1:
            break
        key=source[startPos+4:startPos+9]
        pattern=str.encode('class')
        if key == pattern:
            red_value=source[startPos+15:startPos+17]
            List.append(bytes.decode(red_value))
            start = startPos+18
        else:
            blue_value=source[startPos+4:startPos+6]
            List.append(bytes.decode(blue_value))
            #serial_number= source[(startPos-158-18*6):(startPos-158-18*6+6)]
            #print(serial_number)
            write_record_to_ball_db(List)
            print(List)
            List = []
            start =startPos+6

def main():
    print("start to grab the doubleBall record from zhcw")
    num_list = range(78)
    strStart = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"
    strEnd = ".html"
    for i in num_list:
        if i == 0:
            continue
        index = str(i)
        strUrl = strStart + index + strEnd
        parse_page_find_method(strUrl)



if __name__ == '__main__':
    create_double_ball_db()
    main()
    read_record_from_ball_db()

