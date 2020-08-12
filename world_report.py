#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:16:27 2020

@author: brajendra
"""

#Business Layer
import sys
import json
import pandas as pd

_dirPath = "Data/Corona-Files/"

def GetCountries():
    error_msg = ""
    
    try:
        with open(_dirPath + 'countries_data.json', 'r') as f:
            data = json.load(f)
        
        df_Countries = pd.DataFrame.from_dict(data)
        df_Countries = df_Countries.sort_values(['Country'], ascending=True)
        return df_Countries

    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return error_msg
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return error_msg
    except:
        error_msg = "Unexpected error:", sys.exc_info()[0]
        return error_msg
    finally:
        f.close()


def world_summary():
    error_msg = ""
    try:
        with open(_dirPath + 'summary_data.json', 'r') as f:
            data = json.load(f)
        print('ooo')
        df_Country = pd.DataFrame.from_dict(data["Countries"])
        df_Country.sort_values("TotalConfirmed", axis = 0, ascending = False, 
                 inplace = True, na_position ='last') 
        return df_Country
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return error_msg
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return error_msg
    except:
        error_msg = "Unexpected error:", sys.exc_info()[0]
        return error_msg
    
def world_summaryByAction(action):
    error_msg = ""
    try:
        with open(_dirPath + 'summary_data.json', 'r') as f:
            data = json.load(f)
        
        df_Country = pd.DataFrame.from_dict(data["Countries"])
        df_Country.sort_values(action, axis = 0, ascending = False, 
                 inplace = True, na_position ='last') 
        df_ByAction = df_Country[action]
        print( df_ByAction)
    
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return error_msg
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return error_msg
    except:
        error_msg = "Unexpected error:", sys.exc_info()[0]
        print( error_msg)
def WorldTotal():
    error_msg = ""
    try:
        with open(_dirPath + 'world_total_data.json', 'r') as f:
            data = json.load(f)
        return data

    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return error_msg
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return error_msg
    except:
        error_msg = "Unexpected error:", sys.exc_info()[0]
        return error_msg

GetCountries()