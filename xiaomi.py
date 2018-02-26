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
base_url = 'https://xiaomi-mi.com/mi-smartphones/'
ur = 'https://xiaomi-mi.com'
country = 'CHINA'
company = 'XIAOMI'
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
####################################################################################################################################

################ DECLARE HERE THE EXTRA VARIABLES NEEDED ###########################################################################
ii = []
shref = []


####################################################################################################################################

try:
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'html.parser')
except:
    print('ERROR : BASE URL OF THE WEBSITE IS INVALID/DOWN.')

s1 = soup.find('div', class_='content').find_all('div', class_='item-title')
for s in s1:
    href.append(ur + s.find('a')['href'])
    model_list.append(s.text.strip().strip('\n'))

for i in range(len(model_list)):
    if 'Accessories' in model_list[i]:
        ii.append(i)

### REMOVING THE LINKS OF ACCESSORIES ###
x=0
while x<len(model_list):
    if x in ii:
        model_list.pop(x)
        href.pop(x)
    x = x + 1

model_list = []
########################################

for i in range(len(href)):
    print('MAIN MODEL NO.: %d' %i)
    r = requests.get(href[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    s3 = soup.find_all('div', class_='item-title')
    for s in s3:
        #model_list.append(s.text.strip().strip('\n'))
        ts = s.find('a')['href']
        if 'http' not in ts:
            ts = ur + ts
        if 'https://nis-store.com' not in s.find('a')['href']:
            shref.append(ts)
            model_list.append(s.find('a').text.strip().strip('\n'))
    print('---------------------------------------------------------------------------------------------------------------')

href = shref[:]

print(len(href))

for i in range(len(href)):
    dd = ''
    pp = ''
    mm = ''
    cc = ''
    print(href[i])
    heads = []
    dets = []
    print('SUB MODEL NO.: %d' %i)
    r = requests.get(href[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        usp_text = soup.find('div', class_='content-text').find('p').text
        usp.append(usp_text.strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' '))
    except:
        usp.append('Not Available')
    try:   ### LEAVING OUT THE MODELS 
        s4 = soup.find('table').find_all('tr')
        for j in range(len(s4)):
            s5 = s4[j].find_all('td')
            heads.append(s5[0].text.strip().strip('\n'))
            dets.append(s5[1].text.strip().strip('\n'))

        for j in range(len(heads)):
            if 'dimensions' in heads[j].lower():
                thickness_list.append(dets[j].strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' '))
            if 'display type' in heads[j].lower() or 'size' in heads[j].lower():
                dd = dd + dets[j].strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
            if 'chipset' in heads[j].lower():
                pp = pp + dets[j].strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
            if 'RAM' in heads[j]:
                mm = mm + 'RAM : ' + dets[j].strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
            if 'memory' in heads[j].lower():
                mm = mm + 'ROM : ' + dets[j].strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
            if 'primary camera' in heads[j].lower() or 'Primary&nbsp;camera' in heads[j]:
                match = re.search(r'\d+\.*\d*\s*MP', dets[j])
                try:
                    st = str(match.group())
                    cc = cc + 'Primary Camera : ' + st.strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
                except:
                    pass

            if 'secondary camera' in heads[j].lower() or 'Secondary&nbsp;camera' in heads[j]:
                match = re.search(r'\d+\.*\d*\s*MP', dets[j])
                try:
                    st = str(match.group())
                    cc = cc + 'Secondary Camera : ' + st.strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' ') + ' || '
                except:
                    pass
                
            if 'battery' in heads[j].lower():
                match = re.search(r'\d+\s*mAh', dets[j])
                try:
                    st = str(match.group())
                except:
                    st = 'Not Available'
                battery_list.append(st.strip().strip('\n').replace('<br>', '').replace('\n', ' ').replace(';', ' '))
        if dd!='':
            display_list.append(dd)
        if pp!='':
            processor_list.append(pp)
        if mm!='':
            memory_list.append(mm)
        if cc!='':
            camera_list.append(cc)
    except:
        print('NO SPECS FOR THIS MODEL AVAILABLE.')
        pass
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
    
print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))
print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))
print('LENGTH OF DISPLAY LIST: %d' %len(display_list))
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))
extras_links =  href


############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-xiaomi'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
