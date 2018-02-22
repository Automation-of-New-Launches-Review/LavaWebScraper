import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import datetime
import os
today=datetime.date.today()

camera=[]
model1=[]
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
class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()


    def on_page_load(self):
        self.app.quit()

url = 'https://www.meizu.com/in/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
link= soup.find('div', class_='meizu-header-sub-wrap').find_all('a')
for l in link:
    urls.append(l['href'])
    model.append(l.text.strip('\n\t'))
#print(model)
for u in urls:
    #print(u)
    r=requests.get(u)
    soup=BeautifulSoup(r.text,'html.parser')    
    links=soup.find_all('li',attrs={'class':'subnav-item-spec'})
    for i in links:
        tt=i.find_all('a')
        for u in tt:
            urls1.append('https://www.meizu.com'+u['href'])
#print(urls1)
for p in urls1:
    d=[]
    
    
    r=requests.get(p)
    soup=BeautifulSoup(r.text,'html.parser')    
    links=soup.find_all('div',attrs={'class':'desc-font-style'})
    spe=soup.find_all('div',attrs={'class':'banner-left-top clearfix'})
    if links:
        print(p)
        country.append("CHINA")
        company.append("MEIZU")
        #print("inside if")
        extras_links.append(p)
        #specs.append("NA")
        for i in links:
            tt=i.find_all('p')
            for u in tt:
                d.append(u.text.strip('\n').replace('\n',' '))
        kt=' '
        pt=' '
        for x in d:
            if "mAH" in x or "mAh" in x:
                battery_list.append(x)
            if "inch" in x:
                display_list.append(x)
            
            if "processor" in x or "Processor" in x or 'PROCESSOR' in x or 'MT' in x:
                processor_list.append(x)
                    #print("________")
   
            if "megapixels" in x  or "Megapixels" in x or "megapixel" in x  :
                kt=kt+x+"  "
    
   
    
            if "Thickness " in x or 'thickness ' in x or "THICKNESS" in x:
                thickness_list.append(x)

            if "GB" in x:
                pt=pt+x+" "
        

        camera_list.append('rear/front: '+kt)
        #print("______")
        memory_list.append(pt)
    if spe:
        l=" "
        for z in spe:
            tt=z.find_all('div',attrs={'class':'t2'})
            for n in tt:
                l=l+n.text.replace('<br>'," ").replace('\n',' ').strip()+'||'
        print(l)
        specs.append(l)
                          
                          
        





for i in model:
    if i=='PRO 7':
        pass
    else:
        model1.append(i)


for i in camera_list:
    s=" "
    
    match=re.findall(r'\d+-megapixel',i)
    if not match:
        match=re.findall(r'\d+\s+megapixels',i)
        if not match:
            match=re.findall(r'\d+\s+megapixel',i)
            if not match:
                camera.append("NOT AVAILABLE")
    for k in match:
        s=s+k+"  "
    #print(s)
    camera.append("REAR/FRONT: "+ s)
                
            

print(len(country))
print(len(company))
print(len(model1))
print(len(specs))
print(len(display_list))
print(len(camera))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))
#print(camera_list)

records=[]
for i in range(len(country)):
    records.append((country[i], company[i], model1[i], specs[i], display_list[i], camera[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

path='C:\\LavaWebScraper\\BrandWiseFiles\\'
df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,'meizu-'+str(today)+'.csv'), index=False, encoding='utf-8')


    

