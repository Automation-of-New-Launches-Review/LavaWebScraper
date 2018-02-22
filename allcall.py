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

base_url = 'http://www.allcall.hk/phones.html'
ur='http://www.allcall.hk'
country = 'China'
company = 'AllCall'
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
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('li',attrs={'class':'col-xs-6 col-sm-3 col-md-3 col-lg-3 padding-left-right-def'})
for i in range(len(results)):
    model_list.append(results[i].find('h4').text)
    href.append(results[i].find('a')['href'])
#print(href)
##print(len(href))
##print(model_list)
##print(len(model_list))
HREF=[]
for i in range(len(href)):
    href[i]=ur + href[i]
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12 padding-margin-no padding-margin-def subnavul'})
    if len(results)==1:
        sa=results[0].find_all('li')
        for a in range(len(sa)):
            sb=sa[a].text
            if sb == 'Specification':
                hr.append(ur + sa[a].find('a')['href'])                
    else:
        hr.append(href[i])
        
for i in range(len(hr)):
    s=''
    heads=[]
    dets=[]
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'container overflow-hidden padding-tottom-5'})
    #print(len(results))
    for a in range(len(results)):
        sa=results[a].find_all('ul',attrs={'class':'col-xs-12 col-sm-8 col-md-8 col-lg-8 padding-top-5 padding-margin-def top-info'})
##        print(len(sa))
##        print('                                                    ')
        for b in range(len(sa)):
            sb=sa[b].find_all('li')
            for c in range(len(sb)):
                tt = sb[c].text.strip('\n')
                tt = tt.strip('\t')
                s=s+ tt + ' || '
                s=s.strip('\n')
                s=s.strip('\t').replace('\xa0',' ')
    usp.append(s)
    for a in range(len(results)):
        sa=results[a].find_all('ul',attrs={'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12 padding-margin-def content'})
        for b in range(len(sa)-1):
            sb=sa[b].find_all('li')
            for c in range(len(sb)):
                if c%2 ==0:
                    heads.append(sb[c].text.strip('\n\t'))
                else:
                    dets.append(sb[c].text.strip('\n\t').replace('\xa0',' ').replace('\n',' '))
    st_list_heads.append(heads)
    st_list_dets.append(dets)
##print(st_list_heads)
##print(len(st_list_heads))
##print(len(st_list_dets))      
##print(st_list_dets)
##print(usp)
##print(len(usp))
for i in range(len(st_list_heads)):
    q1 = ''
    q2 = ''
    r1 = ''
    r2 = ''
    s1 = ''
    s2 = ''
    for j in range(len(st_list_heads[i])):
        if 'cpu' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j].replace(' （','(').replace('）',')'))
        if 'memory' in st_list_heads[i][j].lower():
            memory_list.append(st_list_dets[i][j])
        if 'battery' in st_list_heads[i][j].lower():
            battery_list.append(st_list_dets[i][j])
        if 'ram' in st_list_heads[i][j].lower():
            q1='RAM:- '+st_list_dets[i][j]+' || '
        if 'rom' in st_list_heads[i][j].lower():
            q2='ROM:- '+st_list_dets[i][j]+' || '
        if 'screen size' in st_list_heads[i][j].lower() or'display size' in st_list_heads[i][j].lower():
            r1 ='Size:- ' +st_list_dets[i][j]+' || '
        if 'type' in st_list_heads[i][j].lower():
            r2 ='Type:- '+ st_list_dets[i][j]+' || '
        #if 'Rear camera' in st_list_heads[i][j] or 'Rear Camera' in st_list_heads[i][j] or 'rear camera' in st_list_heads[i][j] or 'Rear  Camera' in st_list_heads[i][j]:
            #s1='Rear camera:- '+st_list_dets[i][j]+' || '
        #if 'Front camera' in st_list_heads[i][j] or 'Front Camera' in st_list_heads[i][j] or 'front camera' in st_list_heads[i][j] or 'Front  Camera' in st_list_heads[i][j]:
            #s2='Front camera:- '+st_list_dets[i][j]+' || '
        if 'rear' in st_list_heads[i][j].lower() and 'camera' in st_list_heads[i][j].lower():
            s1='Rear camera:- '+st_list_dets[i][j]+' || '
        if 'front' in st_list_heads[i][j].lower() and 'camera' in st_list_heads[i][j].lower():
            s2='Front camera:- '+st_list_dets[i][j]+' || '
            
        
    if q1!='' or q2!='':
        memory_list.append(q1+' '+q2)
    if r1!='' or r2!='':
        display_list.append(r1+' '+r2)
    if s1!='' or s2!='':
        camera_list.append(s1 +' '+ s2)
    #if 'Dimensions' not in st_list_heads[i]:
        #thickness_list.append('NA')
    #if 'CPU' not in st_list_heads[i]:
        #processor_list.append('NA')
##    if 'Memory' not in st_list_heads[i] and 'memory' not in st_list_heads[i]:
##        memory_list.append('NA')
##    if 'ROM' not in st_list_heads[i] and 'RAM' not in st_list_heads[i]:
##        memory_list.append('NA')
    #if 'Battery' not in st_list_heads[i] and 'battery' not in st_list_heads[i]:
        #battery_list.append('NA')
    #if 'Screen Size' not in st_list_heads[i] and 'Type' not in st_list_heads[i] and 'type' not in st_list_heads[i] and 'Screen size' not in st_list_heads[i] and 'screen size' not in st_list_heads[i] and 'Display Size' not in st_list_heads[i] and 'Display size' not in st_list_heads[i] and 'display size' not in st_list_heads[i]:
        #display_list.append('NA')
    #if 'Rear camera' not in st_list_heads[i] and 'Front camera' not in st_list_heads[i] and 'Rear Camera' not in st_list_heads[i] and 'Front Camera' not in st_list_heads[i]:
        #camera_list.append('NA')

    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
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
#print(usp)
extras_links = hr
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'allcall-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
