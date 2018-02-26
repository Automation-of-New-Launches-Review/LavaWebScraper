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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

import os
import datetime

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'

base_url = 'http://www.samsung.com/in/smartphones/all-smartphones/'
country = 'SOUTH KOREA'
company = 'SAMSUNG/INDIA'
mm = []
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

HREF = []
MODEL_LIST = []

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()


    def on_page_load(self):
        self.app.quit()

ll=[]
ll2=[]

driver = webdriver.Firefox()
driver.get(base_url)

elem = driver.find_element_by_link_text('View more')
while elem:
    try:
        print('BUTTON FOUND.')
        elem.click()
        print('BUTTON CLICKED.')
        elem = driver.find_element_by_link_text('View more')
    except:
        #elem.click()
        break

l1 = driver.find_elements_by_class_name('product-card-pdp-link')



####################################

i = 1
while True:
    try:
        driver.implicitly_wait(10)
        elem_match = driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[' + str(i) +']/div/div[3]/a')
        HREF.append(elem_match.get_attribute('href'))
        MODEL_LIST.append(elem_match.text)
    except:
        break
    i=i+1

href = HREF[:]
model_list = MODEL_LIST[:]

print(len(href))
print(len(model_list))

for i in range(len(href)):
    heads = []
    dets = []
    if 'galaxy-note8' in href[i] or 'galaxy-s8' in href[i]:
        href[i] = href[i] + 'spec-plus/'
        sp = i
    r1 = requests.get(href[i])
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    s1 = soup1.find_all('ul', attrs={'class':'product-specs__highlights-list'})
    if s1!=[]:    ##### FOR ALL EXCEPT GALAXY NOTE 8
        for s in s1:
            s2 = s.find_all('ul', attrs={'class':'product-specs__highlights-desc-list'})
            for q in s2:
                s3 = q.find_all('em', attrs={'class':'product-specs__highlights-sub-title'})
                s4 = q.find_all('span', attrs={'class':'product-specs__highlights-desc'})
                for t in s3:
                    heads.append(t.text.strip())
                for w in s4:
                    dets.append(w.text.strip())
        st_list_heads.append(heads)
        st_list_dets.append(dets)
    else:
        s1 = soup1.find('div', attrs={'class':'f_content-table'}).find_all('div', attrs={'class':'f_table-row'})
        for s in s1:
            s2 = s.find('div', attrs={'class':'f_table-td'}).find_all('li')
            for q in s2:
                s3 = q.find_all('div')
                heads.append(s3[0])
                dets.append(s3[1])
        st_list_heads.append(heads)
        st_list_dets.append(dets)



for i in range(len(st_list_heads)):
    c1 = ''
    c2 = ''
    m1 = ''
    m2 = ''
    p1 = ''
    p2 = ''
    d1 = ''
    d2 = ''
    d3 = ''
    for j in range(len(st_list_heads[i])):
        if 'Standard Battery Capacity' in st_list_heads[i][j]:
            battery_list.append(st_list_dets[i][j] + ' mAh')
        if 'Main Camera - Resolution' in st_list_heads[i][j]:
            c1 = 'Main Camera : ' + st_list_dets[i][j] + ' ||'
        if 'Front Camera - Resolution' in st_list_heads[i][j]:
            c2 = 'Front Camera : ' + st_list_dets[i][j] + ' ||'
        if 'RAM_Size' in st_list_heads[i][j] or 'RAM Size' in st_list_heads[i][j]:
            m1 = 'RAM : ' + st_list_dets[i][j] + ' ||'
        if 'ROM_Size' in st_list_heads[i][j] or 'ROM Size' in st_list_heads[i][j]:
            m2 = 'ROM : ' + st_list_dets[i][j] + ' ||'
        if 'CPU Speed' in st_list_heads[i][j]:
            p1 = st_list_dets[i][j]
        if 'CPU Type' in st_list_heads[i][j]:
            p2 = st_list_dets[i][j]
        if 'Size (Main Display)' in st_list_heads[i][j]:
            d1 = 'Display Size : ' + st_list_dets[i][j] + ' ||'
        if 'Resolution (Main Display)' in st_list_heads[i][j]:
            d2 = 'Main Display Resolution : ' +  st_list_dets[i][j] + ' ||'
        if 'Technology (Main Display)' in st_list_heads[i][j]:
            d3 = 'Main Display Technology : ' + st_list_dets[i][j] + ' ||'
        if 'Dimension (HxWxD, mm)' in st_list_heads[i][j]:
            s = st_list_dets[i][j]
            match = re.search(r'x\s\d\.\d', s)
            if match:
                thickness_list.append(match.group())
            else:
                thickness_list.append('not available')
    if c1!='' or c2!='':
        camera_list.append(c1 + ' ' + c2)
    if m1!='' or m2!='':
        memory_list.append(m1 + ' ' +m2)
    if p1!='' or p2!='':
        processor_list.append(p1 + ' ' + p2)
    if d1!='' or d2!='' or d3!='':
        display_list.append(d1 + ' ' + d2 + ' ' + d3)
    if len(processor_list)==i:
        processor_list.append('not available')
    if len(memory_list)==i:
        memory_list.append('not available')
    if len(thickness_list)==i:
        thickness_list.append('not available')
    if len(display_list)==i:
        display_list.append('not available')
    if len(camera_list)==i:
        camera_list.append('not available')
    if len(battery_list)==i:
        battery_list.append('not available')

for i in range(len(display_list)):
    usp.append('not available')
    

print(len(display_list))
print(len(battery_list))
print(len(memory_list))
print(len(processor_list))
print(len(thickness_list))
print(len(camera_list), end='\n')
print(len(model_list))
print('LEN of href:', end='')
print(len(href))

for m in model_list:
    print(m)

extras_links = href

#####################################################################

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-samsung'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
