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
import datetime
import os
today=datetime.date.today()

base_url = 'http://www.ivoomiindia.com'
#ur='https://www.nokia.com/en_int/phones/'
country = []
company = []
model = []
specs = []
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
#print('yOo')
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('nav',attrs={'class':'hidden-xs'})
#print(len(results))
for a in range(len(results)):
    sa=results[a].find_all('li',attrs={'class':'relative'})
    #print(len(sa))
    for b in range(len(sa)):
        sb=sa[b].find_all('div',attrs={'class':'sub-menu'})
        for c in range(len(sb)):
            sc=sb[c].find_all('a')
            #print(len(sc))
            for d in range(len(sc)):
                model.append(sc[d].text)
                href.append("http://www.ivoomiindia.com"+sc[d]['href'])


#print(href)
#print(len(model))
mk=0
for n in href:
    #specs.append("NA")
    country.append("CHINA")
    company.append("IVOOMI")
    r=requests.get(n)
    soup=BeautifulSoup(r.text,'html.parser')
    dat=soup.find_all('div',attrs={'class':'specs-box'})
    cd=soup.find_all('section',attrs={'class':'specification-section'})
    jk=soup.find_all('div',attrs={'class':'w25'})
    pt=soup.find_all('div',attrs={'class':'col-4'})
    specdat=soup.find_all('h2')
    pescd=soup.find_all('h1')
    #print(cr)
    if dat:
        thickness_list.append("NOT AVAILABLE")
        maal=[]
        daal=[]
        extras_links.append(n)
        print(n)
        print("in dat")
        if specdat:
            
            j=''
            for y in specdat:
                j=j+y.text.strip()+" "
            specs.append(j)
        else:
            specs.append("NOT AVAILABLE")
            
        for z in dat:
            vv=z.find_all("h3")
            tt=z.find_all("p")
            for x in vv:
                for b in x:
                    maal.append(b)
            for o in tt:
                for a in o:
                    daal.append(a)
        #print(maal)
        if maal:
            yo=''
            jo=''
            ln=' '
            for c in maal:
                if "inch" in c:
                    display_list.append(c.strip())
                if 'Core' in c or 'Media' in c:
                    ln=ln+c.strip()
                
                    #print("____")
                if 'mAh' in c or 'mAh' in c:
                    battery_list.append(c.strip())
                    #print("____")
                if 'Camera' in c or 'MP' in c:
                    yo=yo+c.strip()+' '
                if 'GB' in c:
                    jo=jo+c.strip()+" "
            camera_list.append(yo)
            memory_list.append(jo)
            processor_list.append(ln)
            #print("____")
        if daal:
            rr=''
            ee=''
            nn=' '
            
            for f in daal:
                if "inch" in f:
                    display_list.append(f.strip())
                if 'Core' in f or 'core' in f:
                    processor_list.append(f.strip())
                    #print("____")
                if 'mAh' in f:
                    nn=nn+f.strip()
                if 'Camera' in f or 'MP' in f:
                    ee=ee+f.strip()+' '
                if 'GB' in f:
                    rr=rr+f.strip()+" "   
        
            camera_list.append(ee)
            memory_list.append(rr)
            battery_list.append(nn)
           
        
    elif cd:
        dal=[]
        if pescd:
            
            j=''
            for y in pescd:
                j=j+y.text.strip()+" "
            specs.append(j)
        else:
            specs.append("NOT AVAILABLE")
        thickness_list.append("NOT AVAILABLE")
        extras_links.append(n)
        print(n)
        print("in cd")
        for ml in cd:
            tt=ml.find_all("p")
            for o in tt:
                for a in o:
                    dal.append(a)
        if dal:
            rr=''
            ee=''
            nn=' '
            
            for f in dal:
                if "inch" in f:
                    display_list.append(f.strip())
                if 'Core' in f or 'core' in f:
                    processor_list.append(f.strip())
                    #print("____")
                if 'mAh' in f:
                    nn=nn+f.strip()
                if 'Camera' in f or 'MP' in f:
                    ee=ee+f.strip()+' '
                if 'GB' in f:
                    rr=rr+f.strip()+" "   
        
            camera_list.append(ee)
            memory_list.append(rr)
            battery_list.append(nn)
           
    elif jk:
        #print(pt)
        specs.append("NOT AVAILABLE")
        dol=[]
        nol=[]
        thickness_list.append("NOT AVAILABLE")
        extras_links.append(n)
        print(n)
        print("in jk")
        for lk in jk:
            tt=lk.find_all("p")
            for o in tt:
                for a in o:
                    dol.append(a)
        for vv in pt:
            ru=vv.find_all('p')
            for z in ru:
                for d in z:
                    nol.append(d)
        #print(dol)
        if dol:
            qw=''
            er=''
            tv=' '
            
            for f in dol:
                if "inch" in f:
                    display_list.append(f.strip())
                if 'Core' in f or 'core' in f:
                    processor_list.append(f.strip())
                    #print("____")
                if 'mAh' in f:
                    qw=qw+f.strip()
                

            battery_list.append(qw)
        
        if nol:
            rr=''
            ee=''
            
            
            for f in nol:
                if "inch" in f:
                    display_list.append(f.strip())
                if 'Core' in f or 'core' in f:
                    processor_list.append(f.strip())
                    #print("____")
                if 'Camera' in f or 'MP' in f:
                    ee=ee+f.strip()+' '
                if 'GB' in f:
                    rr=rr+f.strip()+" "
            
        
            camera_list.append(ee)
            memory_list.append(rr)
            
           
    
    else:
        specs.append("NOT AVAILABLE")
        extras_links.append(n)
        display_list.append("NOT AVAILABLE")
        camera_list.append("NOT AVAILABLE")
        memory_list.append("NOT AVAILABLE")
        thickness_list.append("NOT AVAILABLE")
        processor_list.append("NOT AVAILABLE")
        battery_list.append("NOT AVAILABLE")
    
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
df.to_csv(os.path.join(path,'ivoomi-'+str(today)+'.csv'), index=False, encoding='utf-8')

