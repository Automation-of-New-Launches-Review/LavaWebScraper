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

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'


base_url = 'http://www.tecno-mobile.com/phones/product-list/#/'
country = 'CHINA'
company = 'TECNO'
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
spec=[]
cam=[]
model=[]
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('ul',attrs={'class':'row list-unstyled product-list'})
for i in range(len(results)):
    sa=results[i].find_all('li',attrs={'class':'col-md-6 col-lg-4 col-xl-4'})
    for a in range(len(sa)):
        href.append(sa[a].find('a')['href'])
        model_list.append(sa[a].find('h4',attrs={'class':'tile-title text-center'}).text)
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'list-unstyled sticky-nav-menu'})
    for a in range(len(results)):
        sa=results[a].find_all('li')
        for b in range(len(sa)):
            if 'Tech Specs' in sa[b].text.strip():
                hr.append(sa[b].find('a')['href'])
for i in range(len(hr)):
    ss=[]
    cc=''
    dd=''
    mm=''
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('section',attrs={'class':'container cs-product-tech-spec parameter-section'})
    for a in range(len(results)):
        sa=results[a].find_all('h3',attrs={'class':'tech-spec-title'})
        for b in range(len(sa)):
            if 'Specification' in sa[b].text:
                sb=results[a].find_all('ul',attrs={'class':'list-unstyled parameter-info-list'})
                for c in range(len(sb)):
                    sc=sb[c].find_all('li')
                    for d in range(len(sc)):
                        if sc[d].text:
                            ss.append(sc[d].text)
                        else:
                            pass
    
            if 'Camera & Interface' in sa[b].text:
                sd=results[a].find_all('div',attrs={'class':'col-sm-9 col-md-10 parameter-col'})
                for s in sd:
                    sf = s.find_all('div', attrs={'class':'col-xs-12 col-sm-6'})
                    for q in sf:
                        if q.text!='':
                            ss.append(q.find('li').text.strip().replace('\n', ' '))
                        else:
                            pass
    for z in ss:
        if 'Thickness' in z and 'Weight' not in z:
            thickness_list.append(z.strip())
        if 'GHz' in z and 'Weight' not in z and 'ROM' not in z and 'RAM' not in z:
            processor_list.append(z.strip())
        if 'mAh' in z and 'Weight' not in z and 'ROM' not in z and 'RAM' not in z:
            battery_list.append(z.strip())
        if 'ROM' in z and 'Weight' not in z and 'Processor' not in z:
            mm = mm + ' ROM: ' + str(z.strip()) + ' || '
        if 'RAM' in z and 'Weight' not in z and 'Processor' not in z:
            mm = mm + ' RAM: ' + str(z.strip()) + ' || '
        if 'Camera' in z and 'Weight' not in z:
            cc = cc + str(z.strip()) + ' || '
        if 'inch' in z and 'Weight' not in z and 'Processor' not in z:
            dd = dd + str(z.strip()) + ' || '
        if 'px' in z and 'Weight' not in z and 'Processor' not in z:
            dd = dd + str(z.strip()) + ' || '
    if mm!='':
        memory_list.append(mm)
    if cc!='':
        camera_list.append(cc)
    if dd!='':
        display_list.append(dd)
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    
print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))
print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))
print('LENGTH OF DISPLAY LIST: %d' %len(display_list))
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))

extras_links =  href
for i in range(len(href)):
    usp.append('Not Available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-tecno'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################

               
            
