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

############## VARIABLES NEEDED : DO NOT CHANGE THE VARIABLE NAMES. JUST FILL IN THEIR VALUES WHEREVER REQUIRED. ####################
base_url = 'https://www.samsung.com/us/mobile/phones/all-phones/s/_/n-10+11+hv1rp/'
country = 'SOUTH KOREA'
company = 'SAMSUNG/ U.S.'
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
href_specs = []
st_list_heads = []
st_list_dets = []


driver = webdriver.Firefox()
driver.get(base_url)
elem = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div')

######################### TRYING TO GRAB ALL THE MODELS AVAILABLE ######################################################
time.sleep(10)
elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[4]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/span[1]')
time.sleep(10)
y = 1
while elem:
    try:
        print('BUTTON FOUND.')
        elem.click()
        print('BUTTON CLICKED.')
        print('CLICK NO.: %d' %y)
        time.sleep(10)
        elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[4]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/span[1]')
    except:
        break
    y = y+1

########################################################################################################################

ll = []
try:
    s11 = elem.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[4]/div/div/div[2]/div/div/div[3]/div[1]')
except:
    print('DIV NOT FOUND')
try:
    s12 = s11.find_elements_by_class_name('ProductCard-root-3423567336')
except:
    print('SECTIONS NOT FOUND.')
    
x=1
for s in s12:
    print('MODEL NO.: %d' %x)
    try:
        s15 = s.find_elements_by_tag_name('a')
    except:
        print('ANCHOR TAGS NOT FOUND.')
    for q in s15:
        try:
            s16 = q.get_attribute('href')
        except:
            print('LINK NOT FOUND.')

        try:
            s18 = q.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[4]/div/div/div[2]/div/div/div[3]/div[1]/section['+str(x)+']/div[2]/div[2]/a[1]/section/p[2]').text            
        except:
            print('MODEL NAME NOT FOUND.')

        try:
            if 'trade-in' not in s16 and 'buy' not in s16 and 'reviews' not in s16 and 'upgrade' not in s16 and 'explore' not in s16:
                ll.append(s16)
        except:
            print('LINK WAS NOT FOUND.')
    x=x+1
    model_list.append(s18)

for m in model_list:
    print(m)

############ REMOVING REDUNDANCY IN LIST OF LINKS #############
for l in ll:
    if l in href:
        pass
    else:
        href.append(l)
###############################################################

########### ERRATIC PART ######################################

if len(href)!=len(model_list):
    print('WARNING:------------------------------------------------------------------------------------------------------------------------------')
    print('ERROR HERE.')
    it = len(href)
    model_list = model_list[:it]
###############################################################

######### FETCHING THE U.S.P.s ##############################
print('\n\n\n')
print('TOTAL NO. OF MODELS: %d' %len(href))
print('\n\n\n')

print('ALL LINKS FETCHED.')
for i in range(len(href)):
    st = ''
    print('------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('MODEL NO.: %d' %i)
    print(href[i])
    print(model_list[i])
    
    print('\n\n\n')
    try:
        r = requests.get(href[i])
        soup = BeautifulSoup(r.text, 'html.parser')
    except:
        print('LINK OF MODEL NOT VALID.')
    try:
        s2  = soup.find_all('div', attrs={'class':'grid'})
    except:
        print('DIV CLASS="GRID" NOT FOUND FOR THE MODEL.')
    try:
        s3 = s2[1].find_all('div', attrs={'class':'card__content-area'})
    except:
        print('DIV CLASS="card__content-area" NOT FOUND FOR THE MODEL.')
    for s in s3:
        try:
            s4 = s.find('p').text
            print(s4)
            try:
                st = st + ' || ' + s4.strip().strip('\n').replace('<br>', ' ').replace(';', ' ').replace('\n',' ')
            except:
                st = st + ' || ' + s4
        except:
            print('NO U.S.P. FOUND.')
    try:
        usp.append(st)
    except:
        print('NO OVERALL U.S.P.s AVAILABLE FOR THE MODEL.')
        usp.append('Not Available')
################################################################

############# FETCHING THE SPECS ###############################



for i in range(len(href)):
    href_specs.append(href[i] + '#specs')

for i in range(len(href_specs)):
    heads = []
    dets = []
    try:
        r = requests.get(href_specs[i])
        print('SUCCESSFUL HTTP REQUEST TO THE SPECS OF THE MODEL NO.: %d' %i)
        print('MODEL NAME: %s' %model_list[i])
        soup = BeautifulSoup(r.text, 'html.parser')
        print('SUCCESSUL PARSING OF HTML OF THE MODEL SEPCS.')
    except:
        print('LINK OF SPECS SECTION OF THE MODEL IS NOT VALID.')
    try:
        s9 =  soup.find('ul', attrs={'class':'row spec-details__list'}).find_all('div', attrs={'class':'sub-specs__item'})
    except:
        print('DIV CLASS="sub-specs__item" NOT FOUND.')
    for s in s9:
        try:
            s10 = s.find_all('p')
            heads.append(str(s10[0].text).strip().replace('\n',' ').replace(';',' '))
            dets.append(str(s10[1].text).strip().replace('\n',' ').replace(';',' '))
        except:
            print('ERROR IN FINDING HEADS/DETS.')
    st_list_heads.append(heads)
    st_list_dets.append(dets)


for i in range(len(st_list_heads)):
    print('---------------------------------------------------------------------------------------------------------------------')
    print('MODEL NO.: %d' %i)
    for j in range(len(st_list_heads[i])):
        print(st_list_heads[i][j], end=' : ')
        print(st_list_dets[i][j])



for i in range(len(st_list_heads)):
    d1 = ''
    d2 = ''
    c1 = ''
    c2 = ''
    for j in range(len(st_list_heads[i])):
        if 'Processor Speed, Type' in st_list_heads[i][j]:
            processor_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        if 'Internal Memory' in st_list_heads[i][j] or 'Internal memory' in st_list_heads[i][j]:
            memory_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        if 'Product Dimensions (inches)' in st_list_heads[i][j]:
            thickness_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        #if 'Battery Type and Size' in st_list_heads[i][j]:
            #battery_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        if 'mAh' in st_list_dets[i][j]:
            battery_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        #if 'Battery, Standby' in st_list_heads[i][j]:
            #battery_list.append(st_list_dets[i][j].strip().replace(';', ' ').strip('\n'))
        if 'Main Display Size' in st_list_heads[i][j]:
            d1 = st_list_dets[i][j].strip().replace(';', ' ').strip('\n')
        if 'Main Display Technology' in st_list_heads[i][j]:
            d2 = st_list_dets[i][j].strip().replace(';', ' ').strip('\n')
        if 'Camera resolution (Front)' in st_list_heads[i][j]:
            c1 = st_list_dets[i][j].strip().replace(';', ' ').strip('\n')
        if 'Camera resolution (Rear)' in st_list_heads[i][j]:
            c2 = st_list_dets[i][j].strip().replace(';', ' ').strip('\n')
    if d1!='' or d2!='':
        display_list.append(d1 + ' (INCHES) || ' + d2)
    if c1!='' or c2!='':
        camera_list.append(c1 + ' FRONT || ' + c2 + ' REAR')
    #if 'Processor Speed, Type' not in st_list_heads[i]:
        #processor_list.append('NA')
    #if 'Internal Memory' not in st_list_heads[i] and 'Internal memory' not in st_list_heads[i]:
        #memory_list.append('NA')
    #if 'Product Dimensions (inches)' not in st_list_heads[i]:
        #thickness_list.append('NA')
    #if 'Battery Type and Size' not in st_list_heads[i] and 'Battery, Standby' not in st_list_heads[i]:
        #battery_list.append('NA')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if c1=='' and c2=='':
        camera_list.append('Not Available')
    if d1=='' and d2=='':
        display_list.append('Not Available')

print('LENGTHS OF THE LISTS:', end='\n')
print(len(processor_list))
print(len(battery_list))
print(len(camera_list))
print(len(thickness_list))
print(len(display_list))
print(len(memory_list))



        
        

extras_links = href

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE NAME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'samsung_us-'+str(datetime.date.today())+'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################

