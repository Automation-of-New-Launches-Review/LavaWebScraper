import datetime
import os
import pandas as pd
import ctypes
today=datetime.date.today()
net_records = []
error_list = []

########################################### SPECIFY HERE THE PATH WHERE THE D.U.C.s & D.C.C.s WILL BE SAVED. ##########################################################
path_of_the_main_csv = 'C:\\LavaWebScraper\\Files\\'
path_of_the_duc_files = 'C:\\LavaWebScraper\\Daily_Updates\\'
path_of_brandwise = 'C:\\LavaWebScraper\\BrandWiseFiles'
path_of_master = 'C:\\LavaWebScraper\\MASTER\\'
mm = 'C:\\LavaWebScraper\\MASTER'
brands = ['agm', 'allcall', 'apple', 'archos', 'asus', 'billion', 'blackview', 'bluboo', 'caterpillar', 'doogee', 'gionee', 'google', 'htc', 'huawei', 'infinix', 'infocus', 'innjoo', 'intex', 'itel', 'ivoomi', 'karbonn', 'lenovo', 'lg', 'lyf', 'maze', 'meiigoo', 'motorola', 'nokia', 'oneplus', 'oppo', 'panasonic', 'razer', 'samsung', 'samsung_us', 'sony', 'tecno', 'ulefone', 'umidigi', 'vivo', 'voto', 'xiaomi', 'zen', 'ziox', 'zopo', 'zte']
brand_files = []
for i in range(len(brands)):
    brand_files.append(str(today)+'-'+brands[i]+'.csv')

#######################################################################################################################################################################

if brand_files[0] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('AGM')
    try:
        from agm import *
        net_records = net_records + records
    except:
        error_list.append('AGM')
else:
    print(brands[0], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[1] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ALLCALL')
    try:
        from allcall import *
        net_records = net_records + records
    except:
        error_list.append('ALLCALL')
else:
    print(brands[1], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[2] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('APPLE')
    try:
        from apple import *
        net_records = net_records + records
    except:
        error_list.append('APPLE')
else:
    print(brands[2], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')
    
if brand_files[3] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ARCHOS')
    try:
        from archos import *
        net_records = net_records + records
    except:
        error_list.append('ARCHOS')
else:
    print(brands[3], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[4] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ASUS')
    try:
        from asus_json import *
        net_records = net_records + records
    except:
        error_list.append('ASUS')
else:
    print(brands[4], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[5] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('BILLION')
    try:
        from billion import *
        net_records = net_records + records
    except:
        error_list.append('BILLION')
else:
    print(brands[5], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[6] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('BLACKVIEW')
    try:
        from blackview import *
        net_records = net_records + records
    except:
        error_list.append('BLACKVIEW')
else:
    print(brands[6], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[7] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('BLUBOO')
    try:
        from bluboo import *
        net_records = net_records + records
    except:
        error_list.append('BLUBOO')
else:
    print(brands[7], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[8] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('CATERPILLAR')
    try:
        from caterpillar import *
        net_records = net_records + records
    except:
        error_list.append('CATERPILLAR')
else:
    print(brands[8], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[9] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('DOOGEE')
    try:
        from doogee import *
        net_records = net_records + records
    except:
        error_list.append('DOOGEE')
else:
    print(brands[9], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[10] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('GIONEE')
    try:
        from gionee import *
        net_records = net_records + records
    except:
        error_list.append('GIONEE')
else:
    print(brands[10], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[11] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('GOOGLE')
    try:
        from google import *
        net_records = net_records + records
    except:
        error_list.append('GOOGLE')
else:
    print(brands[11], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[12] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('HTC')
    try:
        from htc import *
        net_records = net_records + records
    except:
        error_list.append('HTC')
else:
    print(brands[12], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[13] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('HUAWEI')
    try:
        from huwaei import *
        net_records = net_records + records
    except:
        error_list.append('HUAWEI')
else:
    print(brands[13], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[14] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('INFINIX')
    try:
        from Infinix import *
        net_records = net_records + records
    except:
        error_list.append('INFINIX')
else:
    print(brands[14], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[15] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('INFOCUS')
    try:
        from infocus import *
        net_records = net_records + records
    except:
        error_list.append('INFOCUS')
else:
    print(brands[15], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[16] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('INNJOO')
    try:
        from innjoo import *
        net_records = net_records + records
    except:
        error_list.append('INNJOO')
else:
    print(brands[16], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[17] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('INTEX')
    try:
        from intex import *
        net_records = net_records + records
    except:
        error_list.append('INTEX')
else:
    print(brands[17], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[18] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ITEL')
    try:
        from itel_international import *
        net_records = net_records + records
    except:
        error_list.append('ITEL')
else:
    print(brands[18], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[19] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('IVOOMI')
    try:
        from ivoomi import *
        net_records = net_records + records
    except:
        error_list.append('IVOOMI')
else:
    print(brands[19], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[20] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('KARBONN')
    try:
        from karbonn import *
        net_records = net_records + records
    except:
        error_list.append('KARBONN')
else:
    print(brands[20], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[21] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('LENOVO')
    try:
        from lenovo import *
        net_records = net_records + records
    except:
        error_list.append('LENOVO')
else:
    print(brands[21], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[22] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('LG')
    try:
        from lgmain import *
        net_records = net_records + records
    except:
        error_list.append('LG')
else:
    print(brands[22], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[23] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('RELIANCE LYF')
    try:
        from lyf import *
        net_records = net_records + records
    except:
        error_list.append('RELIANCE LYF')
else:
    print(brands[23], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[24] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('MAZE')
    try:
        from maze import *
        net_records = net_records + records
    except:
        error_list.append('MAZE')
else:
    print(brands[24], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[25] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('MEIIGO')
    try:
        from meiigoo import *
        net_records = net_records + records
    except:
        error_list.append('MEIIGO')
else:
    print(brands[25], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[26] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('MOTOROLA')
    try:
        from motointernational import *
        net_records = net_records + records
    except:
        error_list.append('MOTOROLA')
else:
    print(brands[26], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[27] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('NOKIA')
    try:
        from NOKIA1 import *
        net_records = net_records + records
    except:
        error_list.append('NOKIA')
else:
    print(brands[27], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[28] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ONEPLUS')
    try:
        from Oneplusu import *
        net_records = net_records + records
    except:
        error_list.append('ONEPLUS')
else:
    print(brands[28], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[29] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('OPPO')

    try:
        from oppo import *
        net_records = net_records + records
    except:
        error_list.append('OPPO')
else:
    print(brands[29], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[30] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('PANASONIC')
    try:
        from panasonic import *
        net_records = net_records + records
    except:
        error_list.append('PANASONIC')
else:
    print(brands[30], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[31] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('RAZER')
    try:
        from razer import *
        net_records = net_records + records
    except:
        error_list.append('RAZER')
else:
    print(brands[31], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[32] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('SAMSUNG')
    try:
        from samsung import *
        net_records = net_records + records
    except:
        error_list.append('SAMSUNG')
else:
    print(brands[32], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[33] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('SAMSUNG_INTERNATIONAL')
    try:
        from samsung_us import *
        net_records = net_records + records
    except:
        error_list.append('SAMSUNG_INT')
else:
    print(brands[33], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[34] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('SONY')
    try:
        from sony import *
        net_records = net_records + records
    except:
        error_list.append('SONY')
else:
    print(brands[34], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[35] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('TECNO')
    try:
        from tecno import *
        net_records = net_records + records
    except:
        error_list.append('TECNO')
else:
    print(brands[35], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[36] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ULEFONE')
    try:
        from ulefone import *
        net_records = net_records + records
    except:
        error_list.append('ULEFONE')
else:
    print(brands[36], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[37] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('UMIDIGI')
    try:
        from umidigi import *
        net_records = net_records + records
    except:
        error_list.append('UMIDIGI')
else:
    print(brands[37], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[38] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('VIVO')
    try:
        from vivo_json import *
        net_records = net_records + records
    except:
        error_list.append('VIVO')
else:
    print(brands[38], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[39] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('VOTO')
    try:
        from voto import *
        net_records = net_records + records
    except:
        error_list.append('VOTO')
else:
    print(brands[39], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[40] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('XIAOMI')
    try:
        from xiaomi import *
        net_records = net_records + records
    except:
        error_list.append('XIAOMI')
else:
    print(brands[40], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')


if brand_files[41] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ZEN')
    try:
        from zen import *
        net_records = net_records + records
    except:
        error_list.append('ZEN')
else:
    print(brands[41], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[42] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ZIOX')
    try:
        from ziox import *
        net_records = net_records + records
    except:
        error_list.append('ZIOX')
else:
    print(brands[42], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[43] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ZOPO')
    try:
        from zopo import *
        net_records = net_records + records
    except:
        error_list.append('ZOPO')
else:
    print(brands[43], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')

if brand_files[44] not in os.listdir(path_of_brandwise):
    print('NOW RUNNING : ', end='')
    print('ZTE')
    try:
        from zte import *
        net_records = net_records + records
    except:
        error_list.append('ZTE')
else:
    print(brands[44], end=' : ')
    print('ALREADY SCRAPED FOR TODAY.')
    
#######################################################################################################################################################################
print('SUCCESSFULLY FINISHED SCRAPING ALL THE MODELS.')
print('THE FILES THAT POSED ERRORS AND WHICH ARE NOT INCLUDED IN TODAYs D.C.C. ARE AS FOLLOWS:')
print(error_list)
######################################################################################################################################################################

########################################################################################################################################################################

dates_list = []
records_rem = []
if 'master.csv' not in os.listdir(path_of_master):  ## FOR THE FIRST RUN
    print('FIRST RUN')
    df = pd.DataFrame(net_records, columns=['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
    for i in range(len(net_records)):
        dates_list.append('Not Available.')
    #df['DATE'] = dates_list
    df.to_csv(os.path.join(path_of_master, 'master.csv'), index=False, encoding='utf-8-sig')

else:   ## FOR THE SECOND RUN AND ONWARDS
    print('LATER RUN')
    df_master = pd.read_csv(os.path.join(path_of_master, 'master.csv'), encoding = 'latin1')
    records_master =[tuple(x) for x in df_master.to_records(index=False)]
    for r in records_master:
        r = r[:-1]
    for r in net_records:
        if r not in records_master:
            records_rem.append(r)
    for r in records_rem:
        for d in r:
            d = d.replace(u'\u2011',' ').replace(u'\u02da',' ').replace(u'\u02DA',' ').replace('˚',' ').replace(u'\u2019', ' ').replace("’","'").replace("\u2122"," ").replace("\x92"," ")
    for i in range(len(records_rem)):
        dates_list.append(str(today).replace('-','.'))
    df_rem = pd.DataFrame(records_rem, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
    #df_rem['DATE'] = dates_list
    with open(os.path.join(path_of_master, 'master.csv'),'a') as f:
        df_rem.to_csv(f, mode='a', index=False, header = None, encoding='utf8')
    with open(os.path.join(path_of_the_duc_files, str(today)+'-duc.csv'),'a') as f:
        df_rem.to_csv(f, mode='a', index=False, header = None, encoding='utf8')
    
ctypes.windll.user32.MessageBoxW(0, "The scraping of the websites has been completed for this run. Kindly check the results, & if some of the files have posed errors then kindly go for a second run. If the issue still persists, report to the developer.", "Automation of New Launches Review - LavaWebScraper", 0)
ctypes.windll.user32.MessageBoxW(0, str(error_list), "LavaWebScraper : ERRORS OCCURRED WHILE SCRAPING OF THESE BRANDS", 0)
