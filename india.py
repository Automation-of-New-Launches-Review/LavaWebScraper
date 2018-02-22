import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]


try:
    
    from zen import *
    net_records = net_records + records
except:
    error_list.append("ZEN")
try:
    from intex import *
    net_records = net_records + records
except:
    error_list.append("INTEX")
try:
    from karbonn import *
    net_records = net_records + records
except:
    error_list.append("KARBONN")
try:
    from lyf import *
    net_records = net_records + records
except:
    error_list.append("LYF")
try:
    from ziox import *
    net_records = net_records + records
except:
    error_list.append("ZIOX")
try:
    from billion import *
    net_records = net_records + records
except:
    error_list.append("BILLION")

import pandas as pd

path='C:\\LavaWebScraper\\countrywise\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(INDIA).csv'), index=False, encoding='utf-8')

