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

base_url = 'http://www.infocusindia.co.in/mobile-phones/'
#ur='https://www.nokia.com/en_int/phones/'
country = 'USA'
company = 'INFOCUS'
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
results=soup.find_all('div',attrs={'class':'row'})
for i in range(len(results)):
    sa=results[i].find_all('div',attrs={'class':'col-md-3 col-sm-6'})
    for a in range(len(sa)):
        sb=sa[a].find_all('h2')
        for b in range(len(sb)):
            href.append(sb[b].find('a')['href'])
            model_list.append(sb[b].text.strip())
        sc=sa[a].find_all('table',attrs={'class':'product-carousel-price'})
        for c in range(len(sc)):
            u=''
            sd=sc[c].find_all('td')
            for d in range(len(sd)):
                se=sd[d].find_all('li')
                for e in range(len(se)):
                    u=u+se[e].text.replace('•',' ').strip()+' || '
            usp.append(u)                  

for i in range(len(href)):
    p1=''
    m1=''
    c1=''
    d1=''
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'col-sm-8 left'})
    #print(len(results))
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'figure'})
        if len(sa)!=0:
            for b in range(len(sa)):
                sb=sa[b].find_all('div',attrs={'class':'heading'})
                for c in range(len(sb)):
                    if 'outward appearance' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if 'dimension' in se[f].text.lower():
                                        thickness_list.append(sf[f].text)

                    if 'processor' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if 'model' in se[f].text.lower() or 'core' in se[f].text.lower():
                                        p1=p1+(se[f].text+':-'+sf[f].text+' || ')

                    if 'display' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if 'dimension' in se[f].text.lower() or 'material' in se[f].text.lower():
                                        d1=d1+(se[f].text+':-'+sf[f].text+' || ')

                    if 'battery' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if 'capacity' in se[f].text.lower():
                                        battery_list.append(sf[f].text)

                    if 'storage' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if ('ram storage' in se[f].text.lower() or 'rom storage' in se[f].text.lower()) and('material' not in se[f].text.lower()):
                                        m1=m1+(se[f].text+':-'+sf[f].text+' || ')
                    if 'camera' in sb[c].text.lower():
                        sc=sa[b].find_all('table')
                        for d in range(len(sc)):
                            sd=sc[d].find_all('tr')
                            for e in range(len(sd)):
                                se=sd[e].find_all('th')
                                sf=sd[e].find_all('td')
                                for f in range(len(se)):
                                    if 'pixels' in se[f].text.lower() or 'material' in se[f].text.lower():
                                        c1=c1+(sb[c].text.strip().replace('\n',' ')+':-'+sf[f].text.strip().replace('\n',' ')+' || ')
        else:
            sb=results[a].find_all('div',attrs={'class':'feature-icon'})
            for b in range(len(sb)):
                sc=sb[b].find_all('li')
                for c in range(len(sc)):
                    sd=sc[c].find_all('p')
                    for d in range(len(sd)):
                        if 'GB' in sd[d].text:
                            m1=m1+sd[d].text+' || '
                        if 'mAh' in sd[d].text:
                            battery_list.append(sd[d].text)
                        if 'pixel' in sd[d].text.lower():
                            camera_list.append(sd[d].text)
                        if 'thickness' in sd[d].text.lower():
                            thickness_list.append(sd[d].text)
                        if 'cm' in sd[d].text or 'inch' in sd[d].text:
                            display_list.append(sd[d].text)
                        


    if p1!='':
        processor_list.append(p1)
    if c1!='':
        camera_list.append(c1)
    if d1!='':
        display_list.append(d1)
    if m1!='':
        memory_list.append(m1)
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
print(len(model_list))
print(len(usp))
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(battery_list))
print(len(display_list))
print(len(camera_list))
#print(camera_list)
#print(usp)
extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'infocus-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')


