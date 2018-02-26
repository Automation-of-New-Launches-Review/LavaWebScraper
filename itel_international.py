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

## THIS FILE IS A COMMON FORMAT FOR SCRAPING THE WEBSITES. DO NOT CHANGE THE VARIABLE NAMES ALREADY SPECIFIED IN THIS FILE.
## YOU MAY HOWEVER ADD YOUR OWN VARIABLES.

## FINAL LIST OF RESULTS SHOULD BE AVAILABLE IN A LIST 'RECORDS' NECESSARILY FOR THE SAKE OF CONSISTENCY.

############## VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. ####################
base_url = 'http://www.itel-mobile.com/?m=product&a=smartList'
country = 'CHINA'
company = 'ITEL / INTERNATIONAL'
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
#####################################################################################################################################
st_list_heads = []
st_list_dets = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
s1 = soup.find_all('div', attrs={'class':'subproduct-desc'})

for s in s1:
    s1 = s.find_all('span')
    model_list.append(s1[0].text)
    usp.append(s1[1].text)
    s2 = s.find('a')
    href.append('http://www.itel-mobile.com/' + s2['href'])

for i in range(len(href)):
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(href[i])
    st = []
    heads = []
    dets = []
    r1 = requests.get(href[i])
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    s3 = soup1.find('table')
    s4 = s3.find_all('tr')
    for s in s4:
        s6 = s.find_all('span', attrs={'class':'title'})
        s7 = s.find_all('span', attrs={'class':'detail'})
        for q in s6:
            heads.append(q.text.strip())  
        for q in s7:
            dets.append(q.text.strip())
    st_list_heads.append(heads)
    st_list_dets.append(dets)

for i in range(len(st_list_dets)):
    for j in range(len(st_list_dets[i])):
        if 'display' in st_list_heads[i][j].lower():
            display_list.append(st_list_dets[i][j].replace('”','"'))

        if 'CPU' in st_list_heads[i][j] or 'processor' in st_list_heads[i][j].lower() or 'cpu' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
            
        if 'battery' in st_list_heads[i][j].lower():
            if 'capacity' in st_list_dets[i][j].lower():
                st_list_dets[i][j] = st_list_dets[i][j].replace('Capacity', '')
                st_list_dets[i][j] = st_list_dets[i][j].replace('     ', '')
            st_list_dets[i][j] = st_list_dets[i][j].strip()
            battery_list.append(st_list_dets[i][j].strip())
            
        if 'dimension' in st_list_heads[i][j].lower() or 'demension' in st_list_heads[i][j].lower():
            match = re.search(r'\*\d*\.\d*\s*mm', st_list_dets[i][j])
            if match:
                s = match.group()
            if not match:
                match = re.search(r'x\d*\.\d*\s*mm', st_list_dets[i][j])
                if match:
                    s = match.group()
                if not match:
                    match = re.search(r'\*\d*\.\d*\s*MM', st_list_dets[i][j])
                    if match:
                        s = match.group()
                    if not match:
                        s = ' '
            thickness_list.append(s)

        if 'memory' in st_list_heads[i][j].lower():
            memory_list.append(st_list_dets[i][j])
        if 'camera' in st_list_heads[i][j].lower():
            camera_list.append(st_list_dets[i][j])


    #ALTERNATIVE LOOP'S ENDING PART
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')

print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(display_list))
print(len(memory_list))
print(len(camera_list))

extras_links = href        

for i in range(len(st_list_heads)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-itel'+'.csv'), index=False, encoding='utf-8')
