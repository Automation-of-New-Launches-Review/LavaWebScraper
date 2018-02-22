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

base_url = 'https://www.nokia.com/en_int/phones/android-phones'
ur='https://www.nokia.com/en_int/phones/'
country = 'Finland'
company = 'NOKIA'
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
results=soup.find_all('div',attrs={'class':'PhonesGrid'})
for i in range(len(results)):
    sa=results[i].find_all('a',attrs={'class':'GridPhone'})
    for a in range(len(sa)):
        sb=sa[a].find('div',attrs={'class':'GridPhone__row'})
        model_list.append(sb.text)
#print(model_list)
for i in range(len(model_list)):
    s=model_list[i].lower().replace(' ','-')
    m=ur + s
    href.append(m)
#print(href)
hr=href[:]
#print(hr)
for i in range(len(hr)):
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'product-overview__text-block'})
    for a in range(len(results)):
        usp.append(results[a].find('h2').text.replace('® ',' ').replace('™ ',' ').replace('¹ ',' '))
#print(usp)
for i in range(len(href)):
    href[i]=href[i] + '#details'
for i in range(len(href)):
    heads=[]
    dets=[]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'specs__container'})
    for a in range(len(results)):
        sa=results[a].find_all('div',attrs={'class':'specs__specs-block'})
        for b in range(1,len(sa)):
           sb=sa[b].find_all('div',attrs={'class':'content'})
           #print(len(sb))
           for c in range(len(sb)):
               sc=sb[c].find_all('p')
               for d in range(len(sc)):
                   if len(sc[d].contents)!=1:
                       if len(sc[d].contents)==2:
                           heads.append(sc[d].contents[0].text)
                           dets.append(sc[d].contents[1].replace('<sup>',' ').replace('</sup>',' ').replace('\xa0',' ').replace('\t',' ').strip('\xa0'))
                       else:
                           s=''
                           heads.append(sc[d].contents[0].text)
                           for x in range(1,len(sc[d].contents)):
                               s=s+str(sc[d].contents[x])
                                          
                           dets.append(s.replace('<sup>',' ').replace('</sup>',' ').replace('\xa0',' ').replace('\t',' ').strip('\xa0'))
                   else:
                       pass
    st_list_heads.append(heads)
    st_list_dets.append(dets)
##for i in st_list_heads:
##    print(i)
##print(len(st_list_heads))
##print('------------------------------------------------------------------------------------------------------------------------------------')
##for i in st_list_dets:
##    print(i)
##print(len(st_list_dets))



for i in range(len(st_list_heads)):
    m1=''
    m2=''
    c1=''
    c2=''
    
    
    for j in range(len(st_list_heads[i])):
        if st_list_heads[i][j].lower()=='size':
            s=st_list_dets[i][j]
            match=re.search(r'x\s*\d?\.\d+\s*mm', s)
            if match:
                p=str(match.group())
            if not match:
                p=''
                
            thickness_list.append(p)
            
        if 'cpu' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j].replace('® ',' ').replace('™ ',' '))
            
        if 'ram' in st_list_heads[i][j].lower() :
            m1='RAM:- '+st_list_dets[i][j]          
        if 'internal memory' in st_list_heads[i][j].lower():
            m2='ROM:- '+st_list_dets[i][j]
            
        if 'battery type' in st_list_heads[i][j].lower():
            battery_list.append(st_list_dets[i][j])
                        
        if 'size and type' in st_list_heads[i][j].lower():
             display_list.append(st_list_dets[i][j].replace('” ','"'))

        if 'primary camera' in st_list_heads[i][j].lower():
            c1='Main camera:- '+(st_list_dets[i][j].replace('˚','deg.'))
        if 'front-facing camera' in st_list_heads[i][j].lower():
            c2='Front camera:- '+(st_list_dets[i][j])
    if m1!=''or m2!='':
        memory_list.append(m1 +' || '+ m2)
    if c1!=''or c2!='':
        camera_list.append(c1 +' || '+ c2)
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


##    if 'Size' not in st_list_heads[i] and 'size' not in st_list_heads[i][j]:
##        thickness_list.append('NA')
##        
##        
##    if 'CPU' not in st_list_heads[i]:
##        processor_list.append('NA')
##        
##    if 'Internal memory' not in st_list_heads[i] and 'internal memory' not in st_list_heads[i] and 'Internal Memory' not in st_list_heads[i] and 'RAM' not in st_list_heads[i]:
##        memory_list.append('NA')
##        
##    if 'Battery type' not in st_list_heads[i] and 'battery type' not in st_list_heads[i]:
##        battery_list.append('NA')
##        
##    if 'Size and type' not in st_list_heads[i] and 'size and type' not in st_list_heads[i]:
##        display_list.append('NA')
##        
##    if 'Primary Camera' not in st_list_heads[i] and 'Primary camera' not in st_list_heads[i] and 'primary camera' not in st_list_heads[i] and 'Front-facing camera' not in st_list_heads[i] and 'front-facing camera' not in st_list_heads[i]:
##        camera_list.append('NA')
#print(len(model_list))
print(len(usp))
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(battery_list))
print(len(display_list))
print(len(camera_list))
#print(thickness_list)
extras_links = hr
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'nokia-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')

   
                        

                        
    
                           
     
        
    
