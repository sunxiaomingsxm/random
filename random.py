#encoding: utf-8
import os
import sys
import urllib2
sys.path.append(os.path.abspath('.'))

def gethtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

def enclo(row,col,type):
    alllist = []
    if type == 'UP':
        a = col*(row-1)
        b = col*row
        while a >= 0:
            rowline = range(a,b)
            print rowline
            alllist.append(rowline)
            a-=col
            b-=col
    elif type == "DOWN":
        a = 0
        b = col
        while b <= col*row:
            rowline = range(a,b)
            alllist.append(rowline)
            a+=col
            b+=col
    return alllist

if __name__ == '__main__':
	print enclo(3,4,'DOWN')
	#url = "https://www.lagou.com/jobs/list_Python"
	#html = gethtml(url)
	#print html
