import csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
import datetime
import os
today=datetime.date.today()
##def find_between( s, first ):
##    try:
##        start = s.index( first ) + len( first )
##        end = s.index(' ')
##        return s[start:end]
##    except ValueError:
##        return ""
urls=[]
urls1=[]
urls2=[]
model1=[]
models=[]
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
url="https://gionee.co.in/smartphone"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
links=soup.find_all('div',attrs={'class':'buyButton'})
nm=soup.find_all('p',attrs={'class':'name'})
for w in nm:
    models.append(w.text)
for ti in models:
    if ti in model1:
        pass
    elif ti=='{{pl.prod_info.name}}':
        pass
    else:
        model1.append(ti)

#print(model1)
for s in links:
    tt=s.find_all('a')
    
    for x in tt:
        urls1.append(x['href'])
for i in urls1:
    if 'https' in i and i not in urls:
        urls.append(i)
#print(urls)
print("_____________________________________________________________________")
#print(len(urls))
xv=0
for x in urls:
    r1=requests.get(x)
    if r1:
        
        #print(x)
        country.append("CHINA")
        company.append("GIONEE")
        specs.append("NOT AVAILABLE")
        soup1=BeautifulSoup(r1.text,'html.parser')    
        li=soup1.find_all('div',attrs={'class':'accordion-section'})
        md=soup1.find_all('div',attrs={'class':'specs'})
        ban=soup1.find_all('div',attrs={'class':'banner'})
##        if ban:
##            rt=''
##            for lp in ban:
##                print(lp.text)
##                rt=rt+lp.text.strip()+"||"
##            #specs.append(rt)
##        else:
##            specs.append("NA")
##        
        if li:
            
                
                    
            heads=[]
            dets=[]
            print(x)
            if x=='https://gionee.co.in/smartphones/p-series/gionee-p7-max':
                    thickness_list.append("NOT AVAILABLE")
                    print("{{{{")
            if x=='https://gionee.co.in/smartphones/p-series/gionee-p7':
                    thickness_list.append("NOT AVAILABLE")
                    print("{{{{")
            if x=='https://gionee.co.in/smartphones/f-series/gionee-f103-pro':
                    thickness_list.append("NOT AVAILABLE")
                    print("{{{{")
            extras_links.append(x)
            z = 0
            for p in li:
                #print('table No.: %d' %z)
                th=p.find_all('tr')
                w=0
                for b in th:
                    try:
                        #print('<tr> No.: %d' %w)
                        ii=b.find_all('td')
                        #print(ii)
                        heads.append(ii[0].text.strip())
                        dets.append(ii[1].text.strip())
                    except:
                        pass
            pt=''
            y=' '
            
            for i in range(len(heads)):
                if i=='https://gionee.co.in/smartphones/p-series/gionee-p7-max':
                    thickness_list.append("NOT AVAILABLE")
                if i=='https://gionee.co.in/smartphones/p-series/gionee-p5l':
                    thickness_list.append("NOT AVAILABLE")
                if 'RAM' in heads[i] or 'ROM' in heads[i]:
                    #print(dets[i])
                    pt=pt+dets[i].strip()+" "
                if "Display" in heads[i] or 'Type' in heads[i] or'DISPLAY' in heads[i]:
                    #print(dets[i])
                    match=re.search(r'\d*\.\d*cm',dets[i])
                    if match:
                        y=str(match.group())
                        if not match:
                            match=re.search(r'\d+\.\d+\s+CM',dets[i])
                            if match:
                                y=str(match.group())
                                if not match:
                                    match=re.search(r'\d+\.\d+\s+cm',dets[i])
                                    if match:
                                        y=str(match.group())
                                        if not match:
                                            y="NOT AVAILABLE"
                    if not y.startswith(' '):
                        display_list.append(y)
                    else:
                        display_list.append("NOT AVAILABLE")
                if 'CPU' in heads[i]:
                    processor_list.append(dets[i])
                    
                if 'mAh' in dets[i]:
                    
                    battery_list.append(dets[i])
                if 'Size' in heads[i]:
                    thickness_list.append(dets[i])
                    print("____")
                
                if 'Primary' in heads[i]:
                    camera_list.append(dets[i])
                    #print("____")
                    

           
            
            memory_list.append("RAM/ROM: "+pt)
            #print("_______")
            
                
            if len(thickness_list)==xv:
                thickness_list.append('NOT AVAILABLE')
                print("______________")
            if len(memory_list)==xv:
                memory_list.append('NOT AVAILABLE')
        xv=xv+1
        if md:
            data=[]
            extras_links.append(x)
            print(x)
            for kl in md:
                tt=kl.find_all('p')
                for xc in tt:
                    for vv in xc:
                        data.append(vv)
            yu=''
            cb=''
            #print(data)
            for i in data:
                if 'Dimensions' in i:
                    
                    thickness_list.append(i.strip())
                    
                    
                if 'Size' in i:
                    display_list.append(i)
                    
                if 'Rear' in i or 'Front' in i:
                     yu=yu+i+" "
                if 'MT' in i and 'Core' in i:
                     processor_list.append(i)
                     
                if 'mAh' in i:
                     battery_list.append(i)
                if'RAM' in i or 'ROM' in i:
                    cb=cb+i+' '
                    
            camera_list.append(yu)

            memory_list.append(cb)
    else:
        print(x)
        country.append("CHINA")
        company.append("GIONEE")
        specs.append("NOT AVAILABLE")
        camera_list.append("NOT AVAILABLE")
        display_list.append("NOT AVAILABLE")
        memory_list.append("NOT AVAILABLE")
        battery_list.append("NOT AVAILABLE")
        thickness_list.append("NOT AVAILABLE")
        
        processor_list.append("NOT AVAILABLE")
        extras_links.append(x)
                            
##for i in urls:
##    print(i)
mods=[]
mods1=[]
for i in model1:
    if i=='Marathon M5 Lite (CDMA)':
        pass
    elif i=="F103 (3GB)":
        pass
    elif i=='F103 (2GB)':
        pass
    else:
        mods.append(i)
mods.append("f103")
##for n in display_list:
##    print(n)
##    if n.startswith(" "):
##       n=n.replace(" ","NA")
print(display_list)
print(len(country))
print(len(company))
print(len(mods))
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
    records.append((country[i], company[i], mods[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,'gionee-'+str(today)+'.csv'), index=False, encoding='utf-8')



        
