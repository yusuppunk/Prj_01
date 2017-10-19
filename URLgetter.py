#coding:utf-8
#简单爬虫，提取网页中的所有URL
#by ：YusupExmet
import urllib2
from bs4 import BeautifulSoup
import re
url = 'http://47.95.230.75'
response = urllib2.urlopen(url)
bbs = BeautifulSoup(response.read()).findAll('a') #bbs变量里面都是a标签，列表型
#href="http://47.95.230.75/"
pat = re.compile(r'href="([^"]*)"')   #这个正则式用来搞a标签的
pat2 = re.compile(r'http')
for item in bbs:    #列表的每一项都得单独招待
    h = pat.search(str(item))
    href = h.group(1)
    if pat2.search(href):
        ans = href
    else:
        ans = url+href
    print ans
