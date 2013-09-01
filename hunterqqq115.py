# -*- coding:gb18030 -*-
import sys
import urllib.request
import re
import os

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

	
#��ȡ����������
'''
def GetHtmlData(url, index):
                #print(url)
                wp = urllib.request.urlopen(url)#������
                content = wp.read()	#��ȡҳ������
                #print(content)
                content = content.replace(b'\r\n',b'')
                title = ParshTitle(content)
                content = ParshCPI(content)
                fl = title + str.encode(index)  # title is bytes index is str
                ##���ļ�·��תΪgb18030����
                fl = str(fl,'gb18030')
                f = open(fl, 'w')
                f.write(str(content))
                f.close()
'''

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
		#target = '�������䤫'
		#keyWord = str.encode(target,'gb18030')
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
		#keyWord = str.encode('�ɤ��ߤ�','gb18030')
		#keyWord = str.encode('��Ұ����','gb18030')
		#keyWord = str.encode('���}','gb18030')
		#keyWord = str.encode('�g��������','gb18030')
		#keyWord = str.encode('�{����','gb18030')
		#keyWord = str.encode('��ɽ��','gb18030')
		#keyWord = str.encode('���}','gb18030')
		#keyWord = str.encode('��������','gb18030')
		#keyWord = str.encode('�۾��Ȥ�','gb18030')
		#keyWord = str.encode('������','gb18030')
		#keyWord = str.encode('�F�u�椫��','gb18030')
		#keyWord = str.encode('���Fһ��','gb18030')
		#keyWord = str.encode('���x���Ť�','gb18030')
		#keyWord = str.encode('���Τᤰ�� ','gb18030')
		#keyWord = str.encode('��ԭ����','gb18030')
		#keyWord = str.encode('ʯ��������','gb18030')
		#keyWord = str.encode('ʯԭ����','gb18030')
		#keyWord = str.encode('ʯ�\����','gb18030')
		#keyWord = str.encode('���g���ߤ�','gb18030')
		#keyWord = str.encode('�ټ�����','gb18030')
		#keyWord = str.encode('�����餤�~��','gb18030')
		#keyWord = str.encode('�ّc��','gb18030')
		#keyWord = str.encode('�������','gb18030')
		#keyWord = str.encode('�m����','gb18030')
		keyWord = str.encode('����','gb18030')
		#keyWord = str.encode('�оӤ��Ϥ� ','gb18030')
		#keyWord = str.encode('С���ޤ�','gb18030')
		#keyWord = str.encode('�Сҹ��','gb18030')
		#keyWord = str.encode('����ͫ','gb18030')
		#keyWord = str.encode('�Rɭ��','gb18030')
		#keyWord = str.encode('�ߘ�����','gb18030')
		#keyWord = str.encode('�g����Ү','gb18030')
		#keyWord = str.encode('ǰ�ϣ','gb18030')
		#keyWord = str.encode('��Ұ����','gb18030')
		#keyWord = str.encode('������','gb18030')
		#keyWord = str.encode('�����桩��','gb18030')
		#keyWord = str.encode('�瞁����','gb18030')
		#keyWord = str.encode('�Сҹ��','gb18030')
		#keyWord = str.encode('�Сҹ��','gb18030')
		
		GetHtmlData(strTemp, index, keyWord)
	
