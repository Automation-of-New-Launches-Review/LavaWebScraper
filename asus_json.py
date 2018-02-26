import requests
import json
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime

url = 'https://www.asus.com/in/OfficialSiteAPI.asmx/GetModelResults?WebsiteId=5&ProductLevel2Id=1&FiltersCategory=&Filters=&Sort=3&PageNumber=1&PageSize=20'
url2 = 'https://www.asus.com/in/OfficialSiteAPI.asmx/GetModelResults?WebsiteId=5&ProductLevel2Id=1&FiltersCategory=&Filters=&Sort=3&PageNumber=2&PageSize=20'
model_list = []
href = []
country = 'TAIWAN'
company = 'ASUS'
thickness_list = []
processor_list = []
display_list = []
memory_list = []
battery_list = []
camera_list = []
records = []

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'

pdhashedid_list = []
usp = []
payload = {
    #"Host": "www.mywbsite.fr",
    "Connection": "keep-alive",
    "Content-Length": 129,
    #"Origin": "https://www.mywbsite.fr",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Referer": "https://www.asus.com/in/OfficialSiteAPI.asmx/GetHotProduct?WebsiteId=5&ProductLevel2Id=1&ProductLevel3Id=0",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    #"Cookie": "ASP.NET_SessionId=j1r1b2a2v2w245; GSFV=FirstVisit=; GSRef=https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CHgQFjAA&url=https://www.mywbsite.fr/&ei=FZq_T4abNcak0QWZ0vnWCg&usg=AFQjCNHq90dwj5RiEfr1Pw; HelpRotatorCookie=HelpLayerWasSeen=0; NSC_GSPOUGS!TTM=ffffffff09f4f58455e445a4a423660; GS=Site=frfr; __utma=1.219229010.1337956889.1337956889.1337958824.2; __utmb=1.1.10.1337958824; __utmc=1; __utmz=1.1337956889.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
}
# Adding empty header as parameters are being sent in payload
headers = {}
#r = requests.post(url, data=json.dumps(payload), headers=headers).json()

##x = 1
##while True:
##    resp = requests.get('https://www.asus.com/in/OfficialSiteAPI.asmx/GetModelResults?WebsiteId=5&ProductLevel2Id=1&FiltersCategory=&Filters=&Sort=3&PageNumber=' + str(x) + '&PageSize=20').json()
##    print('https://www.asus.com/in/OfficialSiteAPI.asmx/GetModelResults?WebsiteId=5&ProductLevel2Id=1&FiltersCategory=&Filters=&Sort=3&PageNumber=' + str(x) + '&PageSize=20')    
##    hotprolist = resp["Result"]["Obj"]
##    for i in range(len(hotprolist)):
##        ts = ""
##        print('-----------------------------------------------------------------------------------------------------------------------------------------------')
##        model_list.append(hotprolist[i]["PDMarketName"])
##        href.append(hotprolist[i]["Url"])
##        pdhashedid_list.append(hotprolist[i]["PDHashedId"])
##        st = hotprolist[i]["BusinessPDSlogan"]
##        match = re.findall(r'<li>.+?</li>', st)
##        for k in range(len(match)):
##            ts = ts + match[k].strip('<li>').strip('</li>') + ' || '
##        usp.append(ts)
##        
##        
##
##    x = x + 1




r = requests.get(url).json()
r1 = requests.get(url2).json()
hotprolist = r["Result"]["Obj"]
hotprolist2 = r1["Result"]["Obj"]
for i in range(len(hotprolist)):
    ts = ""
    model_list.append(hotprolist[i]["PDMarketName"])
    href.append(hotprolist[i]["Url"])
    pdhashedid_list.append(hotprolist[i]["PDHashedId"])
    st = hotprolist[i]["BusinessPDSlogan"]
    match = re.findall(r'<li>.+?</li>', st)
    for k in range(len(match)):
        ts = ts + match[k].strip('<li>').strip('</li>') + ' || '
    usp.append(ts.replace('°','').replace(u'\u02da',''))
for j in range(len(hotprolist2)):
    ts = ""
    model_list.append(hotprolist2[j]["PDMarketName"])
    href.append(hotprolist2[j]["Url"])
    pdhashedid_list.append(hotprolist2[j]["PDHashedId"])
    st = hotprolist2[j]["BusinessPDSlogan"]
    match = re.findall(r'<li>.+?</li>', st)
    for k in range(len(match)):
        ts = ts + match[k].strip().strip('<li>').strip('</li>') + ' || '
    if not ts.startswith(''):
        usp.append(ts.replace('°','').replace(u'\u02da',''))
    else:
        usp.append('Not Available')




for m in model_list:
    print(m)
for i in range(len(href)):
    if 'https:' not in href[i]:
        href[i] = 'https:' + href[i]



################################## SPECIFICATIONS PART #################################################
for i in range(len(href)):
    print(href[i])
    mm = 'RAM / ROM : '
    cc = 'Rear / Front : '
    try:
        st = 'https://www.asus.com/in/GetData.asmx/getProductSpecByHashedid?param=' + pdhashedid_list[i] + ',1,0'
        r = requests.get(st)
    except:
        print('ERROR OCCURRED : JSON U.R.L. INVALID')
    soup = BeautifulSoup(r.text, 'html.parser')
    s1 = soup.find_all('spec_item')
    for s in s1:
        ts1 = s.find('name').text.replace('<name>', '').replace('</name>', '').replace('<br>', ' | ').replace('<br/>', ' | ').replace('<strong>', ' ').replace('</strong>', ' ')
        ts2 = s.find('spec').text.replace('<spec>', '').replace('</spec>', '').replace('<br>', ' | ').replace('<br/>', ' | ').replace('<strong>', ' ').replace('</strong>', ' ')
        if 'Dimensions' in ts1:
            thickness_list.append(ts2.replace('°','').replace(u'\u02da',''))
        if 'Processor' in ts1:
            processor_list.append(ts2.replace('°','').replace(u'\u02da',''))
        if 'Display' in ts1:
            display_list.append(ts2.replace('°','').replace(u'\u02da',''))
        if 'Memory' in ts1 or 'Capacity' in ts1:
            mm = mm + ts2 + ' || '
        if 'Battery' in ts1:
            match = re.search(r'\d+\s*mAh', ts2)
            if match:
                stt = str(match.group())
            else:
                stt = 'Not Available'
            battery_list.append(stt.replace('°','').replace(u'\u02da',''))
        if 'Camera' in ts1:
            cc = cc + ts2 + ' || '
    if mm!='RAM / ROM : ':
        memory_list.append(mm.replace('°','').replace(u'\u02da',''))
    if cc!='Rear / Front : ':
        camera_list.append(cc.replace('°','').replace(u'\u02da',''))
    if len(thickness_list)==i:
        thickness_list.append('Not Available')
    if len(processor_list)==i:
        processor_list.append('Not Available')
    if len(display_list)==i:
        display_list.append('Not Available')
    if len(memory_list)==i:
        memory_list.append('Not Available')
    if len(battery_list)==i:
        battery_list.append('Not Available')
    if len(camera_list)==i:
        camera_list.append('Not Available')
    #if len(usp)==i:
        #usp.append('Not Available')


print(len(thickness_list))

print(len(processor_list))

print(len(display_list))

print(len(memory_list))

print(len(battery_list))

print(len(camera_list))


extras_links = href
for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today()) + '-asus' + '.csv'), index=False, encoding='utf-8')
