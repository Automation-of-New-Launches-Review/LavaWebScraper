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
class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()


    def on_page_load(self):
        self.app.quit()
        
base_url = 'http://bluboohk.com/products/'
country = 'USA'
company = 'BLUBOO'
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
hrr=[]
shref=[]

url =base_url
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
res = soup.find('div', class_='container-fluid').find('div', class_='row').find('div', class_='entry-content')
ts = str(res)
while True:
    match = re.search(r'href=".+?">', ts)
    if match:
        hrr.append(str(match.group()))
        ts = ts.replace(str(match.group()), ' ')
    else:
        break
for h in hrr:
    h = h.replace('href="','')
    h = h.replace('">', '')
hr=hrr[7:]
for i in range(len(hrr)):
    if hrr[i] not in hr and hrr[i] not in href:
        href.append(hrr[i].replace('href="','').replace('">',''))

for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'wpsm_nav wpsm_nav-tabs'})
    if(len(results)) !=0:
        for a in range(len(results)):
            sa=results[a].find_all('li',attrs={'role':'presentation'})
            for b in range(len(sa)):
                if 'parameter' in sa[b].find('span').text.lower():
                    shref.append(sa[b].find('a')['href'])
    else:
        shref.append('')



for i in range(len(href)):
    shref[i]=href[i]+shref[i]

for i in range(len(shref)):
    cc = 'REAR / FRONT : '
    heads=[]
    dets=[]
    super_dets=[]
    r=requests.get(shref[i])
    soup=BeautifulSoup(r.text,'html.parser')
    try:
        results=soup.find_all('div',attrs={'class':'section group'})
        for a in range(len(results)):
            sa=results[a].find_all('span',attrs={'class':'h3'})
            sb=results[a].find_all('span',attrs={'style':'line-height:35px;font-size:13px;'})
            for b in range(len(sa)):
                heads.append(str(sa[b]))
            for c in range(len(sb)):
                dets.append(str(sb[c]))
        for j in range(len(dets)):
            dets[j] = dets[j].replace('<span style="line-height:35px;font-size:13px;">', '').replace('</span>', '').strip()
            childd = dets[j].split('<br/>')
            for c in childd:
                c = c.strip().strip('\r\n')
            super_dets.append(childd)
        for d in range(len(super_dets)):
            for e in range(len(super_dets[d])):
                super_dets[d][e] = super_dets[d][e].strip().strip('\r\n').strip('\r\n').strip()

        ### NOW SCRAPING THE DETAILS WITH THE HELP OF HEADS.
        for j in range(len(heads)):
            for k in range(len(super_dets[j])):
                if 'Basic Information' in heads[j]:
                    if 'Model' in super_dets[j][k]:
                        model_list.append(super_dets[j][k].replace('Model: ', ' '))
                    if 'Battery' in super_dets[j][k]:
                        battery_list.append(super_dets[j][k])
                    if 'Ram + Rom' in super_dets[j][k] or 'RAM + ROM' in super_dets[j][k]:
                        memory_list.append('RAM/ROM:- ' + super_dets[j][k])
                    if 'Depth' in super_dets[j][k]:
                        match = re.search(r'Depth:\s*\d+\.*\d*\s*mm', super_dets[j][k])
                        if match:
                            st = str(match.group())
                        else:
                            st = 'Not Available'
                        thickness_list.append(st)
                    if 'Systerm' in super_dets[j][k]:
                        processor_list.append(super_dets[j][k])
                if 'Rear Camera' in heads[j] or 'Front Camera' in heads[j]:
                    match = re.search(r'\d+\.*\d*\s*MP', super_dets[j][k])
                    if match:
                        st = 'Rear Camera:- ' + str(match.group())
                    else:
                        st = 'Not Available'
                    cc = cc + st + ' || '
            if 'Display' in heads[j]:
                display_list.append(super_dets[j][0] + ' || ' + super_dets[j][2])

    except:
        pass
    
    if cc!='':
        camera_list.append(cc)
    if len(model_list)==i:
        model_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(usp)==i:
        usp.append('Not Available')
        
                

print(len(display_list))

print(len(camera_list))

print(len(processor_list))

print(len(thickness_list))

print(len(battery_list))

print(len(memory_list))


extras_links = href

############# WRITING TO CSV : DO NOT MAKE ANY CHANGES TO THIS PART EXCEPT WRITING THE FILE Not AvailableME. ###################################
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+ '-bluboo' +'.csv'), index=False, encoding='utf-8')
#####################################################################################################################################            



