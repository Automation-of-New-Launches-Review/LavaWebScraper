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

base_url = 'http://www.zopomobile.com/products/'
#ur='https://www.nokia.com/en_int/phones/'
country = 'CHINA'
company = 'ZOPO'
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
results=soup.find_all('div',attrs={'class':'row pro-list clearfix'})
##print(len(results))
for a in range(len(results)):
    sa=results[a].find_all('div',attrs={'class':'pro-item col-sm-3 col-xs-6'})
    #print(len(sa))
##    print(sa)
    for b in range(len(sa)):
        sb=sa[b].find_all('a')
        if len(sb)!=0:
            for c in range(len(sb)):
                href.append(sb[c]['href'])
                sc=sb[c].find_all('div',attrs={'class':'pro-name'})
                for d in range(len(sc)):
                    model_list.append(sc[d].text.strip())

##print(len(href))
##for i in href:
##    print(i)
##print('\n\n\n\n')
##print(len(model_list))
##for i in model_list:
##    print(i)
for a in range(len(href)):
    #print(a)
    p1=''
    c1=''
    d1=''
    m1=''
    r=requests.get(href[a])
    soup=BeautifulSoup(r.text,'html.parser')
    results = soup.find('div', attrs={'class':'specs'})
    sa=results.find_all('table',attrs={'class':'spec-table'})
    if len(sa)!=0:
        for d in range(len(sa)):
            sc=sa[d].find_all('tr')
            #print(sc)
            for e in range(len(sc)):
                sd = sc[e].find_all('td')
                if 'cpu' in sd[0].text.lower() or 'clock speed' in sd[0].text.lower():
                    p1+=sd[1].text.strip()+' || '
                if 'rom' in sd[0].text.lower() or 'ram' in sd[0].text.lower():
                    m1+=sd[0].text.strip()+':-'+sd[1].text.strip()+'||'
                if 'lcd size' in sd[0].text.lower() or 'display type' in sd[0].text.lower():
                    d1+=sd[1].text.strip().replace('：',':') +' || '
                if 'rear camera' in sd[0].text.lower() or 'front camera' in sd[0].text.lower():
                    match = re.search(r'HW Resolution:.+?,', sd[1].text.strip().replace('：',':').replace('<br>', ' ').replace('\n', ' ').replace('\n', ' ')+'||')
                    try:
                        st = str(match.group())
                    except:
                        pass
                    c1=c1+sd[0].text.strip()+':-'+ st
                    
                    c1 = re.sub( r'([\s][\s])\W+', r' ', c1)
                if 'capacity' in sd[0].text.lower():
                    battery_list.append(sd[1].text.strip())
                if 'special function' in sd[0].text.lower():
                    usp.append(sd[1].text.strip().strip('\n').replace('<br>', ' ').replace('\n', ' '))
    else:
        sb=results.find_all('div',attrs={'class':'parameter-list clearfix'})
        for c in range(len(sb)):
            #sc=sb[c].find_all('div',attrs={'class':'paramater-item'})
            sc=sb[c].find_all('div',class_='paramater-item')
            if len(sc)!=0:
                for d in range(len(sc)):
                    sd=sc[d].find_all('div',attrs={'class':'parameter-name'})
                    for s in range(len(sd)):
                        if 'dimension' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    if 'dimension' in sf[f].text.lower():
                                        thickness_list.append(sg[f].text.strip())
                        if 'battery' in sd[s].text.lower():
                            #print(a)
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                #print(a)
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    
                                    if 'capacity' in sf[f].text.lower():
                                        battery_list.append(sg[f].text.strip())
                                        
                        if 'processor' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    try:
                                        if ('cpu model' in sf[f].text.lower() or 'cores' in sf[f].text.lower() or 'gpu' in sf[f].text.lower()) and 'octa' not in sf[f].text.lower() and 'quad' not in sf[f].text.lower():
                                            p1=p1+sf[f].text+sg[f].text.strip().replace('：',':')+' || '
                                    except:
                                        pass
                        if 'memory' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    try:
                                        if ('rom' in sf[f].text.lower() or 'ram' in sf[f].text.lower() or 'storage' in sf[f].text.lower()) and 'octa' not in sf[f].text.lower() and 'quad' not in sf[f].text.lower():
                                            m1=m1+sf[f].text+sg[f].text.strip().replace('：',':')+' || '
                                    except:
                                        pass
                        if 'display' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    if 'size' in sf[f].text.lower() or 'technology' in sf[f].text.lower():
                                        d1=d1+sf[f].text+sg[f].text.strip().replace('″','"').replace('：',':').replace('，',',')+' || '
                        
                        if 'main camera' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    if 'resolution' in sf[f].text.lower() and 'video' not in sf[f].text.lower():
                                        c1=c1+'Main Camera:- '+sf[f].text+sg[f].text.strip().replace('：',':')+' || '
                        if 'facing camera' in sd[s].text.lower():
                            se=sc[d].find_all('div',attrs={'class':'parameter-value'})
                            for e in range(len(se)):
                                sf=se[e].find_all('dt')
                                sg=se[e].find_all('dd')
                                for f in range(len(sf)):
                                    if 'resolution' in sf[f].text.lower() and 'video' not in sf[f].text.lower():
                                        c1=c1+'Front Camera:- '+sf[f].text+sg[f].text.strip().replace('：',':')+' || '

                
    if p1!='':
        processor_list.append(p1)
    if m1!='':
        memory_list.append(m1)
    if c1!='':
        camera_list.append(c1)
    if d1!='':
        display_list.append(d1)
    if len(battery_list)==a:
        battery_list.append('Not Available')
    if len(memory_list)==a:
        memory_list.append('Not Available')
    if len(processor_list)==a:
        processor_list.append('Not Available')
    if len(display_list)==a:
        display_list.append('Not Available')
    if len(thickness_list)==a:
        thickness_list.append('Not Available')
    if len(camera_list)==a:
        camera_list.append('Not Available')
    if len(usp)==a:
        usp.append('Not Available')
##print('DISPLAY LIST:- ')
print(len(display_list))
##for i in display_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            
#print('PROCESSOR LIST:- ')
print(len(processor_list))
##for i in processor_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
#print('MEMORY LIST:- ')
print(len(memory_list))
##for i in memory_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
#print('CAMERA LIST:- ')
print(len(camera_list))
##for i in camera_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
#print('BATTERY LIST:- ')
print(len(battery_list))
##for i in battery_list:
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
#print('USP LIST:- ')
print(len(usp))
##for i in usp    :
##    print(i)
##print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(len(thickness_list))
##for i in thickness_list:
##    print(i)

extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'zopo-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
   
      
                    
                       

