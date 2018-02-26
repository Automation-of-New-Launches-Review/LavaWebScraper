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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import datetime

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'

base_url = 'http://www.intex.in/mobiles/smart-phones'
country = 'INDIA'
company = 'INTEX'
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

r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'productInner'})

for a in range(len(results)):
    href.append(results[a].find("a")["href"])

for a in range(len(href)):
    cc = ''
    mm = ''
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    print(href[a])
    try:
        s=requests.get(href[a]+'/specifications.html')
        soup=BeautifulSoup(s.text,'html.parser')
    except:
        print('LINK NOT VALID.')
    model=soup.find_all('section',attrs={'id':'main'})
    for i in range(len(model)):
        m=model[i].find('h1').text
        model_list.append(m[:-15])
    sp=soup.find_all('span',attrs={'class':'bignumber'})
    for m in range(len(sp)):
        thickness=sp[2].text
    thickness_list.append(thickness.strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' ')+' cm')
    
    sp3=soup.find_all('div',attrs={'class':'col-sm-8 col-xs-12'})
    for i in range(len(sp3)):
        D=sp3[i].find_all('li')
        display_list.append(str(D[0].text).strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' ') + ' || ' + str(D[1].text).strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' '))

    s9 = soup.find_all('div', attrs={'class':'col-sm-9 col-xs-12'})
    
    for s in s9:
        s11 = []
        s10 = s.find_all('li')
        for q in s10:
            try:
                s11.append(q.text)
            except:
                pass
        for j in range(len(s11)):
            if ('GHz' in s11[j] or 'Ghz' in s11[j]) and '\n' not in s11[j] and '<br>' not in s11[j] and '<br/>' not in s11[j] and 'Cortex' not in s11[j] and 'GPU' not in s11[j]:
                processor_list.append(s11[j].strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' '))
            if 'Capacity' in s11[j]:
                battery_list.append(s11[j].strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' '))
            if ('Rear' in s11[j] or 'Front' in s11[j]) and 'MP' in s11[j] and 'Pixel' not in s11[j] and 'Video' not in s11[j]:
                cc = cc + s11[j] + ' || ' 
            if ('RAM' in s11[j] or 'ROM' in s11[j]) and 'Feature' not in s11[j] and 'DDR' not in s11[j]:
                mm = mm +  s11[j] + ' || '


    if mm!='':
        memory_list.append(mm.strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' '))
    if cc!='':
        camera_list.append(cc.strip().strip('\n').replace(';',' ').replace('<br>', ' ').replace('<br/>', ' '))

    if len(processor_list)==a:
        processor_list.append('not available')
    if len(display_list)==a:
        display_list.append('not available')
    if len(battery_list)==a:
        battery_list.append('not available')
    if len(thickness_list)==a:
        thickness_list.append('not available')
    if len(memory_list)==a:
        memory_list.append('not available')
    if len(camera_list)==a:
        camera_list.append('not available')

    
   
                
print(len(model_list))
print(len(thickness_list))
print(len(display_list))
print(len(processor_list))
print(len(battery_list))
print(len(memory_list))
print(len(camera_list))
extras_links = href
for i in range(len(href)):
    usp.append('not available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-intex'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################

