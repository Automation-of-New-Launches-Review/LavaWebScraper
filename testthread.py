import tkinter as Tkinter   # Python 3
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import requests
import csv
import re
import tkinter.ttk as ttk
from bs4 import BeautifulSoup
import pandas as pd
import bs4 as bs
import urllib.request
import ctypes
import _thread
import threading
root = Tk()
C = Canvas(root)
filename = PhotoImage(file = "C:\\Users\\BALJEET SINGH\\Desktop\\wolf.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

root.title("scraper")
root.geometry("650x680+280+0")
root.configure(background='steelblue')

def abt():
    messagebox.showinfo(title="ABOUT",message="for details look for readme.txt file in the folder")
def rn():
    messagebox.showinfo(title="RUNNING THE SOTWARE",message="for instructions look for instruction.txt file in the folder")
def do_it():
    print("twp")
    
try:
    
    #####################################################################################################################################################################
    #ist function
    def bill():
        try:
        
            import time
            #print(TTTT)
            progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
            country=[]
            company=[]
            urls=[]
            specs=[]
            model=[]
            thickness_list1=[]
            usp=[]
            display_list = []
            memory_list = []
            processor_list = []
            camera_list = []
            battery_list = []
            thickness_list = []
            extras_links = []
            heads = []
            dets = []
            dets1=[]
            url='https://www.billion.in/'
            r1 = requests.get(url)
            soup = BeautifulSoup(r1.text, 'html.parser')
            sp=soup.findAll('a', text = re.compile('Smartphones'), attrs = {'class' : 'sub-nav-link'})
            for t in sp:
                urls.append(t['href'])
            progress['value']=20
            root.update_idletasks()
            time.sleep(1)
            progress.pack()
            for b in urls:
                r1 = requests.get(b)
                soup = BeautifulSoup(r1.text, 'html.parser')
    
                sp=soup.find_all("div",attrs={'class':'fourth-screen'})
                for ghj in sp:
                    hj=ghj.find_all("h1")
                    for y in hj:
                        specs.append(y.text)
                dat=soup.find_all("div",attrs={'class':'second-screen section screen-6'})
                #print(dat)
                for t in dat:
                    s1=t.find_all("h1")
                    s2=t.find_all("h3")
                    for x in s1:
                        heads.append(x.text)
                    kt=""
                    for v in s2:
                        kt=kt+(v.text)
                    dets.append(kt)
                #print(heads)
                progress['value']=50
                root.update_idletasks()
                time.sleep(1)
                progress.pack()
                for i in range(len(heads)):                                                                           
                    if 'Battery' in heads[i]:
                        battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'battery' in heads[i]:
                        battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'BATTERY' in heads[i]:
                        battery_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'Processor & RAM' in heads[i]:
                        processor_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'processor' in heads[i]:
                        processor_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'Camera' in heads[i]:
                        camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'camera' in heads[i]:
                        camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'CAMERA' in heads[i]:
                        camera_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'Display' in heads[i] or 'display' in heads[i] or 'DISPLAY' in heads[i]:
                        display_list.append(dets[i].strip('\r\n\t').replace('\n',''))
                    if 'Storage & Memory' in heads[i] or 'Storage' in heads[i] or 'storage' in heads[i] or 'memory' in heads[i]:
                        memory_list.append(dets[i].strip('\r\n\t').replace('\n',''))
    
    
            for x in range(len(urls)):
                country.append("INDIA")
                company.append("BILLION")
                extras_links.append(urls[x])
                thickness_list.append("NA")
                progress['value']=80
                root.update_idletasks()
                time.sleep(1)
                progress.pack()
            for x in urls:
                r1 = requests.get(x)
                soup = BeautifulSoup(r1.text, 'html.parser')
    
                sp=soup.find_all("div",attrs={'class':'second-screen section'})
                for ghj in sp:
                    hj=ghj.find_all("h1")
                    for y in hj:
                        model.append(y.text)
    
    
            print(len(country))
            print(len(company))
            print(len(model))
            print(len(specs))
            print(len(display_list))
            print(len(camera_list))
            print(len(memory_list))
            print(len(battery_list))
            print(len(thickness_list))
            print(len(processor_list))
            print(len(extras_links))

            records=[]
            for i in range(len(company)):
                records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

            df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
            progress['value']=100
            progress.pack()
            df.to_csv('billion.csv', index=False, encoding='utf-8')
            
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "Error", "Error", 0)
            er =Label(root, text = 'error:').place(x=100,y=500)
            E1 = Label(root, text = str(e)).place(x=190,y=500)
    ###############################################################################################################################################################################
    #2nd fuction
    def rel():
        try:
            import time
            #print(TTTT)
            progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
            import csv
            import requests
            from bs4 import BeautifulSoup
            import csv
            import pandas as pd
            import re
            urls=[]
            model=[]
            company=[]
            specs=[]
            country=[]
            display_list = []
            memory_list = []
            processor_list = []
            camera_list = []
            battery_list = []
            thickness_list = []
            extras_links = []
            url="https://www.mylyf.com/element-series-collection"
            r=requests.get(url)
            soup=BeautifulSoup(r.text,'html.parser')    
            links=soup.find_all('div',attrs={'class':'product-txt'})
            mod=soup.find_all('div',attrs={'class':'btn_panel'})
            for j in links:
    
                tt=j.find_all('p')
                for k in tt:
                    data1=[]
                    data1.append(k.text)
                for l in range(len(data1)):
                    st=""
                    st=st+data1[l]
                    pt=''
                    for k in st:
            
                        pt=pt+k.strip('\n')
                        f=''
                    for t in pt:
                        f=f+t.strip('\r')
                specs.append(f)
            for s in mod:
                tt=s.find_all('a')
                for m in tt:
                    model.append(m.text)
            progress['value']=20
            root.update_idletasks()
            progress.pack()
            #company---
            for i in range(len(model)):
    
                company.append("LYF")
    

            links=soup.find_all('div',attrs={'class':'btn_panel'})
            for x in links:
                v=x.find_all('a')
                for h in v:
                    urls.append(h['href'])

            for i in range(len(urls)):
                country.append("INDIA")
                extras_links.append(urls[i])
    
    
            for z in range(len(urls)):

    
                print(urls[z])
                heads = []
                dets = []
                dets1=[]
                r1 = requests.get(urls[z])
                soup = BeautifulSoup(r1.text, 'html.parser')

                dat=soup.find_all("table")
                for t in dat:
                    s1=t.find_all("tr")
                    #print(s1)
                    for s in s1:
                        s2=s.find_all('td')
                        heads.append(s2[0].text)
                        dets.append(s2[1].text)
                lt=''
                bb=''
    
                for i in range(len(heads)):
        
                    s=''
                    c=''
                    d=''
                    t=''
                    if 'CHIPSET' in heads[i]:
                        bb=bb+dets[i].strip('\r\n\t').replace('\n','')
        
            
            
    
                    if 'BATTERY' in heads[i]:
                        match = re.search(r'\d+\s*m',dets[i])
                        if match:
                            c=str(match.group())
                        if not match:
                            match=re.search(r'\d*m',dets[i].lower())
                            if match:
                                c=str(match.group())
                            if not match:
                                c=' '
                
                        battery_list.append(c+"Ah")
                    if 'DESIGN' in heads[i]:
                        #print("x")
                        match = re.search(r'\d+\.?\d*\s*mm\s*x\s*\d+\.?\d*\s*mm\s*x\s*\d+\.?\d*\s*mm',dets[i])
                        if match:
                            s=str(match.group())
                        if not match:
                            match = re.search(r'x\d+\s*\.*\,*\s*\d*\s*mm',dets[i])
                            if match:
                                 s=str(match.group())
                            if not match:
                                s=' '
                        lt=lt+s
                    if "DESIGN" not in heads:
                
                        lt=lt+" "
        
                        #print("__________")
                    cv=''
                    progress['value']=35
                    root.update_idletasks()
                    progress.pack()
                    if 'CAMERA' in heads[i]:
                        #print(dets[i])
                        match1=re.search(r'Rear Camera :\s*\d+\s*\.*\s*\d*\s*MP',dets[i])
                        if match1:
                            d=str(match1.group())
                        if not match1:
                            match1=re.search(r'Rear Camera:\s+\d+\s*\.*\s*\d*\s*MP',dets[i])
                            if match1:
                                d=str(match1.group())
                            if not match1:
                                match1=re.search(r'Rear Camera:\d+MP',dets[i])
                                if match1:
                                    d=str(match1.group())
                                if not match:
                                    d=' '
                
                        cv=cv+d+" "
                        match12=re.search(r'Front Camera :\s*\d+\s*\.*\s*\d*\s*MP',dets[i])
                        if match12:
                            t=str(match12.group())
                        if not match12:
                            match12=re.search(r'Front Camera:\s+\d+\s*\.*\s*\d*\s*MP',dets[i])
                            if match12:
                                t=str(match12.group())
                            if not match12:
                                match12=re.search(r'Front Camera:\d+MP',dets[i])
                                if match12:
                                    t=str(match12.group())
                                if not match12:
                                    t=' '
                        cv=cv+t
                        camera_list.append(cv)
                    progress['value']=50
                    root.update_idletasks()
                    progress.pack()
                    if 'DISPLAY' in heads[i]:
                        match=re.search(r'Screen Size:\s*\d*\.\d*cm',dets[i])
                        if match:
                        
                            y=str(match.group())
                        if not match:
                            match=re.search(r'Screen Size:\s*\d*\.\d*\s*cm',dets[i])
                            if match:
                                y=str(match.group())
                            if not match:
                                match=re.search(r'Screen Size:\s*\d*\.\d*\s*inch',dets[i])
                                if match:
                                    y=str(match.group())
                                if not match:
                                    y=" "
                             
                             
                
            
                        display_list.append(y)
                thickness_list.append(lt)
                processor_list.append(bb)

                pt=""
                for i in range(len(heads)):
                    if 'STORAGE' in heads[i]:
                        pt=pt+dets[i].strip('\r\n\t')
        
                    if 'PERFORMANCE' in heads[i]:
                        match = re.search(r'RAM:\s*\d*GB',dets[i])
                        if match:
                            pt=pt+str(match.group())
                        if not match:
                            pt=pt+" "

                memory_list.append(pt.replace("\n"," "))
            progress['value']=75
            root.update_idletasks()
            progress.pack()
            print(len(country))
            print(len(company))
            print(len(model))
            print(len(specs))
            print(len(display_list))
            print(len(camera_list))
            print(len(memory_list))
            print(len(battery_list))
            print(len(thickness_list))
            print(len(processor_list))
            print(len(extras_links))

            records=[]
            for i in range(len(company)):
                records.append((country[i], company[i], model[i], specs[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))

            df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
            progress['value']=100
            progress.pack()
            df.to_csv('LYF1.csv', index=False, encoding='utf-8')
            
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "Error", "Error", 0)
            er =Label(root, text = 'error:').place(x=100,y=500)
            E1 = Label(root, text = str(e)).place(x=190,y=500)
    ####################################################################################################################################################################################    
    def zen():
        try:
            
            import time
            #print(TTTT)
            progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
            import requests
            import re
            from bs4 import BeautifulSoup
            import pandas as pd
            import sys
            from PyQt4.QtGui import QApplication
            from PyQt4.QtCore import QUrl
            from PyQt4.QtWebKit import QWebPage
            import bs4 as bs
            import urllib.request
            progress['value']=20
            root.update_idletasks()
            time.sleep(1)
            progress.pack()

            base_url = 'http://www.zenmobile.in/smart-phones/'
            #ur='https://www.nokia.com/en_int/phones/'
            country = 'INDIA'
            company = 'ZEN'
            model_list = []
            usp = []
            display_list = []
            memory_list = []
            processor_list = []
            camera_list = []
            battery_list = []
            thickness_list = []
            extras_links = []
            records = []
            href = []
            st_list_heads=[]
            st_list_dets=[]
            hr=[]
            spec_url=[]
            r=requests.get(base_url)
            soup=BeautifulSoup(r.text,'html.parser')
            results=soup.find_all('div',attrs={'class':'col-md-3 col-sm-4 col-xs-12 bt-gap'})
            #print(len(results))
            for i in range(len(results)):
                href.append(results[i].find('a')['href'])
                model_list.append(results[i].find('p').text)
            ##for i in href:
            ##    print(i)
            for i in range(len(href)):
                heads=[]
                dets=[]
                r=requests.get(href[i])
                soup=BeautifulSoup(r.text,'html.parser')
                results1=soup.find_all('div',attrs={'class':'com-md-12'})
                for z in range(len(results1)):
                    usp.append(results1[z].find('h3').text.strip())
                results=soup.find_all('div',attrs={'class':'row hidden-specification'})
               #print(len(results))
                for a in range(len(results)):
                    sa=results[a].find_all('div',attrs={'class':'col-md-12'})
                    for b in range(len(sa)):
                        sb=sa[b].find_all('table',attrs={'class':'table'})
                        for c in range(len(sb)):
                            sc=sb[c].find_all('tr')
                            for d in range(len(sc)):
                                sd=sc[d].find_all('td')
                                #print(len(sd))
                                heads.append(sd[0].text.strip())
                                dets.append(sd[1].text.strip())
                st_list_heads.append(heads)
                st_list_dets.append(dets)
                if len(usp)==i:
                    usp.append('NA')
            
            progress['value']=40
            root.update_idletasks()
            time.sleep(1)
            progress.pack()
            for i in range(len(st_list_heads)):
                d1 = ''
                d2 = ''
                m1 = ''
                m2 = ''
                c1 = ''
                c2 = ''
                for j in range(len(st_list_heads[i])):
                    if 'Physical size' in st_list_heads[i][j] or 'Physical Size' in st_list_heads[i][j] or 'physical size' in st_list_heads[i][j]:
                        d1=st_list_dets[i][j]
                    if 'Resolution Type' in st_list_heads[i][j] or 'Resolution type' in st_list_heads[i][j] or 'resolution type' in st_list_heads[i][j]:
                        d2=st_list_dets[i][j]
            
                    if 'Capacity' in st_list_heads[i][j] or 'capacity' in st_list_heads[i][j]:
                        battery_list.append(st_list_dets[i][j])
            
                    if 'RAM' in st_list_heads[i][j]:
                        m1=st_list_dets[i][j]
                    if 'ROM' in st_list_heads[i][j]:
                        m2=st_list_dets[i][j]
            
                    if 'Back camera' in st_list_heads[i][j] or 'Back Camera' in st_list_heads[i][j] or 'back camera' in st_list_heads[i][j]:
                        c1 = st_list_dets[i][j]
                    if 'Front camera' in st_list_heads[i][j] or 'Front Camera' in st_list_heads[i][j] or 'front camera' in st_list_heads[i][j]:
                        c2 = st_list_dets[i][j]
            
                    if 'Processor' in st_list_heads[i][j]:
                        processor_list.append(st_list_dets[i][j])
                progress['value']=70
                root.update_idletasks()
                time.sleep(1)
                progress.pack()
        
                if m1!='' or m2!='':
                    memory_list.append(m1+' '+m2)
                if d1!='' or d2!='':
                    display_list.append(d1+' '+d2)
                if c1!='' or c2!='':
                    camera_list.append(c1 +' '+ c2)
                if 'thickness' not in st_list_heads[i]:
                    thickness_list.append('NA')
        
                if 'Processor' not in st_list_heads[i]:
                    processor_list.append('NA')
        
                if 'RAM' not in st_list_heads[i] and 'ROM' not in st_list_heads[i]:
                    memory_list.append('NA')

                if 'Capacity' not in st_list_heads[i] and 'capacity' not in st_list_heads[i]:
                    battery_list.append('NA')
        
                if 'Physical size' not in st_list_heads[i] and 'Resolution Type' not in st_list_heads[i] and 'Resolution type' not in st_list_heads[i] and 'Physical Size' not in st_list_heads[i] and 'physical size' not in st_list_heads[i] and 'resolution type' not in st_list_heads[i]:
                    display_list.append('NA')
        
                if 'Back camera' not in st_list_heads[i] and 'Front camera' not in st_list_heads[i] and 'Back Camera' not in st_list_heads[i] and 'Front Camera' not in st_list_heads[i]:
                    camera_list.append('NA')
    
            extras_links = href
            for i in range(len(model_list)):
                records.append((country, company, model_list[i], usp[i], display_list[i], camera_list[i], memory_list[i], battery_list[i], thickness_list[i], processor_list[i], extras_links[i]))
            progress['value']=100
            progress.pack()
            df = pd.DataFrame(records, columns = ['COUNTRY', 'COMPANY', 'MODEL', 'USP', 'DISPLAY', 'CAMERA', 'MEMORY', 'BATTERY', 'THICKNESS', 'PROCESSOR', 'EXTRAS/ LINKS'])
            df.to_csv('zen.csv', index=False, encoding='utf-8')

            
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "Error", "Error", 0)
            er =Label(root, text = 'error:').place(x=100,y=500)
            E1 = Label(root, text = str(e)).place(x=190,y=500)
    
    def zte():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=40
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=60
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import zte
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def intex():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=40
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=60
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import intex
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def karbon():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=40
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=60
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import karbonn
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def ziox():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=40
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=60
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ziox
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def india():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import india
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def razer():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import razer
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def apple():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import india
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def cater():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import caterpillar
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def blub():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import bluboo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def infocus():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import infocus
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def google():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import google
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def usa():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import usa
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def sony():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import sony
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def maze():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import maze
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def panasonic():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import panasonic
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def japan():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import japan
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def nokia():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import NOKIA1
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def lg():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import lgmain
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def asus():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import asus_json
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def archos():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import archos
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def dodgee():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import doogee
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def othercountries():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import other_countries
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def xiomi():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import xiaomi
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def vivo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import vivo_json
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def oppo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import oppo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def itel():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import itel_international
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def lenovo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import lenovo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def huawei():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import huwaei
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def oneplus():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import Oneplusu
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def tecno():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import tecno
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def agm():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import agm
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def allcall():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import allcall
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gionee():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gionee
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def infinix():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import Infinix
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def ivoomi():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ivoomi
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def innjoo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import innjoo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def meizu():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import meizu
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def meiigo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import meiigoo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def nubia():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import nubia
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def umidigi():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import umidigi
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def voto():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import voto
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def zopo():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import zopo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def moto():
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import motointernatonal
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def china():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import china
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def scall():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import main
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def ulefone():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ulefone
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def apple():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import apple
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def htc():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import htc
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gcelkon():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gcelkon
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def ghuawei():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ghuawei
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def glava():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import glava
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gmicromax():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gmicromax
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gspice():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gspice
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gxolo():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gxolo
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gall():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gsm
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gyu():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gyu
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def galcatel():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import galcatel
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def gcoolpad():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gcoolpad
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def sam():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import samsung
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    def samint():
        try:
            #print("GGG")
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import samsung_us
            progress['value']=100
            progress.pack()
            ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)


except BaseException as e:
        ctypes.windll.user32.MessageBoxW(None, "close the software and connect to internet", "Error", 0)
        ak =Label(root, text = 'error:').place(x=1,y=500)
        hh =Label(root, text = str(e)).place(x=50,y=500)
        
       
    


def uu(i):
    print(i)
   
    
    if i==0:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import lyf
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==1:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gmicromax
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==2:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import intex
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==3:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import karbonn
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==4:
            try:
                import time
                progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
                progress['value']=20
                progress.pack()
                root.update_idletasks()
                time.sleep(1)
                progress['value']=30
                progress.pack()
                root.update_idletasks()      
                time.sleep(1)
                progress['value']=50
                progress.pack()
                root.update_idletasks()
                time.sleep(1)
                import zen
                progress['value']=100
                progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
            except BaseException as e:
                ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
                ak =Label(root, text = 'error:').place(x=1,y=500)
                hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==5:
            try:
                import time
                progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
                progress['value']=20
                progress.pack()
                root.update_idletasks()
                time.sleep(1)
                progress['value']=30
                progress.pack()
                root.update_idletasks()      
                time.sleep(1)
                progress['value']=50
                progress.pack()
                root.update_idletasks()
                time.sleep(1)
                import ziox
                progress['value']=100
                progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
            except BaseException as e:
                ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
                ak =Label(root, text = 'error:').place(x=1,y=500)
                hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==6:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import billion
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==7:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import xiaomi
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==8:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import vivo_json
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==9:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import oppo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i ==10:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import itel_international
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==11:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import lenovo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==12:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import motointernational
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==13:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import huwaei
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==14:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import Oneplusu
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==15:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import infocus
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==16:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import tecno
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==17:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import agm
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==18:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import allcall
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==19:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import blackview        
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==20:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gionee
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==21:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import infinix
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==22:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ivoomi
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==23:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import innjoo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==24:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import meizu
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==25:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import meiigoo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==26:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import nubia
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==27:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import umidigi
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==28:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ulefone
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==29:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import voto
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==30:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import zte
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==31:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import razer
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==32:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import apple
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==33:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import caterpillar
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==34:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import bluboo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==35:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import google
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==36:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import sony
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==37:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import maze
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==38:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import panasonic
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==39:
        ak =Label(root, text = 'SAMSUNG will be availabe using above selenium option').place(x=1,y=500)
    elif i==40:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import NOKIA1
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==41:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import lgmain
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==42:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import asus_json
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==43:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import alcatel
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==44:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import archos
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==45:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import doogee
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==46:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gyu
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==47:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import zopo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==48:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import htc
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==49:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gcelkon
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==50:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import ghuawei
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==51:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import glava
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==52:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gspice
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
        
    elif i==53:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gxolo
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==54:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import galcatel
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)
    elif i==55:
        try:
            import time
            progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
            progress['value']=20
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            progress['value']=30
            progress.pack()
            root.update_idletasks()      
            time.sleep(1)
            progress['value']=50
            progress.pack()
            root.update_idletasks()
            time.sleep(1)
            import gcoolpad
            progress['value']=100
            progress.pack()
            #ak =Label(root, text = 'COMPLETED!!!:').place(x=280,y=500)
        except BaseException as e:
            ctypes.windll.user32.MessageBoxW(None, "ERROR", "Error", 0)
            ak =Label(root, text = 'error:').place(x=1,y=500)
            hh =Label(root, text = str(e)).place(x=50,y=500)    
        
        
        
        
            
    print("KK")  
    ak=Label(root, text = 'COMPLETED!!!:').pack()
def sel():                   #function for selecting multiple
    a=lB.curselection()
    print(a)
    
    for j in a:
        s=()
        s=s+(j,)
        _thread.start_new_thread ( uu,s)
    
        

heading=Label(root,text="WEBSITES SCRAPER",font=("Courier New",40,"bold"),fg="red",bg="steelblue").pack()
#pic=PhotoImage(file="lava.png")
#label3=Label(root,image=pic).place(x=1300)
##########################################################################################################################################################
#selection function where work takes place is sel()
lB = Listbox(root,selectmode=EXTENDED,width=100,height=20)
label1=Label(root,text="SELECT MULTIPLE WEBSITES(hold ctrl and click on website): ",font=("arial",12,"bold"),fg="RED" ,bg="steelblue")
lB.configure(background='#f0f0f0')
lB.insert(1,'RELIANCE LYF')
lB.insert(2,'MICROMAX(GSM)')######
lB.insert(3,'INTEX')
lB.insert(4,'KARBON')
lB.insert(5,'ZEN')
lB.insert(6,'ZIOX')
lB.insert(7,'BILLION')
lB.insert(8,'XIOMI')
lB.insert(9,'VIVO')
lB.insert(10,'OPPO')
lB.insert(11,'ITEL')
lB.insert(12,'LENOVO')
lB.insert(13,'MOTOROLA')
lB.insert(14,'HUAWEI')
lB.insert(15,'ONEPLUS')
lB.insert(16,'INFOCUS')##########
lB.insert(17,'TECHNO')
lB.insert(18,'AGM')
lB.insert(19,'ALLCALL')
lB.insert(20,'BLACKVIEW')########
lB.insert(21,'GIONEE')
lB.insert(22,'INFINIX')
lB.insert(23,'IVOOMI')
lB.insert(24,'INNJOO')
lB.insert(25,'MEIZU')
lB.insert(26,'MEIGOO')
lB.insert(27,'NUBIA')
lB.insert(28,'UMIDIGI')
lB.insert(29,'ULEFONE')
lB.insert(30,'VOTO')
lB.insert(31,'ZTE')
lB.insert(32,'RAZER')
lB.insert(33,'APPLE')
lB.insert(34,'CATERPILLER')
lB.insert(35,'BLUBOO')
lB.insert(36,'GOOGLE')
lB.insert(37,'SONY')
lB.insert(38,'MAZE')
lB.insert(39,'PANASONIC')
lB.insert(40,'SAMSUNG')
lB.insert(41,'NOKIA')
lB.insert(42,'LG')
lB.insert(43,'ASUS')
lB.insert(44,'ALCATEL')##############
lB.insert(45,'ARCHOS')
lB.insert(46,'DOOGEE')
lB.insert(47,'YU(GSM)')
lB.insert(48,'ZOPO')
lB.insert(49,'htc')
#lB.insert(50,'AMAZON')
lB.insert(50,'CELKON(GSM)')
lB.insert(51,'GSM(HUAWEI)')
lB.insert(52,'LAVA(GSM)')
#lB.insert(53,'MICROMAX')
lB.insert(53,'SPICE(GSM)')
lB.insert(54,'XOLO(GSM)')
lB.insert(55,'ALCATELGSM)')
lB.insert(56,'COOLPAD(GSM)')


yscroll=Scrollbar(root,orient=VERTICAL)
lB['yscrollcommand']=yscroll.set
yscroll['command']=lB.yview
b=Button(root,text="SUBMIT",command=sel)
label1.pack()
yscroll.place(x=1,y=300)
lB.pack()
b.pack()

############################################################################################################
#india menu
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="INDIA",menu=submenu)
submenu.add_command(label="ZEN",command=zen)
#submenu.add_command(label="MICROMAX",command=do_it)
submenu.add_command(label="INTEX",command=intex)
submenu.add_command(label="KARBONN",command=karbon)
submenu.add_command(label="RELIANCE LYF",command=rel)
submenu.add_command(label="ZIOX",command=ziox)
submenu.add_command(label="BILLION",command=bill)
#submenu.add_command(label="YU",command=do_it)
def ii():
    a=()
    t1 = threading.Thread(target=india)
    t1.start()

submenu.add_command(label="SCRAP ALL",command=ii)
##############################################################################################################
#CHINA MENU
editmenu=Menu(menu)
menu.add_cascade(label="CHINA",menu=editmenu)
editmenu.add_command(label="XIOMI",command=xiomi)
editmenu.add_command(label="VIVO",command=vivo)
editmenu.add_command(label="OPPO",command=oppo)
editmenu.add_command(label="ITEL",command=itel)
editmenu.add_command(label="LENOVO",command=lenovo)
editmenu.add_command(label="HUAWEI",command=huawei)
editmenu.add_command(label="ONEPLUS",command=oneplus)
editmenu.add_command(label="HONOR",command=do_it)
editmenu.add_command(label="TECNO",command=tecno)
editmenu.add_command(label="AGM",command=agm)
editmenu.add_command(label="ALLCALL",command=allcall)
#editmenu.add_command(label="COOLPAD",command=do_it)
editmenu.add_command(label="GIONEE",command=gionee)
editmenu.add_command(label="INFINIX",command=infinix)
editmenu.add_command(label="IVOOMI",command=ivoomi)
editmenu.add_command(label="INNJOO",command=innjoo)
editmenu.add_command(label="MEIZU",command=meizu)
editmenu.add_command(label="MEIIGO",command=meiigo)
editmenu.add_command(label="NUBIA",command=nubia)
editmenu.add_command(label="UMIDIGI",command=umidigi)
editmenu.add_command(label="ULEFONE",command=ulefone)
editmenu.add_command(label="VOTO",command=voto)
editmenu.add_command(label="ZTE",command=zte)
editmenu.add_command(label="ZOPO",command=zopo)
editmenu.add_command(label="MOTOROLLA",command=moto)
def hh():
    a=()
    t1 = threading.Thread(target=china)
    t1.start()

editmenu.add_command(label="SCRAP ALL",command=hh)
###############################################################################################################################
#USA
rmenu=Menu(menu)
menu.add_cascade(label="USA",menu=rmenu)
rmenu.add_command(label="RAZER",command=razer)
rmenu.add_command(label="CATERPILLER",command=cater)
rmenu.add_command(label="BLUBOO",command=blub)
rmenu.add_command(label="INFOCUS",command=infocus)
rmenu.add_command(label="GOOGLE",command=google)
rmenu.add_command(label="APPLE",command=apple)
def gg():
    a=()
    t1 = threading.Thread(target=usa)
    t1.start()

rmenu.add_command(label="SCRAP ALL",command=gg)
##################################################################################################################################
#JAPAN
Jmenu=Menu(menu)
menu.add_cascade(label="JAPAN",menu=Jmenu)
Jmenu.add_command(label="SONY",command=sony)
Jmenu.add_command(label="MAZE",command=maze)
Jmenu.add_command(label="PANASONIC",command=panasonic)
def ff():
    a=()
    t1 = threading.Thread(target=japan)
    t1.start()

Jmenu.add_command(label="SCRAP ALL",command=ff)
###################################################################################################################################
#OTHER COUNTRIES
Omenu=Menu(menu)
menu.add_cascade(label="OTHER COUNTRIES",menu=Omenu)
Omenu.add_command(label="NOKIA",command=nokia)
Omenu.add_command(label="LG",command=lg)
Omenu.add_command(label="ASUS",command=asus)
Omenu.add_command(label="ARCHOS",command=archos)
Omenu.add_command(label="DODGEE",command=dodgee)
Omenu.add_command(label="HTC",command=htc)
def ee():
    a=()
    t1 = threading.Thread(target=othercountries)
    t1.start()

Omenu.add_command(label="SCRAP ALL",command=ee)
##############################################################################################################################
#selenium websites
pcmenu=Menu(menu)
menu.add_cascade(label="WEBSITES USING SELENIUM",menu=pcmenu)
def dd():
    a=()
    t1 = threading.Thread(target=sam)
    t1.start()
pcmenu.add_command(label="SAMSUNG",command=dd)
def aa():
    a=()
    t1 = threading.Thread(target=samint)
    t1.start()

pcmenu.add_command(label="SAMSUNG US",command=aa)
#stop_event = threading.Event()


####################################################################################################################################
#scrapall
scmenu=Menu(menu)
def bb():
    a=()
    t1 = threading.Thread(target=scall)
    t1.start()
menu.add_cascade(label="SCRAP ALL",menu=scmenu)
scmenu.add_command(label="SCRAP ALL",command=bb)
###################################################################################################################################
#gsm
gmenu=Menu(menu)
menu.add_cascade(label="GSM ARENA",menu=gmenu)
gmenu.add_command(label="CELKON",command=gcelkon)
gmenu.add_command(label="HUAWEI",command=ghuawei)
gmenu.add_command(label="LAVA",command=glava)
gmenu.add_command(label="MICROMAX",command=gmicromax)
gmenu.add_command(label="SPICE",command=gspice)
gmenu.add_command(label="XOLO",command=gxolo)
gmenu.add_command(label="YU",command=gyu)
gmenu.add_command(label="ALCATEL",command=galcatel)
gmenu.add_command(label="COOLPAD",command=gcoolpad)

def cc():
    a=()
    t1 = threading.Thread(target=gall)
    t1.start()
gmenu.add_command(label="SCRAP ALL",command=cc)



###############################################################################################################################
#HELPMENU
hmenu=Menu(menu)
menu.add_cascade(label="HELP",menu=hmenu)
hmenu.add_command(label="ABOUT SOFTWARE",command=abt)
hmenu.add_command(label="RUNNING SOFTWARE",command=rn)


root.update() 
root.mainloop()
