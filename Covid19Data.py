#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:44:35 2020
@author: brajendra
Getting API from below URL:
https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#e831c268-9da1-4d86-8b5a-8d7f61910af8
"""
import urllib.request, json 

'''
Returns all daily data. This call results 
in 10MB of data being returned and should be used infrequently.
'''
_dirPath = "Data/Corona-Files/"
def All():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/all") as url:
            data = json.loads(url.read().decode())
        
        with open(_dirPath + 'all_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API All Data")
        
''' A summary of new and total cases per country updated daily.'''
def Summary():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/summary") as url:
            data = json.loads(url.read().decode())
        
        with open(_dirPath + 'summary_data.json', 'w') as f:
            json.dump(data, f)
        return "1"
    except:
        print("Error in API Summary")
        return "0"

'''Returns all the available countries and provinces, 
as well as the country slug for per country requests.'''
def Countries():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/countries") as url:
            data = json.loads(url.read().decode())
        
        with open(_dirPath + 'countries_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API Countries")

#Returns all cases by case type for a country from the first recorded case.        
def ByCountries(_country):
    try:
        country = _country
        URL = "https://api.covid19api.com/dayone/country/" + country
        with urllib.request.urlopen(URL) as url:
            data = json.loads(url.read().decode())
        
        with open(_dirPath + country + '_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API Countries")
        
    finally:
        f.close()
        
        
#Returns all live cases by case type for a country after a given date. 
#These records are pulled every 10 minutes and are ungrouped.         
def WorldTotal():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/world/total") as url:
            data = json.loads(url.read().decode())
        
        with open(_dirPath + 'world_total_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API WorldTotal")
        
#All()