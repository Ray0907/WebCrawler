#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup

name=input('請輸入要爬的ptt版名稱:')
url='https://www.ptt.cc/bbs/%s/index.html' %name
num_page = int(input("請問您想擷取幾頁？"))
count=1

while(num_page > 0):
    print("******************第%d頁******************" %count)
    c_url = url
    res = requests.get(url, cookies={'over18': '1'})
    html = res.text
    soup = BeautifulSoup(html,"lxml")
    page=soup.select('div.btn-group-paging a')
    articles=soup.select('div.title a')
    for article in articles:
        print(article.text,'https://www.ptt.cc/'+article['href'])
    print("---------------------------------")
    next_page='https://www.ptt.cc/'+page[1]['href']
    url=next_page
    count=count+1
    num_page = num_page-1


