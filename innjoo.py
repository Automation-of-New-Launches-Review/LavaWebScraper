import csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import datetime
import os
today=datetime.date.today()

urls=[]
urls1=[]
urls2=[]
model=[]
company=[]
specs=[]
country=[]
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []
url="http://www.innjoo.com/Product/phone"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('li',attrs={'class':'dropdown dropdown-phone active'})
#print(links)
for i in links:
    tt=i.find_all('ul',attrs={'class':'product-series-classify'})
    for x in tt:
        z=x.find_all('a')
        for b in z:
            urls1.append('http://www.innjoo.com'+b['href'])
for s in urls1:
    r=requests.get(s)
    soup=BeautifulSoup(r.text,'html.parser')    
    link=soup.findAll('a', text = re.compile('Tech Specs'))
    for a in link:
        urls.append('http://www.innjoo.com'+a['href'])
#print(urls)
for u in urls:
    specs.append("NOT AVAILABLE")
    heads=[]
    dets=[]
    company.append("INJOO")
    country.append("CHINA")
    r=requests.get(u)
    soup=BeautifulSoup(r.text,'html.parser')
    s=soup.find_all('div',attrs={'class':'wd'})
    t=soup.find_all('div',attrs={'class':"techspec-content ltr-style"})
    m=soup.find_all('div',attrs={'class':"product-name"})
    if s:
        k=''
        print(u)
        extras_links.append(u)
        for x in m:
            if x.text not in model:
                model.append(x.text)
        for tk in s:
            th=tk.find_all('span')
            heads.append(th[0].text.strip(":"))
            dets.append(th[1].text)
        
        for i in range(len(heads)):
            if 'CPU' in heads[i]:
                processor_list.append(dets[i])
                #print("____")
            if 'Screen Size' in heads[i]:
                display_list.append(dets[i])
            if 'Memory' in heads[i]:
                k=k+dets[i]+" "
            if 'Storage ' in heads[i]:
                k=k+dets[i]
            if 'Capacity' in heads[i]:
                battery_list.append(dets[i])
                
            if 'Dimensions' in heads[i]:
                thickness_list.append(dets[i])
            if 'Camera' in heads[i] or 'Pixel' in heads[i]:
                camera_list.append(dets[i])
                #print("________")
                
        memory_list.append(k)
                
                
    if t:
        xx=[]
        bn=' '
        print(u)
        if u not in extras_links:
            extras_links.append(u)
        for x in m:
            if x.text not in model:
                model.append(x.text)
        for k in t :
            th=k.find_all('td')
            for z in th:
                xx.append(z.text)
        #print(xx)
        for j in xx:
            if 'mAh' in j:
                battery_list.append(j)
            if 'inch' in j:
                display_list.append(j)
            if 'Front' in j and("Megapixel" in j or 'MP' in j or 'megapixel' in j or 'pixels' in j):
                camera_list.append(j)
                #print("________")
            if 'GB' in j:
                bn=bn+j+" "
            if 'mm' in j and('*' in j or 'x' in j):
                thickness_list.append(j)
            if 'GHz' in j and('MT' in j or 'Core' in j or 'core' in j):
                processor_list.append(j)
                #print("______")
        memory_list.append("RAM/ROM:"+bn)
    
                    
               
                
            

           
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
df.to_csv(os.path.join(path,'innjoo-'+str(today)+'.csv'), index=False, encoding='utf-8')
    
