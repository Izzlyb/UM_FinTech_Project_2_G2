import streamlit as st
import pandas as pd
import yfinance as yf
from pathlib import Path


DJI_CSV = "DowJones.csv"
SP500_CSV = "SP500_sub.csv"
NASDAQ_CSV = "Nasdaq100"
RUS2000_CSV = "Russell2000.csv"
list_header = ('Symbol', 'Open', 'High', 'Low', 'Close', '52w-Low', '52w-High', 'Sector', 'Industry', 'Beta')



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

        ticker_names = pd.read_csv(Path(f"Resources/{index_csv}"))
        tickers = list(ticker_names.loc[:]['Symbol'])
    
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
        print(i, idx)
        idx_stk_df = tkrs_df[idx]
        df1 = reshape_sngl_stock_df(idx, idx_stk_df)
        sk_df = pd.concat([sk_df, df1])

    sk_df.reset_index(drop=True, inplace=True)
        
    return sk_df


def get_stock_data(ticker, date1="", date2=""):
    df = yf.download(ticker, start=date1, end=date2)

    return df


