import requests
from urllib.parse import urlencode
import json
import  pandas as pd

data={
    'lang':'tw',
    'act':'aqi-epa',
    
}
url='https://taqm.epa.gov.tw/taqm/aqs.ashx?lang='+urlencode(data)

res=requests.get(url)

html=res.text
temp=json.loads(html)

result=temp.get('Data')



df=pd.DataFrame(result)
CleanDf=df.drop(['AQIStyle','Address','AreaKey','CityCode',
                 'DataSrc','MainPollutant','MainPollutantKey',
                 'MonobjName','SiteId','SiteKey','lat','lng','THC','x','y'],axis=1)
print(CleanDf)





