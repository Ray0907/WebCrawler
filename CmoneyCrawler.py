#!/usr/bin/python
#coding:utf-8
import requests
from urllib.parse import urlencode
import json
import pandas as pd


data={
	'action':'GetTechnicalData',
	'stockId':1101,
	'time':'d',
	'range':100,
	'cmkey':'IO6lXiCIlYj0t7kPE64/WA==',
}

headers={
    'authority':'www.cmoney.tw',
    'method':'GET',
    'path':'/finance/ashx/MainPage.ashx?action=GetTechnicalData&stockId=1101&time=d&range=100&cmkey=9QPs9jkiRYY%2BNJN1THYr4Q%3D%3D',
    'scheme':'https',
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie':'__auc=0d53e4f6160bc60151a9d6b77b7; _ga=GA1.2.307356922.1514988902; AspSession=ob5kvwjxzqivqhehqor1d33d; __asc=fe66d9b7160cf636dd491d7f219',
    'referer':'https://www.cmoney.tw/finance/technicalanalysis.aspx?s=1101',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}
url='https://www.cmoney.tw/finance/ashx/MainPage.ashx?'+urlencode(data)
res=requests.get(url,headers=headers)
html=res.text
temp=json.loads(html)
result=pd.DataFrame(temp)
print(result)
    
