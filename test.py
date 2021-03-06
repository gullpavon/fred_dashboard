

from IPython import get_ipython
import config
import helpers
import pandas as pd
import numpy as np
from fredapi import Fred
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
import plotly.graph_objects as go
get_ipython().run_line_magic('matplotlib', 'inline')
#from datetime import datetime, timedelta
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
#Stock package
from yahoo_fin.stock_info import *
from yahoo_fin import stock_info as si


#Plotly Dash components 
import jupyterlab_dash
import dash
import dash_core_components as dcc
import dash_html_components as html
external_stylesheets = ['https://codepen.io/gullpavon1/pen/bGVWQEr.css']


#Connect to Federal Reserve Economic Data
fred = Fred(api_key=config.fred_api_code)


#round(si.get_live_price('FRC'),2)


#get_data('AMZN' , start_date = seven_days_back , end_date = seven_days_back + timedelta(days=1))

#get_data('AMZN' , start_date = '05/14/2020' , end_date ='05/15/2020' )


#print('done')
#getting dates for % change analysis on the stocks
#dates2 are used in order to get a value when a particular date does not exist. This will give you a range of dates and select the earliest available one.
todays_date = date.today() 
todays_date2 = date.today() + timedelta(days=-3)

seven_days_back = todays_date + timedelta(days=-7)
seven_days_back2 = todays_date + timedelta(days=-13)

thirty_days_back =  todays_date + timedelta(days=-30)
thirty_days_back2 =  todays_date + timedelta(days=-35)

six_months_back =   todays_date + timedelta(days=-180)
six_months_back2 =   todays_date + timedelta(days=-185)

one_year_back =   todays_date + timedelta(days=-365)
one_year_back2 =   todays_date + timedelta(days=-370)

three_years_back = todays_date + timedelta(days=-1095)
three_years_back2 = todays_date + timedelta(days=-1100)

print(six_months_back)
#get_data('AMZN' , start_date = '2019-11-16' , end_date = '2019-11-20').get('close')#.to_frame().reset_index().sort_values('index').iloc[1]

#had to create this because sometimes the respective date does not exist, so we need to get a range of dates near and select the first. 
def stock_back_date_value (ticker,date_start,date_end):
    return get_data(ticker , start_date = date_end , end_date = date_start).get('close').to_frame().reset_index().sort_values('index', ascending=False).iloc[0,1]


def get_stock_data(ticker, metric_type):
    '''
    NOTES:
    STOCK_LIVE = round(si.get_live_price("FRC"),2)
    STOCK_PREV = round(si.get_quote_table('FRC').get('Previous Close'),2)
    FRC_CHG = round((FRC_STOCK_LIVE - FRC_STOCK_PREV) / (FRC_STOCK_PREV) * 100,2)
    
    '''


    if metric_type == 'live':
        return round(si.get_live_price(ticker),2)
    if metric_type == 'prev':
         return round(si.get_quote_table(ticker).get('Previous Close'),2)
    if metric_type == 'perc_chg_1_day':
         return round((round(si.get_live_price(ticker),2) - round(si.get_quote_table(ticker).get('Previous Close'),2)) / (round(si.get_quote_table(ticker).get('Previous Close'),2)) * 100,2)
    if metric_type == 'seven_days_back':
        return round((round(si.get_live_price(ticker),2) - stock_back_date_value(ticker,seven_days_back,seven_days_back2) ) / (stock_back_date_value(ticker,seven_days_back,seven_days_back2)) * 100,2)
    if metric_type == 'thirty_days_back':
        return round((round(si.get_live_price(ticker),2) - stock_back_date_value(ticker,thirty_days_back,thirty_days_back2) ) / (stock_back_date_value(ticker,thirty_days_back,thirty_days_back2)) * 100,2)
    if metric_type == 'six_months_back':
        return round((round(si.get_live_price(ticker),2) - stock_back_date_value(ticker,six_months_back,six_months_back2) ) / (stock_back_date_value(ticker,six_months_back,six_months_back2)) * 100,2)
    if metric_type == 'one_year_back':
        return round((round(si.get_live_price(ticker),2) - stock_back_date_value(ticker,one_year_back,one_year_back2) ) / (stock_back_date_value(ticker,one_year_back,one_year_back2)) * 100,2)
    if metric_type == 'three_years_back':
        return round((round(si.get_live_price(ticker),2) - stock_back_date_value(ticker,three_years_back,three_years_back2) ) / (stock_back_date_value(ticker,three_years_back,three_years_back2)) * 100,2)



get_stock_data("FRC", "thirty_days_back")

#get_stock_data('FRC','perc_chg_1_day')

#get_stock_data("BAC", "live")


# import requests
# import json
# import prettytable
# headers = {'Content-type': 'application/json'}
# data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":"2011", "endyear":"2014"})
# p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
# json_data = json.loads(p.text)
# for series in json_data['Results']['series']:
#     x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
#     seriesId = series['seriesID']
#     for item in series['data']:
#         year = item['year']
#         period = item['period']
#         value = item['value']
#         footnotes=""
#         for footnote in item['footnotes']:
#             if footnote:
#                 footnotes = footnotes + footnote['text'] + ','
#         if 'M01' <= period <= 'M12':
#             x.add_row([seriesId,year,period,value,footnotes[0:-1]])
#     output = open(seriesId + '.txt','w')
#     output.write (x.get_string())
#     output.close()


# import requests
# import json
# import pandas as pd
# from pandas.io.json import json_normalize
# url = 'https://api.bls.gov/publicAPI/v1/timeseries/data/CEU0800000003' #CEU0800000003 Employment & Unemployment
# data = requests.get(url).json()


# print('Status: ' + data['status'])

# print(data['Results'])



import pandas as pd
from blsconnect import RequestBLS, bls_search


bls = RequestBLS(key=config.dep_labor_api_key)


# Get seasonally-adjusted unemployment rates for Florida, Georgia, and all U.S.
series_names = bls_search(data="cpi", sa=True)
CPI = bls.series(series_names, start_year=2019, end_year=2020)
CPI
# UNRATE['date'] = UNRATE['year'].astype(str)  + UNRATE['period'].str.replace('M','',regex=True)
# UNRATE['date'] = pd.to_datetime(UNRATE['date'], format='%Y%m', errors='coerce').dropna()
# UNRATE = UNRATE.rename(columns={'LNS14000000':'value'})

# UNRATE

