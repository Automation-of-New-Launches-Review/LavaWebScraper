import csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import datetime
import os
today=datetime.date.today()
memory=[]
urls=[]
urls1=[]
urls2=[]
model=[]
company=[]
specs=[]
country=[]
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []
url="https://consumer.huawei.com/en/support/phones/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('div',attrs={'class':'product_items'})

for s in links:
    tt=s.find_all('a',attrs={'class':'a-common'})
    for v in tt:
        urls1.append(v['href'])

for m in urls1:
    r1=requests.get(m)
    
    soup1=BeautifulSoup(r1.text,'html.parser')    
    link=soup1.find_all('a',attrs={'class':'a-subsection a-common'})
    if link:
        for y in link:
            urls2.append(y['href'])


for z in urls2:
    
    if "specs" in z:
        urls.append("https://consumer.huawei.com"+z)

xv=0
for i in urls:
    country.append("CHINA")
    company.append("HUAWEI")
    extras_links.append(i)
    specs.append("NOT AVAILABLE")
    if i=='https://consumer.huawei.com/en/phones/mate8/specs':
        battery_list.append("NOT AVAILABLE")    
    kst=[]
    r2=requests.get(i)
    soup2=BeautifulSoup(r2.text,'html.parser')    
    lin=soup2.find_all('div',attrs={'class':'spec-contect'})
    tit=soup2.find('div',attrs={'class':'spec-title-pro'})
    model.append(tit.text)
    if lin:
        print(i)
        for xc in lin:
            ty=xc.find_all('p')
            for ss in ty:
                for bn in ss:
                    kst.append(bn)
        yo=''
        no=''
        jo=''
        xc=''
        for v in kst:
            if ('inches' in v or 'inch' in v or '”' in v or '"' in v  or "'" in v) and 'Rear' not in v and 'Resolution' not in v and '<dl class="items">' not in v:
                xc=xc+v.strip()
                    
            if 'GB' in v and("RAM" in v or "ROM" in v) and "VKY-Al00" not in v and 'Graphite' not in v:
                yo=yo+v.strip()
            if  'GHz' in v and ('CPU' in v or 'Core' in v or 'core' in v or 'Snapdragon' in v or 'MT' in v):
                no=no+v.strip()
            if 'MP' in v and ('camera' in v or 'Camera' in v or 'CAMERA' in v or 'Monochrome' in v or 'Back' in v )or ('Front' in v or 'Back' in v or 'MP' in v) and 'Dual' not in v and 'MHz' not in v and 'MP3' not in v and 'MPE' not in v and 'JPEG' not in v and 'PN' not in v and 'BMP' not in v and 'CPU' not in v and 'MP4' not in v:
                jo=jo+v.strip()+" "
            if 'mAh' in v or 'mAh*' in v:
                battery_list.append(v.strip())
            if 'mm' in v and 'Depth' in v:
                thickness_list.append(v.strip())
            if 'mm' in v and '*' in v:
                thickness_list.append(v.strip())            
        
        if len(thickness_list)==xv:
            thickness_list.append('NOT AVAILABLE')
        processor_list.append(no)
        memory_list.append(yo)
        camera_list.append(jo)
        display_list.append(xc)       
    xv=xv+1    
        
                
            
print(len(country))
print(len(company))
print(len(model))
print(len(specs))
print(len(display_list))
print(len(camera_list))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))

records=[]
for i in range(len(company)):
    records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'-huawei'+'.csv'), index=False, encoding='utf-8')

            
    
    
