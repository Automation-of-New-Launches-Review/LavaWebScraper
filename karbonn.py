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

############## VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. ####################
base_url = 'http://www.karbonnmobiles.com/smart-phones'
country = 'INDIA'
company = 'KARBONN'
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
specs_list = []
####################################################################################################################################



r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('h3',attrs={'class':'product_name'})


for i in range(len(results)):
    href.append('http://www.karbonnmobiles.com' + results[i].find('a')['href'])
    model_list.append(results[i].find('a').text)
specs=soup.find_all('div', attrs={'class':'product_info'})
for i in range(len(specs)):
    spec=specs[i].find('p')
    sp_list = []
    sp = spec.text
    spp = sp.split('\n')
    for s in spp:
        sp_list.append(s.replace('<br>',' ').replace('\n', ' ').replace('\r',' ').strip().strip('\n'))
    specs_list.append(sp_list)

for i in range(len(specs_list)):
    cc = ''
    for j in range(len(specs_list[i])):
        if 'Processor' in specs_list[i][j]:
            processor_list.append(specs_list[i][j])
        if 'Display' in specs_list[i][j]:
            display_list.append(specs_list[i][j])
        if 'Battery' in specs_list[i][j] or 'battery' in specs_list[i][j]:
            battery_list.append(specs_list[i][j])
        if 'camera' in specs_list[i][j] or 'Camera' in specs_list[i][j]:
            cc = cc + specs_list[i][j] + ' || '
    if cc!='':
        camera_list.append(cc)
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    thickness_list.append('Not Available')
    memory_list.append('Not Available')

print(len(processor_list))
print(len(display_list))
print(len(battery_list))
print(len(camera_list))
print(len(thickness_list))
print(len(memory_list))
    


extras_links = href
for i in range(len(href)):
    usp.append('Not Available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+ '-karbonn' +'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
