import csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
import datetime
import os
today=datetime.date.today()
urls=[]
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
url="https://www.mylyf.com/element-series-collection"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('div',attrs={'class':'product-txt'})
mod=soup.find_all('div',attrs={'class':'btn_panel'})
for j in links:
    
    tt=j.find_all('p')
    for k in tt:
        data1=[]
        data1.append(k.text)
    for l in range(len(data1)):
        st=""
        st=st+data1[l]
        pt=''
        for k in st:
            
            pt=pt+k.strip('\n')
            f=''
        for t in pt:
            f=f+t.strip('\r')
    specs.append(f)
for s in mod:
    tt=s.find_all('a')
    for m in tt:
        model.append(m.text)
#company---
for i in range(len(model)):
    
    company.append("LYF")
    

links=soup.find_all('div',attrs={'class':'btn_panel'})
for x in links:
    v=x.find_all('a')
    for h in v:
        urls.append(h['href'])

for i in range(len(urls)):
    country.append("INDIA")
    extras_links.append(urls[i])
    
    
for z in range(len(urls)):

    
    print(urls[z])
    heads = []
    dets = []
    dets1=[]
    r1 = requests.get(urls[z])
    soup = BeautifulSoup(r1.text, 'html.parser')

    dat=soup.find_all("table")
    for t in dat:
        s1=t.find_all("tr")
        #print(s1)
        for s in s1:
            s2=s.find_all('td')
            heads.append(s2[0].text)
            dets.append(s2[1].text)
    lt=''
    bb=''
    
    for i in range(len(heads)):
        
        s=''
        c=''
        d=''
        t=''
        if 'CHIPSET' in heads[i]:
            bb=bb+dets[i].strip('\r\n\t').replace('\n','')
        
            
            
    
        if 'BATTERY' in heads[i]:
            match = re.search(r'\d+\s*m',dets[i])
            if match:
                c=str(match.group())
            if not match:
                match=re.search(r'\d*m',dets[i].lower())
                if match:
                    c=str(match.group())
                if not match:
                    c=' '
                
            battery_list.append(c+"Ah")
        if 'DESIGN' in heads[i]:
            #print("x")
            match = re.search(r'\d+\.?\d*\s*mm\s*x\s*\d+\.?\d*\s*mm\s*x\s*\d+\.?\d*\s*mm',dets[i])
            if match:
                s=str(match.group())
            if not match:
                match = re.search(r'x\d+\s*\.*\,*\s*\d*\s*mm',dets[i])
                if match:
                     s=str(match.group())
                if not match:
                    s=' '
            lt=lt+s
        if "DESIGN" not in heads:
                
            lt=lt+" "
        
            #print("__________")
        cv=''
        if 'CAMERA' in heads[i]:
            #print(dets[i])
            match1=re.search(r'Rear Camera :\s*\d+\s*\.*\s*\d*\s*MP',dets[i])
            if match1:
                d=str(match1.group())
            if not match1:
                match1=re.search(r'Rear Camera:\s+\d+\s*\.*\s*\d*\s*MP',dets[i])
                if match1:
                    d=str(match1.group())
                if not match1:
                    match1=re.search(r'Rear Camera:\d+MP',dets[i])
                    if match1:
                        d=str(match1.group())
                    if not match:
                        d=' '
                
            cv=cv+d+" "
            match12=re.search(r'Front Camera :\s*\d+\s*\.*\s*\d*\s*MP',dets[i])
            if match12:
                t=str(match12.group())
            if not match12:
                match12=re.search(r'Front Camera:\s+\d+\s*\.*\s*\d*\s*MP',dets[i])
                if match12:
                    t=str(match12.group())
                if not match12:
                    match12=re.search(r'Front Camera:\d+MP',dets[i])
                    if match12:
                        t=str(match12.group())
                    if not match12:
                        t=' '
            cv=cv+t
            camera_list.append(cv)
        if 'DISPLAY' in heads[i]:
            match=re.search(r'Screen Size:\s*\d*\.\d*cm',dets[i])
            if match:
                y=str(match.group())
            if not match:
                match=re.search(r'Screen Size:\s*\d*\.\d*\s*cm',dets[i])
                if match:
                    y=str(match.group())
                if not match:
                    match=re.search(r'Screen Size:\s*\d*\.\d*\s*inch',dets[i])
                    if match:
                        y=str(match.group())
                    if not match:
                        y="NOT AVAILABLE "
                             
                             
                
            
            display_list.append(y)
    thickness_list.append(lt)
    processor_list.append(bb)

    pt=""
    for i in range(len(heads)):
        if 'STORAGE' in heads[i]:
            pt=pt+dets[i].strip('\r\n\t')
        
        if 'PERFORMANCE' in heads[i]:
            match = re.search(r'RAM:\s*\d*GB',dets[i])
            if match:
                pt=pt+str(match.group())
            if not match:
                pt=pt+" "
    memory_list.append(pt.replace("\n"," ").replace("\r"," "))
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
df.to_csv(os.path.join(path,str(today)+'-lyf'+'.csv'), index=False, encoding='utf-8')
