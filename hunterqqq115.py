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
	num_list = range(35)        
	#http://qqq115.com/html/part/30_31.html
	strUrl="http://qqq115.com/html/part/30_"
	for i in num_list:
		if i==0 or i==1:
			continue
		index = str(i)
		strTemp = strUrl + index + ".html"
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
		#keyWord = str.encode('伊織涼子','gb18030')
		#keyWord = str.encode('蜜井とわ','gb18030')
		#keyWord = str.encode('本真ゆり','gb18030')
		#keyWord = str.encode('霧島ゆかり','gb18030')
		#keyWord = str.encode('朝霧一花','gb18030')
		#keyWord = str.encode('川辺いづみ','gb18030')
		#keyWord = str.encode('有奈めぐみ ','gb18030')
		#keyWord = str.encode('北原夏美','gb18030')
		#keyWord = str.encode('石川しずか','gb18030')
		#keyWord = str.encode('石原谅子','gb18030')
		#keyWord = str.encode('石黒树里','gb18030')
		#keyWord = str.encode('滝沢すみれ','gb18030')
		#keyWord = str.encode('仲间丽奈','gb18030')
		#keyWord = str.encode('さくらい葉菜','gb18030')
		#keyWord = str.encode('橘慶子','gb18030')
		#keyWord = str.encode('持田優美香','gb18030')
		#keyWord = str.encode('宮村恋','gb18030')
		keyWord = str.encode('冴子','gb18030')
		#keyWord = str.encode('中居ちはる ','gb18030')
		#keyWord = str.encode('小川まみ','gb18030')
		#keyWord = str.encode('町村小夜子','gb18030')
		#keyWord = str.encode('立花瞳','gb18030')
		#keyWord = str.encode('稲森琴','gb18030')
		#keyWord = str.encode('高橋真梨','gb18030')
		#keyWord = str.encode('沢村麻耶','gb18030')
		#keyWord = str.encode('前田優希','gb18030')
		#keyWord = str.encode('夢野怜子','gb18030')
		#keyWord = str.encode('杏美月','gb18030')
		#keyWord = str.encode('藤崎梨々花','gb18030')
		#keyWord = str.encode('早瀬和香','gb18030')
		#keyWord = str.encode('町村小夜子','gb18030')
		#keyWord = str.encode('町村小夜子','gb18030')
		
		GetHtmlData(strTemp, index, keyWord)
	
