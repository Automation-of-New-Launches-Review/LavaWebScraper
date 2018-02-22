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

base_url = 'http://www.zenmobile.in/smart-phones/'
#ur='https://www.nokia.com/en_int/phones/'
country = 'INDIA'
company = 'ZEN'
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
soup=BeautifulSoup(r.text,'html5lib')
results=soup.find_all('div',attrs={'class':'col-md-3 col-sm-4 col-xs-12 bt-gap'})
#print(len(results))
for i in range(len(results)):
    sa=results[i].find_all('div',attrs={'class':'item_per1 thisdiv'})
    for a in range(len(sa)):
        sb=sa[a].find_all('div',attrs={'class':'ruby-col-3 upto-5'})
        #print(len(sb))
        for b in range(len(sb)):
            sc=sb[b].find_all('div',attrs={'class':'ruby-col-5'})
            for c in range(len(sc)):
                sd=sc[c].find_all('p',attrs={'class':'ruby-c-title'})
                for d in range(len(sd)):
                    print(sd[d].find('a')['href'])
                    print(sd[d].text.strip())
                          
for i in range(len(results)):
    href.append(results[i].find('a')['href'])
    model_list.append(results[i].find('p').text)

for i in range(len(href)):
    m1=''
    d1=''
    c1=''
    heads=[]
    dets=[]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results1=soup.find_all('div',attrs={'class':'com-md-12'})
    for z in range(len(results1)):
        usp.append(results1[z].find('h3').text.strip())
    results=soup.find_all('div',attrs={'class':'row hidden-specification'})
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'col-md-12'})
        for b in range(len(sa)):
            sb=sa[b].find('h5').text.lower()
            #print(sb)
            if 'display' in sb:
                sd=sa[b].find_all('table',attrs={'class':'table'})
                for d in range(len(sd)):
                    se=sd[d].find_all('tr')
                    for e in range(len(se)):
                        sf=se[e].find_all('td')
                        for f in range(len(sf)):
                            if 'physical size' in sf[f].text.lower() or 'resolution type' in sf[f].text.lower():
                                d1=d1+sf[f].text.strip().replace('\n',' ')+':- '+sf[f+1].text.strip().replace('\n',' ')+' || '
                    

            if 'camera' in sb:
                sd=sa[b].find_all('table',attrs={'class':'table'})
                for d in range(len(sd)):
                    se=sd[d].find_all('tr')
                    for e in range(len(se)):
                        sf=se[e].find_all('td')
                        for f in range(len(sf)):
                            if 'back camera' in sf[f].text.lower() or 'front camera' in sf[f].text.lower():
                                c1=c1+sf[f].text.strip().replace('\n',' ')+':- '+sf[f+1].text.strip().replace('\n',' ')+' || '

            if 'hardware' in sb:
                sd=sa[b].find_all('table',attrs={'class':'table'})
                for d in range(len(sd)):
                    se=sd[d].find_all('tr')
                    for e in range(len(se)):
                        sf=se[e].find_all('td')
                        for f in range(len(sf)-1):
                            if 'processor' in sf[f].text.lower() and 'graphic' not in sf[f].text.lower():
                                processor_list.append(sf[f+1].text.strip().replace('\n',' '))
                            if 'RAM' in sf[f].text or 'rom' in sf[f].text.lower():
                                m1=m1+sf[f].text.strip().replace('\n',' ')+':- '+sf[f+1].text.strip().replace('\n',' ')+' || '

            
            if 'battery' in sb:
                sd=sa[b].find_all('table',attrs={'class':'table'})
                for d in range(len(sd)):
                    se=sd[d].find_all('tr')
                    for e in range(len(se)):
                        sf=se[e].find_all('td')
                        for f in range(len(sf)):
                            if 'capacity' in sf[f].text.lower():
                                battery_list.append(sf[f+1].text.strip().replace('\n',' '))
    if d1!='':
        display_list.append(d1)
    if c1!='':
        camera_list.append(c1)
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
#print(processor_list)
print(len(memory_list))
#print(memory_list)
print(len(battery_list))
print(len(display_list))
print(len(camera_list))
#print(usp)
extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'zen-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
   
      
                    
                       
                        
                    
                                     

