import csv
import requests
from bs4 import BeautifulSoup
import csv

import pandas as pd
import datetime
import os
today=datetime.date.today()
url2=[]
model=[]
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
           
url="https://www.oppo.com/in/smartphones/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
results=soup.find_all('a',attrs={'class':'box-link'})
#print(results)
href=[]
for i in range(len(results)):
    url2.append("https://www.oppo.com"+results[i]["href"])
#print(url2)
company=[]
for h in range(len(url2)):
    
    company.append("oppo")
    country.append("china")
    extras_links.append(url2[h])
for z in range(len(url2)):
     print(url2[z])
     link=url2[z]
     if link=='https://www.oppo.com/in/smartphone-f5':
         r=requests.get(link)
         soup=BeautifulSoup(r.text,'html.parser')
         title=soup.find_all("div",{"class":"nav-title"})
         for j in title:
             model.append(j.text)
             print("_____")
     elif link=="https://www.oppo.com/in/smartphone-f1":
         model.append("OPPO F1")
##         r=requests.get(link)
##         soup=BeautifulSoup(r.text,'html.parser')
##         title=soup.find_all("div",{"class":"left"})
##         for t in title:
##             tt=t.find_all('p')
##             for u in tt:
##                 if u:
##                     model.append(u.text)
##                     print("_____")
##                 else:
##                     model.append("NA")
     else:
         r=requests.get(link)
         soup=BeautifulSoup(r.text,'html.parser')  
         title=soup.find_all("span",{"class":"h-delta"})
         for j in title:
             
         
             model.append(j.text)
             print("__________")


for i in range(len(url2)):
    #print(url2[i])
    data1=[]
    
    r=requests.get(url2[i])
    soup=BeautifulSoup(r.text,'html.parser')  
    st=""
    data=soup.find_all("div",{"class":"badge-info"})
   
    for j in data:
        
        x=j.find_all("p")
        for k in x:
            data1.append(k.text)
    #print(data1)
    for l in range(len(data1)):
        
        #print(l)
        st=st+data1[l]
    #print(st)
    specs.append(st)  #specs list-------------------------------------------------------


for it in url2:
    #print(it)
    heads = []
    dets = []
    dets1=[]
    r1 = requests.get(it)
    soup = BeautifulSoup(r1.text, 'html.parser')

    dat=soup.find_all("div",{"class":"specs-table"})
    for x in dat:
        tt=x.find_all("th",{"class":"specs-title"})
        ty=x.find_all("td",{"class":"specs-text"})
        for b in tt:
            heads.append(b.text.strip('\n'))
        for v in ty:
            dets.append(v.text.strip('\n'))
    xt=' '
    vt=''
    nt=''
    for i in range(len(heads)):
        if ('Processor' in heads[i] or 'processor' in heads[i]) and dets[i] not in nt:
            
            nt=nt+dets[i]
           # print("_________")
    
        if 'Battery' in heads[i] and dets[i] not in vt:
            vt=vt+dets[i]

        if ('Thickness' in heads[i] or 'thickness' in heads[i])and dets[i] not in xt:
            xt=xt+dets[i]
    
    thickness_list.append(xt)
    
    battery_list.append(vt)
    
    processor_list.append(nt)

    #print("_____________")


    tt=''
    for i in range(len(heads)):
        if 'Size' in heads[i] and dets[i] not in tt:
            tt=tt+dets[i]+" "
        if 'Type' in heads[i]and dets[i] not in tt:    
            tt=tt+dets[i]
        #if 'Resolution' in heads[i]and dets[i] not in tt:    
            #tt=tt+dets[i]
        #if 'Touchscreen ' in heads[i]and dets[i] not in tt:    
            #tt=tt+dets[i]
    display_list.append(tt)


    pt=''
    for k in range(len(heads)):
        if 'RAM ' in heads[k]and dets[k] not in pt:
            pt=pt+dets[k]+" "
        if 'Storage ' in heads[k]and dets[k] not in pt:
            pt=pt+dets[k]+" "
    memory_list.append(pt)

    lt=''
    for k in range(len(heads)):
        if 'Rear Sensor' in heads[k]and dets[k] not in lt:
            lt=lt+"REAR CAMERA "+dets[k]+" "
        if 'Front Sensor' in heads[k]and dets[k] not in lt:
            lt=lt+"FRONT CAMERA "+dets[k]+" "
    camera_list.append(lt)
thi=[]
for i in thickness_list:
    if i==" ":
        thi.append("NOT AVAILABLE")
    else:
        thi.append(i)
spe=[]
for i in specs:
    if i=="":
        spe.append("NOT AVAILABLE")
    else:
        spe.append(i)
di=[]
for i in display_list:
    if i=="":
        di.append("NOT AVAILABLE")
    else:
        di.append(i)
ca=[]
for i in camera_list:
    if i=="":
        ca.append("NOT AVAILABLE")
    else:
        ca.append(i)
mem=[]
for i in memory_list:
    if i=="":
        mem.append("NOT AVAILABLE")
    else:
        mem.append(i)
bat=[]
for i in battery_list:
    if i=="":
        bat.append("NOT AVAILABLE")
    else:
        bat.append(i)
pr=[]
for k in processor_list:
    #print(k)
    if k=="":
        pr.append("NOT AVAILABLE")
        #print("KK")
    else:
        pr.append(k)
print(len(country))
print(len(company))
print(len(model))
print(len(spe))
print(len(di))
print(len(ca))
print(len(mem))
print(len(bat))
print(len(thi))
print(len(pr))
print(len(extras_links))
#print(pr)

records=[]
for i in range(len(country)):
    records.append((country[i], company[i], model[i], spe[i], di[i], ca[i], mem[i], bat[i], thi[i], pr[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'-oppo'+'.csv'), index=False, encoding='utf-8')


