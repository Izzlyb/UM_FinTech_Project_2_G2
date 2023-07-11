import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/',
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

DJI_CSV = "DowJones.csv"
SP500_CSV = "SP500_sub.csv"
NASDAQ_CSV = "Nasdaq100"
RUS2000_CSV = "Russell2000.csv"
list_header = ('Symbol', 'Open', 'High', 'Low', 'Close', '52w-Low', '52w-High', 'Sector', 'Industry', 'Beta')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('Welcome to Grahmy, Your Financial App 📱')

st.write("""
         We will help you with your Portfolio Management and Analysis! 🏦
         
         Please select an action from the sidebar.
         
         Thanks for using our application
""")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
if "watchlist_nm" not in st.session_state:
    st.session_state.watchlist_nm = ""                  # string name of watchlist we are working:
if "new_portfolio_nm" not in st.session_state:
    st.session_state.new_portfolio_nm = ""              # string name of portfolio we are working:
if "watchlist_df" not in st.session_state:
    st.session_state.watchlist_df = pd.DataFrame()      # list of dataframes with watchlist
if "work_portfolio_df" not in st.session_state:
    st.session_state.work_portfolio_df = pd.DataFrame() # list of dataframes with portfolios
if "stks_to_newpf" not in st.session_state:
    st.session_state.stks_to_newpf = []                 # list of new stocks to add to portfolio dataframe
if "idx_stock_df" not in st.session_state:
    st.session_state.idx_stock_df = pd.DataFrame()      # temporary pass dataframe between form
if "stock_list_name" not in st.session_state:
    st.session_state.stock_list_name = ""               # list of wl/pf stocks to retreive
if "stock_list_action" not in st.session_state:
    st.session_state.stock_list_action = ""             # action to perform on watchlist or portfolio
if "ticker_qty" not in st.session_state:
    st.session_state.ticker_qty = 0                     # quantity of stocks to buy or sell or add to watchlist or portfolio
if "ticker_name" not in st.session_state:
    st.session_state.ticker_name = ""                   # ticker name to buy or sell or add to watchlist or portfolio

# Load some example data.
# DATA_URL = \
#     "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
# data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
# # Select some rows using st.multiselect. This will break down when you have >1000 rows.
# st.write('### Full Dataset', data)
# selected_indices = st.multiselect('Select rows:', data.index)
# selected_rows = data.loc[selected_indices]
# st.write('### Selected Rows', selected_rows)
# emoji reference: streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
# 🙌️ yeah emoji on Emoji Finder 😅 📱

