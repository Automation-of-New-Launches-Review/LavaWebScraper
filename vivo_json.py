import requests
import json
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime

path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles\\'


base_url = 'https://www.vivo.com/en/vivorestapi/products'
model_list = []
href = []
country = 'VIVO'
company = 'CHINA'
thickness_list = []
processor_list = []
display_list = []
memory_list = []
battery_list = []
camera_list = []
records = []
usp = []

r = requests.get(base_url).json()
hotprolist = r["data"]
for i in range(len(hotprolist)):
    model_list.append(hotprolist[i]["name"])
    href.append('https://www.vivo.com' + hotprolist[i]["url"])
    usp.append(hotprolist[i]["features"].replace('<p>', '').replace('</p>', ''))
    processor_list.append(hotprolist[i]["details"]["processor"])
    memory_list.append('RAM / ROM : ' + hotprolist[i]["details"]["ram"] + ' || ' + hotprolist[i]["details"]["storage"])
    battery_list.append(hotprolist[i]["details"]["battery"])
    display_list.append(hotprolist[i]["details"]["Display Size"].replace('&quot;', "''").replace('&#039;', "'").replace("ï¼š", " ").replace('ï¼š', ' ').replace(':', ' ') + ' || ' + hotprolist[i]["details"]["Display Type"])
    camera_list.append(hotprolist[i]["details"]["camera"])
    thickness_list.append(hotprolist[i]["details"]["dimensions"])


extras_links = href

for i in range(len(model_list)):
    records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_brandwise, str(datetime.date.today())+'-vivo'+'.csv'), index=False, encoding='utf-8')

