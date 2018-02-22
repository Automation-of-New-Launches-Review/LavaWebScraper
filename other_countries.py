import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]

try:
    
    from NOKIA1 import *
    net_records = net_records + records
except:
    error_list.append("NOKIA")
try:
    from lgmain import *
    net_records = net_records + records
except:
    error_list.append("LG")
try:
    from asus_json import *
    net_records = net_records + records
except:
    error_list.append("ASUS")
try:
    from archos import *
    net_records = net_records + records
except:
    error_list.append("ARCHOS")
try:
    from doogee import *
    net_records = net_records + records
except:
    error_list.append("DOOGEE")


import pandas as pd

path='C:\\LavaWebScraper\\countrywise\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(OTHER_COUNTRIES).csv'), index=False, encoding='utf-8')

