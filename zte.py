##import pandas as pd
##import requests
##from bs4 import BeautifulSoup
##url='http://www.ztedevice.com/product'
##ur='http://www.ztedevice.com'
##r=requests.get(url)
##soup=BeautifulSoup(r.text,'html.parser')
##results=soup.find_all('div',attrs={'class':'title'})
##href=[]
##models=[]
##usp=[]
##spec=[]
##company='ZTE'
##st_list_heads=[]
##st_list_dets=[]
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
import os
import datetime


###############################################################
path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'
###############################################################

base_url = 'http://www.ztedevice.com/product'
ur='http://www.ztedevice.com'
country = 'China'
company = 'ZTE'
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
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'title'})
for i in range(len(results)):
    href.append(results[i].find('a')['href'])
    model_list.append(results[i].find('a').text.strip())
rr=soup.find_all('div',attrs={'class':'prodDetail pcOnly'})
for l in range(len(rr)):
    usp.append(rr[l].find('p').text.strip())                 
u=0
t=0
while u<len(href):
    if href[u] in href[u+1:]:
        href.pop(u)
    u=u+1
while t<len(model_list):
    if model_list[t] in model_list[t+1:]:
        model_list.pop(t)
    t=t+1
#print(href)
#print(len(href))
##print(usp)
##print(len(usp))
##print(model_list)
##print(len(model_list))
for m in range(len(href)):
    heads=[]
    dets=[]
    href[m]=ur+href[m]
    r=requests.get(href[m])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('p',attrs={'class':'info-value2'})
    for i in range(len(results)):        
        if len(results[i].contents)!=1:
##            if len(results[i].contents)==2:
##                heads.append(results[i].contents[0].text)
##                dets.append(results[i].contents[1].replace('<sup>',' ').replace('</sup>',' ').replace('\xa0',' ').replace('\t',' ').strip('\xa0'))
        
            s=''
            heads.append(results[i].contents[0].text)
            #print(heads)
            for x in range(1,len(results[i].contents)):
                s=s+str(results[i].contents[x])
                                          
            dets.append(s.replace('<sup>',' ').replace('</sup>',' ').replace('\xa0',' ').replace('\t',' ').strip('\xa0'))
            #print(dets)
        else:
            pass
    st_list_heads.append(heads)
    st_list_dets.append(dets)
##print(st_list_heads)
##print(st_list_dets)
        
       
for i in range(len(st_list_heads)):
    m1=''
    m2=''
    c1=''
    c2=''
    
    
    for j in range(len(st_list_heads[i])):
        if 'Dimension' in st_list_heads[i][j] or 'dimension' in st_list_heads[i][j]:
            st = ''
            match = re.search(r'\*\s*\d+\.\d+\s*mm', st_list_dets[i][j])
            if match:
                st = str(match.group())
            if not match:
                match = re.search(r'x\s*\d+\.\d+\s*mm', st_list_dets[i][j])
                if match:
                    st = str(match.group())
                if not match:
                    match = re.search(r'\*\s*\d+\.\d+"', st_list_dets[i][j])
                    if match:
                        st = str(match.group())
                    if not match:
                        match = re.search(r'\*\s*\d+\.\d+''', st_list_dets[i][j])
                        if match:
                            st = str(match.group())
                        if not match:
                            match = re.search(r'\*\s*\d+\.\d+”', st_list_dets[i][j])
                            if match:
                                st = str(match.group())
                            if not match:
                                st = 'Not Available'
            thickness_list.append(st)
                        
            
        if 'processor' in st_list_heads[i][j].lower():
            processor_list.append(st_list_dets[i][j])
            
        if 'internal' in st_list_heads[i][j].lower():
            memory_list.append(st_list_dets[i][j].replace('<br>',' || ').replace('</br>',' || '))
            
        if 'battery capacity' in st_list_heads[i][j].lower():
            battery_list.append(st_list_dets[i][j])
                        
        if 'display' in st_list_heads[i][j].lower():
             display_list.append(st_list_dets[i][j].replace('’’','"').replace('“','"').replace('”','"').replace('，',' '))

        if 'rear camera' in st_list_heads[i][j].lower():
            c1=('Rear Camera:- '+st_list_dets[i][j])
        if 'front camera' in st_list_heads[i][j].lower():
            c2=('Front Camera:- '+st_list_dets[i][j])
##    if m1!=''or m2!='':
##        memory_list.append(m1 +' || '+ m2)
    if c1!=''or c2!='':
        camera_list.append(c1 +' || '+ c2)
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
    if len(usp)==i:
        usp.append('Not Available')         


##    if 'Dimensions' not in st_list_heads[i] and 'dimensions' not in st_list_heads[i]:
##        thickness_list.append('NA')
##        
##        
##    if 'Processor' not in st_list_heads[i] and 'processor' not in st_list_heads[i]:
##        processor_list.append('NA')
##        
##    if 'Internal' not in st_list_heads[i] and 'internal' not in st_list_heads[i]:
##        memory_list.append('NA')
##        
##    if 'Battery Capacity' not in st_list_heads[i] and 'Battery capacity' not in st_list_heads[i] and 'battery capacity' not in st_list_heads[i]:
##        battery_list.append('NA')
##        
##    if 'Display' not in st_list_heads[i] and 'display' not in st_list_heads[i]:
##        display_list.append('NA')
##        
##    if 'Rear Camera' not in st_list_heads[i] and 'Rear camera' not in st_list_heads[i] and 'rear camera' not in st_list_heads[i] and 'Front Camera' not in st_list_heads[i] and 'front camera' not in st_list_heads[i] and 'Front camera' not in st_list_heads[i]:
##        camera_list.append('NA')
print(len(model_list))
print(len(usp))
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(battery_list))
print(len(display_list))
print(len(camera_list))
#print(thickness_list)
extras_links = href

for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'zte-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')               
                                
