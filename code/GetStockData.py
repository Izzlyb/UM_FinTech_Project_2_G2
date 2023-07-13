import streamlit as st
import pandas as pd
import yfinance as yf
from pathlib import Path
import time
from datetime import date
from PortfolioAsset import *
import os

TEST_FLAG = False

list_header = ('Symbol', 'Open', 'High', 'Low', 'Close', '52w-Low', '52w-High', 'Sector', 'Industry', 'Beta')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def select_file_name(ix_seltd):
    if ix_seltd == 'DJI':
        index_csv = DJI_CSV
    elif ix_seltd == 'SP500':
        index_csv = SP500_CSV
    elif ix_seltd == 'NASDAQ':
        index_csv = NASDAQ_CSV
    elif ix_seltd == 'RUS2000':
        index_csv = RUS2000_CSV

    st.write(index_csv)
    
    return index_csv

#-----------------------------------------------------------


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# get stock to buy or sell and create a single stock df to add to the portfolio dataframe:
def mk_stock_tx_item(tkr, prc, qty):
    pass

    # data = { "Ticker" : (dji_tickers['Symbol'].sort_values()).values,
    #         "Open" : (df_dji['Open'].values)[0],
    #         "High" : (df_dji['High'].values)[0],
    #         "Low" : (df_dji['Low'].values)[0],
    #         "Close" : (df_dji['Close'].values)[0],
    #         "Adj Close" : (df_dji['Adj Close'].values)[0],
    #         "Volume" : (df_dji['Volume'].values)[0]
    #         }

    # # dji = tkrs_df.copy()
    # data_df = pd.DataFrame(data = {
    #     }, columns
#-----------------------------------------------------------



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_portfolio_assets(pf_name):
    
    pf_df = pd.read_csv(Path(f"data/pf__{pf_name}.csv"))

    return pf_df
#-----------------------------------------------------------




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_watchlist_df(wl_name):
    
    df = pd.read_csv(Path(f"data/wl__{wl_name}.csv"))

    return df
#-----------------------------------------------------------





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_portfolio_names():
    # folder path
    dir_path = r'data//'
    
    # list to store files
    fl_lst = []
    fl_lst.append("Make Selection from List")
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if path.find('wl__') < 0:
            if os.path.isfile(os.path.join(dir_path, path)):
                path = path.replace("pf__", "" )
                path = path.replace(".csv", "" )
                fl_lst.append(path)

    return fl_lst
#----------------------------------------------------------------




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_watchlist_names():
    # folder path
    dir_path = r'data//'
    
    # list to store files
    fl_lst = []
    fl_lst.append("Make Selection from List")
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if path.find('pf__') < 0:
            if os.path.isfile(os.path.join(dir_path, path)):
                path = path.replace("wl__", "" )
                path = path.replace(".csv", "" )
                fl_lst.append(path)

    return fl_lst
#----------------------------------------------------------------




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_idx_stocks_list(index_csv):
    ticker_names = pd.read_csv(Path(f"Resources/{index_csv}"))
    tickers = list(ticker_names.loc[:]['Symbol'])

    return tickers
#-----------------------------------------------------------


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def save_watchlist():
    
    wl_name = st.session_state.stock_list_name
    csv_file = Path(f"data/wl__{wl_name}.csv")
    st.session_state.watchlist_df.to_csv(csv_file)
    st.write(f">{wl_name}< saved successfully.")

    return st.session_state.watchlist_df
#-----------------------------------------------------------



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def add_ticker_to_list(stk, close, qty):

    data = {'Ticker':[stk],
            'OriginalPrice': [close],
            'Quantity': [qty],
            'OriginalDate': [date.today()],
            'ActualPrice' : [close],
            'TransType' : ['BTO'] 
    }

    pf_stk = pd.DataFrame(data)
    st.write("sell stock and add to portfolio:")
    st.session_state.watchlist_df = pd.concat([st.session_state.watchlist_df, pf_stk])


#-----------------------------------------------------------




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def load_stock_prices(ticker="", start="", end="", index=""):
    # https://pypi.org/project/yfinance/
    if ticker != "" and index == "": 
        tickers = ticker
    else:
        if index == 'DJI':
            index_csv = DJI_CSV
        elif index == 'SP500':
            index_csv = SP500_CSV
        elif index == 'NASDAQ':
            index_csv = NASDAQ_CSV
        elif index == 'RUS2000':
            index_csv = RUS2000_CSV
        else:
            index_csv = "DowJones.csv"

        tickers = get_idx_stocks_list(index_csv)

    if start != "":
        d1 = start
        d2 = end
        prd = "1d"
    else:
        d1 = ""
        d2 = ""
        prd = "ytd"
    
    data = yf.download(
        # or prd.get_data_yahoo(...
        # tickers list or string 
        tickers,

        # use "period" instead of start/end
        # valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        # (optional, default is '1mo'
        start = d1,
        end = d2,

        # use "period" instead of start/end
        # valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        # (optional, default is '1mo'
        period = prd,
        
        # Fetch data by interval (including intraday if period is < 60 days)
        # valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        # (Optional, default is '1d'
        interval = "1d",

        # group by ticker (to access via data['spy'])
        # (optional, default is 'column'
        group_by = 'ticker', 

        # adjust all OHLC automatically
        # (optional, default is false
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False
        prepost = True,

        # use threads for mass downloading? (True/False/Trigger)
        # (optional, default is None)
        threads = True,

        # proxy URL scheme use when downloading?
        # (optional, default is None)
        proxy = None
    )
    
    return data

# this function takes a stock ticker and a single day stock price dataframe
# and creates a data frame to concatenate with others from a single list

def reshape_sngl_stock_df(tkr, tkr_df):
    sbl = tkr
    opn = tkr_df['Open']
    hgh = tkr_df['High']
    lw = tkr_df['Low']        
    close = tkr_df['Close']

    # dictionary of lists 
    dict = {'Symbol': sbl, 'Open': opn, 'High': hgh, 'Low': lw, 'Close': close}

    for idx in tkr_df:
        df = pd.DataFrame( dict,
                          columns = (list_header[0:5])
                          )
    return df

# this function will take a list of stocks, 
#    retrieve single stock historical price data
#    and loop through the list of stocks and concatenate them all:

def concat_multi_stocks(idx_stk_lst):
    d1 = "2023-7-3"
    d2 = "2023-7-4"

    tkrs = idx_stk_lst
    tkrs_df = load_stock_prices(ticker=tkrs, start="2023-5-1", end="2023-5-2")
    tkrs_df
    
    idx = idx_stk_lst[0]
    idx_stk_df = tkrs_df[idx_stk_lst[0]]
    sk_df = reshape_sngl_stock_df(idx, idx_stk_df)
    
    for i in range(1, (len(idx_stk_lst)-1)):
        idx = idx_stk_lst[i+1]
        idx_stk_df = tkrs_df[idx]
        df1 = reshape_sngl_stock_df(idx, idx_stk_df)
        sk_df = pd.concat([sk_df, df1])

    sk_df.reset_index(drop=True, inplace=True)
        
    return sk_df


################################################################
def get_stock_data(ticker, date1="", date2=""):
    df = yf.download(ticker, start=date1, end=date2)

    return df
# ---------------------------------------------------------------    



################################################################
def create_portfolio_2(data):
    # Select some rows using st.multiselect. This will break down when you have >1000 rows.
    # data is a dataframe.
    st.write('### Full Dataset', data)
    selected_indices = st.multiselect('Select rows:', data.index)
    selected_rows = data.loc[selected_indices]
    st.write('### Selected Rows for your new portfolio', selected_rows)
    
    return selected_rows
# ---------------------------------------------------------------    


#################################################################
@st.cache_data
def get_stock_data(ticker, date1="", date2=""):
    
    data = yf.download(
        tickers = ticker,
        start=date1,
        end=date2,
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

    stock_df = data

    return data
#----------------------------------------------------------------


#################################################################
@st.cache_data
def get_index_stocks_data(index):
    sec_now = time.time()
    sec_ytrdy = time.time()-(24*60*60)
    now = time.localtime(sec_now)
    yesterday = time.localtime(sec_ytrdy)
    # print(time.strftime("%y/%m/%d %H:%M", now))
    # st.write(f">the start time is: {start_date}<, >the end time is: {end_date}<")
    # dji_tickers = pd.read_csv(Path("Resources/DowJones.csv"))

    if index == 'DJI':
        index_csv = DJI_CSV
    elif index == 'SP500':
        index_csv = SP500_CSV
    elif index == 'NASDAQ':
        index_csv = NASDAQ_CSV
    elif index == 'RUS2000':
        index_csv = RUS2000_CSV

    dji_tickers = pd.read_csv(Path(f"Resources/{index_csv}"))
    tickers_lst = list(dji_tickers.loc[:]['Symbol'])

    if TEST_FLAG == True:
        tkrs_df = pd.read_csv(Path("Resources/sp500_cont_prices.csv"))
    else:
        tkrs_df = concat_multi_stocks(tickers_lst)

    # data = { "Ticker" : (dji_tickers['Symbol'].sort_values()).values,
    #         "Open" : (df_dji['Open'].values)[0],
    #         "High" : (df_dji['High'].values)[0],
    #         "Low" : (df_dji['Low'].values)[0],
    #         "Close" : (df_dji['Close'].values)[0],
    #         "Adj Close" : (df_dji['Adj Close'].values)[0],
    #         "Volume" : (df_dji['Volume'].values)[0]
    #         }

    # # dji = tkrs_df.copy()
    # data_df = pd.DataFrame(data = {
    #     }, columns

    return tkrs_df
#----------------------------------------------------------------



