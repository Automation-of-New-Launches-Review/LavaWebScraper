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

base_url = 'https://www.catphones.com/en_gb/smartphones.html'
#ur='https://www.nokia.com/en_int/phones/'
country = 'USA'
company = 'CATERPILLAR'
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
results=soup.find_all('ol',attrs={'class':'products list items product-items'})
#print(len(results))
for i in range(len(results)):
    sa=results[i].find_all('li',attrs={'class':'item product product-item'})
    for a in range(len(sa)):
        sb=sa[a].find_all('h3',attrs={'class':'product-item-name'})
        #print(len(sb))
        for b in range(len(sb)):
            href.append(sb[b].find('a')['href'])
            sc=sb[b].find('a').contents[0].strip('\n').strip().replace('®',' ')
            model_list.append(sc)

for i in range(len(href)):
    u=''
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'feature-icon'})
    for a in range(len(results)):
        sa=results[a].find_all('h4',attrs={'class':'feature-text'})
        for b in range(len(sa)):
            u=u+sa[b].text.replace('&nbsp',' ')+' || '
    usp.append(u)
##for i in usp:
##    print(i)
for i in range(len(href)):
    c1=''
    m1=''
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'product-tech-specs'})
    #print(len(results))
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'spectable-wrap'})
        for b in range(len(sa)):
            sb=sa[b].find_all('h4')
            sc=sa[b].find_all('div',attrs={'class':'spectable'})
            for c in range(len(sb)):
                if 'battery' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'capacity' in se[e].text.lower():
                                battery_list.append(sf[e].text.replace('&nbsp',' ').replace('”',' '))
                if 'display' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'type' in se[e].text.lower():
                                display_list.append(sf[e].text.replace('&nbsp',' ').replace('”',' ').replace(' – ',' - ').replace('″ ','"').replace('×','x'))
                if 'size' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'size' in se[e].text.lower():
                                thickness_list.append(sf[e].text.replace('&nbsp',' ').replace('”',' '))
                if 'processor' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'processor type' in se[e].text.lower():
                                processor_list.append(sf[e].text.replace('&nbsp',' ').replace('”',' '))
                if 'camera' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'rear' in se[e].text.lower() or 'front' in se[e].text.lower():
                                c1=c1+se[e].text+':- '+sf[e].text.replace('&nbsp',' ').replace('”',' ')+ ' || '
                if 'memory' in sb[c].text.lower():
                    sd=sc[c].find_all('div',attrs={'class':'specrow'})
                    for d in range(len(sd)):
                        se=sd[d].find_all('div',attrs={'class':'specl'})
                        sf=sd[d].find_all('div',attrs={'class':'specr'})
                        for e in range(len(se)):
                            if 'rom' in se[e].text.lower() or 'ram' in se[e].text.lower():
                                m1=m1+se[e].text+':- '+sf[e].text.replace('&nbsp',' ').replace('”',' ')+ ' || '
    if m1!='':
        memory_list.append(m1)
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
    if len(usp)==i:
        usp.append('Not Available')

    
                    
print(len(battery_list))
print(len(display_list))
print(len(thickness_list))
print(len(processor_list))
print(len(camera_list))
print(len(memory_list))


extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'caterpillar-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
   
      
                    
                       
                        
                    
                                     

