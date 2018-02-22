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
import datetime
import os


path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'

base_url = 'http://www.meiigoo.com/article_list_89.html'
ur='http://www.meiigoo.com'
country = 'CHINA'
company = 'Meiigoo'
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
HEADS = []
DETS = []
wholetext = []
details = []

r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'mian_content clearfix'})
for a in range(len(results)):
    sa=results[a].find_all('ul',attrs={'class':'product phone'})
    for b in range(len(sa)):
        sb=sa[b].find_all('li')
        for c in range(len(sb)):
            href.append(sb[c].find('a')['href'])
            model_list.append(sb[c].text.strip())
print(href)
print(model_list)
for i in range(len(href)):
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
    print('MODEL NO.: %d' %(i+1))
    heads=[]
    href[i]=ur + href[i]
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    result=soup.find('li',attrs={'id':'tab_con_2'})
    wholetext.append(result.text.strip().strip('\n').replace('\n', '').replace('\xa0', ' '))
    for i in range(len(wholetext)):
        childw = wholetext[i].split('●')
    details.append(childw)
        


for i in range(len(details)):
    for j in range(len(details[i])):
        if 'Display' in details[i][j] and 'Main Features' not in details[i][j]:
            display_list.append(details[i][j])
        if 'CPU' in details[i][j] and 'Main Features' not in details[i][j]:
            processor_list.append(details[i][j])
        if 'RAM + ROM' in details[i][j] and 'Main Features' not in details[i][j]:
            memory_list.append(details[i][j])
        if 'Camera' in details[i][j] and 'Main Features' not in details[i][j]:
            camera_list.append(details[i][j])
    battery_list.append('Not Available')
    thickness_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')

print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LENGTH OF DISPLAY LIST: %d' %len(display_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))

print('----------------------------------------------------------------------------------------------------------------------------------------------------------')

extras_links =  href
for i in range(len(href)):
    usp.append('Not Available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'meiigo-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################


