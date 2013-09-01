# -*- coding:gb18030 -*-
from html.parser import HTMLParser
import sys
import urllib.request
import re
import os

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)        
        
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':
                    print(value)
if __name__ == '__main__':
    string = "http://ys.755bb.com/vodlist/1_1.htm"
    doc = urllib.request.urlopen(string).read()
    my = MyParser()
    # 传入要分析的数据，是html的。
    my.feed(str(doc))
