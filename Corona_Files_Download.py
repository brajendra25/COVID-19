#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:27:47 2020

@author: brajendra
"""

import bs4
import os
import sys
import urllib.request
from datetime import datetime

#For creating dynamic dir
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def donload_CoronaFiles():
    try:
        url = "https://api.covid19india.org/csv/"
        #Logic for downloading corona files daily bases
        error = "0"
        webpage=urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(webpage)
        _lis= soup.get_text().replace('\n','').split(" ")
        res = [] 
        for sub in _lis: 
            sub = sub.replace("https",",https").replace('.csv','.csv,')
            if sub.count("https") > 0:
                res.append(sub)
                
        finalResult = []
        for txt in res:
            link = txt.split(",")[1]
            finalResult.append(link)
        
        _dirPath = "Data/Corona-Files/" 
        ensure_dir(_dirPath)
        
        for fileUrl in finalResult:
           if(fileUrl.count('https')):
               name = fileUrl.split('/')[5]
               if os.path.isfile(_dirPath + name):
                   os.remove(_dirPath + name)
                       
               urllib.request.urlretrieve (fileUrl, _dirPath + name)    
               print(name," file download successfully!!")
           error="1"
        
    except OSError as err:
        error = "OS error: {0}".format(err)
    except EnvironmentError as eberr:
        error = "OS error: {0}".format(eberr)
    except:
         error = "Unexpected error:", sys.exc_info()[0]
    return error
        
'''Start Downloading files from Indian Gov. site'''
#donload_CoronaFiles()

