import csv
import requests
from bs4 import BeautifulSoup
import csv
import re

import pandas as pd
import datetime
import os
today=datetime.date.today()
url1=[]
urls=[]
url2=[]
url3=[]
model=[]
company=[]
specs=[]
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
battery_list1 = []
thickness_list = []
extras_links = []
country=[]
           
url="http://www.umidigi.com/page-phones.html"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
lin=soup.find_all('div',attrs={'class':'wrap'})
for i in lin:
    tt=i.find_all('p')
    for r in tt:
        cc=r.find_all('a')
        for o in cc:
            url2.append('http://www.umidigi.com/'+o['href'])

for c in url2:
    if '.html' in c:
        url3.append(c)
#print(len(url3))


for i in url3:
    r=requests.get(i)
    soup=BeautifulSoup(r.text,'html.parser')    
    lin=soup.find_all('div',attrs={'class':'borderpx'})
    if(lin):
        for v in lin:
            kk= v.findAll('a', text = re.compile('Specification'))
            for n in kk:
                bb=n['href']
                #print(bb)
                if 'http' in bb:
                    urls.append(bb)
                else:
                    urls.append('http://www.umidigi.com'+bb)
                        
                    
                
                
                
                
#print(len(urls))
jk=0
for p in urls:
    print(p)
    if p=='http://www.umidigi.com/page-umidigi_z1_specification.html':
        yy=[]
        gh=[]
        dat1=soup.find_all('div',attrs={'class':'z1pro'})
        dat2=soup.find_all('div',attrs={'class':'z1'})
        if dat1:
            for i in dat1:
                yy.append(i.text)

           
            for x in yy:
                
                if "mAH" in x or "mAh" in x:
                    battery_list.append(x)
                if "inch" in x:
                    display_list.append(x)
                if "ARM" in x or "MHz" in x or 'Mali' in x or 'Mail' in x:
                    processor_list.append(x)
               
                if "mm" in x and("*" in x or "x" in x):
                   thickness_list.append(x)
                   #print("_____________")
            if len(thickness_list)==jk:
                thickness_list.append("NOT AVAILABLE on website")
                #print("_____________")
            lt=''
            for k in yy:
                if 'GB' in k:
                    lt=lt+k+" "
            memory_list.append("RAM/ROM:"+lt)

            ht=''
            for k in yy:
                if 'MP' in k and 'MHz' not in k and 'MP3' not in k and 'MPE' not in k:
                    ht=ht+k+" "
            camera_list.append("REAR/FRONT: "+ht)
            model.append(yy[1])
            country_list.append('china')
            company_list.append('umidigi')
            specs.append("NOT AVAILABLE")
            extras_links.append(p)
    
        if dat2:
            for i in dat2:
                gh.append(i.text)

           
            for x in gh:
                
                if "mAH" in x or "mAh" in x:
                    battery_list.append(x)
                if "inch" in x:
                    display_list.append(x)
                if "ARM" in x or "MHz" in x or 'Mali' in x or 'Mail' in x:
                    processor_list.append(x)
               
                if "mm" in x and("*" in x or "x" in x):
                   thickness_list.append(x)
                   #print("_____________")
            if len(thickness_list)==jk:
                thickness_list.append("NOT AVAILABLE on website")
                #print("_____________")
            lt=''
            for k in gh:
                if 'GB' in k:
                    lt=lt+k+" "
            memory_list.append("RAM/ROM:"+lt)

            ht=''
            for k in gh:
                if 'MP' in k and 'MHz' not in k and 'MP3' not in k and 'MPE' not in k:
                    ht=ht+k+" "
            camera_list.append("REAR/FRONT: "+ht)
            model.append(gh[1])
            country_list.append('china')
            company_list.append('umidigi')
            specs.append("NOT AVAILABLE")
            extras_links.append(p)
            
    else:
        heads=[]
        dets=[]
        r=requests.get(p)
        soup=BeautifulSoup(r.text,'html.parser')    
        dat=soup.find_all('div',attrs={'class':'content_box params'})
        sp=soup.find_all('ul',attrs={'class':'param'})
        for i in dat:
            th=i.find_all('li')
            for i in th:
                heads.append(i.text)
        for x in heads:
            if "mAH" in x or "mAh" in x:
                battery_list.append(x)
            if "inch" in x:
                display_list.append(x)
            if "ARM" in x or "MHz" in x or 'Mali' in x or 'Mail' in x:
                processor_list.append(x)
               
            if "mm" in x and("*" in x or "x" in x):
               thickness_list.append(x)
               print("_____________")
        if len(thickness_list)==jk:
            thickness_list.append("NOT AVAILABLE on website")
            print("_____________")
        lt=''
        for k in heads:
            if 'GB' in k:
                lt=lt+k+" "
        memory_list.append("RAM/ROM:"+lt)

        ht=''
        for k in heads:
            if 'MP' in k and 'MHz' not in k and 'MP3' not in k and 'MPE' not in k:
                ht=ht+k+" "
        camera_list.append("REAR/FRONT: "+ht)
        model.append(heads[5])
        specs.append("NOT AVAILABLE")
        company.append("umidigi")
        country.append("china")
        extras_links.append(p)
    jk=jk+1
    
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
#print(battery_list)

records=[]
for i in range(len(country)):
    records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'-umidigi'+'.csv'), index=False, encoding='utf-8')


    
        
