
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/',
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def get_stock_data(ticker, date1="", date2=""):
    df = yf.download(ticker, start=date1, end=date2)

    return df

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('Welcome to Grahmy, Your Financial App')

st.write("""
         We will help you with your Portfolio Management and Analysis! 👋
""")

st.sidebar.success("Make a Selection above.")

stock_df = get_stock_data("PANW", "2023-6-26", "2023-6-27")

stock_df

