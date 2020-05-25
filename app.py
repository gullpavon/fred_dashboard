# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from IPython import get_ipython
from datetime import datetime
import config
import helpers
import pandas as pd
import numpy as np
from fredapi import Fred
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from datetime import timedelta, date
get_ipython().run_line_magic('matplotlib', 'inline')

#Stock package
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import *

# U.S. Department of Labor API
from blsconnect import RequestBLS, bls_search
bls = RequestBLS(key=config.dep_labor_api_key)


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
xlf_bank_index #SP500 financial stocks - method 1

BKX = get_data('^BKX' , start_date = '01/01/2020' ).reset_index().rename(columns={"index": "date"})
BKX = BKX[['date','close']] #Bank index - method 2

#Unemployment rate from FRED (not updated as frequently)
#UNRATE = fred.get_series_all_releases('UNRATE')
#fast_filter = (UNRATE.date >= '2020-01-01')
#UNRATE = UNRATE[fast_filter] #Unemployment Rate 

#UNEMPLOYMENT from BLS
series_names = bls_search(data="ur", sa=True)
UNRATE = bls.series(series_names, start_year=2019, end_year=2020)
UNRATE['date'] = UNRATE['year'].astype(str)  + UNRATE['period'].str.replace('M','',regex=True)
UNRATE['date'] = pd.to_datetime(UNRATE['date'], format='%Y%m', errors='coerce').dropna()
UNRATE = UNRATE.rename(columns={'LNS14000000':'value'})




M2V = fred.get_series_all_releases('M2V')
fast_filter = (M2V.date >= '2019-01-01')
M2V = M2V[fast_filter] #Velocity of M2 Money Stock 

GDPC1 = fred.get_series_all_releases('GDPC1')
fast_filter = (GDPC1.date >= '2019-01-01')
GDPC1 = GDPC1[fast_filter] #Real Gross Domestic Product 



###Bank Economy Watch

USNIM = fred.get_series('USNIM').to_frame().reset_index()
USNIM = USNIM.rename(columns={"index": "date", USNIM.columns[1]: "value"})
fast_filter = (USNIM.date >= '2019-01-01')
USNIM = USNIM[fast_filter] #Net Interest Margin for all U.S. Banks 

USNINC = fred.get_series('USNINC').to_frame().reset_index()
USNINC = USNINC.rename(columns={"index": "date", USNINC.columns[1]: "value"})
fast_filter = (USNINC.date >= '2019-01-01')
USNINC = USNINC[fast_filter] #Net Income for Commercial Banks in United States 


DRALACBS = fred.get_series('DRALACBS').to_frame().reset_index()
DRALACBS = DRALACBS.rename(columns={"index": "date", DRALACBS.columns[1]: "value"})
fast_filter = (DRALACBS.date >= '2019-01-01')
DRALACBS = DRALACBS[fast_filter]  #Delinquency Rate on All Loans, All Commercial Banks


RESBALNS = fred.get_series_all_releases('RESBALNS')
fast_filter = (RESBALNS.date >= '2020-01-01')
RESBALNS = RESBALNS[fast_filter] #Total Reserve Balances Maintained with Federal Reserve Banks


USLLRTL = fred.get_series('USLLRTL').to_frame().reset_index()
USLLRTL = USLLRTL.rename(columns={"index": "date", USLLRTL.columns[1]: "value"})
fast_filter = (USLLRTL.date >= '2019-01-01')
USLLRTL = USLLRTL[fast_filter] #Loan Loss Reserve to Total Loans for all U.S. Banks


CASACBW027SBOG = fred.get_series_all_releases('CASACBW027SBOG')
fast_filter = (CASACBW027SBOG.date >= '2020-01-01')
CASACBW027SBOG = CASACBW027SBOG[fast_filter] #Cash Assets, All Commercial Banks (

WDDSL = fred.get_series_all_releases('WDDSL')
fast_filter = (WDDSL.date >= '2020-01-01')
WDDSL = WDDSL[fast_filter] #Demand Deposits: Total 



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
#EXHOSLUSM495S

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

#A PPI from the commodity classification system measures change in
# prices received for a product or service regardless of industry of origin.
#  It organizes products by similarity, end use, or material composition.
# another Inflation watch:
PPIACO = fred.get_series_all_releases('PPIACO') 
fast_filter = (PPIACO.date >= '2020-01-01')
PPIACO = PPIACO[fast_filter] #  Producer Price Index for All Commodities



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



#had to create this because sometimes the respective date does not exist, so we need to get a range of dates near and select the first. 
def stock_back_date_value (ticker,date_start,date_end):
    return get_data(ticker , start_date = date_end , end_date = date_start).get('close').to_frame().reset_index().sort_values('index', ascending=False).iloc[0,1]



#Stock Prices Data

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


def color_picker(value_input):
    if value_input > 0:
        return '#409f83'
    else: 
        return '#ef3b46'



#Styling / CSS Stuff 

stock_ticker_style={'background':'#36404e', 'padding-top': '3px','padding-right':'6px','padding-bottom':'3px', 'padding-left': '6px', }


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
   go.Scatter(x=SP500['date'], y=SP500['value'], name="SP500", line=dict(color= '#9F86FF' ), fill='tozeroy', fillcolor='rgba(159,134,255, 0.8)',  opacity=0.8,),
    secondary_y=False,
)

fig2.add_trace(
    go.Scatter(x=BKX['date'], y=BKX['close'], name="Banks", line=dict(color= '#1CA8DD'), fill='tozeroy', fillcolor='rgba(28,168,221, 0.8)', opacity=0.8,),
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
        html.H4(f'{get_stock_data("FRC", "perc_chg_1_day")}%', style={'color': f'{color_picker(get_stock_data("FRC", "perc_chg_1_day"))}'}),
        html.H6(f'7 days: {get_stock_data("FRC", "seven_days_back")}%', style={'color': f'{color_picker(get_stock_data("FRC", "seven_days_back"))}'}),
        html.H6(f'30 days: {get_stock_data("FRC", "thirty_days_back")}%', style={'color': f'{color_picker(get_stock_data("FRC", "thirty_days_back"))}'}),
        html.H6(f'6 Mons: {get_stock_data("FRC", "six_months_back")}%', style={'color': f'{color_picker(get_stock_data("FRC", "six_months_back"))}'}),
        html.H6(f'1 Yr: {get_stock_data("FRC", "one_year_back")}%', style={'color': f'{color_picker(get_stock_data("FRC", "one_year_back"))}'}),
        html.H6(f'3 Yrs: {get_stock_data("FRC", "three_years_back")}%', style={'color': f'{color_picker(get_stock_data("FRC", "three_years_back"))}'}),

        ], className="two columns", style=stock_ticker_style),

        html.Div([
        html.H2(f'JPM ${get_stock_data("JPM", "live")}'),
        html.H4(f'{get_stock_data("JPM", "perc_chg_1_day")}%', style={'color': f'{color_picker(get_stock_data("JPM", "perc_chg_1_day"))}'}),
        html.H6(f'7 days: {get_stock_data("JPM", "seven_days_back")}%', style={'color': f'{color_picker(get_stock_data("JPM", "seven_days_back"))}'}),
        html.H6(f'30 days: {get_stock_data("JPM", "thirty_days_back")}%', style={'color': f'{color_picker(get_stock_data("JPM", "thirty_days_back"))}'}),
        html.H6(f'6 Mons: {get_stock_data("JPM", "six_months_back")}%', style={'color': f'{color_picker(get_stock_data("JPM", "six_months_back"))}'}),
        html.H6(f'1 Yr: {get_stock_data("JPM", "one_year_back")}%', style={'color': f'{color_picker(get_stock_data("JPM", "one_year_back"))}'}),
        html.H6(f'3 Yrs: {get_stock_data("JPM", "three_years_back")}%', style={'color': f'{color_picker(get_stock_data("JPM", "three_years_back"))}'}),

        ], className="two columns", style=stock_ticker_style),

        html.Div([
        html.H2(f'BAC ${get_stock_data("BAC", "live")}'),
        html.H4(f'{get_stock_data("BAC", "perc_chg_1_day")}%', style={'color': f'{color_picker(get_stock_data("BAC", "perc_chg_1_day"))}'}),
        ], className="two columns", style=stock_ticker_style),


        html.Div([
        html.H2(f'WFC ${get_stock_data("WFC", "live")}'),
        html.H4(f'{get_stock_data("WFC", "perc_chg_1_day")}%', style={'color': f'{color_picker(get_stock_data("WFC", "perc_chg_1_day"))}'}),
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

html.Div([

html.Div([

html.H3('Economy Watch', style={'text-align': 'center'}),
html.H5("""Banks are heavily correlated with the economy.The banking sector is an industry and a 
section of the economy devoted to the holding of financial assets for others and investing those 
financial assets as a leveraged way to create more wealth. The sector also includes the regulation 
of banking activities by government agencies, insurance, mortgages, investor services
, and credit cards.""", style={'text-align': 'center'}),

    html.Div([

    dcc.Graph(figure=fig2),
          ], className="eleven columns"),



html.Div([
 dcc.Graph(
        id='UNRATE',
        figure={
            'data': [
                     { "x": UNRATE['date'],"y": UNRATE['value'],"mode": "lines","name": 'Rate', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Unemployment Rate',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   

html.Div([
dcc.Graph(
        id='M2V',
        figure={
            'data': [
                     { "x": M2V['date'],"y": M2V['value'],"mode": "lines","name": 'Velocity', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Velocity of M2 Money Stock',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   

html.Div([
dcc.Graph(
        id='GDPC1',
        figure={
            'data': [
                     { "x": GDPC1['date'],"y": GDPC1['value'],"mode": "lines","name": 'GDP', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Real Gross Domestic Product ',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   







          ], ),   


] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),


#####################################################################################################################
#ROW BANK ECONOMY WATCH:

html.Div([
html.H3('Bank Economy Watch', style={'text-align': 'center'}),
] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),

html.Div([
html.H5("""blah blah b lah blahj fpoksdnfg poksndg odshg pdsfngop dshg;kdshidsf;gj dskgnsdkng;dfkjgdfg
dfjkngdsflkjng dsjng ldsjgdl skg sdlkjngldksjgnlas;f dsjknflsda flkasjnfliasdbflasjibflasijfbasdfsdkjafbh 
nsdfkjsdb fkjsb fsadjbf lasjbflksajbdfaisjbfoaisdfosdfho saifiawfjewibfiuawfliaw fusb fuisw faewb kjhvku.""", style={'text-align': 'center'}),

] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),

html.Div([

    



html.Div([




html.Div([
 dcc.Graph(
        id='USNIM',
        figure={
            'data': [
                     { "x": USNIM['date'],"y": USNIM['value'],"mode": "lines","name": 'Net Int Margin', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'NIM for all U.S. Banks ',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="five columns"),   


html.Div([
dcc.Graph(
        id='USNINC',
        figure={
            'data': [
                     { "x": USNINC['date'],"y": USNINC['value'],"mode": "lines","name": 'Income', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'NII Commercial Banks in United States',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="five columns"),   







          ],  className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" } ),   


] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),


####BANK ENCONOMY ROW 2




#Cash Assets, All Commercial Banks (CASACBW027SBOG)
#Demand Deposits: Total (WDDSL)	


html.Div([



html.Div([
 dcc.Graph(
        id='DRALACBS',
        figure={
            'data': [
                     { "x": DRALACBS['date'],"y": DRALACBS['value'],"mode": "lines","name": 'Rate', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Delinq. Rate on All Loans',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   

html.Div([
dcc.Graph(
        id='RESBALNS',
        figure={
            'data': [
                     { "x": RESBALNS['date'],"y": RESBALNS['value'],"mode": "lines","name": 'Balance', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Reserve Balances Maintained with Fed',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   

html.Div([
dcc.Graph(
        id='USLLRTL',
        figure={
            'data': [
                     { "x": USLLRTL['date'],"y": USLLRTL['value'],"mode": "lines","name": 'Ratio', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Loan Loss Reserve to Total Loans for all U.S. Banks',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="threehalf columns"),   






] , className="row", style={'textAlign': 'center', "width": "100%", "display": "flex", "align-items": "center", "justify-content": "center" }),



####BANK ENCONOMY ROW 3






html.Div([



html.Div([
dcc.Graph(
        id='CASACBW027SBOG',
        figure={
            'data': [
                     { "x": CASACBW027SBOG['date'],"y": CASACBW027SBOG['value'],"mode": "lines","name": 'Balance', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Cash Assets, All Commercial Banks',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="twelve columns"),   

html.Div([
dcc.Graph(
        id='WDDSL',
        figure={
            'data': [
                     { "x": WDDSL['date'],"y": WDDSL['value'],"mode": "lines","name": 'Balance', 'line': {'color': '#1CA8DD'}},    
                    ],
            'layout': {
                'title': 'Demand Deposits: Total ',
                "paper_bgcolor": "rgb(46, 54, 65)",
                "plot_bgcolor": "rgb(46, 54, 65)",
                'font': {'color': "rgb(255,255,255)"},
                'tickangle': '90',

                    }
               }
       
          )
          ], className="twelve columns"),   






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

[x] S&P 500 (SP500)
[x] Banking Sector 
[NA] Wilshire 5000 Total Market Full Cap Index (WILL5000INDFC)
[X] Unemployment Rate  (UNRATE)
[X] Velocity of M2 Money Stock (M2V)
[X] Real Gross Domestic Product (GDPC1)



###Bank Economy Watch

Net Interest Margin for all U.S. Banks (USNIM)
Net Income for Commercial Banks in United States (USNINC)
Bank Z-Score for United States (DDSI01USA645NWDB)


Delinquency Rate on Consumer Loans, All Commercial Banks (DRCLACBS)
Total Reserve Balances Maintained with Federal Reserve Banks (RESBALNS)
Loan Loss Reserve to Total Loans for all U.S. Banks (USLLRTL)

Cash Assets, All Commercial Banks (CASACBW027SBOG)
Demand Deposits: Total (WDDSL)	



##BANK Factors
Effective Federal Funds Rate (FEDFUNDS) 
Required Reserves of Depository Institutions (REQRESNS)
Excess Reserves of Depository Institutions  (EXCSRESNW)
Bank Prime Loan Rate (MPRIME)

"""



# %%


