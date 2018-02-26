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

base_url = 'https://mobile.panasonic.com/in/'
country = 'JAPAN'
company = 'PANASONIC'
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
st_list_heads = []
st_list_dets = []


url_list = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

series_url=['productlist/eluga', 'productlist/p-series']
specs=[]

for u in series_url:
    uurl = base_url + u
    r1 = requests.get(uurl)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    s1 = soup1.find_all('li', attrs={'class':'col-md-4 col-sm-6 product-list-item'})
    for s in s1:
        p = s.find('a')['href']
        q = s.find('h2').text
        href.append('https://mobile.panasonic.com' + p)
        model_list.append(str(q))

for i in range(len(href)):
    print(href[i])
    uu = ''
    heads = []
    dets = []
    r2 = requests.get(href[i])
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    try:
        p1 = soup2.find('ul', attrs={'class':'short-specification'}).find_all('li')
        for p in p1:
            uuu = str(p.text)
            uuu = uuu.strip().replace('\n', ' ').replace('<br>', ' ')
            uu = uu + uuu + ' || '
        usp.append(uu)
    except:
        usp.append('Not Available')
    
    s2 = soup2.find_all('div', attrs={'class':'col-md-12 col-sm-12 col-xs-12 sepec-bor'})
    s3 = soup2.find_all('div', attrs={'class':'col-md-12 col-sm-12 col-xs-12 sepec-bor margin-top-20'})
    for s in s2:
        t1 = s.find_all('div', attrs={'class':'row'})
        for t in t1:
            q1 = t.find_all('div')
            heads.append(q1[0].text.strip('\n').strip().replace('\n', ' ').replace('\r', ' '))
            dets.append(q1[1].text.strip('\n').strip().replace('\n', ' ').replace('\r', ' '))
    for s in s3:
        t1 = s.find_all('div', attrs={'class':'row'})
        for t in t1:
            q2 = t.find_all('div')
            heads.append(q2[0].text.strip('\n').strip().replace('\n', ' ').replace('\r', ' '))
            dets.append(q2[1].text.strip('\n').strip().replace('\n', ' ').replace('\r', ' '))
    st_list_heads.append(heads)
    st_list_dets.append(dets)

for i in  range(len(st_list_heads)):
    dd = ''
    mm = ''
    cc = ''
    for j in range(len(st_list_heads[i])):
        if 'Size' in st_list_heads[i][j] or 'Resolution' in st_list_heads[i][j]:
            dd = dd + st_list_dets[i][j] + ' || '
        if 'Processor' in st_list_heads[i][j]:
            processor_list.append(st_list_dets[i][j])
        if 'RAM' in st_list_heads[i][j]: 
            mm = mm + 'RAM : ' + st_list_dets[i][j] + ' || '
        if 'ROM' in st_list_heads[i][j]:
            mm = mm + 'ROM : ' + st_list_dets[i][j] + ' || '
        if 'Rear camera' in st_list_heads[i][j] or 'Rear Camera' in st_list_heads[i][j]:
            cc = cc + 'Rear : ' + st_list_dets[i][j] + ' || '
        if 'Front camera' in st_list_heads[i][j] or 'Front Camera : ' in st_list_heads[i][j]:
            cc = cc + 'Front' + st_list_dets[i][j] + ' || '
        if 'Battery (mAh)' in st_list_heads[i][j]:
            battery_list.append(st_list_dets[i][j] + ' mAh')
        if 'Dimensions' in st_list_heads[i][j]:
            st  = ''
            match = re.search(r'\*\s*\d+\.\d+\s*mm', st_list_dets[i][j])
            if match:
                st = str(match.group())
            if not match:
                match = re.search(r'\*\s*\d+\.\d+\s*\(\s*mm\s*\)', st_list_dets[i][j])
                if match:
                    st = str(match.group())
                if not match:
                    st = 'Not Available'
            thickness_list.append(st.strip().strip('*'))
    if dd!='':
        display_list.append(dd)
    if mm!='':
        memory_list.append(mm)
    if cc!='':
        camera_list.append(cc)
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')

print('LENGTH OF DISPLAY LIST: %d' %len(display_list))
print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))
print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))
print('LENGTH OF U.S.P. LIST: %d' %len(usp))


extras_links = href

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
try:
    for i in range(len(model_list)):
        records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))
except:
    print('ERROR: :LENGTH OF LISTS NOT EQUAL.')

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-panasonic'+'.csv'), index=False, encoding='utf-8')
####################################################################################################################################
