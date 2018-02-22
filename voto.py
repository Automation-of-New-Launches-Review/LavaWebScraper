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

## THIS FILE IS A COMMON FORMAT FOR SCRAPING THE WEBSITES. DO NOT CHANGE THE VARIABLE NAMES ALREADY SPECIFIED IN THIS FILE.
## YOU MAY HOWEVER ADD YOUR OWN VARIABLES.

## FINAL LIST OF RESULTS SHOULD BE AVAILABLE IN A LIST 'RECORDS' NECESSARILY FOR THE SAKE OF CONSISTENCY.


path = 'E:\\LavaWebScraper\\BrandWiseFiles\\'


############## VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. ####################
base_url = 'http://www.votoglobal.com/product/test?m1=7&m2=8&m3=9'
country = 'CHINA'
company = 'VOTO'
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


heads=[]
dets=[]
href2=[]

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
s1 = soup.find_all('tr')
for i in range(len(s1)):
    s2 = s1[i].find('td', attrs={'class':'col-md-3 col-sm-4'})
    s4 = s1[i].find_all('td')
    heads.append(s2.text)
    l = len(s4)-1

for i in range(l):
    d=[]
    for j in range(len(s1)):
        s3 = s1[j].find_all('td', attrs={'class':'col-md-3 text-center'})
        d.append(s3[i].text)
    dets.append(d)

for i in range(len(dets)):
    c1 = 'Primary Camera : '
    c2 = 'Secondary Camera : '
    m1 = 'RAM : '
    m2 = 'ROM : '
    for j in range(len(heads)):
        if 'model no.' in heads[j].lower():
            model_list.append(dets[i][j])
        if 'RAM' in heads[j]:
            m1 = m1 + dets[i][j]
        if 'ROM' in heads[j]:
            m2 = m2 + dets[i][j]
        if 'screen size' in heads[j].lower():
            display_list.append(dets[i][j])
        if 'primary camera' in heads[j].lower():
            c1 = c1 + dets[i][j]
        if 'secondary camera' in heads[j].lower():
            c2 = c2 + dets[i][j]
        if 'battery' in heads[j].lower():
            battery_list.append(dets[i][j])
        if 'processor' in heads[j].lower():
            processor_list.append(dets[i][j])
    thickness_list.append('Not Available')
    usp.append('Not Available')
    extras_links.append('Not Available')
    if c1!='Primary Camera : ' and c2!='Secondary Camera : ':
        camera_list.append(c1 + ' || ' + c2)
    if m1!='RAM : ' and m2!='ROM : ':
        memory_list.append(m1 + ' ||  ' + m2)
    
########################### GETTING THE USPs ####################################################
url2 = 'http://www.votoglobal.com/'
r = requests.get(url2)
soup = BeautifulSoup(r.text, 'html.parser')
s1 = soup.find_all('ul', attrs={'class':'dropdown-menu'})
s2 = s1[0].find_all('a')
for s in s2:
    href2.append(s['href'])

extras_links = href2

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'voto-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
