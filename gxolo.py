import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import time
import random
import urllib3
import datetime
import os
today=datetime.date.today()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user_agent = {'User-agent':'Mozilla/5.0'}
base_url = 'https://www.gsmarena.com/makers.php3'
ur='https://www.gsmarena.com/'
country = 'INDIA'
company = 'XOLO'
model_list = []
usp = []
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []
records = []
href = []
st_list_heads=[]
st_list_dets=[]
hr=[]
spec_url=[]
HREF=[]
BRANDS=[]
device_num=[]
price_list=[]
launch_date_list=[]
company_name_list=[]
devnum=[]
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'st-text'})
URL=''
PAGES=[]
for a in range(len(results)):
    sa=results[a].find_all('table')
    #print(len(sa))
    for b in range(len(sa)):
        sb=sa[b].find_all('tr')
        #print(len(sb))
        for c in range(len(sb)):
            sc=sb[c].find_all('td')
            for d in range(len(sc)):
                sd=sc[d].find('a')
                if'xolo' in sd.text.lower():
                    URL=sc[d].find('a')['href']
URL=ur+URL                
#print(URL)
R=requests.get(URL)
soup=BeautifulSoup(R.text,'html5lib')
results1=soup.find('div',attrs={'class':'nav-pages'})
PAGES.append(URL)
#print(results1)
if (results1) is not None:    
    sa=results1.find_all('a')
    for a in range(len(sa)):
        PAGES.append(ur+ sa[a]['href'])
for i in range(len(PAGES)):
    PAGES[i]=ur+PAGES[i]
    print(PAGES[i])
for a in range(len(PAGES)):
    r=requests.get(PAGES[a])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'makers'})
    for b in range(len(results)):
            sb=results[b].find_all('ul')
            for c in range(len(sb)):
                sc=sb[c].find_all('li')
                for d in range(len(sc)):
                    href.append(sc[d].find('a')['href'])
                    usp.append(sc[d].find('img')['title'])
                    model_list.append(sc[d].find('strong').text.strip())
print('href:-',end='')
print(len(href))
print('USP:-',end='')
print(len(usp))
print('model list:-',end='')
print(len(model_list))
for i in range(len(href)):
    href[i]=ur+href[i]
    c1=''
    d1=''
    r=requests.get(href[i])
    soup = BeautifulSoup(r.text,'html5lib')
    results=soup.find_all('div',attrs={'id':'specs-list'})
    for a in range(len(results)):
        sa=results[a].find_all('table',attrs={'cellspacing':'0'})
        for b in range(len(sa)):
            sb=sa[b].find_all('tbody')
            for c in range(len(sb)):
                sc=sb[c].find('th').text

                if 'body' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'dimension' in se[e].text.lower():
                                thickness_list.append(sf[e].text)

                if 'platform' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'cpu' in se[e].text.lower():
                                processor_list.append(sf[e].text)

                if 'memory' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'internal' in se[e].text.lower():
                                memory_list.append(sf[e].text)

                if 'camera' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'primary' in se[e].text.lower() or 'secondary' in se[e].text.lower():
                                c1=c1+se[e].text+':- '+sf[e].text+' || '
                
                if 'display' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'type' in se[e].text.lower() or 'size' in se[e].text.lower():
                                d1=d1+se[e].text+':- '+sf[e].text+' || '

                if 'battery' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'mah' in sf[e].text.lower():
                                battery_list.append(sf[e].text)

                if 'launch' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'announce' in se[e].text.lower():
                                launch_date_list.append(sf[e].text.strip())

                if 'misc' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'price' in se[e].text.lower():
                                price_list.append(sf[e].text.strip())

                

    if d1!='':
        display_list.append(d1)
    if c1!='':
        camera_list.append(c1)
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(price_list)==i:
        price_list.append('Not Available')
    if len(usp)==i:
        usp.append('Not Available')
    if len(launch_date_list)==i:
        launch_date_list.append('Not Available')
##    if var==500:
##        break

print('DISPLAY LIST:- ')
print(len(display_list))
##for i in display_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            
print('PROCESSOR LIST:- ')
print(len(processor_list))
##for i in processor_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('MEMORY LIST:- ')
print(len(memory_list))
##for i in memory_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('CAMERA LIST:- ')
print(len(camera_list))
##for i in camera_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('BATTERY LIST:- ')
print(len(battery_list))
##for i in battery_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('THICKNESS LIST:-')
print(len(thickness_list))
##for i in thickness_list:
##    print(i)    
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('PRICE LIST:_')
print(len(price_list))
##for i in price_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LAUNCH DATE:-')
print(len(launch_date_list))
##for i in launch_date_list:
##    print(i)    

extras_links = href

    
for i in range(len(model_list)):
    records.append((country,company,model_list[i],price_list[i],launch_date_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))


path='C:\\LavaWebScraper\\GSMARENA\\'
df = pd.DataFrame(records, columns = ['COUNTRY','COMPANY', 'MODEL', 'PRICE','LAUNCH DATE', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,'gsmXOLO'+str(today)+'.csv'), index=False, encoding='utf-8')


                       

                
                

                

    
