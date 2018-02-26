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


base_url = 'https://www.mazephone.com/buy-maze-mobile'
country = 'Japan'
company = 'Maze'
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
titles = []
href1=[]
usp1=[]
href_final = []
st_list_heads = []
st_list_dets = []
usp_final = []

r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'category-products'})


for i in range(len(results)):
    sa=results[i].find_all('a')
    #print(sa)
    for a in range(len(sa)):
        href1.append(sa[a]['href'])
        usp1.append(sa[a]['title'])
for i in range(len(href1)):
    if href1[i] in href:
        pass
    else:
        href.append(href1[i])

for i in range(len(usp1)):
    if usp1[i] in usp:
        pass
    else:
        usp.append(usp1[i])


i = 0
while i<len(href):
    if 'screen' in href[i] or 'case' in href[i] or 'film' in href[i]:
        pass
    else:
        href_final.append(href[i])
        usp_final.append(usp[i])
    i=i+1
        

for i in range(len(href_final)):
    heads = []
    dets = []
    r=requests.get(href_final[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('table',attrs={'border':'1'})
    for a in range(len(results)):
        sc=results[a].find_all('tr')
        for c in range(len(sc)):
            sa=sc[c].find_all('td')
            if len(sa)==1:
                continue
            else:
                heads.append(sa[0].text.strip().replace('<br>',' ').replace('\n', ' '))
                dets.append(sa[1].text.strip().replace('<br>',' ').replace('\n', ' '))
    st_list_heads.append(heads)
    st_list_dets.append(dets)

for i in range(len(st_list_heads)):
    m1 = 'ROM : '
    m2 = 'RAM : '
    d1 = ''
    d2 = ''
    print('MODEL NO.:', end=' : ')
    print(i)
    for j in range(len(st_list_heads[i])):
        if 'model' in st_list_heads[i][j].lower():
            model_list.append(st_list_dets[i][j])
        if 'cpu' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
        if 'ROM' in st_list_heads[i][j]:
            m1 = m1 + st_list_dets[i][j]
        if 'RAM' in st_list_heads[i][j]:
            m2 = m2 + st_list_dets[i][j]
        if 'Display&nbsp;Size' in st_list_heads[i][j] or 'display' in st_list_heads[i][j].lower():
            d1 = st_list_dets[i][j]
        if 'type' in st_list_heads[i][j].lower() and 'ringtones' not in st_list_heads[i][j].lower():
            d2 = st_list_dets[i][j]
        if 'camera' in st_list_heads[i][j].lower():
            camera_list.append(st_list_dets[i][j])
        if 'size' in st_list_heads[i][j].lower():
            match = re.search(r'x\s+\d.\d\s+mm', st_list_dets[i][j])
            if match:
                thickness_list.append(match.group())

    if m1!='ROM : ' or m2!='RAM : ':
        memory_list.append(m1 + ' ' + m2)
    if d1!='' or d2!='':
        display_list.append(d1 + ' ' + d2)
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
    #if len(usp)==i:
        #usp.append('Not Available')
    #battery_list.append('Not Availble')

extras_links= href_final

print(len(model_list))
print(len(usp_final))
print(len(thickness_list))
print(len(battery_list))
print(len(processor_list))
print(len(memory_list))
print(len(display_list))
print(len(camera_list))
print(len(extras_links))


############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-maze'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
        
