#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
from bs4 import BeautifulSoup


path='/Users/jeff/Desktop/chromedriver'

web=webdriver.Chrome(path)
name=input('請輸入要爬的ptt版名稱:')
url='https://www.ptt.cc/bbs/%s/index.html' %name
web.get(url)

num_page = int(input("請問您想擷取幾頁？"))
count=1

while(num_page > 0):
    print("******************第%d頁******************" %count)
    c_url = web.current_url #使用webdriver的current_url方法取得當前的網址
    web.get(c_url) #瀏覽器轉跳至當前的網址
    html = web.page_source
    soup = BeautifulSoup(html,"lxml") #讀進soup中
    articles=soup.select('div.title a')

    for article in articles:
        print(article.text,'https://www.ptt.cc/'+article['href'])
    print("---------------------------------")
    count=count+1
    num_page = num_page-1
    web.find_element_by_link_text("‹ 上頁").click() #按頁面上的"‹ 上頁"link


web.close() #關閉瀏覽器

