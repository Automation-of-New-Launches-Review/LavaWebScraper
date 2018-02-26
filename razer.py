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
hh=[]
url="https://www.razerzone.com/mobile/razer-phone"
extras_links.append(url)
company.append('RAZOR')
country.append('USA')
model.append('RAZOR PHONE')
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('div',attrs={'class':'col-sm-9'})
for i in links:
    urls.append(i.text)
    tt=i.find_all('li')
    
    for y in tt:
        hh.append(y.text)
k=' '
print(hh)   
for uu in range(0,2):
    k=k+hh[uu]+"||"
specs.append(k)
        
        
for u in range(1,len(urls)):
    urls1.append(urls[u])
    
#print(urls1)
for x in urls1:
    c=' '
    if "mAH" in x or "mAh" in x:
        match = re.search(r'\s*\d+\s*\,*\s*\d*\s*mAh',x)
        if match:
            c=str(match.group())
                #print(c)
            if not match:
                c=' '
            #print(c)
            battery_list.append(c)  
        
    if "inch" in x:
        display_list.append(x)
    if 'Snapdragon™' in x:
        processor_list.append(x)
    if 'Internal' in x:
        memory_list.append(x)
    if 'MP AF' in x:
        camera_list.append(x)
    op=''
    if 'mm' in x:
        match = re.search(r'x\s*\d*\s*mm',x)
        if match:
            op=str(match.group())
            if not match:
                match=re.search(r'\s*\d+\s*\,*\s*\d*\s*mm',x)
                if match:
                    op=str(match.group())
                if not match:
                    op=" "
            thickness_list.append(op)
        
               

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
df.to_csv(os.path.join(path,str(today)+'-razer'+'.csv'), index=False, encoding='utf-8')


                                
