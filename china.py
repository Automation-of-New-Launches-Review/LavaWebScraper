import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]
try:
    
    from zte import *
    net_records = net_records + records
except:
    error_list.append("ZTE")
try:
    from nubia import *
    net_records = net_records + records
except:
    error_list.append("nubia")
try:
    from meiigoo import *
    net_records = net_records + records
except:
    error_list.append("MEIIGOO")
try:
    from motointernational import *
    net_records = net_records + records
except:
    error_list.append("MOTOROLA")
try:
    from vivo_json import *
    net_records = net_records + records
except:
    error_list.append("VIVO")
try:
    from oppo import *
    net_records = net_records + records
except:
    error_list.append("OPPO")
try:
    from itel_international import *
    net_records = net_records + records
except:
    error_list.append("ITEL")
try:
    from lenovo import *
    net_records = net_records + records
except:
    error_list.append("LENOVO")
try:
    from huwaei import *
    net_records = net_records + records
except:
    error_list.append("HUWAEI")
try:
    from Oneplusu import *
    net_records = net_records + records
except:
    error_list.append("ONEPLUS")
try:
    from tecno import *
    net_records = net_records + records
except:
    error_list.append("TECNO")
try:
    from agm import *
    net_records = net_records + records
except:
    error_list.append("AGM")
try:
    from allcall import *
    net_records = net_records + records
except:
    error_list.append("ALLCALL")
try:
    from gionee import *
    net_records = net_records + records
except:
    error_list.append("GIONEE")
try:
    from Infinix import *
    net_records = net_records + records
except:
    error_list.append("INFINIX")
try:
    from ivoomi import *
    net_records = net_records + records
except:
    error_list.append("IVOOMI")
try:
    from innjoo import *
    net_records = net_records + records
except:
    error_list.append("INNJOO")
try:
    from umidigi import *
    net_records = net_records + records
except:
    error_list.append("UMIDIGI")
try:
    from voto import *
    net_records = net_records + records
except:
    error_list.append("VOTO")
try:
    from zopo import *
    net_records = net_records + records
except:
    error_list.append("ZOPO")
try:
    from  xiaomi import *
    net_records = net_records + records
except:
    error_list.append("XIAOMI")
#from meizu import *
#net_records = net_records + records 

import pandas as pd

path='C:\\LavaWebScraper\\countrywise\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(CHINA).csv'), index=False, encoding='utf-8')
