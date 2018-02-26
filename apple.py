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
base_url = 'https://www.apple.com/iphone/'
country = 'USA'
company = 'APPLE'
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
ur = 'https://www.apple.com'
hr_specs = []   #LIST CONTAINING THE URLs OF THE SPECIFICATION PAGES OF ALL THE MODELS.
# num_models_page :  NO. OF MODELS ON EACH SPECS PAGE.


####################################################################################################################################
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
s1 = soup.find('ul', attrs={'class':'chapternav-items'}).find_all('li')
for q in s1:
    s3 = q.find('a')
    if 'compare' not in s3['href'] and 'accessories' not in s3['href'] and 'ios' not in s3['href']:
        href.append(ur + s3['href'])
        #model_list.append(s3.text.strip().strip('\n').replace('\n', ' ').replace('<br>', ' '))

for i in range(len(href)):
    r1 = requests.get(href[i])
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    s4 = soup1.find_all('a')
    for s in s4:
        if 'Tech Specs' in s.text:
            if ur not in s['href']:
                hr_specs.append(ur + s['href'].strip().strip('\n'))
            else:
                hr_specs.append(s['href'].strip().strip('\n'))

x = 0 # TOTAL NO. OF MODELS.
href = []
for i in range(len(hr_specs)):
    c = 0
    rowheader_list = []
    r2 = requests.get(hr_specs[i])
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    s9 = soup2.find_all('div', attrs={'role':'columnheader'})
    num_models_page = len(s9)-1 ## THE FIRST SUCH DIV IS NOT TO BE COUNTED, SO DOING "len(s9)-1."
    x = x + num_models_page
    for j in range(1,len(s9)):
        model_list.append(s9[j].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' '))
        href.append(hr_specs[i])
    for c in range(num_models_page):
        tcam = ''
        s10 = soup2.find_all('div', attrs={'role':'rowgroup'})
        for h in range(len(s10)):
            t11 = s10[h].find('div', attrs={'role':'rowheader'}).text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' ')
            rowheader_list.append(t11)
            s11 = s10[h].find_all('div', attrs={'role':'cell gridcell'})
            if len(s11)>=num_models_page:
                s12 = s11[c].find_all('li')
                if 'Display' in t11:
                    display_list.append(s12[0].text + ' || ' + s12[1].text)
                if 'Size and Weight' in t11:
                    s13 = s11[c].find('figure').find('p', attrs={'class':'diagram-text diagram-text-3'})
                    if s13 is None:
                        s13 = s11[c].find('figure').find('p', attrs={'class':'diagram-text diagram-text-depth'})
                    thickness_list.append(s13.text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' '))
                    
            if 'Chip' in t11:
                s12 = s11[0].find_all('li')
                ts = ''
                n=0
                while n<len(s12):
                    ts = ts + ' || ' + str(s12[n].text)
                    n = n + 1
                processor_list.append(ts)

            if 'Camera' in t11:
                s12 = s11[0].find_all('li')
                try:
                    tcam = tcam + t11 + ' : ' + str(s12[0].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' ')) + ' || '
                except:
                    tcam = tcam + t11 + ' : ' + str(s11[0].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' ')) + ' || '

            if 'Capacity' in t11:
                
                try:
                    s14 = s11[0].find_all('li')
                    memory_list.append('Storage Capacity : ' + s14[0].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' ') + ' OR ' + s14[1].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' '))
                except:
                    s14 = s11[0].find('table').find_all('tr')                    
                    memory_list.append('Storage Capacity : ' + s14[0].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' ') + ' OR ' + s14[1].text.strip().strip('\n').replace('<br>', ' ').replace('&nbsp', ' ').replace('\n', ' '))
                
        camera_list.append(tcam)
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


for i in range(len(model_list)):
    battery_list.append('Not Available')
    usp.append('Not Available')
            
            
        
                
                    
                
print(len(display_list))
print(len(processor_list))
print(len(battery_list))            
print(len(camera_list))
           
print(len(thickness_list))
           
print(len(memory_list))

            
            
        
extras_links = href       

    



############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today()) + '-apple' + '.csv'), index=False, encoding='utf-8-sig')
#####################################################################################################################################
