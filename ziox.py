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
url="http://ziox.in/product-category/smart-phones/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('a',attrs={'class':'product-desc-link'})
lin=soup.find_all('a',attrs={'class':'page-numbers'})
for x in links:
    urls.append(x['href'])

for c in lin:
    urls1.append(c['href'])

for t in urls1:
    r=requests.get(t)
    soup=BeautifulSoup(r.text,'html.parser')    
    links=soup.find_all('a',attrs={'class':'product-desc-link'})
    
    for x in links:
        urls.append(x['href'])
urls2=list(set(urls))
##print(urls2)

for b in urls2:
    print(b)
    extras_links.append(b)
    r=requests.get(b)
    soup=BeautifulSoup(r.text,'html.parser')
    tit=soup.find_all('h1',attrs={'class':'product_title entry-title'})
    for hj in tit:
        model.append(hj.text)
    bat=soup.find_all('div',attrs={'class':'summary entry-summary'})
    yu=''
    for x in bat:
        z=x.find_all('li')
        k=[]
        for f in z:
            
            k.append(f.text)
        
        for it in range(len(k)):
            if 'Batter' in k[it] or 'battery' in k[it]:
                battery_list.append(k[it])
                #print('________')
            if 'display' in k[it] or 'Display' in k[it]:
                display_list.append(k[it])
            if 'RAM' in k[it]:
                memory_list.append(k[it])
            
            if 'Processor' in k[it] or 'processor' in k[it] :
                yu=yu+k[it]
                
                #processor_list.append(yu)
               
            if 'Camera' in k[it] or 'camera' in k[it] :
                camera_list.append(k[it])
              
                #processor_list.append(yu)
    #print(yu)
    processor_list.append(yu)
for i in range(len(urls2)):
    country.append("INDIA")
    company.append("ZIOX")
    specs.append("NOT AVAILABLE")
    thickness_list.append("NOT AVAILABLE ON WEBSITE")
    
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
df.to_csv(os.path.join(path,'ziox-'+str(today)+'.csv'), index=False, encoding='utf-8')
