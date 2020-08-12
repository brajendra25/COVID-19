#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:09:44 2020

@author: brajendra
"""
import pandas as pd
from datetime import datetime
import os

class CoronaAnalysis:
    _dirPath=""
    def __init__(self):
        self._dirPath = "Data/Corona-Files/"
        
    def Get_case_time_series(self):
        df_case_time_series = pd.read_csv(self._dirPath + "case_time_series.csv")
        df_case_time_series = df_case_time_series.tail(50)
        return df_case_time_series

    def Get_state_wise(self,state):
        df_state_wise = pd.read_csv(self._dirPath + "state_wise.csv")
        if(state != 'TT'):
            df_state_wise = df_state_wise[df_state_wise['State_code']==state]
        elif state == 'TT':
            df_state_wise = df_state_wise
        
        return df_state_wise
    
    def Get_Daily_state_wise(self):
        df_daily_state_wise = pd.read_csv(self._dirPath + "state_wise_daily.csv")
        return df_daily_state_wise
    
    def Get_District_wise(self):
        df_district_wise = pd.read_csv(self._dirPath + "district_wise.csv")
        return df_district_wise
    
    def Get_District_By_State_Code(self,stateCode):
        df_district_wise = pd.read_csv(self._dirPath + "district_wise.csv")
        df_district_StateCode = df_district_wise[df_district_wise['State_Code']==stateCode]
        return df_district_StateCode
    
#c1 = CoronaAnalysis()
#c1.Get_case_time_series()