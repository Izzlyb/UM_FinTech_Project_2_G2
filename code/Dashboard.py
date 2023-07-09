
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


st.title('Welcome to Grahmy, Your Financial App')

st.write("""
         We will help you with your Portfolio Management and Analysis! 👋
         
         Please select an action from the sidebar.
         
         Thanks for using our application
""")


# Load some example data.
# DATA_URL = \
#     "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
# data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
# # Select some rows using st.multiselect. This will break down when you have >1000 rows.
# st.write('### Full Dataset', data)
# selected_indices = st.multiselect('Select rows:', data.index)
# selected_rows = data.loc[selected_indices]
# st.write('### Selected Rows', selected_rows)

