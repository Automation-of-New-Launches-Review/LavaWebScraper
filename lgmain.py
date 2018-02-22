import csv
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import datetime
import os
today=datetime.date.today()
url2=[]
model=[]
specs=[]
company=[]
country=[]
display_list = []
memory_list = []
processor_list = []
camera_list = []
battery_list = []
thickness_list = []
extras_links = []

url="http://www.lg.com/in/smartphones"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
results=soup.find_all('p',attrs={'class':'model-num'})
for z in results:
    model.append(z.text)
#print(model)
links=soup.find_all('p',attrs={'class':'model-num'})
for k in links:
    tt=k.find_all('a')
    for u in range(len(tt)):
        #print(tt[u]["href"])
        url2.append("http://www.lg.com"+tt[u]["href"])
  
#print(url2)
for u in range(len(model)):
    company.append("LG")

for z in url2:
    heads = []
    dets = []
    dets1=[]
    link=z
    print(link)
    r=requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    dat=soup.find_all("div",attrs={'class':'tech_spec_wrap'})
    for t in dat:
        s1=t.find_all("table")
        #print(s1)
        for s in s1:
            tt=s.find_all('tr')
            for k in tt:
                th=k.find_all('th')
                td=k.find_all('td')
                for i in th:
                    heads.append(i.text)
                for ui in td:
                    dets.append(ui.text)
    for i in range(len(heads)):
            
        if 'Battery' in heads[i]:
            battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
        
    pt=""
    for i in range(len(heads)):
        if 'RAM' in heads[i]:
            pt=pt+dets[i].strip('\r\n\t')+" "
        
        if 'Internal Memory Size' in heads[i]:
            pt=pt+dets[i].strip('\r\n\t')+" "
        if 'External memory slot' in heads[i]:
            pt=pt+dets[i].strip('\r\n\t')+" "
    memory_list.append(pt.replace("\n"," "))
    lt=''
    for i in range(len(heads)):
        
        if 'Camera' in heads[i]:
        
            lt=lt+dets[i].strip('\r\n\t')
        if 'camera' in heads[i]:
        
            lt=lt+dets[i].strip('\r\n\t')
    camera_list.append(lt.replace("\n"," "))
    llt=''
    for i in range(len(heads)):
    
        if 'Display' in heads[i]:
        
            llt=llt+dets[i].strip('\r\n\t')
        if 'dispaly' in heads[i]:
        
            llt=llt+dets[i].strip('\r\n\t')
    display_list.append(llt.replace("\n"," "))
    vt=''
    for i in range(len(heads)):
    
        if 'CPU' in heads[i]:
        
            vt=vt+dets[i].strip('\r\n\t')
        if 'Processor' in heads[i]:
        
            vt=vt+dets[i].strip('\r\n\t')
    processor_list.append(vt.replace("\n"," "))
    xx=''
    for i in range(len(heads)):
        s=''                              
        if 'Size' in heads[i]:
            match = re.search(r'x\s*\d+\.\d+\s*\(D\)\s*mm',dets[i])
            if match:
                s=str(match.group())
            if not match:
                s=" "
            xx=xx+s
        if 'Dimensions' in heads[i]:
        #print("x")
            match = re.search(r'x\s*\d*\.\d*\s*mm',dets[i])
            if match:
                s=str(match.group())
            if not match:
                match = re.search(r'x\s*\d*\s*mm',dets[i])
                if match:
                    s=str(match.group())
                if not match:
                    match=re.search(r'x\d+\.\d+mm',dets[i])
                    if match:
                        s=str(match.group())
                    if not match:
                        s='NOT AVAILABLE'
            xx=xx+s
    thickness_list.append(xx)
    
    
for i in range(len(url2)):
    country.append("SOUTH KOREA")
    extras_links.append(url2[i])
    specs.append("NOT AVAILABLE")
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
df.to_csv(os.path.join(path,'lgmain-'+str(today)+'.csv'), index=False, encoding='utf-8')


        
    
