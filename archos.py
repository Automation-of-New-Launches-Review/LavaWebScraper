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

base_url = 'https://www.archos.com/fr/products/smartphones/index.html?cat=all#haut'
ur='http://agmmobile.com/en/'
country = 'France'
company = 'Archos'
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
results=soup.find_all('div',attrs={'class':'col-sm-3 col-md-3 img-range-zoom'})
for i in range(len(results)):
    href.append(results[i].find('a')['href'])
    sa=results[i].find_all('div')
    for a in range(len(sa)):
        model_list.append(sa[a].text)

for i in range(len(href)):
    heads=[]
    dets=[]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'panel panel-danger'})
    for a in range(len(results)-1):
        sa=results[a].find_all('li')
        for b in range(len(sa)):
            s=''
            try:
                heads.append(sa[b].contents[0].text)
                for c in range(1,len(sa[b].contents)):
                    try:
                        s+=sa[b].contents[c].strip(':').strip()
                    except:
                       print('DETS NOT FOUND FOR THIS ELEMENT.')
                dets.append(s)
            except:
                pass
    st_list_heads.append(heads)
    st_list_dets.append(dets)
i=1
for i in range(len(st_list_heads)):
    m1 = ''
    m2 = ''
    d1 = ''
    d2 = ''
    cc = 'Back / Front : '
    for j in range(len(st_list_heads[i])):
        if 'cpu' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
            
        if 'ram' in st_list_heads[i][j].lower():
            m1='RAM- '+(st_list_dets[i][j])+' || '
            
        if 'internal storage' in st_list_heads[i][j].lower():
            m2='ROM- '+st_list_dets[i][j]+' || '
            
        if 'battery size' in st_list_heads[i][j].lower():
            battery_list.append(st_list_dets[i][j])
        
        if 'diagonal size' in st_list_heads[i][j].lower():
            d1 ='Size- '+ st_list_dets[i][j]+' || '
            
        if 'technology' in st_list_heads[i][j].lower():
            d2 ='Type- '+ st_list_dets[i][j]+' || '
            
        if 'back camera' in st_list_heads[i][j].lower() or 'front camera' in st_list_heads[i][j].lower() or 'back photos' in st_list_heads[i][j].lower() or 'back pictures' in st_list_heads[i][j].lower() or 'front photos' in st_list_heads[i][j].lower() or 'front pictures' in st_list_heads[i][j].lower():
            cc = cc + st_list_dets[i][j] + ' || '
        
    if m1!='' or m2!='':
        memory_list.append(m1+' '+m2)
    if d1!='' or d2!='':
        display_list.append(d1+' '+d2)
    if cc!='Back / Front : ':
        camera_list.append(cc)
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
print(usp)
print(len(href))
extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today()) + '-archos' +'.csv'), index=False, encoding='utf-8')

