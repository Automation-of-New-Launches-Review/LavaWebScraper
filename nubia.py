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

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()


    def on_page_load(self):
        self.app.quit()



base_url = 'https://www.nubia.com/in/'
url = base_url
client_response = Client(url)
source = client_response.mainFrame().toHtml()

country = 'CHINA'
company = 'NUBIA'
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
ST_LIST_DETS=[]

hr=[]
HREF=[]
spec_url=[]
r=requests.get(base_url)
soup = bs.BeautifulSoup(source, 'lxml')
results=soup.find_all('li',attrs={'class':'product'})

for i in range(len(results)):
    sa=results[i].find_all('div',attrs={'class':'container'})
    for a in range(len(sa)):
        sb=sa[a].find_all('li')
        for b in range(len(sb)):
            href.append(sb[b].find('a')['href'])
            model_list.append(sb[b].find('span').text)
HREF=href[:]
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'nav navbar-nav navbar-right'})
    for a in range(len(results)):
        sa=results[a].find_all('li')
        for b in range(len(sa)):
            if 'spec' in sa[b].text.lower():
                hr.append(sa[b].find('a')['href'])

for i in range(len(href)):
    if href[i].endswith('index.html'):
        href[i]=href[i][:-10]
    href[i]=href[i]+hr[i]


# href : Links of specifications pages.
# HREF : Links of model main pages.

for i in range(len(href)):
    heads=[]
    dets=[]
    print('MODEL NO.: %d' %(i+1))
    r=requests.get(href[i])
    soup5=BeautifulSoup(r.text,'html5lib')
    results=soup5.find('div',attrs={'class':'col-md-9'})
    s2 = results.find_all('section',attrs={'style':'padding-bottom: 140px; padding-top:  100px;border-top: 1px solid #eee;'})
    for b in range(len(s2)):
        sa = s2[b].find('div',attrs={'class':'row'})
        heads.append(sa.find('h3').text)
        section_text = sa.text.strip().strip('\n')
        dets.append(section_text.replace('\t', '').replace('\n', ' '))
    for j in range(len(heads)):
        if 'camera' in heads[j].lower():
            st = ''
            match1 = re.search(r'Rear Camera\s+\d+MP', dets[j])
            try:
                st = st + str(match1.group()) + ' || '
            except:
                st = st + 'Rear Camera : Not Available' + ' || '
            match2 = re.search(r'Front Camera\s+\d+MP', dets[j])
            try:
                st = st + str(match2.group())
            except:
                st = st + 'Front Camera : Not Available'
            if st!='':
                camera_list.append(st)
        if 'display' in heads[j].lower() or 'screen' in heads[j].lower():
            match1 = re.search(r'Size.+Resolution', dets[j])
            match2 = re.search(r'Display technology.+Manufacturing', dets[j])
            try:
                st = str(match1.group()) + ' || ' + str(match2.group())
                st = st.replace('Resolution', '').replace('Manufacturing', '').replace(';', '')
            except:
                st = 'Not Available'
            if st!='':
                display_list.append(st)
        if 'processor' in heads[j].lower():
            if dets[j]!='':
                processor_list.append(dets[j].replace(';', ''))
        if 'RAM' in heads[j]:
            if dets[j]!='':
                memory_list.append(dets[j])
        if 'battery' in heads[j].lower():
            match = re.search(r'\d+\s*mAh', dets[j].replace(';', ''))
            try:
                st = str(match.group())
            except:
                st = 'Not Available'
            if st!='':
                battery_list.append(st)
    thickness_list.append('Not Available')
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
for i in range(len(href)):
    usp.append('Not Available')

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'nubia-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################


           
