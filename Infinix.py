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

base_url = 'http://www.infinixmobility.com/'
country = 'HONG KONG'
company = 'INFINIX'
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
herf=[]
model=[]
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'static_block all-products'})
for i in range(len(results)):
    sa=results[i].find_all('ul')
    for a in range(len(sa)):
        sb=sa[a].find_all('li')
        for b in range(len(sb)):
            model.append(sb[b].text.strip().replace('/',' ').replace('\xa0',' '))
            herf.append(sb[b].find('a')['href'])
for i in range(len(herf)):
    if 'smartphone' in herf[i]:
        href.append(herf[i])
        model_list.append(model[i])

for i in range(len(href)):
    href[i]=base_url+href[i]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'sub-nav sub-nav-list'})
    for a in range(len(results)):
        sa=results[a].find_all('li')
        for b in range(len(sa)):
            try:
                if 'SPEC' in sa[b].text or 'Spec' in sa[b].text or 'spec' in sa[b].text:
                    hr.append(sa[b].find('a')['href'])
            except:
                pass
for i in range(len(hr)):
    u=''
    hr[i]=base_url+hr[i]
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'main-data-list'})
    for a in range(len(results)):
        sa=results[a].find_all('ul')
        for b in range(len(sa)):
            sb=sa[b].find_all('li')
            for c in range(len(sb)):
                u=u+sb[c].text.strip().replace('<span>',' ').replace('</span>',' ')+' || '
    usp.append(u)
for i in range(len(hr)):
    c1=''
    d1=''
    m1=''
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'container columns'})
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'parameter-box'})
        for b in range(len(sa)):
            sb=sa[b].find_all('div',attrs={'class':'col-lg-3 col-md-3 col-sm-3 columns'})
            for c in range(len(sb)):
                sc=sb[c].find_all('div',attrs={'class':'specs-label'})
                for d in range(len(sc)):
                    try:
                        if 'platform' in sc[d].text.lower():
                            sd=sa[b].find_all('div',attrs={'class':'col-lg-9 col-md-9 col-sm-9 columns'})
                            for e in range(len(sd)):
                                se=sd[e].find_all('li')
                                for f in range(len(se)):
                                    if 'cpu frequency' in se[f].text.lower() or 'cpu freouency'  in se[f].text.lower():
                                        processor_list.append(se[f].text.strip().replace('<span>',' ').replace('</span>',' ').replace('\n',' :'))
                        if 'memory' in sc[d].text.lower():
                            sd=sa[b].find_all('div',attrs={'class':'col-lg-9 col-md-9 col-sm-9 columns'})
                            for e in range(len(sd)):
                                se=sd[e].find_all('li')
                                for f in range(len(se)):
                                    if 'rom' in se[f].text.lower() or'ram' in se[f].text.lower() or'internal' in se[f].text.lower():
                                        m1=m1+se[f].text.strip().replace('<span>',' ').replace('</span>',' ').replace('\n',' :').replace('<br>', ' ').replace(' ','')+' || '
                    
                        if 'battery' in sc[d].text.lower():
                            sd=sa[b].find_all('div',attrs={'class':'col-lg-9 col-md-9 col-sm-9 columns'})
                            for e in range(len(sd)):
                                se=sd[e].find_all('li')
                                for f in range(len(se)):                           
                                    if 'capacity' in se[f].text.lower():
                                        battery_list.append(se[f].text.strip().replace('<span>',' ').replace('</span>',' ').replace('\n',' :').replace('    ',' '))
                        if 'display' in sc[d].text.lower():
                            sd=sa[b].find_all('div',attrs={'class':'col-lg-9 col-md-9 col-sm-9 columns'})
                            for e in range(len(sd)):
                                se=sd[e].find_all('li')
                                for f in range(len(se)):
                                    if 'size' in se[f].text.lower() or'type' in se[f].text.lower():
                                        d1=d1+se[f].text.strip().replace('<span>',' ').replace('</span>',' ').replace('\n',' :')+' || '
                        if 'camera' in sc[d].text.lower():
                            sd=sa[b].find_all('div',attrs={'class':'col-lg-9 col-md-9 col-sm-9 columns'})
                            for e in range(len(sd)):
                                se=sd[e].find_all('li')
                                for f in range(len(se)):
                                    if 'pixel' in se[f].text.lower() and 'image size' not in se[f].text.lower() and 'location' not in se[f].text.lower():

                                        c1=c1+se[f].text.strip().replace('<span>',' ').replace('</span>',' ').replace('\n',' :').replace('<br>', ' ').replace(' ','')+' || '
                                        if c1=='':
                                            c1 = 'Not Available'
                    except:
                        pass
##    if len(camera_list)==i:
##        camera_list.append('NA')
##    if len(display_list)==i:
##        display_list.append('NA')
##    if len(processor_list)==i:
##        processor_list.append('NA')
##    if len(battery_list)==i:
##        battery_list.append('NA')
##    if len(memory_list)==i:
##        memory_list.append('NA')
    memory_list.append(m1)
    camera_list.append(c1)
    display_list.append(d1)                    
for i in range(len(model_list)):
    thickness_list.append('Not Available')

extras_links = href
print(len(model_list))
print(len(usp))
print(len(display_list))
print(len(camera_list))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))


for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+ '-infinix' +'.csv'), index=False, encoding='utf-8')
   
      

                
    

      
                
