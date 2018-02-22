import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]


try:
    
    from razer import *
    net_records = net_records + records
except:
    error_list.append("RAZER")
try:
    from caterpillar import *
    net_records = net_records + records
except:
    error_list.append("CATERPILLAR")
try:
    from bluboo import *
    net_records = net_records + records
except:
    error_list.append("BLUBOO")
try:
    from infocus import *
    net_records = net_records + records
except:
    error_list.append("INFOCUS")
try:
    from google import *
    net_records = net_records + records
except:
    error_list.append("GOOGLE")


import pandas as pd

path='C:\\LavaWebScraper\\countrywise\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(USA).csv'), index=False, encoding='utf-8')

