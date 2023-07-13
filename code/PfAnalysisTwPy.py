"""
## Portfolio Analysis Using Python

ref: https://tradewithpython.com/portfolio-analysis-using-python
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fmgr
import seaborn as sb
import yfinance as yf
from datetime import date


plt.style.use('fivethirtyeight') #setting matplotlib style

# 'ANET', 'DHI', 'CB', 'DXCM', 'EOG', 'ETSY', 'FDX', 'HLT', 'ILMN', 'ENPH', 'FDX', 'ABBV', 'UNH', 'MU', 'INTC',

def PfAnalysisTwPy():
    stocksymbols = ['LEN', 'CSCO', 'DOW', 'SB', 'PEP', 'CRM', 'TTWO']
    startdate = date(2019,10,14)
    end_date = date.today()
    # print(end_date)
    # print(f"You have {len(stocksymbols)} assets in your porfolio" )

    df = yf.download(stocksymbols,start=startdate, end=(end_date))['Adj Close']

# ***** "Portfolio Close Price History" *****
    fig, ax = plt.subplots(figsize=(15,8))
    for i in df.columns.values :
        ax.plot(df[i], label = i, linewidth = 2)
    ax.set_title("Portfolio Close Price History")
    ax.set_xlabel('Date', fontsize=18)
    ax.set_ylabel('Close Price INR (₨)' , fontsize=18)
    ax.legend(df.columns.values , loc = 'upper left')

    st.pyplot(fig)

    # plt.show()
    # # plt.show(fig)
    # # st.line_chart(fig)

# ***** "Correlation Matrix" *****
    correlation_matrix = df.corr(method='pearson')
    correlation_matrix
    fig1 = plt.figure()
    plt.title('Correlation Matrix')
    sb.heatmap(correlation_matrix,xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns,
    cmap='YlGnBu', annot=True, linewidth=0.5)
    # fmgr.FontProperties(size=8.0)

    # print('Correlation between Stocks in your portfolio')
    st.write('Correlation between Stocks in your portfolio')
    # # plt.show(fig1)
    # Plot!
    # st.plotly_chart(fig1, use_container_width=True)
    st.pyplot(fig1)

# ***** "Daily Simple Returns" *****
    print('Average Daily returns(%) of stocks in your portfolio')
    daily_simple_return = df.pct_change(1)
    daily_simple_return.dropna(inplace=True)
    daily_simple_return
    print('Daily simple returns')
    fig, ax = plt.subplots(figsize=(15,8))
    for i in daily_simple_return.columns.values:
        ax.plot(daily_simple_return[i], lw=1, label=i)
    ax.legend( loc = 'upper right' , fontsize =10)
    ax.set_title('Volatility in Daily simple returns ')
    ax.set_xlabel('Date')
    ax.set_ylabel('Daily simple returns')
    st.pyplot(fig)
    # plt.show()
    # plt.show(fig)
    # st.plotly_chart(fig, use_container_width=True)

# ***** "Average Daily returns(%) of stocks in your portfolio" *****
    Avg_daily = daily_simple_return.mean()
    print(Avg_daily*100)
    # daily_simple_return.plot(kind = "box",figsize = (20,10), title = "Risk Box Plot")
    # plt.plot(kind = "box", figsize = (20,10), title = "Risk Box Plot")
    # plt.show()
    
    print('Annualized Standard Deviation (Volatality(%), 252 trading days) of individual stocks in your portfolio on the basis of daily simple returns.')
    print(daily_simple_return.std() * np.sqrt(252) * 100)
    Avg_daily / (daily_simple_return.std() * np.sqrt(252)) *100
    daily_cummulative_simple_return =(daily_simple_return+1).cumprod()
    daily_cummulative_simple_return
    #visualize the daily cummulative simple return
    print('Cummulative Returns')
    fig, ax = plt.subplots(figsize=(18,8))
    for i in daily_cummulative_simple_return.columns.values :
        ax.plot(daily_cummulative_simple_return[i], lw =2 ,label = i)

    ax.legend( loc = 'upper left' , fontsize =10)
    ax.set_title('Daily Cummulative Simple returns/growth of investment')
    ax.set_xlabel('Date')
    ax.set_ylabel('Growth of ₨ 1 investment')
    # plt.show()
    st.pyplot(fig)

