#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:44:35 2020

@author: brajendra
"""
import urllib.request, json 

'''
Returns all daily data. This call results 
in 10MB of data being returned and should be used infrequently.
'''
def All():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/all") as url:
            data = json.loads(url.read().decode())
        
        with open('all_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API All Data")
        
''' A summary of new and total cases per country updated daily.'''
def Summary():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/summary") as url:
            data = json.loads(url.read().decode())
        
        with open('summary_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API Summary")

'''Returns all the available countries and provinces, 
as well as the country slug for per country requests.'''
def Countries():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/countries") as url:
            data = json.loads(url.read().decode())
        
        with open('countries_data.json', 'w') as f:
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
        
        with open(country + '_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API Countries")
        
        
#Returns all live cases by case type for a country after a given date. 
#These records are pulled every 10 minutes and are ungrouped.         
def WorldTotal():
    try:
        with urllib.request.urlopen("https://api.covid19api.com/world/total") as url:
            data = json.loads(url.read().decode())
        
        with open('world_total_data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error in API WorldTotal")