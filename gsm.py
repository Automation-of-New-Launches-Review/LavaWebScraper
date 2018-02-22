import datetime
import os
today=datetime.date.today()
net_records = []
error_list=[]


try:
    
    from gcelkon import *
    net_records = net_records + records
except:
    error_list.append("gcelkon")
try:
    from ghuawei import *
    net_records = net_records + records
except:
    error_list.append("ghuawei")
try:
    from glava import *
    net_records = net_records + records
except:
    error_list.append("glava")
try:
    from gmicromax import *
    net_records = net_records + records
except:
    error_list.append("gmicromax")
try:
    from gspice import *
    net_records = net_records + records
except:
    error_list.append("gspice.ice")
##try:
##    from gxolo import *
##    net_records = net_records + records
##except:
##    error_list.append("gxolo")
print(error_list)
import pandas as pd

path='C:\\LavaWebScraper\\GSMARENA\\'
df = pd.DataFrame(net_records, columns = ['COUNTRY','COMPANY', 'MODEL', 'PRICE','LAUNCH DATE', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path,str(today)+'(GSM(FULL)).csv'), index=False, encoding='utf-8')


