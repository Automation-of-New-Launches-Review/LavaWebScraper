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
user_agent = {'User-agent':'Mozilla/5.0'}
base_url = 'http://www.htc.com/in/smartphones/'
ur='http://www.htc.com'
country = 'TAIWAN'
company = 'HTC'
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
r=requests.get(base_url, headers=user_agent)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'product-list comparison'})
#print(len(results))
for a in range(len(results)):
    sa=results[a].find_all('div',attrs={'class':'item'})
    #print(len(sa))
    for b in range(len(sa)):
        href.append(sa[b].find('a')['href'])
        model_list.append(sa[b].find('div',attrs={'class':'name'}).text)
##print(len(href))
##print(len(model_list))
for i in range(len(href)):
    href[i]=ur+href[i]
    
for i in range(len(href)):
    #print(href[i])
    m1=''
    d1=''
    b1=''
    p1=''
    c1='MAIN / FRONT : '
    r=requests.get(href[i])
    soup=BeautifulSoup(r.text,'html.parser')
    results=soup.find_all('div',attrs={'class':'specs-list'})
    #print(len(results))
    for a in range(len(results)):
        sa=results[a].find_all('ul')
        #print(len(sa))
        for b in range(len(sa)):
            sb=sa[b].find_all('li',attrs={'class':''})
            sc=sa[b].find_all('li',attrs={'class':'mobile-hide'})
            #print(sb)
            for c in range(len(sb)):
                sd=sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'dimension' in sd[d].text.lower() or 'size' in sd[d].text.lower():
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            thickness_list.append(se[e].text)
            for f in range(len(sc)):
                sf=sc[f].find_all('h4')
                for g in range(len(sf)):
                    if 'dimension' in sf[g].text.lower() or 'size' in sf[g].text.lower():
                        sg=sc[f].find_all('span',attrs={'class':'long'})
                        for h in range(len(sg)):
                            thickness_list.append(sg[h].text.replace(',  ',','))
            for c in range(len(sb)):
                sd=sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'memory' in sd[d].text.lower():
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            ts = se[e].text.strip().replace('<br>', ' ').replace('<br/>', ' ').replace('\n', ' ')
                            ram_match = re.search(r'RAM\s*:\s*\d+\s*GB', ts)
                            if ram_match:
                                m1 = m1 + str(ram_match.group()) + ' || '
                            else:
                                m1 = m1 + 'RAM : Not Available ||'
                            rom_match = re.search(r'ROM\s*:\s*\d+\s*GB', ts)
                            if rom_match:
                                m1 = m1 + str(rom_match.group()) + ' || '
                            else:
                                rom_match = re.search(r'Total storage:\s*\d+\s*GB', ts)
                                if rom_match:
                                    m1 = m1 + str(rom_match.group()) + ' || '
                                else:
                                    m1 = m1 + ' ROM : Not Available'
                            #m1+= ts
            for c in range(len(sb)):
                sd=sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'display' in sd[d].text.lower():
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            ts = se[e].text.strip().replace('<br>', ' ').replace('<br/>', ' ').replace('\n', ' ')
                            match = re.search(r'.+?\(', ts)
                            if match:
                                ts = str(match.group()).strip('(').strip().replace('®',' ')
                            else:
                                ts = se[e].text.strip().replace('<br>', ' ').replace('<br/>', ' ').replace('\n', ' ').replace('®',' ')
                            d1+= ts
            for c in range(len(sb)):
                sd=sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'battery' in sd[d].text.lower():
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            ts = se[e].text.strip()
                            match = re.search(r'\d+?\smAh', ts)
                            if match:
                                ts = str(match.group())
                            else:
                                ts = 'Not Available'
                            b1+= ts
            for c in range(len(sb)):
                sd=sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'cpu' in sd[d].text.lower():
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            p1+=se[e].text.strip().replace('™ ',' ').replace('®',' ')
            for c in range(len(sb)):
                sd = sb[c].find_all('h4')
                for d in range(len(sd)):
                    if 'camera' in sd[d].text.lower():
##                        print(i)
##                        print(model_list[i], end=' ')
##                        print('GOTCHA')
                        se=sb[c].find_all('span',attrs={'class':'long'})
                        for e in range(len(se)):
                            ts = se[e].text.strip().replace('<br>', ' ').replace('<br/>', ' ').replace('\n', ' ')
                            matches = re.findall(r'\d+\s*MP\s?', ts)
                            if len(matches)==2:
                                c1 += matches[0] + ' || ' + matches[1]
                            elif len(matches)==1:
                                c1 = c1 + matches[0] + ' || '
                            else:
                                match_alt = re.findall(r'\d+-megapixel', ts)
                                if len(match_alt)==2:
                                    c1 += match_alt[0] + ' || ' + match_alt[1]
                                elif len(match_alt)==1:
                                    c1 = c1 + match_alt[0] + ' || '
                                else:   
                                    c1 =  c1 + 'Not Available' + ' || '

            for e in range(len(sc)):
                sg = sc[e].find_all('h4')
                for l in range(len(sg)):
                    if 'camera' in sg[l].text.lower():
##                        print(i)
##                        print(model_list[i], end=' ')
##                        print('GOTCHA DIFFERENT.')
                        sx = sc[e].find_all('span', attrs={'class':'long'})
                        for k in range(len(sx)):
                            ts = sx[k].text.strip().replace('<br>',' ').replace('<br/>', ' ').replace('\n', ' ')
                            matches = re.findall(r'\d+\s*MP\s?', ts)
                            if len(matches)==2:
                                c1 += matches[0] + ' || ' + matches[1]
                            elif len(matches)==1:
                                c1 = c1 + matches[0] + ' || '
                            else:
                                match_alt = re.findall(r'\d+-megapixel', ts)
                                if len(match_alt)==2:
                                    c1 += match_alt[0] + ' || ' + match_alt[1]
                                elif len(match_alt)==1:
                                    c1 = c1 + match_alt[0] + ' || '
                                else:   
                                    c1 =  c1 + 'Not Available' + ' || '
                                
                        

    if m1!='':
        memory_list.append(m1)
    if d1!='':
        display_list.append(d1)
    if b1!='':
        battery_list.append(b1)
    if p1!='':
        processor_list.append(p1)
    if c1!='MAIN / FRONT : ':
        camera_list.append(c1)
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
                        
##                if 'dimension' in sb[c].find('h4').text.lower():
##                    sd=sb[c].find_all('span',attrs={'class':'short'})
##                    for d in range(len(sd)):
##                        thickness_list.append(sd[d].find('p').text)
print(len(thickness_list))
##for i in thickness_list:
##    print(i)
##print('----------------------------------------------------------------------------------------------------------------------------------------')
print(len(memory_list))
##for i in memory_list:
##    print(i)
##print('----------------------------------------------------------------------------------------------------------------------------------------')
print(len(display_list))
##for i in display_list:
##    print(i)
##print('----------------------------------------------------------------------------------------------------------------------------------------')
print(len(battery_list))
##for i in battery_list:
##    print(i)
##print('----------------------------------------------------------------------------------------------------------------------------------------')
print(len(processor_list))
##for i in processor_list:
##    print(i)
##print('----------------------------------------------------------------------------------------------------------------------------------------')
print(len(camera_list))
##for i in camera_list:
##    print(i)
print(len(usp))
extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, 'hTC-'+str(datetime.date.today()) +'.csv'), index=False, encoding='utf-8')
   
      
                    
                       
