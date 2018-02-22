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
base_url = 'http://agmmobile.com/en/products'
ur='http://agmmobile.com/en/'
country = 'China'
company = 'AGM'
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
results=soup.find_all('div',attrs={'class':'box-bd'})
for i in range(len(results)):
    sa=results[i].find_all('h2')
    for a in range(len(sa)):
        if sa[a].text =='Accessories':
            b=a
for c in range(len(results)):
    sb=results[c].find_all('ul',attrs={'class':'row'})
    sb.pop(b)
    for a in range(len(sb)):
        sc=sb[a].find_all('li')
        for b in range(len(sc)):
            href.append(sc[b].find('a')['href'])
            model_list.append(sc[b].find('h3').text)


for i in range(len(href)):
    href[i]=ur + href[i]
HREF=href
for i in range(len(href)):
    u=''
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'text'})
    for a in range(len(results)):
        sa=results[a].find_all('h2')
        for b in range(len(sa)):
            u=u+sa[b].text.strip().replace('<br>',' ').replace('\n',' ').replace('“','"').replace('”','"').replace('’’ ','"')+' || '
    usp.append(u)
##for i in usp:
##    print(i)
##print(len(usp))
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'secNav-wrap row'})
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'col-xs-12 col-sm-8 col-1 right'})
        for b in range(len(sa)):
            sb=sa[b].find_all('a')
            for c in range(len(sb)):
                sc=sb[c].text
                if sc =='Specification' or sc =='specification' or sc =='Specifications' or sc =='specifications':
                    spec_url.append(sb[c]['href'])
for i in range(len(href)):
    href[i]=href[i] + spec_url[i]
    #print(href[i])
for i in range(len(href)):
    heads=[]
    dets=[]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'part-2'})
    #print(len(results))
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'item'})
        #print(len(sa))
        for b in range(len(sa)):
            sb=sa[b].find_all('div',attrs={'class':'row item-box'})
            #print(len(sb))
            for c in range(len(sb)):
                sh=sb[c].find_all('div',attrs={'class':'col-xs-12 col-sm-4 left'})
                sd=sb[c].find_all('div',attrs={'class':'col-xs-12 col-sm-8 right'})
                for d in range(len(sh)):
                    heads.append(sh[d].text)
                for e in range(len(sd)):
                    dets.append(sd[e].text)
    st_list_heads.append(heads)
    st_list_dets.append(dets)


for i in range(len(st_list_heads)):    
    for j in range(len(st_list_heads[i])):
        if 'dimension' in st_list_heads[i][j].lower():
            #thickness_list.append(st_list_dets[i][j])
            s=st_list_dets[i][j]
            match=re.search(r'\s*\d+\.*\d*\s*mm', s)
            if not match:
                match=re.search(r'\d+\.*\d*\smm', s)
            if match:
                #print(match.group())
                thickness_list.append(match.group())
            else:
                #print('NA')
                thickness_list.append('Not Available')
            
        if 'platform' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
            
        if 'built-in memory' in st_list_heads[i][j].lower() :
            memory_list.append(st_list_dets[i][j])
            
        if 'battery' in st_list_heads[i][j].lower():
            battery_list.append(st_list_dets[i][j])
                        
        if 'physical size' in st_list_heads[i][j].lower():
             display_list.append(st_list_dets[i][j])

        if 'camera' in st_list_heads[i][j].lower():
            camera_list.append(st_list_dets[i][j].replace('\n',' || ').replace('<br>',' ').replace('\r',' '))

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
    if len(usp)==i:
        usp.append('Not Available')         
##    if 'Dimension' not in st_list_heads[i] and 'dimension' not in st_list_heads[i][j] and 'Dimensions' not in st_list_heads[i][j] and 'dimensions' not in st_list_heads[i][j]:
##        thickness_list.append('NA')
##        
##        
##    if 'Platform' not in st_list_heads[i] and 'platform' not in st_list_heads[i][j]:
##        processor_list.append('NA')
##        
##    if 'Built-in Memory' not in st_list_heads[i]:
##        memory_list.append('NA')
##        
##    if 'Battery' not in st_list_heads[i] and 'battery' not in st_list_heads[i]:
##        battery_list.append('NA')
##        
##    if 'Physical Size' not in st_list_heads[i]:
##        display_list.append('NA')
##        
##    if 'Cameras' not in st_list_heads[i] and 'cameras' not in st_list_heads[i] and 'Camera' not in st_list_heads[i] and 'camera' not in st_list_heads[i]:
##        camera_list.append('NA')
print(len(model_list))
print(len(usp))
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(battery_list))
print(len(display_list))
print(len(camera_list))
print(camera_list)
#print(usp)
extras_links = HREF
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'agm-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')

