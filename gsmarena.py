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
import time
import random
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#path_of_url_file = 'C:\\Users\\rakshit sharma\\Desktop\\'

path_of_reference_files = 'C:\\LavaWebScraper\\GSMARENA\\GSMarena_complete\\reference_files\\'
path_of_gsmarena_complete_csv = 'C:\\LavaWebScraper\\GSMARENA\\GSMarena_complete\\'

user_agent = {'User-agent':'Mozilla/5.0'}
base_url = 'https://www.gsmarena.com/makers.php3'
ur='https://www.gsmarena.com/'
##country = 'TAIWAN'
##company = 'hTC'
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
HREF=[]
BRANDS=[]
device_num=[]
price_list=[]
launch_date_list=[]
company_name_list=[]
devnum=[]

######################################################## PARAMETERS READ FROM THE FILES ##############################################################################
href_file = []
usp_file = []
company_name_list_file = []
model_list_file = []



with open(os.path.join(path_of_reference_files, 'gsmarena_href.txt'), 'r') as f:
    href_file = f.readlines()

with open(os.path.join(path_of_reference_files, 'gsmarena_usp.txt'), 'r') as f:
    usp_file = f.readlines()

with open(os.path.join(path_of_reference_files, 'gsmarena_modelnames.txt'), 'r') as f:
    model_list_file = f.readlines()

with open(os.path.join(path_of_reference_files, 'gsmarena_company_name_list.txt'), 'r') as f:
    company_name_list_file = f.readlines()

for i in range(len(href_file)):
    href_file[i] = href_file[i].replace('\n','')
    model_list_file[i] = model_list_file[i].replace('\n','')
    usp_file[i] = usp_file[i].replace('\n','')
    company_name_list_file[i] = company_name_list_file[i].replace('\n','')

######################################################################################################################################################################

#PAGES=[]
#r=requests.get(base_url, headers=user_agent)

http = urllib3.PoolManager()

#####################################
response = http.request('GET', base_url)
soup = BeautifulSoup(response.data, 'html.parser')

#####################################
results=soup.find_all('div',attrs={'class':'st-text'})
#print(len(results))
for a in range(len(results)):
    sa=results[a].find_all('table')
    #print(len(sa))
    for b in range(len(sa)):
        sb=sa[b].find_all('tr')
        #print(len(sb))
        for c in range(len(sb)):
            sc=sb[c].find_all('td')
            for d in range(len(sc)):
                HREF.append(sc[d].find('a')['href'])
                sd=sc[d].find('a')
                BRANDS.append(sd.contents[0])
                device_num.append(sd.contents[2].text)
#print(len(HREF))
for i in range(len(HREF)):
    HREF[i]=ur+HREF[i]
print('------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in range(len(BRANDS)):
    print(BRANDS[i])
print('------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in device_num:
    print(i)
    #print(HREF[i])
print(len(BRANDS))
print(len(device_num))
for a in range(len(HREF)):
    
    PAGES=[]
    print('9')
    #r=requests.get(HREF[a])
    r = http.request('GET', HREF[a])
    soup = BeautifulSoup(r.data, 'html.parser')
    results=soup.find_all('div',attrs={'class':'nav-pages'})
    print(BRANDS[a])
    print(device_num[a])
    print(len(results))
    
    PAGES.append(HREF[a])
    if len(results)!=0:
        for b in range(len(results)):
            sa=results[b].find_all('a')
            for c in range(len(sa)):
                t=ur +sa[c]['href']
                PAGES.append(t)
    print('No.of pages are:- ',end='')
    print(len(PAGES))
    for i in PAGES:
        print(i)
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(PAGES)):
        #r1=requests.get(PAGES[i])
        r1 = http.request('GET', PAGES[i])
        soup = BeautifulSoup(r1.data, 'html.parser')
        results1=soup.find_all('div',attrs={'class':'makers'})
        for d in range(len(results1)):
            sb=results1[d].find_all('ul')
            for e in range(len(sb)):
                sc=sb[e].find_all('li')
                for f in range(len(sc)):
                    ts = ur + sc[f].find('a')['href']
                    if ts not in href_file:
                        href.append(sc[f].find('a')['href'])
                    if sc[f].find('img')['title'].replace('″','"') not in usp_file:
                        usp.append(sc[f].find('img')['title'].replace('″','"'))
                    if sc[f].find('strong').text.strip() not in model_list_file:
                        model_list.append(sc[f].find('strong').text.strip())
                    if BRANDS[a] not in company_name_list_file:
                        company_name_list.append(BRANDS[a])

print('length of href is:- ',end='')
print(len(href))
for i in range(len(href)):
    href[i]=ur+href[i]
##    print(href[i])
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print('length of usp is:- ',end='')
print(len(usp))
for i in usp:
    print(i)
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print('length of model_list is:- ',end='')
print(len(model_list))
print(len(company_name_list))
##for i in model_list:
##    print(i)
print('--------------------------------------------------------------------------------------------------------------------------------------------')
var=1

##
##with open(os.path.join(path_of_url_file, 'gsmarena_href.txt'), 'w') as f:
##    for k in range(len(href)):
##        f.write(href[k] + '\n')
##
##with open(os.path.join(path_of_url_file, 'gsmarena_modelnames.txt'), 'w') as f:
##    for k in range(len(model_list)):
##        f.write(model_list[k] + '\n')
##
##with open(os.path.join(path_of_url_file, 'gsmarena_usp.txt'), 'w') as f:
##    for k in range(len(usp)):
##        try:
##            f.write(usp[k] + '\n')
##        except:
##            f.write('Not Available' + '\n')
##
##with open(os.path.join(path_of_url_file, 'gsmarena_company_name_list.txt'), 'w') as f:
##    for k in range(len(company_name_list)):
##        try:
##            f.write(company_name_list[k] + '\n')
##        except:
##            f.write('Not Available' + '\n')






for i in range(len(href)):
##    r = random.randint(5,10)
##    print('SLEEPING FOR %d SECONDS NOW.' %r)
##    time.sleep(r)
    #var=var+1
    c1=''
    d1=''
    print('MODEL NO.%d' %i)
    r=requests.get(href[i])
    #r = http.request('GET', href[i])
    soup = BeautifulSoup(r.text,'html5lib')
    results=soup.find_all('div',attrs={'id':'specs-list'})
    for a in range(len(results)):
        sa=results[a].find_all('table',attrs={'cellspacing':'0'})
        for b in range(len(sa)):
            sb=sa[b].find_all('tbody')
            for c in range(len(sb)):
                sc=sb[c].find('th').text

                if 'body' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'dimension' in se[e].text.lower():
                                thickness_list.append(sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"'))

                if 'platform' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'cpu' in se[e].text.lower():
                                processor_list.append(sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"'))

                if 'memory' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'internal' in se[e].text.lower():
                                memory_list.append(sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"'))

                if 'camera' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'primary' in se[e].text.lower() or 'secondary' in se[e].text.lower():
                                c1=c1+se[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"')+':- '+sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"')+' || '
                
                if 'display' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'type' in se[e].text.lower() or 'size' in se[e].text.lower():
                                d1=d1+se[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"')+':- '+sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"')+' || '

                if 'battery' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'mah' in sf[e].text.lower():
                                battery_list.append(sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"'))

                if 'launch' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'announce' in se[e].text.lower():
                                launch_date_list.append(sf[e].text.replace('μ','mu').replace('α','alpha').replace('”','"').replace(u'\x94', '"').strip())

                if 'misc' in sc.lower():
                    sd=sb[c].find_all('tr')
                    for d in range(len(sd)):
                        se=sd[d].find_all('td',attrs={'class':'ttl'})
                        sf=sd[d].find_all('td',attrs={'class':'nfo'})
                        for e in range(len(sf)):
                            if 'price' in se[e].text.lower():
                                
                                ts = sf[e].text.replace('α','alpha').replace('μ','mu').replace('”','"').replace(u'\x94', '"').strip()
                                #ts = ts.decode('utf-8').replace(u'\x94', '"')
                                price_list.append(ts)

                

    if d1!='':
        display_list.append(d1)
    if c1!='':
        camera_list.append(c1)
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(price_list)==i:
        price_list.append('Not Available')
    if len(usp)==i:
        usp.append('Not Available')
    if len(launch_date_list)==i:
        launch_date_list.append('Not Available')
##    if var==500:
##        break

print('DISPLAY LIST:- ')
print(len(display_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            
print('PROCESSOR LIST:- ')
print(len(processor_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('MEMORY LIST:- ')
print(len(memory_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('CAMERA LIST:- ')
print(len(camera_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('BATTERY LIST:- ')
print(len(battery_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('THICKNESS LIST:-')
print(len(thickness_list))
    
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('PRICE LIST:_')
print(len(price_list))

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('LAUNCH DATE:-')
print(len(launch_date_list))
    

extras_links = href

    
for i in range(len(model_list)):
    records.append((company_name_list[i],model_list[i],price_list[i],launch_date_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COMPANY', 'MODEL', 'PRICE','LAUNCH DATE', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
with open(os.path.join(path_of_gsmarena_complete_csv, 'GSM-ARENA.csv'), 'a') as f:
    df.to_csv(f, index=False, mode='a', header=False, encoding='utf-8')
   
      
                    
                       

                
                

                
