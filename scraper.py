from bs4 import BeautifulSoup
import requests
import json 

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url,timeout=5)
soup = BeautifulSoup(response.text,"html.parser")

data={}
data['links']=[]

for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i-1]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    data['links'].append(download_url)

with open('data.txt','w') as outfile:
    json.dump(data,outfile,indent=2,sort_keys=True)