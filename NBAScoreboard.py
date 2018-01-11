#!/usr/bin/python
# coding:utf-8
import requests
import json
print('NBA Scoreboard')
date=input('Please input the date (ex0101):')
url='https://data.nba.net/prod/v2/2018'+date+'/scoreboard.json'
res=requests.get(url)
html=res.text
result=json.loads(html)

for item in result['games']:
    hTeam=item.get('hTeam').get('triCode')
    hTeamScore=item.get('hTeam').get('score')
    vTeam = item.get('vTeam').get('triCode')
    vTeamScore = item.get('vTeam').get('score')
    if hTeamScore > vTeamScore:
        win=hTeam
    else:
        win=vTeam
    print(hTeam+': '+vTeam+' '+hTeamScore+':'+vTeamScore+' '+'%s win!!!' %win+'\n')

