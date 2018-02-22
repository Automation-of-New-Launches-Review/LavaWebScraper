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
urls3=[]
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
url="https://oneplusstore.in/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')    
sp=soup.findAll('a', text = re.compile('OnePlus'))
for x in sp:
    urls1.append(x['href'])
for i in range(0,(len(urls1)-2)):
    urls.append(urls1[i])

#x=list(set(urls))
for ui in urls:
    if ui in urls3:
        pass
    else:
        urls3.append(ui)
        
for ae in urls3:
    lt=''
    r=requests.get(ae)
    soup=BeautifulSoup(r.text,'html.parser')    
    spo=soup.findAll('h2')
    for t in spo:
        lt=lt+t.text.strip()+" "
    if lt in specs:
        pass
    else:
        specs.append(lt)
    
for z in urls3:
    r=requests.get(z)
    soup=BeautifulSoup(r.text,'html.parser')    
    spo=soup.findAll('a', text = re.compile('Specs'))
    for k in spo:
        if k['href']=='#':
            urls2.append(z)
        else:
            urls2.append(k['href'])
for v in urls2:
    country.append("CHINA")
    company.append("OnePlus")
    #specs.append("NA")
    r=requests.get(v)
    soup=BeautifulSoup(r.text,'html.parser')    
    rr=soup.find_all('div', attrs={'class':'item-box'})#one5t
    oo=soup.find_all('div', attrs={'class':'props flex'})#one5
    nn=soup.find_all('div', attrs={'class':'col-sm-8'})#3,3t
    fivtit=soup.find_all('div', attrs={'class':'menus'})
    thrm=soup.find_all('a', attrs={'class':'nav-title'})
    
    if rr:
        st=' '
        data=[]
        print(v)
        for h in fivtit:
            nx=h.find('h2')
            model.append(nx.text.strip())
            extras_links.append(v)
        for df in rr:
            tt=df.find_all('p')
            for xc in tt:
                for jk in xc:
                    data.append(jk)
        for q in data:
            if 'inches' in q:
                display_list.append(q.strip())
            
            if 'GB LPDDR4X' in q:
                memory_list.append("RAM: "+q.strip())
            if 'Snapdragon™' in q and 'GHz' in q:
                processor_list.append(q.strip())
                #print("_______")
                #print(display_list)
            if 'Megapixels' in q:
                st=st+q.strip()+" "
            if 'mAh' in q:
                battery_list.append(q.strip())
            if 'mm' in q and('*' in q or 'x' in q):
                thickness_list.append(q.strip())
        camera_list.append("rear/front:"+st)       
    elif oo:
        data2=[]
        no=''
        print(v)
        for h in fivtit:
            model.append('OnePlus 5')
            extras_links.append(v)
        for ui in oo:
            tt=ui.find_all("p")
            for y in tt:
                data2.append(y.text.strip())
        for e in data2:
            if 'inches' in e and  'Resolution' not in e:
                display_list.append(e.strip())
                
            if 'GB LPDDR4X' in e:
                memory_list.append("RAM: "+e.strip())
            if 'Snapdragon™' in e and 'GHz' in e:
                processor_list.append(e.strip())
                #print("_______")
                #print(display_list)
            if 'Megapixels' in e:
                no=no+e.strip()+" "
            if 'mAh' in e:
                battery_list.append(e.strip())
            if 'mm' in e and('*' in e or 'x' in e):
                thickness_list.append(e.strip())
        camera_list.append("rear(wideangle|telephoto)/front:"+no)      
    elif nn:
        data3=[]
        yo=''
        print(v)
        for ls in thrm:
            model.append(ls.text)
            extras_links.append(v)
        for hp in nn:
            tt=hp.find_all('div')
            for z in tt:
                for k in z:
                    data3.append(k)
#print(data3)
    
        for en in data3:
            if ('inches' in en or 'inch' in en or '”' in en)and 'Resolution' not in en:
                display_list.append(en.strip())
                
            if 'GB LPDDR4X' in en or"GB LPDDR4" in en:
                memory_list.append("RAM: "+en.strip())
            if 'Snapdragon™' in en:
                processor_list.append(en.strip())
                #print("_______")
                #print(processor_list)
            if 'MP' in en and 'MHz' not in en and 'MP3' not in en and 'MPE' not in en and 'JPEG' not in en and 'PN' not in en and 'BMP' not in en:
                yo=yo+en.strip()+" "
            if 'mAh' in en:
                battery_list.append(en.strip())
            if 'mm' in en and('*' in en or 'x' in en):
                thickness_list.append(en.strip())
        camera_list.append("rear(wideangle|telephoto)/front:"+yo)
    else:
        model.append.append('NOT AVAILABLE')
        specs.append.append('NOT AVAILABLE')
        display_list.append('NOT AVAILABLE')
        camera_list.append('NOT AVAILABLE')
        memory_list.append('NOT AVAILABLE')
        battery_list.append('NOT AVAILABLE')
        thickness_list.append('NOT AVAILABLE')
        processor_list.append('NOT AVAILABLE')
        extras_links.append('NOT AVAILABLE')



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
df.to_csv(os.path.join(path,'Oneplus-'+str(today)+'.csv'), index=False, encoding='utf-8')





        
    


