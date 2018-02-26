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
display_list = []
display_list1 = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []
urls=[]
model=[]
company=[]
specs=[]
detail2=[]
aa=[]
country=[]
memory_list=[]
url="https://www.sonymobile.com/in/products/phones/"    
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('a',attrs={'class':'product-name p2'})
for s in links:
    tt=s.find_all("strong")
    
    for y in tt:
        model.append(y.text)
links1=soup.find_all('a',attrs={'class':'product-name p2'})
for t in links:
    urls.append(t['href'])
#print(urls)
for i in urls:
    data1=[]
    
    
    z=i
    r=requests.get(z)
    soup=BeautifulSoup(r.text,'html.parser')    
    
    data=soup.find_all('p',attrs={'class':'copy ghost-center with-icon'})
    for s in data:
        
        tt=s.find_all("span")
        for p in tt:
            data1.append(p.text)
        #print(data1)
        st=''
        for l in range(len(data1)):
            st=st+data1[l]
    specs.append(st)
for i in range(len(specs)):
    company.append("SONY")


#detailed-----
for x in urls:
    
    aa.append(x+"specifications/")

for k in aa:
    d=k
    print(d)
    heads = []
    dets = []
    r=requests.get(d)
    soup=BeautifulSoup(r.text,'html.parser')
    dat=soup.find_all('div', attrs={'class':'grid no-grid-at-567 spec-section'})
    for ta in dat:
        
        tt=ta.find_all('h6', attrs={'class':'t6-light section-label'})
        d=ta.find_all('div', attrs={'class':'span4'})
        for t in tt:
            
            heads.append(t.text)
            st=''
    
        for yy in d:
            st=st+(yy.text.strip())
        dets.append(st)
    #print(heads)
    #print(dets)
    
    for i in range(len(heads)):
        #print(heads[i])
        

        
        if 'Memory and storage' in heads[i]:
            memory_list.append(dets[i])
        op=''    
        if 'Display'  in heads[i]:
            match = re.search(r'\s*\d+\s*\.*\,*\s*\d*\s*cm',dets[i])
            if match:
                op=str(match.group())
            if not match:
                match=re.search(r'\s*\d+\s*\,*\s*\d*\s*cm',dets[i])
                if match:
                    op=str(match.group())
                if not match:
                    op=" "
            display_list.append(op+" HD DISPLAY")
            #print("________________________________________")
 
        if 'Processor (CPU)' in heads[i]:
            processor_list.append(dets[i])
        c=''
        if 'Battery' in heads[i]:
            match = re.search(r'\s*\d+\s*\,*\s*\d*\s*mAh',dets[i])
            if match:
                c=str(match.group())
                #print(c)
            if not match:
                c=' '
            #print(c)
            battery_list.append(c)   
        
        if 'Dimensions' in heads[i]:
            match = re.search(r'x\s*\d*\.\d*\s*mm',dets[i])
            if match:
                thickness_list.append(match.group())
            if not match:
                match = re.search(r'x\s*\d*\s*mm',dets[i])
                thickness_list.append(match.group())
    st=" "
    st1=''
    s=''
    b=''
    d=''
    
    for i in range(len(heads)):
        if 'Main Camera'in heads[i] or 'Main camera' in heads[i]:
            st=st+dets[i]
            match=re.search(r'\d+\s*\.*\s*\d*\s*MP',st)
            if match:
                s=str(match.group())
            if not match:
                s=" "
            d=d+"MAIN CAMERA"+s
        if 'Front Camera'in heads[i] or 'Front camera' in heads[i]:
            st1=st1+dets[i]
            mare=re.search(r'\d+\s*\.*\s*\d*\s*MP',st1)
            if match:
                b=str(match.group())
            if not match:
                b=" "
            d=d+"  FRONT CAMERA"+b
    camera_list.append(d)
for x in aa:
    extras_links.append(x)
    country.append('JAPAN')
print(len(country))
print(len(company))
print(len(specs))
print(len(camera_list))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))


records=[]
for i in range(len(aa)):
    records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))


path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'-sony'+'.csv'), index=False, encoding='utf-8')


