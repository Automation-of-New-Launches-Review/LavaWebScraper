import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import datetime
import os

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'

############################## VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. ######################################
base_url = 'https://www3.lenovo.com/in/en/smartphones/c/smartphones?menu-id=Smartphones'
country = 'CHINA'
company = 'LENOVO/ INDIA'
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
#######################################################################################################################################################################

url_list=[]
a2=[]
specs=[]
records=[]
usp_links=[]
usp_list=[]


r=requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0'})

soup=BeautifulSoup(r.content, 'html.parser')

try:
    s1=soup.find_all('ul', attrs={'class':'sidebarNav-list-b subSeries'})
    l1=soup.find_all('ul', attrs={'class':'sidebarNav-list first'})
except:
    print('NAVIGATION DIV NOT FOUND.')

####USP COLLECTION
try:
    for l in l1:
        l2=l.find('a')['href']
        usp_links.append('https://www3.lenovo.com' + l2)
except:
    print('ERROR IN USP COLLECTION.')

for i in range(len(usp_links)):
    r9=requests.get(usp_links[i], headers={'User-Agent': 'Mozilla/5.0'})
    soup9=BeautifulSoup(r9.text, 'html.parser')

    ##FINDING THE LINKS FROM HERE ITSELF.
    s11 = soup9.find_all('h3', attrs={'class':'seriesListings-title'})
    for j in range(len(s11)):
        try:
            href.append('https://www3.lenovo.com' + s11[j].find('a')['href'])
            model_list.append(s11[j].find('a').text)
        except:
            pass
        
        
    
    s9=soup9.find_all('div', attrs={'class':'seriesListings-description'})
    for s in s9:
        tst=''
        s10=s.find_all('li')
        for u in s10:
            tst += (u.text + ' || ')
        if tst=='':
            tst += (s.text)
        usp_list.append(tst)

for u in usp_list:
    if u in usp:
        pass
    else:
        usp.append(u)

for i in range(len(href)):
    heads = []
    dets = []
    st=''
    print(href[i])
    r1=requests.get(href[i], headers={'User-Agent': 'Mozilla/5.0'})
    soup1=BeautifulSoup(r1.content, 'html.parser')
    s2=soup1.find_all('table', attrs={'class':'techSpecs-table'})
    for s in s2:
        s3=s.find_all('tr')
        for q in range(len(s3)):
            s4=s3[q].find_all('td')
            if q != 0:
                heads.append(s4[0].text)
                dets.append(s4[1].text)
    st_list_heads.append(heads)
    st_list_dets.append(dets)

for i in range(len(st_list_heads)):
    cc = ''
    for j in range(len(st_list_heads[i])):
        if 'display' in st_list_heads[i][j].lower():
            display_list.append(st_list_dets[i][j])
        if 'processor' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
        if 'mah' in st_list_dets[i][j].lower():
            match = re.search('\d+\s*mAh', st_list_dets[i][j])
            if match:
                ts = str(match.group())
            else:
                ts = 'Not Available'
            battery_list.append(ts)
        if 'dimensions' in st_list_heads[i][j].lower() and 'dimensions (inches)' not in st_list_heads[i][j].lower():
            thickness_list.append(st_list_dets[i][j])
        if 'camera' in st_list_heads[i][j].lower():
            cc = cc + st_list_dets[i][j] + ' || '
        if 'memory' in st_list_heads[i][j].lower():
            memory_list.append(st_list_dets[i][j])
    if cc!='':
        camera_list.append(cc)
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')

print('LENGTH OF PROCESSOR LIST: %d' %len(processor_list))
print('LENGTH OF DISPLAY LIST: %d' %len(display_list))
print('LENGTH OF BATTERY LIST: %d' %len(battery_list))
print('LENGTH OF THICKNESS LIST: %d' %len(thickness_list))
print('LENGTH OF CAMERA LIST: %d' %len(camera_list))
print('LENGTH OF MEMORY LIST: %d' %len(memory_list))

extras_links = href

########################## WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ########################################################
try:
    for i in range(len(model_list)):
        records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

    df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
    df.to_csv(os.path.join(path_of_brandwise, 'lenovo-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
except:
    print('LENGTHS OF LISTS NOT EQUAL: FAILED TO CREATE C.S.V. FILE.')
#######################################################################################################################################################################
    




