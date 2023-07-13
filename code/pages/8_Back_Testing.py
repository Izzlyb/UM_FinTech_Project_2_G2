import streamlit as st
import pandas as pd
import time
import yfinance as yf
from pathlib import Path
from assets import stock_portfolio, portfolios, PortfolioAssets

st.write("""
         #In this page you can backtest a trading strategy. 📝
         
         You can select a trading strategy and a portfolio or
         watchlist to analyze your strategy
         
         """)

# initialize all data.
sel_portf_name = ""


