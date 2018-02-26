import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import sys
import bs4 as bs
import urllib.request
import datetime
import os

today=datetime.date.today()
country=[]
company=[]
urls=[]
specs=[]
model=[]
thickness_list1=[]
usp=[]
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []
heads = []
dets = []
dets1=[]
url='https://www.billion.in/'
r1 = requests.get(url)
soup = BeautifulSoup(r1.text, 'html.parser')
sp=soup.findAll('a', text = re.compile('Smartphones'), attrs = {'class' : 'sub-nav-link'})
for t in sp:
    urls.append(t['href'])
for b in urls:
    r1 = requests.get(b)
    soup = BeautifulSoup(r1.text, 'html.parser')
    
    sp=soup.find_all("div",attrs={'class':'fourth-screen'})
    for ghj in sp:
        hj=ghj.find_all("h1")
        for y in hj:
            specs.append(y.text)
    dat=soup.find_all("div",attrs={'class':'second-screen section screen-6'})
    #print(dat)
    for t in dat:
        s1=t.find_all("h1")
        s2=t.find_all("h3")
        for x in s1:
            heads.append(x.text)
        kt=""
        for v in s2:
            kt=kt+(v.text)
        dets.append(kt)
    for i in range(len(heads)):                                                                           
        if 'Battery' in heads[i]:
            battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'battery' in heads[i]:
            battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'BATTERY' in heads[i]:
            battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'Processor & RAM' in heads[i]:
            processor_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'processor' in heads[i]:
            processor_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'Camera' in heads[i]:
            camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'camera' in heads[i]:
            camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'CAMERA' in heads[i]:
            camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'Display' in heads[i] or 'display' in heads[i] or 'DISPLAY' in heads[i]:
            display_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        if 'Storage & Memory' in heads[i] or 'Storage' in heads[i] or 'storage' in heads[i] or 'memory' in heads[i]:
            memory_list.append(dets[i].strip('\r\n\t').replace('\n',''))
    
    
for x in range(len(urls)):
    country.append("INDIA")
    company.append("BILLION")
    extras_links.append(urls[x])
    thickness_list.append("NOT AVAILABLE")
    
for x in urls:
    r1 = requests.get(x)
    soup = BeautifulSoup(r1.text, 'html.parser')
    
    sp=soup.find_all("div",attrs={'class':'second-screen section'})
    for ghj in sp:
        hj=ghj.find_all("h1")
        for y in hj:
            model.append(y.text)
    

print(len(country))
print(len(company))
print(len(model))
print(len(specs))
print(len(display_list))
print(len(camera_list))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))

records=[]
for i in range(len(company)):
    records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'-billion'+'.csv'), index=False, encoding='utf-8')

