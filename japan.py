import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]


try:
    
    from sony import *
    net_records = net_records + records
except:
    error_list.append("SONY")
try:
    from maze import *
    net_records = net_records + records
except:
    error_list.append("MAZE")
try:
    from panasonic import *
    net_records = net_records + records
except:
    error_list.append("PANASONIC")


import pandas as pd

path='C:\\LavaWebScraper\\countrywise\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(JAPAN).csv'), index=False, encoding='utf-8')

