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
import os
import datetime


###############################################################
path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'
###############################################################

base_url = 'http://www.blackview.hk/smartphone/'
ur='http://www.blackview.hk'
country = 'Not Available'
company = 'BLACKVIEW'
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
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'productslist'})
for i in range(len(results)):
    sa=results[i].find_all('ul')
    for b in range(len(sa)):
        sb=sa[b].find_all('li')
        for c in range(len(sb)):
            sc=sb[c].find_all('span',attrs={'class':'border'})
            for d in range(len(sc)):
                href.append(sc[d].find('a')['href'])
                model_list.append(sc[d].find('a')['title'].replace('（','(').replace('）',')'))
for i in range(len(href)):
    if ur not in href[i]:
        href[i]=ur+href[i]
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'id':'parameters'})
    for a in range(len(results)):
        sa=results[a].find_all('ul')
        for b in range(len(sa)):
            sb=sa[b].find_all('li',attrs={'class':'row'})
            for c in range(len(sb)):
                sc=sb[c].find_all('div',attrs={'class':'label'})
                for d in range(len(sc)):
                    try:
                        if 'dimension' in sc[d].text.lower():
                            sd=sb[c].find_all('tbody')
                            for e in range(len(sd)):
                                se=sd[e].find_all('td',attrs={'valign':'top'})
                                for f in range(len(se)):
                                    thickness_list.append(se[f].text.strip().replace('\r','').replace('\t','').replace('\n',''))
                        if 'cpu' in sc[d].text.lower():
                            sd=sb[c].find_all('div',attrs={'class':'value'})
                            for e in range(len(sd)):
                                processor_list.append(sd[e].text.strip().replace('\r','').replace('\t','').replace('\n','').replace(' – ','-'))
                        if 'memory' in sc[d].text.lower():
                            sd=sb[c].find_all('div',attrs={'class':'value'})
                            for e in range(len(sd)):
                                memory_list.append(sd[e].text.strip().replace('\r','').replace('\t','').replace('\n',''))
                        if 'display' in sc[d].text.lower():
                            sd=sb[c].find_all('div',attrs={'class':'value'})
                            for e in range(len(sd)):
                                display_list.append(sd[e].text.strip().replace('\r','').replace('\t','').replace('\n','').replace('”','inch'))
                        if 'camera' in sc[d].text.lower():
                            sd=sb[c].find_all('div',attrs={'class':'value'})
                            for e in range(len(sd)):
                                camera_list.append(sd[e].text.strip().replace('\r','').replace('\t','').replace('\n',' || ').replace('<br>',' || '))
                        if 'battery' in sc[d].text.lower():
                            sd=sb[c].find_all('div',attrs={'class':'value'})
                            for e in range(len(sd)):
                                sd=sb[c].find_all('tbody')
                                for e in range(len(sd)):
                                    se=sd[e].find_all('td',attrs={'colspan':'2'})
                                    battery_list.append(se[0].text.strip().replace('\r','').replace('\t','').replace('\n',''))
                                
                        
                    except:
                        pass
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(usp)==i:
        usp.append('Not Available')
        
                                                         
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(display_list))
print(len(camera_list))
print(len(battery_list))
print(len(usp))

extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today()) +'-blackview'+'.csv'), index=False, encoding='utf-8')
   
      
                    

   
