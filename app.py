# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

from IPython import get_ipython
import config
import helpers
import pandas as pd
import numpy as np
from fredapi import Fred
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
get_ipython().run_line_magic('matplotlib', 'inline')

#Stock package
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import *

#Plotly Dash components 
import jupyterlab_dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/gullpavon1/pen/bGVWQEr.css']

#Connect to Federal Reserve Economic Data
fred = Fred(api_key=config.fred_api_code)

#Search for FRED data
#fred.search('mortgage').T





# %%
###### GET DATA ########


#Econcomy 
SP500 = fred.get_series('SP500').to_frame().reset_index()
SP500 = SP500.rename(columns={"index": "date", SP500.columns[1]: "value"})
fast_filter = (SP500.date >= '2020-01-01')
SP500 = SP500[fast_filter] 
SP500 = SP500.dropna()
SP500#SP500 


xlf_bank_index = get_data('XLF' , start_date = '01/01/2020' ).reset_index().rename(columns={"index": "date"})
xlf_bank_index = xlf_bank_index[['date','close']]
xlf_bank_index

UNRATE = fred.get_series_all_releases('UNRATE')
fast_filter = (UNRATE.date >= '2020-01-01')
UNRATE = UNRATE[fast_filter] #Unemployment Rate   

M2V = fred.get_series_all_releases('M2V')
fast_filter = (M2V.date >= '2020-01-01')
M2V = M2V[fast_filter] #Velocity of M2 Money Stock 

GDPC1 = fred.get_series_all_releases('GDPC1')
fast_filter = (GDPC1.date >= '2020-01-01')
GDPC1 = GDPC1[fast_filter] #Real Gross Domestic Product 




#Mortgage Rates Data
MORTGAGE30US = fred.get_series_all_releases('MORTGAGE30US')
fast_filter = (MORTGAGE30US.date >= '2020-01-01')
MORTGAGE30US = MORTGAGE30US[fast_filter]

MORTGAGE15US = fred.get_series_all_releases('MORTGAGE15US')
fast_filter = (MORTGAGE15US.date >= '2020-01-01')
MORTGAGE15US = MORTGAGE15US[fast_filter]

MPRIME = fred.get_series_all_releases('MPRIME')
fast_filter = (MPRIME.date >= '2020-01-01')
MPRIME = MPRIME[fast_filter]

#Home Data
EXHOSLUSM495S = fred.get_series('EXHOSLUSM495S').to_frame().reset_index()
EXHOSLUSM495S = EXHOSLUSM495S.rename(columns={"index": "date", EXHOSLUSM495S.columns[1]: "value"})
fast_filter = (EXHOSLUSM495S.date >= '2020-01-01')
EXHOSLUSM495S = EXHOSLUSM495S[fast_filter] 
EXHOSLUSM495S

MSACSR = fred.get_series_all_releases('MSACSR') 
fast_filter = (MSACSR.date >= '2020-01-01')
MSACSR = MSACSR[fast_filter] #  Monthly Supply of Houses in the United States

CSUSHPINSA = fred.get_series_all_releases('CSUSHPINSA') 
fast_filter = (CSUSHPINSA.date >= '2020-01-01')
CSUSHPINSA = CSUSHPINSA[fast_filter] #  Monthly Supply of Houses in the United States




#MONEY SUPPLY VS INFLATION
BOGMBASEW = fred.get_series_all_releases('BOGMBASEW') 
fast_filter = (BOGMBASEW.date >= '2020-01-01')
BOGMBASEW = BOGMBASEW[fast_filter] # Monetary Base

M2 = fred.get_series_all_releases('M2') 
fast_filter = (M2.date >= '2020-01-01')
M2 = M2[fast_filter] #  M2 Money Stock (M2)

CPIAUCSL = fred.get_series_all_releases('CPIAUCSL') 
fast_filter = (CPIAUCSL.date >= '2020-01-01')
CPIAUCSL = CPIAUCSL[fast_filter] #   Consumer Price Index for All Urban Consumers: All Items in U.S. City Average


#Bank Factors Data
FEDFUNDS = fred.get_series_all_releases('FEDFUNDS') 
fast_filter = (FEDFUNDS.date >= '2020-01-01')
FEDFUNDS = FEDFUNDS[fast_filter] # Effective Federal Funds Rate

REQRESNS = fred.get_series_all_releases('REQRESNS') 
fast_filter = (REQRESNS.date >= '2020-01-01')
REQRESNS = REQRESNS[fast_filter] #  Required Reserves of Depository Institutions 

EXCSRESNW = fred.get_series_all_releases('EXCSRESNW') 
fast_filter = (EXCSRESNW.date >= '2020-01-01')
EXCSRESNW = EXCSRESNW[fast_filter] #  Excess Reserves of Depository Institutions



#Live Stock Prices
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
    if metric_type == 'perc_chg':
         return round((round(si.get_live_price(ticker),2) - round(si.get_quote_table(ticker).get('Previous Close'),2)) / (round(si.get_quote_table(ticker).get('Previous Close'),2)) * 100,2)


def color_picker(value_input):
    if value_input > 0:
        return '#409f83'
    else: 
        return '#ef3b46'


# %%

# x = MORTGAGE30US['date']
# x2 = MORTGAGE30US['date'].astype(np.int64)
# y = MORTGAGE30US['value']

# data = go.Scatter(x=x, y=y, mode='lines+markers', marker={'color': x2, 'colorscale': 'Rainbow', 'size': 10},)

# layout = dict(plot_bgcolor='white', margin=dict(t=0, b=0, r=0, l=0, pad=0),
#               xaxis=dict(showgrid=False, zeroline=False, mirror=True, linecolor='gray'),
#               yaxis=dict(showgrid=False, zeroline=False, mirror=True, linecolor='gray'))

# fig = go.Figure(data=data, layout=layout)


# %%
#Styling / CSS Stuff 

stock_ticker_style={'background':'#36404e', 'padding-top': '3px','padding-right':'6px','padding-bottom':'3px', 'padding-left': '6px', }


# %%
################# Home Supply Vs Home Prices ############

fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=EXHOSLUSM495S['date'], y=EXHOSLUSM495S['value'], name="Sales", line=dict(color= '#9F86FF' ), ),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=MSACSR['date'], y=MSACSR['value'], name="Supply", line=dict(color= '#1CA8DD'),),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Home Sales Vs Supply"
   ,title_x=0.5
)

# Set x-axis title
#fig.update_xaxes(title_text="Date")


# Set y-axes titles
fig.update_yaxes(title_text="<b>Sales</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Supply</b>", secondary_y=True)

fig.update_layout(
                 paper_bgcolor = "#2e3641",
                 plot_bgcolor =  "#2e3641",
                 font = {"color":"White"},
                 xaxis =  {'showgrid': False, 'showline': False},
                 yaxis = {'showgrid': False, 'showline': False},
                 yaxis2 = {'showgrid': False, 'showline': False},


    )



################# SP500 VS BANK Industry ############
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig2.add_trace(
   go.Scatter(x=SP500['date'], y=SP500['value'], name="SP500", line=dict(color= '#9F86FF' ), fill='tozeroy', fillcolor='#9F86FF',  opacity=0.1,),
    secondary_y=False,
)

fig2.add_trace(
    go.Scatter(x=xlf_bank_index['date'], y=xlf_bank_index['close'], name="Banks", line=dict(color= '#1CA8DD'), fill='tonexty', fillcolor='#1CA8DD', opacity=0.1,),
    secondary_y=True,
)

# Add figure title
fig2.update_layout(
    title_text="SP500 Vs. Banking"
   ,title_x=0.5
)

# Set x-axis title
#fig.update_xaxes(title_text="Date")


# Set y-axes titles
fig2.update_yaxes(title_text="<b>SP500</b>", secondary_y=False)
fig2.update_yaxes(title_text="<b>Banking</b>", secondary_y=True)

fig2.update_layout(
                 paper_bgcolor = "#2e3641",
                 plot_bgcolor =  "#2e3641",
                 font = {"color":"White"},
                 xaxis =  {'showgrid': False, 'showline': False},
                 yaxis = {'showgrid': False, 'showline': False},
                 yaxis2 = {'showgrid': False, 'showline': False},


    )







# %%
####################Dash App###############################################################################################
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div( style={'padding-top': '10px',} , children=[

#STOCK TICKER INFO
 html.Div([
    html.Div([


        html.Div([
        html.H2(f'FRC ${get_stock_data("FRC", "live")}'),
        html.H4(f'{get_stock_data("FRC", "perc_chg")}%', style={'color': f'{color_picker(get_stock_data("FRC", "perc_chg"))}'}),
        ], className="two columns", style=stock_ticker_style),

        html.Div([
        html.H2(f'JPM ${get_stock_data("JPM", "live")}'),
        html.H4(f'{get_stock_data("JPM", "perc_chg")}%', style={'color': f'{color_picker(get_stock_data("JPM", "perc_chg"))}'}),
        ], className="two columns", style=stock_ticker_style),

        html.Div([
        html.H2(f'BAC ${get_stock_data("BAC", "live")}'),
        html.H4(f'{get_stock_data("BAC", "perc_chg")}%', style={'color': f'{color_picker(get_stock_data("BAC", "perc_chg"))}'}),
        ], className="two columns", style=stock_ticker_style),


        html.Div([
        html.H2(f'WFC ${get_stock_data("WFC", "live")}'),
        html.H4(f'{get_stock_data("WFC", "perc_chg")}%', style={'color': f'{color_picker(get_stock_data("WFC", "perc_chg"))}'}),
        ], className="two columns", style=stock_ticker_style),





    ], className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center"  })
]),



    html.H1(children='Hello  WTF Dash'),

   
    
   
#dcc.Graph(figure=fig),

    html.Div(children='''
        Dash: A web application framework for Python. 
    '''),

   


#     html.H2(children='Money Supply vs. Inflation'),

#####################################################################################################################
#ROW ECONOMY WATCH:
html.H3('Economy Watch', style={'text-align': 'center'}),
html.H5("""Banks are heavily correlated with the economy.The banking sector is an industry and a 
section of the economy devoted to the holding of financial assets for others and investing those 
financial assets as a leveraged way to create more wealth. The sector also includes the regulation 
of banking activities by government agencies, insurance, mortgages, investor services
, and credit cards.""", style={'text-align': 'center'}),
html.Div([

html.Div([


 dcc.Graph(
        id='SP500',
        figure={
            'data': [
                 { "x": SP500['date'],"y": SP500['value'],"mode": "lines","name": '30 YR', 'line': {'color': '#9F86FF' }},
                      ],
            'layout': {
                'title': 'SP 500',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          ),

    html.Div([

    dcc.Graph(figure=fig2),
          ], className="twelve columns"),




          ], ),   
# S&P 500 (SP500)
# Unemployment Rate  (UNRATE)
# Velocity of M2 Money Stock (M2V)
# Real Gross Domestic Product (GDPC1)


] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),

#####################################################################################################################
#ROW: HOME PRICING / SUPPLY 

html.H3('Mortgage Watch', style={'text-align': 'center'}),
html.H5("""Mortgages are a huge part of a bank's business; the below gives indication of the health of the mortgage market. 
    If the below graph(s) is showing a negative trajectory, the bank's mortgage business should be monitored closesly.  """, style={'text-align': 'center'}),


html.Div([



   
#30yr/15yr Mortage Rates 
 html.Div([
 dcc.Graph(
        id='MORTGAGE_RATES',
        figure={
            'data': [
                 { "x": MORTGAGE30US['date'],"y": MORTGAGE30US['value'],"mode": "lines","name": '30 YR', 'line': {'color': '#9F86FF' }},
                 { "x": MORTGAGE15US['date'],"y": MORTGAGE15US['value'],"mode": "lines","name": '15 YR', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Mortgage Rates',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),    
          
#Home Supply vs. Home Sales
 html.Div([

    dcc.Graph(figure=fig),
          ], className="threehalf columns"),


 html.Div([
 dcc.Graph(
        id='CSUSHPINSA',
        figure={
            'data': [
                 { "x": CSUSHPINSA['date'],"y": CSUSHPINSA['value'],"mode": "lines","name": '30 YR', 'line': {'color': '#9F86FF' }},
                    ],
            'layout': {
                'title': 'U.S. National Home Price Index',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"}
                    }
               }
       
          )
          ], className="threehalf columns"),    
          


          


] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),


#####################################################################################################################
#ROW: Bank Factors

html.H3('Bank Factors Watch', style={'text-align': 'center'}),
html.H5("""The below metrics help showcase some factors that may affect a bank's health. Banks are required by the 
    Federal Reserve to maintain money at the Federal Reserve Bank. This is to mitigate bank runs, finacial crisis stressors, 
    and overall ensure bank's can withstand downturns. However this can be seen as a double edge sword, for every dollar that is
    locked up at the federal reserve, means that money cannot be put into other investments, and ultimately can slow the bank's
    overall growth. The Fed may implement lower reserve requirments in tiumes of downturns to reduce the bank's risk of folding due 
    to lack of access to capuital. During Covid-19 the Fed has reduced the requirements to 0%. """, style={'text-align': 'center'}),


html.Div([

 html.Div([
 dcc.Graph(
        id='FEDFUNDS',
        figure={
            'data': [
                 { "x": FEDFUNDS['date'],"y": FEDFUNDS['value'],"mode": "lines","name": 'Rate', 'line': {'color': '#9F86FF' }},
                    ],
            'layout': {
                'title': ' Federal Funds Rate',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"}
                    }
               }
       
          )
          ], className="threehalf columns"),    
          
 html.Div([
 dcc.Graph(
        id='REQRESNS',
        figure={
            'data': [
                 { "x": REQRESNS['date'],"y": REQRESNS['value'],"mode": "lines","name": 'Reserves', 'line': {'color': '#9F86FF' }},
                    ],
            'layout': {
                'title': 'Required Reserves of Depository Institutions',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"}
                    }
               }
       
          )
          ], className="threehalf columns"),    
          
html.Div([
 dcc.Graph(
        id='EXCSRESNW',
        figure={
            'data': [
                 { "x": EXCSRESNW['date'],"y": EXCSRESNW['value'],"mode": "lines","name": 'Excess Reserves', 'line': {'color': '#9F86FF' }},
                    ],
            'layout': {
                'title': 'Excess Reserves of Depository Institutions',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"}
                    }
               }
       
          )
          ], className="threehalf columns"),    
          



] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),



##################################################################################################################################


#ROW 2 
html.Div([

html.Div([
 
  dcc.Graph(
        id='M1',
        figure={
            'data': [
                 { "x": BOGMBASEW['date'],"y": BOGMBASEW['value'],"mode": "lines","name": 'Monetary Base', 'line': {'color': '#9F86FF' }},
               
              
            ],
            'layout': {
                'title': 'Monetary Base',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
              #  'yaxis': {'type': 'log', 'autorange': 'true'}, #log functionality 
            }
        }
       
    ), ], className="threehalf columns"),

#---

  html.Div([    
    dcc.Graph(
        id='M2',
        figure={
            'data': [
                 { "x": M2['date'],"y": M2['value'],"mode": "lines","name": 'M2', 'line': {'color': '#1CA8DD'}},
               
              
            ],
            'layout': {
                'title': 'M2',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
              #  'yaxis': {'type': 'log', 'autorange': 'true'}, #log functionality 
            }
        }
       
    ),
], className="threehalf columns"),
#---

        html.Div([

    dcc.Graph(
        id='CPI',
        figure={
            'data': [
                  { "x": CPIAUCSL['date'],"y": CPIAUCSL['value'],"mode": "lines","name": 'CPI - Inflation', 'line': {'color': '#FFFFFF'}},


               
              
            ],
            'layout': {
                'title': 'CPI - Inflation',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
              #  'yaxis': {'type': 'log', 'autorange': 'true'}, #log functionality 
            }
        }
       
    )
       

        ], className="threehalf columns",),



], className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),






#######################################################################################################################


 



 
              

])


# Running the server
if __name__ == "__main__":
    app.run_server(debug=False)




# # %%
# #30 Yr Mortgage Rates
# MORTGAGE30US.plot.line(x='date', y='value')
# plt.title ('30 Yr Mortgage Rates')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')


# # %%

# #Unemployment Rate
# #For Unemployment number use: UNEMPLOY
# UNRATE = fred.get_series_all_releases('UNRATE')
# UNRATE = UNRATE[UNRATE.date >= '2019-01-01']

# UNRATE.plot.line(x='date', y='value')
# plt.title ('Unemployment Rate')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')


# # %%


# #Fed Funds Rate
# FEDFUNDS = fred.get_series_all_releases('FEDFUNDS')
# FEDFUNDS = FEDFUNDS[FEDFUNDS.date >= '2019-01-01']

# FEDFUNDS.plot.line(x='date', y='value')
# plt.title ('Federal Funds Rate')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')


# # %%

# #10-2 Treasury Yield Spread
# T10Y2Y = fred.get_series_all_releases('T10Y2Y')
# T10Y2Y = T10Y2Y[T10Y2Y.date >= '2019-01-01']
# T10Y2Y.dropna(inplace= True)

# T10Y2Y.plot.line(x='date', y='value')
# plt.title ('10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity ')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')
# plt.axhline(0, 0, 1, label='0')


# # %%
# #10-2 Treasury Yield Spread
# T10YIE = fred.get_series_all_releases('T10YIE')
# T10YIE = T10YIE[T10YIE.date >= '2020-01-01']
# T10YIE.dropna(inplace= True)


# T10YIE.plot.line(x='date', y='value')
# plt.title ('10-Year Breakeven Inflation Rate')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')
# plt.axhline(0, 0, 1, label='0')


# # %%

# CSUSHPINSA = fred.get_series_all_releases('CSUSHPINSA')
# CSUSHPINSA = CSUSHPINSA[CSUSHPINSA.date >= '2019-01-01']
# CSUSHPINSA.dropna(inplace= True)
# CSUSHPINSA.plot.line(x='date', y='value')

# plt.title ('S&P/Case-Shiller U.S. National Home Price Index')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')
# plt.axhline(0, 0, 1, label='0')


# # %%

# IOER = fred.get_series_all_releases('IOER')
# IOER = IOER[IOER.date >= '2019-01-01']
# IOER.dropna(inplace= True)
# IOER.plot.line(x='date', y='value')

# plt.title ('Interest Rate on Excess Reserves')
# plt.xlabel ('Date')
# plt.ylabel ('Rate')
# plt.axhline(0, 0, 1, label='0')


# %%
"""


##Mortage Watch
[X] Existing Home Sales (EXHOSLUSM495S)
[X] Monthly Supply of Houses in the United States (MSACSR)
[X] S&P/Case-Shiller U.S. National Home Price Index (CSUSHPINSA)

10-Year Treasury Constant Maturity Rate (DGS10)

###ECONOMY WATCH

[X] Monetary Base; Total (BOGMBASEW)
[X] M2 Money Stock (M2)
[X] Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCSL)

S&P 500 (SP500)
Wilshire 5000 Total Market Full Cap Index (WILL5000INDFC)
Unemployment Rate  (UNRATE)
Velocity of M2 Money Stock (M2V)
Real Gross Domestic Product (GDPC1)



###Bank Economy Watch
Delinquency Rate on Consumer Loans, All Commercial Banks (DRCLACBS)
Net Interest Margin for all U.S. Banks (USNIM)
Net Income for Commercial Banks in United States (USNINC)
Total Reserve Balances Maintained with Federal Reserve Banks (RESBALNS)
Cash Assets, All Commercial Banks (CASACBW027SBOG)
Demand Deposits: Total (WDDSL)	
Loan Loss Reserve to Total Loans for all U.S. Banks (USLLRTL)
Bank Z-Score for United States (DDSI01USA645NWDB)

##BANK Factors
Effective Federal Funds Rate (FEDFUNDS) 
Required Reserves of Depository Institutions (REQRESNS)
Excess Reserves of Depository Institutions  (EXCSRESNW)
Bank Prime Loan Rate (MPRIME)

"""


# %%


