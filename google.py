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
path_of_brandwise  = 'C:\\LavaWebScraper\\BrandWiseFiles\\'


base_url = 'https://store.google.com/category/phones'
ur='https://store.google.com'
country = 'USA'
company = 'GOOGLE'
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
slink=[]
href_specs = []

r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('a',attrs={'class':'mqn-abf mqn-abk mqn-abr'})
for i in range(len(results)):
    hr.append(results[i]['href'])


for i in range(len(hr)):
    href.append(ur + hr[i])

for i in range(len(href)):
    print(href[i])
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results1=soup.find_all('div',attrs={'jsname':'r4nke'})
    for a in range(len(results1)):
        sa=results1[a].find_all('h1',attrs={'class':'title-text header-text-3'})
        for b in range(len(sa)):
            model_list.append(sa[b].text.strip())

    sb = soup.find_all('a', attrs={'class':'subpage-link'})
    for s in sb:
        if s.text == 'Tech Specs':
            href_specs.append(ur + s['href'])
        else:
            pass

for i in range(len(href_specs)):
    print('MODEL NO.: %d' %i)
    heads = []
    dets = []
    r3 = requests.get(href_specs[i])
    soup3 = BeautifulSoup(r3.text, 'html.parser')
    s9 = soup3.find_all('div', attrs={'class':'row-2017'})
    for q in s9:
        s10 = q.find_all('div')
        if s10[0].text=='Tech specs':
            s11 = s10[1].find_all('div', attrs={'class':'accordion-category'})
            for s in s11:
                s13 = s.find('div').find_all('div')
                heads.append(s13[0].text.strip())
                dets.append(s13[1].text.strip())
    for j in range(len(heads)):
        if 'Display' in heads[j]:
            display_list.append(dets[j])
        if 'Processors' in heads[j]:
            processor_list.append(dets[j])
        if 'Cameras' in heads[j]:
            camera_list.append(dets[j])
        if 'Memory and storage' in heads[j]:
            memory_list.append(dets[j])
        if 'Battery' in heads[j]:
            battery_list.append(dets[j])
    thickness_list.append('Not Available')
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

print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))
print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))
print('LENGTH OF DISPLAY LIST: %d' %len(display_list))
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))

extras_links =  href
for i in range(len(href)):
    usp.append('Not Available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'google-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
            
            
            
    
    
