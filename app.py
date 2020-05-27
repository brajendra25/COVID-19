from flask import Flask, render_template,request
import json 
import Corona_Analysis as GA
import Corona_Files_Download as DL
import pandas as pd
import sys
import feedparser
import Covid19Data as CD
import urllib.request
from xml.etree.ElementTree import parse

app = Flask(__name__)
colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
objc = GA.CoronaAnalysis()
df_Case_Time =  objc.Get_case_time_series()

def getStates():
    state_dict = {'AN': 'Andaman and Nicobar Islands', 'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS': 'Assam',
                  'BR': 'Bihar', 'CH': 'Chandigarh', 'CT': 'Chhattisgarh', 'DD': 'Dadra and Nagar Haveli and Daman and Diu', 
                 'DN': 'Daman and Diu', 'DL': 'Delhi', 'GA': 'Goa', 'GJ': 'Gujarat', 'HR': 'Haryana', 'HP': 'Himachal Pradesh', 
                 'JK': 'Jammu and Kashmir', 'JH': 'Jharkhand', 'KA': 'Karnataka', 'KL': 'Kerala', 'LA': 'Ladakh', 'LD': 'Lakshadweep', 
                 'MP': 'Madhya Pradesh', 'MH': 'Maharashtra', 'MN': 'Manipur', 'ML': 'Meghalaya', 'MZ': 'Mizoram', 'NL': 'Nagaland', 
                 'OR': 'Odisha', 'PY': 'Puducherry', 'PB': 'Punjab', 'RJ': 'Rajasthan', 'SK': 'Sikkim', 'TN': 'Tamil Nadu', 
                 'TG': 'Telangana', 'TR': 'Tripura', 'UP': 'Uttar Pradesh', 'UT': 'Uttarakhand', 'WB': 'West Bengal'
                 }
    return state_dict

@app.route('/')
def index():
    try:
        objc = GA.CoronaAnalysis()
        df_State_Wise =  objc.Get_state_wise('TT')
        #total_cases = str(sum(df_State_Wise[:1][action]))
        df_State_Wise = df_State_Wise[1:]
        df_filter = df_State_Wise.iloc[:,0:7]
        '''
        var_url = urllib.request.urlopen('https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/?output=rss&lang=en&from=0&sort=&format=summary&count=20&fb=&page=1&skfp=&index=tw&q=')
        xmldoc = parse(var_url)
        print(xmldoc)    '''
        feed ="" # feedparser.parse('https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/?output=rss&lang=en&from=0&sort=&format=summary&count=20&fb=&page=1&skfp=&index=tw&q=')
        return render_template('app.html',  tables=df_filter,feed=feed, titles=df_filter.columns.values)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/India')
def india():
    try:
        objc = GA.CoronaAnalysis()
        df_State_Wise =  objc.Get_state_wise('TT')
        #total_cases = str(sum(df_State_Wise[:1][action]))
        df_State_Wise = df_State_Wise[1:]
        df_filter = df_State_Wise.iloc[:,0:7]

        feed = feedparser.parse('http://zeenews.india.com/hindi/india.xml')
        return render_template('app.html',  tables=df_filter,feed=feed.entries, titles=df_filter.columns.values)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/about')
def about():
    try:
        return render_template('about.html', title='About this COVID-19 Project')
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/download')
def download():
    try:
        objdownload = DL.donload_CoronaFiles()
        if objdownload == "1":
            files_download = "Download Process Completed Successfully!!"
            return render_template('download.html', title='About this Project', download = files_download)
        else:
            files_download = objdownload
            return render_template('download.html', title='About this Project' ,download = files_download)
        
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return render_template("error.html", error=error_msg)
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return render_template("error.html", error=error_msg)
    except:
         error_msg = "Unexpected error:", sys.exc_info()[0]
         return render_template("error.html", error=error_msg)

@app.route('/wordldb')
def wordldb():
    try:
        objdownload = CD.Summary()
        if objdownload == "1":
            files_download = "Download Process Completed Successfully!!"
            return render_template('download.html', title='About this Project', download = files_download)
        else:
            files_download = objdownload
            return render_template('download.html', title='About this Project' ,download = files_download)
        
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return render_template("error.html", error=error_msg)
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return render_template("error.html", error=error_msg)
    except:
         error_msg = "Unexpected error:", sys.exc_info()[0]
         return render_template("error.html", error=error_msg)

@app.route('/Country')
def Country():
    try:
        g_color = '#FFA833'
        labels = df_Case_Time["Date"]
        values = df_Case_Time["Daily Confirmed"]
        bar_labels=labels
        bar_values=values
        
        Total_Confirmed = sum(df_Case_Time.tail(1)['Total Confirmed'])
        Total_Recovered = sum(df_Case_Time.tail(1)['Total Recovered'])
        Total_Deceased = sum(df_Case_Time.tail(1)['Total Deceased'])
        Total_Active = Total_Confirmed - (Total_Recovered + Total_Deceased)
        
        total_cases = {"Total Confirmed":Total_Confirmed, "Total Active": Total_Active , "Total Recovered" : Total_Recovered , 
                       "Total Deceased" : Total_Deceased }
        return render_template('country.html', title='Daily COVID-19 Cases in India', max=4500, cases_dict=total_cases, color=g_color, labels=bar_labels, values=bar_values)
    except:
        return render_template("error.html", error="Something else went wrong.")


@app.route('/action')
def action():
    try:
        g_max = 4500
        g_color = '#FFA833'
       
        action = request.args.get("action")
        if action is None:
            action = 'Confirmed'
        if action =='Recovered':
            g_max = 2000
            g_color = 'green'
        if action =='Deceased':
            g_max = 150
            g_color = 'red'
            
        action = "Daily " + action
        
        #df_Case_Time = df_Case_Time.head(10)
        labels = df_Case_Time["Date"]
        values = df_Case_Time[action]
        bar_labels=labels
        bar_values=values
        Total_Confirmed = sum(df_Case_Time.tail(1)['Total Confirmed'])
        Total_Recovered = sum(df_Case_Time.tail(1)['Total Recovered'])
        Total_Deceased = sum(df_Case_Time.tail(1)['Total Deceased'])
        Total_Active = Total_Confirmed - (Total_Recovered + Total_Deceased)
        
        total_cases = {"Total Confirmed":Total_Confirmed, "Total Active": Total_Active , "Total Recovered" : Total_Recovered , 
                       "Total Deceased" : Total_Deceased }
        return render_template('country.html', title= action + ' Corona Growth', max=g_max, cases_dict=total_cases, color=g_color, labels=bar_labels, values=bar_values)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/dictrict')
def dictrict():
    try:
        g_color = '#FFA833'
        stateList = getStates()
        objc = GA.CoronaAnalysis()
        df_District =  objc.Get_District_By_State_Code('UP')
        bar_labels = df_District['District']
        bar_Confirmed = df_District['Confirmed']
        bar_Recovered = df_District['Recovered']
        bar_Deceased = df_District['Deceased']
        
        return render_template('dictrict.html', title='In UP, Dictrict Wise Cases', max=800,color=g_color, 
                               states = stateList, labels=bar_labels, Confirmed=bar_Confirmed,
                               Recovered=bar_Recovered, Deceased=bar_Deceased)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/state')
def state():
    try:
        
        g_color = '#FFA833'
        stateList = getStates()
        objc = GA.CoronaAnalysis()
        df_State_Wise =  objc.Get_state_wise('TT')
        df_State_Wise = df_State_Wise[1:]
        df_CoronaFree = df_State_Wise[df_State_Wise['Active'] == 0]
        corona_free_state = list(df_CoronaFree['State'])
        df_filter = df_State_Wise[df_State_Wise['Confirmed'] >= 5]
       
        bar_labels = df_filter['State']
        bar_values = df_filter['Confirmed']
        
        return render_template('state.html', title='State Wise Confirmed Cases', max=25000, color=g_color, corona_Free=corona_free_state,
                               labels=bar_labels, values=bar_values,states = stateList , Total_Cases={})
    except:
        return render_template("error.html", error="Something else went wrong.")
    
@app.route('/statebyaction/')
def statebyaction():
    try:
        g_color = '#FFA833'
        stateList = getStates()
        objc = GA.CoronaAnalysis()
        #g_max = 5000
        g_color = '#FFA833'
        action = request.args.get("action")
        state_code = request.args.get("code")
        state = request.args.get("state")
        ''' Corona Free'''
        df_State_Wise =  objc.Get_state_wise('TT')
        df_State_Wise = df_State_Wise[1:]
        df_CoronaFree = df_State_Wise[df_State_Wise['Active'] == 0]
        corona_free_state = list(df_CoronaFree['State'])
        '''End'''
        if action is None:
            action = 'Confirmed'
        if action =='Recovered':
            g_max = 2000
            g_color = 'green'
        if action =='Deceased':
            g_max = 200
            g_color = 'red'
       
        _df =  objc.Get_Daily_state_wise()
        df_StateWise = _df[_df['Status']== action]
        g_max = max(df_StateWise[state_code])
        bar_labels = df_StateWise['Date']
        bar_values = df_StateWise[state_code]
        
         
        df_Confirmed = _df[_df['Status']== 'Confirmed']
        Total_Confirmed = sum(df_Confirmed[state_code])
        print(Total_Confirmed)
        df_Recovered = _df[_df['Status']== 'Recovered']
        Total_Recovered = sum(df_Recovered[state_code])

        df_Deceased = _df[_df['Status']== 'Deceased']
        Total_Deceased = sum(df_Deceased[state_code])

        Total_Active = Total_Confirmed - (Total_Recovered + Total_Deceased)
        
        total_cases = {"Total Confirmed":Total_Confirmed, "Total Active": Total_Active , "Total Recovered" : Total_Recovered , 
                       "Total Deceased" : Total_Deceased }


        return render_template('state.html', title="Daily " + action +" cases in state " + state, max=g_max, color=g_color, 
                               corona_Free=corona_free_state,labels=bar_labels, values=bar_values,states = stateList, Total_Cases=total_cases)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/dictrictbystate')
def dictrictbystate():
    try:
        state_code = request.args.get("code")
        print(state_code)
        objc = GA.CoronaAnalysis()
        df_District =  objc.Get_District_By_State_Code(state_code)
        bar_labels = df_District['District']
        return dict(bar_labels)
    except:
        print("Something else went wrong.")


@app.route('/dictrictbyaction')
def dictrictbyaction():
    try:
        g_color = '#FFA833'
        stateList = getStates()
        objc = GA.CoronaAnalysis()
        #g_max = 5000
        action=""
        g_color = '#FFA833'
        state_code = request.args.get("code",default="AN")
        state = request.args.get("state",default="AN")
        if state_code is None:
            state_code = "UP"
        #print("Code : ",state_code)
        if action is None:
            action = 'Confirmed'
        if action =='Recovered':
            g_color = 'green'
        if action =='Deceased':
            g_color = 'red'
       
        df_District =  objc.Get_District_By_State_Code(state_code)
        #print(df_District[0,0:5])
        bar_labels = df_District['District']
        bar_Confirmed = df_District['Confirmed']
        bar_Recovered = df_District['Recovered']
        bar_Deceased = df_District['Deceased']
        
        return render_template('dictrict.html', title='In ' + state + ' Dictrict Wise' + action +' Cases', max=800,color=g_color, 
                               states = stateList, labels=bar_labels, Confirmed=bar_Confirmed,
                               Recovered=bar_Recovered, Deceased=bar_Deceased)
    except:
        return render_template("error.html", error="Something else went wrong.")

@app.route('/confirmed')
def confirmed():
    try:
        objc = GA.CoronaAnalysis()
        df_State_Wise =  objc.Get_state_wise('TT')
        #total_cases = str(sum(df_State_Wise[:1][action]))
        df_State_Wise = df_State_Wise[1:]
        labels = df_State_Wise['State']
        values = df_State_Wise['Confirmed']
        return render_template('state.html', title='State Wise Confirmed Cases', max=25000, sat=zip(values, labels, colors))
    
    except:
        return render_template("error.html", error="Something else went wrong.")
    
@app.route('/world')
def world():
    import world_report as WR
    try:
        df_Country = WR.world_summary()
        df_TotalRecords = WR.WorldTotal()
        print(df_TotalRecords)
        feed = "" #feedparser.parse('https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/?output=rss&lang=en&from=0&sort=&format=summary&count=20&fb=&page=1&skfp=&index=tw&q=')
        return render_template('world.html',title="Corona Cases in World",feed=feed,
        tables=df_Country,TotalRecords=df_TotalRecords)
    
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return render_template("error.html", error=error_msg)
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return render_template("error.html", error=error_msg)
    except:
         error_msg = "Unexpected error from App page:", sys.exc_info()[0]
         return render_template("error.html", error=error_msg)

@app.route('/grahview')
def world_grahview():
    import world_report as WR
    try:
        g_color = '#FFA833'
        df_Country = WR.world_summary()
        bar_labels = df_Country["Country"].head(30)
        bar_values = df_Country["TotalConfirmed"].head(30)
        return render_template('world_graphview.html', title="Corona Cases in World" , max=25000, color=g_color,
                               labels=bar_labels, values=bar_values)
    
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return render_template("error.html", error=error_msg)
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return render_template("error.html", error=error_msg)
    except:
         error_msg = "Unexpected error from App page:", sys.exc_info()[0]
         return render_template("error.html", error=error_msg)
     
@app.route('/wordl_action')
def wordl_action():
    import world_report as WR
    try:
        g_color = '#FFA833'
        action = request.args.get("action",default="TotalConfirmed")
        if action is None:
            action = "Confirmed"
            
        if action =='Recovered':
            g_color = 'green'
        if action =='Deaths':
            g_color = 'red'
            
        action = "Total"+ action
      
        df_Byaction = WR.world_summary()
        bar_labels = df_Byaction["Country"].head(30)
        bar_values = df_Byaction[action].head(30)
        return render_template('world_graphview.html', title='World Wise Cases', max=25000, color=g_color,
                               labels=bar_labels, values=bar_values)
    
    except OSError as err:
        error_msg = "OS error: {0}".format(err)
        return render_template("error.html", error=error_msg)
    except EnvironmentError as eberr:
        error_msg = "OS error: {0}".format(eberr)
        return render_template("error.html", error=error_msg)
    except:
         error_msg = "Unexpected error from App page:", sys.exc_info()[0]
         return render_template("error.html", error=error_msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)