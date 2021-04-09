# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os

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

	
#提取各地区数据
'''
def GetHtmlData(url, index):
                #print(url)
                wp = urllib.request.urlopen(url)#打开连接
                content = wp.read()	#获取页面内容
                #print(content)
                content = content.replace(b'\r\n',b'')
                title = ParshTitle(content)
                content = ParshCPI(content)
                fl = title + str.encode(index)  # title is bytes index is str
                ##将文件路径转为gb18030编码
                fl = str(fl,'gb18030')
                f = open(fl, 'w')
                f.write(str(content))
                f.close()
'''

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



if __name__ =="__main__":
	#首先找到www.ssshot.com的首页
	num_list = range(329)        #生成0～143的数字
	#http://ys.755bb.com/vodlist/15_1.htm
	strUrl="http://ys.18zzzz.com/vodlist/1_"
	for i in num_list:
		if i==0 or i==1:
			continue
		index = str(i)
		strTemp = strUrl + index + ".htm"
		#target = os.system(sys.argv[1])
		#target = '川瀬さやか'
		#keyWord = str.encode(target,'gb18030')
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
		#keyWord = str.encode('松すみれ','gb18030')
		#keyWord = str.encode('芳野京子','gb18030')
		#keyWord = str.encode('朝倉','gb18030')
		#keyWord = str.encode('沢田美奈子','gb18030')
		#keyWord = str.encode('恵けい','gb18030')
		#keyWord = str.encode('青山葵','gb18030')
		#keyWord = str.encode('朝倉','gb18030')
		keyWord = str.encode('伊織涼子','gb18030')
		#keyWord = str.encode('蜜井とわ','gb18030')
		#keyWord = str.encode('鮎川','gb18030')
		#keyWord = str.encode('持田美琴','gb18030')
		#keyWord = str.encode('青山ナナ ','gb18030')
		#keyWord = str.encode('松下美雪','gb18030')
		#keyWord = str.encode('八重いろは','gb18030')
		#keyWord = str.encode('佐伯れい ','gb18030')
		#keyWord = str.encode('吉野艶子 ','gb18030')
		#keyWord = str.encode('藤田樹里奈 ','gb18030')
		#keyWord = str.encode('川嶋成美 ','gb18030')
		#keyWord = str.encode('井川翔子 ','gb18030')
		#keyWord = str.encode('人妻百景 ','gb18030')
		#keyWord = str.encode('変態宣言 ','gb18030')
		#keyWord = str.encode('橘エレナ ','gb18030')
		#keyWord = str.encode('中山穂香 ','gb18030')
		#keyWord = str.encode('速水怜 ','gb18030')
		#keyWord = str.encode('樹本つばさ ','gb18030')
		#keyWord = str.encode('HYK-017 ','gb18030')
		#keyWord = str.encode('HYK-027 ','gb18030')
		GetHtmlData(strTemp, index, keyWord)
	
