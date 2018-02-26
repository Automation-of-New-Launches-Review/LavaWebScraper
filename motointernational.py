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

####################### VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. #############################################
base_url = 'https://www.motorola.com/us/products/moto-smartphones'
country = 'CHINA'
company = 'MOTO/U.S.'
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
#######################################################################################################################################################################
urls1=[]
urls=[]
specs=[]
detail=[]
mod=[]
wholetext=[]

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')   
link=soup.find_all('div',attrs={'class':'field-item even'})
md=soup.find_all('div',attrs={'class':'field field-name-field-ppkg-product-subtitle field-type-text field-label-hidden'})

for x in link:
    
    tt=x.find_all('a')
    for k in tt:
        urls1.append(k['href'])

for zx in range(len(urls1)-2):
    urls.append(urls1[zx])  
href = urls   #URLs SCRAPED OUT.

for sc in md:
    model_list.append(sc.text.replace('⁴','4').replace('³', '3').replace('⁵','5').replace('²','2').replace('⁵ˢ','5S'))  #MODEL NAMES SCRAPED OUT.

########################################################################################################################################################################
for i in range(len(href)):
    usp_string = ''
    r = requests.get(href[i])
    soup = BeautifulSoup(r.text, 'html5lib')
    s1 = soup.find_all('div',attrs={'class':'field field-name-field-specifications-summary-lft field-type-text-long field-label-hidden'})
    s2 = soup.find_all('div',attrs={'class':'field field-name-field-specifications-summary-rgt field-type-text-long field-label-hidden'})
    for s in s1:
        s3 = s.find_all('h5')
        for q in s3:
            usp_string = usp_string + q.text.strip().replace('\n', ' ').replace('<br>', ' ').strip('\n').replace('\t', ' ') + ' || '
    if usp_string!='':
        usp.append(usp_string)  #USPs SCRAPED OUT.
    else:
        usp.append('Not Available')
    try:
        sdiv = soup.find('div', attrs={'class':'specifications-details-text-wrapper col-xs-12 col-sm-8'})
        s9 = sdiv.find('div', attrs={'class':'field field-name-field-specifications-full-lft field-type-text-long field-label-hidden'}).find('div', attrs={'class':'field-items'}).find('div', attrs={'class':'field-item even'})
        s10 = sdiv.find('div', attrs={'class':'field field-name-field-specifications-full-rgt field-type-text-long field-label-hidden'}).find('div', attrs={'class':'field-items'}).find('div', attrs={'class':'field-item even'})
        wholetext.append(str(s9) + ' || ' + str(s10))
    except:
        wholetext.append('Not Available')


#print(len(wholetext))
i = 0
for w in wholetext:
    mm = ''
    cc = ''
    w = w[29:-7].replace('<div class="field-item even">', '').replace('</div>', '')
    childw = w.split('<h5>')
    #print(childw)
    for j in range(len(childw)):
        if 'system architecture/processor' in childw[j].lower() or 'System architecture/Processor' in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')
            processor_list.append(st.replace('<br/>', ' ').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', ''))

        if 'Memory (RAM)' in childw[j] or 'memory (RAM)' in childw[j] or 'Storage (ROM)' in childw[j] or 'storage (ROM)' in childw[j] or 'Storage' in childw[j] or 'storage' in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')
            if 'GB' in st:
                mm = mm + st.replace('<br/>', ' ').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', '') + ' || '
            while True:
                match = re.search(r'<span.+/span>', mm)
                if match:
                    mm = mm.replace(str(match.group()), ' ')
                else:
                    break

        if 'Dimensions' in childw[j] or 'dimensions' in childw[j] or 'Dimension' in childw[j] or 'dimension' in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')

            match0 = re.search(r'\d?\.\d+\s*mm', st)
            try:
                st = str(match0.group())
            except:
                st = 'Not Available'
            while True:
                match = re.search(r'<span.+/span>', st)
                if match:
                    st = st.replace(str(match.group()), ' ')
                else:
                    break
            thickness_list.append(st.replace('<br/>', ' ').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', ''))

        if ('"' in childw[j] or 'ppi' in childw[j]) and ('Display' in childw[j] or 'display' in childw[j]) and ('href' not in childw[j] and 'moto' not in childw[j].lower()) and 'MP' not in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')
            while True:
                match = re.search(r'<span.+/span>', st)
                if match:
                    st = st.replace(str(match.group()), ' ')
                else:
                    break
            display_list.append(st.replace('<br/>', ' ').replace('”','"').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', ''))

        if 'Battery' in childw[j] or 'battery' in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')
            match0 = re.search(r'\d+\s*mAh', st)
            try:
                st = str(match0.group())
            except:
                st = 'Not Available'
            while True:
                match = re.search(r'<span.+/span>', st)
                if match:
                    st = st.replace(str(match.group()), ' ')
                else:
                    break
            battery_list.append(st.replace('<br/>', ' ').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', ''))

        if 'Rear Camera' in childw[j] or 'Front Camera' in childw[j] or 'Rear camera' in childw[j] or 'Front camera' in childw[j] or 'rear camera' in childw[j] or 'front camera' in childw[j]:
            st = find_between(childw[j], '<p>', '</p>')
            if st=='':
                st = find_between(childw[j], '<p class="p1">', '</p>')
            match0 = re.search(r'\d+\s*MP', st)
            try:
                st = str(match0.group())
            except:
                st = 'Not Available'
            cc = cc + st.replace('<br/>', ' ').replace('<br>', ' ').replace('<sup>', ' ').replace('</sup>', ' ').replace('\n', ' ').replace('<em>', '').replace('</em>', '') + ' || '
            while True:
                match = re.search(r'<span.+/span>', cc)
                if match:
                    cc = cc.replace(str(match.group()), ' ')
                else:
                    break
            

    if mm!='':
        memory_list.append('RAM / ROM : ' + mm)
    if cc!='':
        camera_list.append('Rear / Front : ' + cc)
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')




    i = i + 1
print(len(thickness_list))
print(len(camera_list))
print(len(display_list))


    
    
extras_links = href
############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-motorola'+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################
