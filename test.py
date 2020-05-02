

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
EXHOSLUSM495S = fred.get_series('EXHOSLUSM495S').to_frame().reset_index()
EXHOSLUSM495S = EXHOSLUSM495S.rename(columns={"index": "date", EXHOSLUSM495S.columns[1]: "value"})
fast_filter = (EXHOSLUSM495S.date >= '2020-01-01')
EXHOSLUSM495S = EXHOSLUSM495S[fast_filter] 
EXHOSLUSM495S
