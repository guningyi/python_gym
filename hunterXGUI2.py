# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os
from tkinter import *
from tkinter import ttk

 
#��html�н�������
def ParshTitle(html):
	startPos = html.find(b'<title>')
	endpos = html.find(b'</title>')	
	strTmp = html[startPos+29:endpos]
	strTmp = strTmp.replace(b'</font>', b'')
	return strTmp

#��html�н���CPI����
def ParshCPI(html):
	startPos = html.find(b'<div class="list">')
	endpos = html.find(b'</div>')
	
	strTmp = html[startPos:endpos]
	return  b"<table>"+ strTmp + b"</table>"#convert bytes to str failed implicitly


def GetHtmlData(url, index, keyWord):
                wp = urllib.request.urlopen(url)#������
                content = wp.read()	#��ȡҳ������
                content = content.replace(b'\r\n',b'')
                flag  = content.find(keyWord)
                if flag == -1:
                        print("not found!")
                else:
                        title = ParshTitle(content)
                        content = ParshCPI(content)
                        fl = title + str.encode(index)  # title is bytes index is str
                        ##���ļ�·��תΪgb18030����
                        fl = str(fl,'gb18030')
                        f = open(fl, 'w')
                        f.write(str(content))
                        f.close()


def searchMain():
	#�����ҵ�www.ssshot.com����ҳ
	num_list = range(3)        #����0��143������
	strUrl="http://www.ssshot.com/yazhoushipin/page_"
	for i in num_list:
		if i==0 or i==1:
			continue
		index = str(i)
		strTemp = strUrl + index + ".html"
		#target = os.system(sys.argv[1])
		target = var.get()
		print(target)
		keyWord = str.encode(target,'gb18030')
		#keyWord = str.encode('�������䤫','gb18030')
		#keyWord = str.encode('ǳ�}����','gb18030')
		#keyWord = str.encode('��������','gb18030')
		#keyWord = str.encode('��Ұ�ޤꤢ','gb18030')
		#keyWord = str.encode('���ˤ��','gb18030')
		#keyWord = str.encode('�������Ρ�','gb18030')
		#keyWord = str.encode('����������','gb18030')
		#keyWord = str.encode('�ߘ����w','gb18030')
		#keyWord = str.encode('����','gb18030')
		#keyWord = str.encode('����Ӣ��','gb18030')
		#keyWord = str.encode('ĺ椦��','gb18030')
		#keyWord = str.encode('��������','gb18030')
		#keyWord = str.encode('�۾��Ȥ�','gb18030')
		GetHtmlData(strTemp, index, keyWord)

def printOut():
        print('hello world')

#if __name__ =="__main__":

win =Tk()
win.title('HunterXGUI')
#win.geometry('200x160')
mainframe=ttk.Frame(win,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)


#entry.pack(width=30,height=5)
button = Button(win, text='����',relief='groove',bg='yellow', fg='red',command=searchMain)
#button = Button(win, text='����', command=printOut)
button.pack()
button.configure(width=10,height=2)
var=StringVar()
#Label(win,text='���ҹؼ���', bg='green',fg='red').pack(fill = X,expand = 0,side = LEFT)
Label(win,text='���ҹؼ���', bg='green',fg='red').grid(column=3, row=1, sticky=W)
entry = ttk.Entry(mainframe,width=7,textvariable = var)
entry.grid(column=2, row=1, sticky=(W, E))
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#Label(win,text='���ҽ���λ��', bg='green',fg='red').pack(expand = 1,side = LEFT)
for child in mainframe.winfo_children(): child.grid_configure(padx=5,  pady=5)
win.mainloop()
