import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import sys
#from PyQt4.QtGui import QApplication
#from PyQt4.QtCore import QUrl
#from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import os
import datetime


###############################################################
path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'
###############################################################
base_url = 'http://ulefone.com/product.html'
country = 'China'
company = 'Ulefone'
user_agent = {'User-Agent':'Mozilla/5.0'}
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
specs=[]
st_list_heads=[]
st_list_dets=[]
r=requests.get(base_url, headers=user_agent)
soup=BeautifulSoup(r.text,'html.parser')

results=soup.find_all('div',attrs={'class':'row row-box product-row'})

#print(len(results))
for i in range(len(results)):
    ss=results[i].find_all('div',attrs={'id':'4G'})
    for u in range(len(ss)):
        st=ss[u].find_all('div',attrs={'class':'col-sm-12 col-lg-6 col-xl-3 product-item'})
        #print(len(st))
        for a in range(len(st)):
            sm=st[a].find_all('div',attrs={'class':'product-item-desc'})
            model_list.append(sm[0].find('h3').text)
            sa=st[a].find_all('div',attrs={'class':'row'})
            href.append(sa[1].find('a')['href'])
            su=st[a].find_all('div',attrs={'class':'f-sm'})
            if su[0].text.strip()!='':
                usp.append(su[0].text.strip().replace('\r', ' ').replace('\t', ' ').replace('\n', ' '))
            else:
                usp.append('Not Available')
#print(usp)
for x in range(len(usp)):
    usp[x]=usp[x].replace('\r',' ')
    usp[x]=usp[x].replace('\n',' ')
    usp[x]=usp[x].replace('\t',' ')
for i in range(len(href)):
    s=''
    s_alt = []
    href[i]=href[i].replace('features','spec')
    r=requests.get(href[i], headers=user_agent)
    soup=BeautifulSoup(r.text,'html.parser')
    heads=[]
    dets=[]
    try:   
        results=soup.find_all('div',attrs={'id':'vproduct-para-contain'})
        if len(results)==0:  ###FOR LATTER MODELS
            results1=soup.find_all('div',attrs={'class':'content'})
            sp=results1[0].find_all('table',attrs={'class':'spec'})
            for a in range(len(sp)-1):
                ss=sp[a].find_all('tr')
                for b in range(len(ss)):
                    s=s+ss[b].text.strip()
                    s=s.replace('\t',' ')
                    s=s.replace('\r',' ')
                    s=s.replace('\n',' ')
                    sc=ss[b].find_all('td')

                    if sc:
                        heads.append(sc[0].text.strip())
                        dets.append(sc[2].text.strip())
                        ##################### MAY BE ERRATIC ###########################
                        s_alt.append(sc[0].text.strip() + ' : ' + sc[2].text.strip())
                        ################################################################
     

        else:   ### FOR EARLIER MODELS
            #print('IN ELSE.')
            sp=results[0].find_all('div',attrs={'class':'vproduct-para-contain hasmore-color'})
            for m in range(len(sp)):
                sa=sp[m].find_all('div',attrs={'class':'vpro-para-section cl'})
                for b in range(len(sa)):
                    ss=sa[b].find_all('div',attrs={'class':'vpro-parasec-info'})
                    for c in range(len(ss)):
                        sc=ss[c].find_all('dd',attrs={'class':'cl'})
                        for d in range(len(sc)):
##                            s=s+sc[d].text.strip() + ' || '
##                            s=s.replace('\t',' ')
##                            s=s.replace('\n',' ')
                            s_alt.append(sc[d].text.strip().replace('\t', ' ').replace('\n', ' '))
        #specs.append(s)
        specs.append(s_alt)                    

        if heads!=[]:
            st_list_heads.append(heads)
        if dets!=[]:
            st_list_dets.append(dets)
    except:
      results1=soup.find_all('div',attrs={'class':'vpro-para-section cl'})


for i in range(len(specs)):
    dd = ''
    cc = ''
    mm = ''
    for j in range(len(specs[i])):
        if 'thickness' in specs[i][j].lower() or 'dimensions' in specs[i][j].lower():
            thickness_list.append(specs[i][j].strip().replace('Thickness',''))
        if 'battery' in specs[i][j].lower() and len(battery_list)==i and 'mAh' in specs[i][j]:
            battery_list.append(specs[i][j].strip().replace('Battery',''))
        if 'size' in specs[i][j].lower() or 'resolution' in specs[i][j].lower():
            dd = dd + specs[i][j].strip().replace('Size','Size -').replace('Resolution','Resolution -') + ' || '
        if 'rear camera' in specs[i][j].lower() or 'front camera' in specs[i][j].lower():
            cc = cc + specs[i][j].strip().replace('Rear camera','Rear camera -').replace('Front camera','Front camera -').replace('ƒ/',' ').replace('（','(').replace('）',')').replace(' （','(').replace('）',')') + ' || '
        if ('cpu' in specs[i][j].lower() or 'GHz' in specs[i][j]) and 'GPU' not in specs[i][j] and len(processor_list)==i:
            processor_list.append(specs[i][j].strip())
        if 'storage capacity' in specs[i][j].lower() or 'RAM' in specs[i][j] or 'ROM' in specs[i][j]:
            mm = mm + specs[i][j].strip() + ' || ' 
    if dd!='':
        display_list.append(dd)
    if cc!='':
        camera_list.append(cc)
    if mm!='':
        memory_list.append(mm)
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(thickness_list)==i:
        thickness_list.append('Not Available')



        

print(len(model_list))
print(len(usp))
print(len(thickness_list))
print(len(processor_list))
print(len(memory_list))
print(len(battery_list))
print(len(display_list))
print(len(camera_list))

extras_links = href

for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'ulefone-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf_8_sig')
#####################################################################################################################################

