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

base_url = 'http://www.doogee.cc/category/mobile'
ur='http://www.doogee.cc'
country = 'SPAIN'
company = 'DOOGEE'
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
mod=[]
hre=[]
spec_url=[]
index_list=[]
qw=[]
HREF=[]
MODEL_LIST=[]
HR=[]
USP=[]
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'plane'})
#print(len(results))
for i in range(len(results)):
    sa=results[i].find_all('li')
    for a in range(len(sa)):
##        href.append(sa[a].find('a')['href'])
##        model_list.append(sa[a].find('h3').text.strip())
        href.append(sa[a].find('a')['href'])
        model_list.append(sa[a].find('h3').text.strip())
for i in range(len(href)):
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'subMenu'})
    for a in range(len(results)):
        sa=results[a].find_all('li')
        for b in range(len(sa)):
            sb=sa[b].find_all('a')
            for c in range(len(sb)):                
                if 'Specifications' in sb[c].contents[1] or 'SPEC' in sb[c].contents[1]:
                    hr.append(sb[c]['href'])
                    index_list.append(i)

i = 0
while i<len(model_list):
    if i not in index_list:
        model_list.pop(i)
    i=i+1

for i in range(len(hr)):
    u=''
    if ur not in hr[i]:
        hr[i]=href[i]+hr[i]
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('ul',attrs={'class':'clearfix'})
    if len(results) ==1:
        for a in range(len(results)):
            sa=results[a].find_all('li')
            for b in range(len(sa)):
                u=u + (sa[b].text.strip().replace('<small>',' ').replace('</small>',' ').replace('\n',' ')+' || ')
        usp.append(u)
    else:
        usp.append('Not Available')
#print(len(usp))
##for i in usp:
##    print(i)
for i in range(len(hr)):
    c1=''
    d1=''
    m1=''
    r=requests.get(hr[i])
    soup=BeautifulSoup(r.text,'html.parser')
    try:
        results=soup.find_all('div',attrs={'id':'spc'})
        if len(results)!=0:
            for a in range(len(results)):
                sa=results[a].find_all('div',attrs={'class':'container'})
                for b in range(len(sa)):
                    sb=sa[b].find_all('div',attrs={'class':'col-md-4 spc-title'})
                    #############################################################
                    if len(sb)!=0:
                        for c in range(len(sb)):
                            if 'dimension' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-6'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-6'})
                                for d in range(len(sc)):
                                    if 'thickness' in sc[d].text.lower():
                                        thickness_list.append(sd[d].text.replace('\n', ' ').replace('<br>', ' '))
                            if 'appearance' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-6'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-6'})
                                for d in range(len(sc)):
                                    if 'dimension' in sc[d].text.lower():
                                        match = re.search(r'\d?\.\d+\s*mm', sd[d].text)
                                        if match:
                                            ts = str(match.group())
                                        else:
                                            ts = 'Not Available'
                                        thickness_list.append(ts)
                            if 'memory' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-6'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-6'})
                                for d in range(len(sc)):
                                    if 'ram' in sc[d].text.lower() or 'rom' in sc[d].text.lower():
                                        m1=m1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '
                            
                            if 'basic parameter' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-6'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-6'})
                                for d in range(len(sc)):
                                    if 'processor' in sc[d].text.lower():
                                        processor_list.append(sd[d].text.replace('\n', ' ').replace('<br>', ' '))
                                    if 'ram' in sc[d].text.lower() or 'rom' in sc[d].text.lower():
                                        m1=m1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '
                                    if 'battery' in sc[d].text.lower():
                                        match = re.search(r'\d+\s*mAh', sd[d].text)
                                        if match:
                                            ts = str(match.group())
                                        else:
                                            ts = 'Not Available'
                                        battery_list.append(ts)

                            if 'display' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-6'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-6'})
                                for d in range(len(sc)):
                                    if 'size' in sc[d].text.lower() or 'type' in sc[d].text.lower() or 'aspect ratio' in sc[d].text.lower():
                                        d1=d1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '

                            if 'camera' in sb[c].text.lower():
                                camera_list.append(sa[b].text.replace('<br>', ' ').replace('\n', ' '))

                    else:
                        sb=sa[b].find_all('div',attrs={'class':'col-md-2 spc-title'})
                        for c in range(len(sb)):
                            if 'dimension' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-4'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-8'})
                                for d in range(len(sc)):
                                    if 'thickness' in sc[d].text.lower():
                                        thickness_list.append(sd[d].text.replace('\n', ' ').replace('<br>', ' '))
                            if 'appearance' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-4'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-8'})
                                for d in range(len(sc)):
                                    if 'dimension' in sc[d].text.lower():
                                        match = re.search(r'\d?\.\d+\s*mm', sd[d].text)
                                        if match:
                                            ts = str(match.group())
                                        else:
                                            ts = 'Not Available'
                                        thickness_list.append(ts)
                            if 'memory' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-4'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-8'})
                                for d in range(len(sc)):
                                    if 'ram' in sc[d].text.lower() or 'rom' in sc[d].text.lower():
                                        m1=m1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '
                            
                            if 'basic parameter' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-4'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-8'})
                                for d in range(len(sc)):
                                    if 'processor' in sc[d].text.lower():
                                        processor_list.append(sd[d].text.replace('\n', ' ').replace('<br>', ' '))
                                    if 'ram' in sc[d].text.lower() or 'rom' in sc[d].text.lower():
                                        m1=m1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '
                                    if 'battery' in sc[d].text.lower():
                                        match = re.search(r'\d+\s*mAh', sd[d].text)
                                        if match:
                                            ts = str(match.group())
                                        else:
                                            ts = 'Not Available'
                                        battery_list.append(ts)

                            if 'display' in sb[c].text.lower():
                                sc=sa[b].find_all('dt',attrs={'class':'col-sm-4'})
                                sd=sa[b].find_all('dd',attrs={'class':'col-sm-8'})
                                for d in range(len(sc)):
                                    if 'size' in sc[d].text.lower() or 'type' in sc[d].text.lower() or 'aspect ratio' in sc[d].text.lower():
                                        d1=d1+sc[d].text.replace('\n', ' ').replace('<br>', ' ')+':- '+sd[d].text.replace('\n', ' ').replace('<br>', ' ')+' || '

                            if 'camera' in sb[c].text.lower():
                                camera_list.append(sa[b].text.replace('<br>', ' ').replace('\n', ' '))
                        
                        

        else:
            cc = ''
            mm = ''
            dd = ''
            res2 = soup.find('div', attrs={'class':'container'}).find('table').find('tbody').find_all('tr')
            for y in range(len(res2)):
                res3 = res2[y].find_all('td')
                if 'appearance' in str(res3[0]).lower():
                    res4 = str(res3[1]).split('<br/>')
                    for r in res4:
                        if 'dimension' in r.lower():
                            thickness_list.append(r.strip().replace('\n','').replace('<td>', '').replace('</td>', ''))

                if 'basic parameters' in str(res3[0]).lower():
                    res4 = str(res3[1]).split('<br/>')
                    for r in res4:
                        if 'processor' in r.lower():
                            processor_list.append(r.strip().replace('\n','').replace('<td>', '').replace('</td>', ''))
                        if 'battery' in r.lower():
                            battery_list.append(r.strip().replace('\n', '').replace('<td>', '').replace('</td>', ''))

                if 'memory' in str(res3[0]).lower():
                    res4 = str(res3[1]).split('<br/>')
                    for r in res4:
                        if 'RAM' in r.lower():
                            mm = mm + 'RAM : ' + r.strip().replace('\n', '').replace('<td>', '').replace('</td>', '') + ' || '
                        if 'ROM' in r.lower():
                            mm = mm +  'ROM : ' + r.strip().replace('\n', '').replace('<td>', '').replace('</td>', '') + ' || '

                if 'camera' in str(res3[0]).lower():
                    res4 = str(res3[1]).split('<br/>')
                    for r in res4:
                        if 'rear camera' in r.lower():
                            cc = cc + 'Rear : ' + r.strip().replace('\n', '').replace('<td>', '').replace('</td>', '') + ' || '
                        if 'front camera' in r.lower():
                            cc = cc + 'Front : ' + r.strip().replace('\n', '').replace('<td>', '').replace('</td>', '') + ' || '

                if 'display' in str(res3[0]).lower():
                    res4 = str(res3[1]).split('<br/>')
                    for r in res4:
                        if 'size' in r.lower() or 'resolution' in r.lower():
                            dd = dd + r.strip().replace('\n', '').replace('<td>', '').replace('</td>', '') + ' || '

            if mm!='':
                memory_list.append(mm)
            if cc!='':
                camera_list.append(cc)
            if dd!='':
                display_list.append(dd)

    except:
        pass
    if m1!='':
        memory_list.append(m1)
    if d1!='':
        display_list.append(d1)
    if c1!='':
        camera_list.append(c1)
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(usp)==i:
        usp.append('Not Available')




######################################################################################################################################################################
extras_links = hr
print(len(model_list))
print(len(usp))
print(len(display_list))
print(len(camera_list))
print(len(memory_list))
print(len(battery_list))
print(len(thickness_list))
print(len(processor_list))
print(len(extras_links))
print(len(extras_links))
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

##for r in records:
##    print(r)

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'doogee-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
   
      

                   
                   
                   
                   
                   
