# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os
from tkinter import *
from tkinter import ttk

 
#从html中解析标题
def ParshTitle(html):
	startPos = html.find(b'<title>')
	endpos = html.find(b'</title>')	
	strTmp = html[startPos+29:endpos]
	strTmp = strTmp.replace(b'</font>', b'')
	return strTmp

#从html中解析CPI数据
def ParshCPI(html):
	startPos = html.find(b'<div class="list">')
	endpos = html.find(b'</div>')
	
	strTmp = html[startPos:endpos]
	return  b"<table>"+ strTmp + b"</table>"#convert bytes to str failed implicitly


def GetHtmlData(url, index, keyWord):
                wp = urllib.request.urlopen(url)#打开连接
                content = wp.read()	#获取页面内容
                content = content.replace(b'\r\n',b'')
                flag  = content.find(keyWord)
                if flag == -1:
                        print("not found!")
                else:
                        title = ParshTitle(content)
                        content = ParshCPI(content)
                        fl = title + str.encode(index)  # title is bytes index is str
                        ##将文件路径转为gb18030编码
                        fl = str(fl,'gb18030')
                        f = open(fl, 'w')
                        f.write(str(content))
                        f.close()


def searchMain():
	#首先找到www.ssshot.com的首页
	num_list = range(3)        #生成0～143的数字
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
		#keyWord = str.encode('川瀬さやか','gb18030')
		#keyWord = str.encode('浅倉彩音','gb18030')
		#keyWord = str.encode('北条美里','gb18030')
		#keyWord = str.encode('夢野まりあ','gb18030')
		#keyWord = str.encode('愛乃ゆな','gb18030')
		#keyWord = str.encode('宇佐美奈々','gb18030')
		#keyWord = str.encode('内田美奈子','gb18030')
		#keyWord = str.encode('高橋美緒','gb18030')
		#keyWord = str.encode('松浦','gb18030')
		#keyWord = str.encode('加藤英子','gb18030')
		#keyWord = str.encode('暮町ゆうこ','gb18030')
		#keyWord = str.encode('伊織涼子','gb18030')
		#keyWord = str.encode('蜜井とわ','gb18030')
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
button = Button(win, text='查找',relief='groove',bg='yellow', fg='red',command=searchMain)
#button = Button(win, text='查找', command=printOut)
button.pack()
button.configure(width=10,height=2)
var=StringVar()
#Label(win,text='查找关键字', bg='green',fg='red').pack(fill = X,expand = 0,side = LEFT)
Label(win,text='查找关键字', bg='green',fg='red').grid(column=3, row=1, sticky=W)
entry = ttk.Entry(mainframe,width=7,textvariable = var)
entry.grid(column=2, row=1, sticky=(W, E))
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#Label(win,text='查找结束位置', bg='green',fg='red').pack(expand = 1,side = LEFT)
for child in mainframe.winfo_children(): child.grid_configure(padx=5,  pady=5)
win.mainloop()
