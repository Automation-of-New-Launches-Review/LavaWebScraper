
import datetime
import os
today=datetime.date.today()
net_records = []
error_list = []

########################################### SPECIFY HERE THE PATH WHERE THE D.U.C.s & D.C.C.s WILL BE SAVED. ########################################################
path_of_the_main_csv = 'C:\\LavaWebScraper\\Files\\'
path_of_the_duc_files = 'C:\\LavaWebScraper\\Daily_Updates\\'
path_of_master = 'C:\\LavaWebScraper\\MASTER\\'

#######################################################################################################################################################################

##print('NOW RUNNING : ', end='')
##print('MEIZU')
##try:
##    from meizu import *
##    net_records = net_records + records
##except:
##    error_list.append('MEIZU')

print('NOW RUNNING : ', end='')
print('INTEX')

from intex import *
net_records = net_records + records

error_list.append('INTEX')

##
print('NOW RUNNING : ', end='')
print('BLUBOO')
try:
    from bluboo import *
    net_records = net_records + records
except:
    error_list.append('BLUBOO')



print('NOW RUNNING : ', end='')
print('OPPO')

try:
    from oppo import *
    net_records = net_records + records
except:
    error_list.append('OPPO')


print('NOW RUNNING : ', end='')
print('AGM')
try:
    from agm import *
    net_records = net_records + records
except:
    error_list.append('AGM')


print('NOW RUNNING : ', end='')
print('ALLCALL')
try:
    from allcall import *
    net_records = net_records + records
except:
    error_list.append('ALLCALL')


print('NOW RUNNING : ', end='')
print('ARCHOS')
try:
    from archos import *
    net_records = net_records + records
except:
    error_list.append('ARCHOS')


print('NOW RUNNING : ', end='')
print('BILLION')
try:
    from billion import *
    net_records = net_records + records
except:
    error_list.append('BILLION')

##
print('NOW RUNNING : ', end='')
print('GIONEE')
try:
    from gionee import *
    net_records = net_records + records
except:
    error_list.append('GIONEE')

##
print('NOW RUNNING : ', end='')
print('HUAWEI')
try:
    from huwaei import *
    net_records = net_records + records
except:
    error_list.append('HUAWEI')
##
##
print('NOW RUNNING : ', end='')
print('INNJOO')
try:
    from innjoo import *
    net_records = net_records + records
except:
    error_list.append('INNJOO')


print('NOW RUNNING : ', end='')
print('ITEL')
try:
    from itel_international import *
    net_records = net_records + records
except:
    error_list.append('ITEL')


print('NOW RUNNING : ', end='')
print('IVOOMI')
try:
    from ivoomi import *
    net_records = net_records + records
except:
    error_list.append('IVOOMI')


print('NOW RUNNING : ', end='')
print('KARBONN')
try:
    from karbonn import *
    net_records = net_records + records
except:
    error_list.append('KARBONN')


print('NOW RUNNING : ', end='')
print('LG')
try:
    from lgmain import *
    net_records = net_records + records
except:
    error_list.append('LG')

##
print('NOW RUNNING : ', end='')
print('RELIANCE LYF')
try:
    from lyf import *
    net_records = net_records + records
except:
    error_list.append('RELIANCE LYF')
    



print('NOW RUNNING : ', end='')
print('NOKIA')
try:
    from NOKIA1 import *
    net_records = net_records + records
except:
    error_list.append('NOKIA')


print('NOW RUNNING : ', end='')
print('ONEPLUS')
try:
    from Oneplusu import *
    net_records = net_records + records
except:
    error_list.append('ONEPLUS')

##
print('NOW RUNNING : ', end='')
print('RAZER')
try:
    from razer import *
    net_records = net_records + records
except:
    error_list.append('RAZER')

##
print('NOW RUNNING : ', end='')
print('SONY')
try:
    from sony import *
    net_records = net_records + records
except:
    error_list.append('SONY')

##
print('NOW RUNNING : ', end='')
print('UMIDIGI')
try:
    from umidigi import *
    net_records = net_records + records
except:
    error_list.append('UMIDIGI')


print('NOW RUNNING : ', end='')
print('ZEN')
try:
    from zen import *
    net_records = net_records + records
except:
    error_list.append('ZEN')


print('NOW RUNNING : ', end='')
print('ZIOX')
try:
    from ziox import *
    net_records = net_records + records
except:
    error_list.append('ZIOX')


print('NOW RUNNING : ', end='')
print('ZTE')
try:
    from zte import *
    net_records = net_records + records
except:
    error_list.append('ZTE')


print('NOW RUNNING : ', end='')
print('GOOGLE')
try:
    from google import *
    net_records = net_records + records
except:
    error_list.append('GOOGLE')


print('NOW RUNNING : ', end='')
print('INFOCUS')
try:
    from infocus import *
    net_records = net_records + records
except:
    error_list.append('INFOCUS')





print('NOW RUNNING : ', end='')
print('LENOVO')
try:
    from lenovo import *
    net_records = net_records + records
except:
    error_list.append('LENOVO')


print('NOW RUNNING : ', end='')
print('MAZE')
try:
    from maze import *
    net_records = net_records + records
except:
    error_list.append('MAZE')


print('NOW RUNNING : ', end='')
print('MEIIGO')
try:
    from meiigoo import *
    net_records = net_records + records
except:
    error_list.append('MEIIGO')


print('NOW RUNNING : ', end='')
print('MOTOROLA')
try:
    from motointernational import *
    net_records = net_records + records
except:
    error_list.append('MOTOROLA')

print('NOW RUNNING : ', end='')
print('PANASONIC')
try:
    from panasonic import *
    net_records = net_records + records
except:
    error_list.append('PANASONIC')


print('NOW RUNNING : ', end='')
print('TECNO')
try:
    from tecno import *
    net_records = net_records + records
except:
    error_list.append('TECNO')


print('NOW RUNNING : ', end='')
print('VOTO')
try:
    from voto import *
    net_records = net_records + records
except:
    error_list.append('VOTO')


print('NOW RUNNING : ', end='')
print('XIAOMI')
try:
    from xiaomi import *
    net_records = net_records + records
except:
    error_list.append('XIAOMI')


print('NOW RUNNING : ', end='')
print('APPLE')
try:
    from apple import *
    net_records = net_records + records
except:
    error_list.append('APPLE')





print('NOW RUNNING : ', end='')
print('BLACKVIEW')
try:
    from blackview import *
    net_records = net_records + records
except:
    error_list.append('BLACKVIEW')


print('NOW RUNNING : ', end='')
print('CATERPILLAR')
try:
    from caterpillar import *
    net_records = net_records + records
except:
    error_list.append('CATERPILLAR')


print('NOW RUNNING : ', end='')
print('DOOGEE')
try:
    from doogee import *
    net_records = net_records + records
except:
    error_list.append('DOOGEE')


print('NOW RUNNING : ', end='')
print('INFINIX')
try:
    from Infinix import *
    net_records = net_records + records
except:
    error_list.append('INFINIX')


print('NOW RUNNING : ', end='')
print('ZOPO')
try:
    from zopo import *
    net_records = net_records + records
except:
    error_list.append('ZOPO')


print('NOW RUNNING : ', end='')
print('ASUS')
try:
    from asus_json import *
    net_records = net_records + records
except:
    error_list.append('ASUS')


print('NOW RUNNING : ', end='')
print('VIVO')
try:
    from vivo_json import *
    net_records = net_records + records
except:
    error_list.append('VIVO')


print('NOW RUNNING : ', end='')
print('SAMSUNG')
try:
    from samsung import *
    net_records = net_records + records
except:
    error_list.append('SAMSUNG')


print('NOW RUNNING : ', end='')
print('SAMSUNG_INTERNATIONAL')
try:
    from samsung_us import *
    net_records = net_records + records
except:
    error_list.append('SAMSUNG_INT')
print('NOW RUNNING : ', end='')
print('ULEFONE')
try:
    from ulefone import *
    net_records = net_records + records
except:
    error_list.append('ULEFONE')
print('NOW RUNNING : ', end='')
print('HTC')
try:
    from htc import *
    net_records = net_records + records
except:
    error_list.append('HTC')

print('SUCCESSFULLY FINISHED SCRAPING ALL THE MODELS.')

import pandas as pd

######################################################################################################################################################################
print('THE FILES THAT POSED ERRORS AND WHICH ARE NOT INCLUDED IN TODAYs D.C.C. ARE AS FOLLOWS:')
print(error_list)

######################################################################################################################################################################
try:
    pp=[]
    list_of_all_dcc_files = os.listdir(path_of_the_main_csv)
    print(list_of_all_dcc_files)
    for l in list_of_all_dcc_files:
        pp.append(l.strip('dcc-').strip('.csv'))

    print(pp)

    date_of_last_dcc = max(pp)
except:
    pass
today = datetime.date.today()




df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df.to_csv(os.path.join(path_of_the_main_csv, 'dcc-' + str(today) + '.csv'), index=False, encoding='utf-8')


################################################### MAKING COMPARISONS AND MAKING TODAY'S DUC FILE ###################################################################

records_rem = []
df_old = pd.read_csv(os.path.join(path_of_the_main_csv, 'dcc-' + date_of_last_dcc + '.csv'))


############################# FOR FIRST RUN ########################################################################################################################
##dates_list = []
##for i in range(len(net_records)):
##    dates_list.append('Not Available')
##
##df = pd.DataFrame(net_records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
##df['DATE'] = dates_list
##df.to_csv(os.path.join(path_of_master, 'master.csv'), index=False, encoding='utf-8')

####################################################################################################################################################################
records_old =[tuple(x) for x in df_old.to_records(index=False)]
for r in net_records:
    if r not in records_old:
        records_rem.append(r)



df_rem = pd.DataFrame(records_rem, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
df_rem.to_csv(os.path.join(path_of_the_duc_files, 'duc-'+str(today)+'.csv'), index=False, encoding = 'utf-8')

################################################### FOR SECOND RUN & ONWARDS #########################################################################################
for i in range(len(records_rem)):
    dates_list.append(str(datetime.date.today()))
df_rem['DATE'] = dates_list
with open(os.path.join(path_of_master, 'master.csv'),'a') as f:
    df_rem.to_csv(f, mode='a', index=False, encoding='utf-8')
######################################################################################################################################################################

    
