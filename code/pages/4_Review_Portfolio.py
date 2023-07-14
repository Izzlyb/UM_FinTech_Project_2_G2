import streamlit as st
import pandas as pd
import numpy as np
import time
import yfinance as yf
from pathlib import Path
from assets import stock_portfolio, portfolios, PortfolioAssets
from PfAnalysisTwPy import *


import riskfolio as rp
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


st.write("""
         # You are in the Analyze Portfolio Page 📊
         
         From the selection list below, you can select one \n
         of your portfolios or watchlist to analyze.
         
         """)



################################################################
def portf_risk_analysis():
    
    start_date = "2022-01-01"
    end_date = "2022-12-30"

    assets = ["BTC-USD", "ETH-USD", "XMR-USD", "LINK-USD", "DOGE-USD", "USDT-USD", "USDC-USD", "ADA-USD", "SOL-USD"]

    data = yf.download(assets, start_date, end_date)

    # returns = data['Adj Close'].pct_change()
    returns = data['Close'].pct_change()
    
    returns.replace([np.inf, -np.inf], np.nan).dropna(axis=1) # You can replace inf and -inf with NaN, and then select non-null rows.
    returns.dropna(inplace=True)

    # variables that are needed by library

    method_mu = 'hist'
    method_cov = 'hist'
    hist=True
    model = 'Classic'
    rm = 'MV'
    obj = 'Sharpe'
    rf = 0
    l = 0

    # portfolio initial calculation
    portf = rp.Portfolio(returns = returns)
    portf.assets_stats(method_mu=method_mu, method_cov = method_cov)
    w = portf.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)
    w

    ax = rp.plot_pie(w=w, title="Optimum Portfolio", others=0.05, cmap='tab20')
    ax
#----------------------------------------------------------------


################################################################
def portfolio_components():

    assets = st.text_input("Provide your assets (comma-separated)", "AAPL, MSFT, CAT")

    start = st.date_input("Pick a start date for your analysis", value = pd.to_datetime('2022-06-01'))
    start = st.date_input("Pick a start date for your analysis", value = pd.to_datetime('2023-04-30'))

    # portfolio downloading and returns:
    data = yf.download(assets, start = start)['Adj Close']
    return_df = data.pct_change()
    cumul_return = (return_df + 1).cumprod() - 1

    pf_cumul_return = cumul_return.mean(axis=1)   # this takes the mean across all stocks of portfolio.

    # benchmark downloading and returns:
    benchmark = yf.download("^GSPC", start=start)['Adj Close']
    bench_return = benchmark.pct_change()
    bench_dev = (bench_return + 1).cumprod() -1
    # bench_dev

    st.subheader("Portfolio vs Index Development")

    #.........................................
    # data
    # wt = calculate_weights(data)
    # wt
    #.........................................

    # portfolio risk calculation:
    W = (np.ones(len(return_df.cov()))/len(return_df.cov()))

    pf_var = W.dot(return_df.cov()).dot(W)
    pf_std_dev = W.dot(return_df.cov()).dot(W) ** (1/2)

    tog = pd.concat([bench_dev, pf_cumul_return], axis=1)
    tog.columns = ['S&P 500', 'Portfolio Performance']

    st.line_chart(data = tog)

    st.subheader("Portfolio Risk:")
    pf_std_dev

    st.subheader("Benchmark Risk:")
    bench_risk = bench_return.std()
    bench_risk

    st.subheader("Portfolio Composition:")
    fig, ax = plt.subplots(facecolor="#121212")
    ax.pie(W, labels=data.columns, autopct="%1.1f%%", textprops={'color':'white'})

    st.pyplot(fig)
#----------------------------------------------------------------

################################
def calculate_weights(data):
    returns = data.pct_change()

    returns.replace([np.inf, -np.inf], np.nan).dropna(axis=1) # You can replace inf and -inf with NaN, and then select non-null rows.
    returns.dropna(inplace=True)

    # variables that are needed by library

    method_mu = 'hist'
    method_cov = 'hist'
    hist=True
    model = 'Classic'
    rm = 'MV'
    obj = 'Sharpe'
    rf = 0
    l = 0

    # portfolio initial calculation
    portf = rp.Portfolio(returns = returns)
    portf.assets_stats(method_mu=method_mu, method_cov = method_cov)
    w = portf.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

    return w
#----------------------------------------------------------------


################################################################
def chart_display():
    df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

    my_table = st.table(df1)

    df2 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

    my_table.add_rows(df2)
    # Now the table shown in the Streamlit app contains the data for
    # df1 followed by the data for df2.
    # Assuming df1 and df2 from the example above still exist...
    my_chart = st.line_chart(df1)
    my_chart.add_rows(df2)
    # Now the chart shown in the Streamlit app contains the data for
    # df1 followed by the data for df2.

    my_chart = st.vega_lite_chart({
        'mark': 'line',
        'encoding': {'x': 'a', 'y': 'b'},
        'datasets': {
        'some_fancy_name': df1,  # <-- named dataset
        },
        'data': {'name': 'some_fancy_name'},
    })

    my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
#---------------------------------------------------------------


PfAnalysisTwPy()
# chart_display()
