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
        # �������¶����˴���ʼ��ǩ�ĺ���
        if tag == 'a':
            # �жϱ�ǩ<a>������
            for name,value in attrs:
                if name == 'href':
                    print(value)
if __name__ == '__main__':
    string = "http://ys.755bb.com/vodlist/1_1.htm"
    doc = urllib.request.urlopen(string).read()
    my = MyParser()
    # ����Ҫ���������ݣ���html�ġ�
    my.feed(str(doc))
