

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

#Home Data
# EXHOSLUSM495S = fred.get_series('EXHOSLUSM495S').to_frame().reset_index()
# EXHOSLUSM495S = EXHOSLUSM495S.rename(columns={"index": "date", EXHOSLUSM495S.columns[1]: "value"})
# fast_filter = (EXHOSLUSM495S.date >= '2020-01-01')
# EXHOSLUSM495S = EXHOSLUSM495S[fast_filter] 
# # EXHOSLUSM495S


# SP500 = fred.get_series('SP500').to_frame().reset_index()
# SP500 = SP500.rename(columns={"index": "date", SP500.columns[1]: "value"})
# fast_filter = (SP500.date >= '2020-01-01')
# SP500 = SP500[fast_filter] 
# SP500 = SP500.dropna()
# SP500

# fast_filter = (SP500.date >= '2020-01-01')
# SP500 = SP500[fast_filter] #SP500 



 #Wilshire 5000 Total Market Full Cap Index (WILL5000INDFC)
# WILL5000INDFC = fred.get_series_all_releases('WILL5000INDFC')
# fast_filter = (WILL5000INDFC.date >= '2020-01-01')
# WILL5000INDFC = WILL5000INDFC[fast_filter] #Unemployment Rate  

# WILL5000INDFC

# xlf_bank_index = get_data('XLF' , start_date = '01/01/2020' ).reset_index().rename(columns={"index": "date"})
# xlf_bank_index = xlf_bank_index[['date','close']]
# xlf_bank_index

M2V = fred.get_series_all_releases('M2V')
fast_filter = (M2V.date >= '2020-01-01')
M2V = M2V[fast_filter] #Velocity of M2 Money Stock 

M2V
