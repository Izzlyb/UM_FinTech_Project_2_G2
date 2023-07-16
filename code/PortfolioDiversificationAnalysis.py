"""_summary_
Optimize Your Stock Portfolio With Python

NeuralNine          Aug 14, 2021            Python For Finance

Today we build a simple tool for analyzing the diversification of stock portfolios.

DISCLAIMER: This is not investing advice. I am not a professional 
who is qualified in giving any financial advice. This is a video 
purely about programming using financial data.


ref: https://youtu.be/gWPYdvsKPlM?list=PL7yh-TELLS1HJzPsb6Xjdse2zbyQ-ocDH

"""

import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from GetStockData import *
import pickle

plt.style.use("dark_background")

run_all_code = True

def PortfolioDiversificationAnalysis(tickers):

    countries = []
    market_caps = []
    industries = []
    fiftyTwoWeekLow = []
    fiftyTwoWeekHigh = []

    values = []
    etf_values = []
    crypto_values = []
    industry_dist = {}
    country_dist = {}

    stock_list = ['AAPL', 'PANW', 'ABBV', 'KO', 'MSFT', 'NVDA', 'JPM', 'WM', 'CVX', 'AMZN' ]
    amounts = [80, 35, 80, 70, 32, 40, 60, 37, 62, 45, 100, 33]
    cash = 40_000

    market_cap_dist = {'small' : 0.0, 'mid' : 0.0, 'large' : 0.0, 'huge' : 0.0}
    
    if len(tickers) == 0:
        stocks = stock_list
    else:
        st.session_state.work_portfolio_df = get_portfolio_assets(st.session_state.work_portfolio_nm)
        stocks = get_portfolio_assets_symbols(st.session_state.work_portfolio_df)
        amounts = get_portfolio_assets_quantities(st.session_state.work_portfolio_df)

    # st.write(f"We will work the following stocks: [{stocks}]")


    # st.write("There seems to be a problem with the yfinance API to get information about a stock.")
    for i in range(0, len(stocks)):
        values.append(float(yf.Ticker(stocks[i]).info['previousClose'])*amounts[i])
        market_caps.append(yf.Ticker(stocks[i]).info['marketCap'])
        indtr = yf.Ticker(stocks[i]).info['industry']
        industries.append(indtr)


    etfs = ['SCHX', 'IVV', 'DGRO', 'VIG', 'FTEC', 'NOBL']
    etf_amounts = [ 100, 60, 48, 33, 22, 40 ]
    for i in range(0, len(etfs)):
        etf_values.append(yf.Ticker(etfs[i]).info['previousClose'] * etf_amounts[i])
        # print(etfs[i])


    cryptos = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'DOGE-USD']
    crypto_amounts = [0.84, 2.33, 600, 800]
    for i in range(0, len(cryptos)):
        crypto_values.append(yf.Ticker(cryptos[i]).info['previousClose'] * crypto_amounts[i])


    # st.write(f"the industries present are: [{industries}]")
    for i in range(len(industries)):
        if industries[i] not in industry_dist.keys():
            industry_dist[industries[i]] = 0
        industry_dist[industries[i]] += values[i]


    for i in range(len(countries)):
        if countries[i] not in country_dist.keys():
            country_dist[countries[i]] = 0
        country_dist[countries[i]] += values[i]


    for i in range(len(market_caps)):
        if market_caps[i] < 2_000_000_000:
            market_cap_dist['small'] += values[i]
        elif market_caps[i] < 10_000_000_000:
            market_cap_dist['mid'] += values[i]
        elif market_caps[i] < 1_000_000_000_000:
            market_cap_dist['large'] += values[i]
        else:
            market_cap_dist['huge'] += values[i]

    general_dist = {
            "Stocks" : sum(values), 
            "ETF" : sum(etf_values),
            "Crypto" : sum(crypto_values),
            "Cash" : cash
        }

    # if cryptos == "" or etfs == "" or stocks == "":
    #     st.write("There is an error with the yfinance Ticker() function.")
    # else:
    #     with open('pickle/general.pickle', 'wb') as f:
    #         pickle.dump(general_dist, f)
            
    #     with open('pickle/sector.pickle', 'wb') as f:
    #         pickle.dump(industry_dist, f)
            
    #     with open('pickle/country.pickle', 'wb') as f:
    #         pickle.dump(country_dist, f)
            
    #     with open('pickle/market_cap.pickle', 'wb') as f:
    #         pickle.dump(market_cap_dist, f)

        # --------------------------------------------
        # read the pickle files safed in a previous run:

        # with open("pickle/general.pickle", 'rb') as f:
        #     general_dist = pickle.load()

        # with open("pickle/industry.pickle", 'rb') as f:
        #     sector_dist = pickle.load()

        # with open("pickle/country.pickle", 'rb') as f:
        #     country_dist = pickle.load()

        # with open("pickle/market_cap.pickle", 'rb') as f:
        #     market_cap_dist = pickle.load()

    if cryptos == "" or etfs == "" or stocks == "":
        st.write("There is an error with the yfinance Ticker() function.")
    else:
        # fig, axs = plt.subplots(2,2)
        fig, axs = plt.subplots(2, 2)
        # plt.figure(figsize=(1200,1200))
        plt.rcParams['figure.figsize'] = [16, 16]
        plt.figure().set_figheight(18)

        fig.suptitle("Portfolio Diversification Analysis", fontsize=9)

        axs[0,0].pie(general_dist.values(), labels=general_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[0,0].set_title("General Distribution")

        axs[0,1].pie(industry_dist.values(), labels=industry_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[0,1].set_title("Stocks by Industry")

        # axs[1,0].pie(country_dist.values(), labels=country_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        # axs[1,0].set_title("Stocks by Country")
        axs[1,0].pie(values, labels=stocks, autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[1,0].set_title("Stocks by Country")


        axs[1,1].pie(market_cap_dist.values(), labels=market_cap_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[1,1].set_title("Stocks by Market Cap.")

        # plt.show()
        
        st.pyplot(fig)




    
 
    # if run_all_code:
    #     for i in range(0, len(stocks)):
    #         # print(yf.Ticker(stocks[i]).get_info()['marketCap'])
    #         sectors.append(yf.Ticker(stocks[i]).get_info()['sector'])
    #         countries.append(yf.Ticker(stocks[i]).get_info()['country'])
    #         market_caps.append(yf.Ticker(stocks[i]).get_info()['marketCap'])
    #         industries.append(yf.Ticker(stocks[i]).get_info()['industry'])
    #         # fiftyTwoWeekLow.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekLow'])
    #         # fiftyTwoWeekHigh.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekHigh'])

    #     for i in range(0, len(stocks)):
    #         values.append(yf.Ticker(stocks[i]).get_info()['previousClose'] * amounts[i])
    #         # print(yf.Ticker(stocks[i]).get_info()['marketCap'])
    #         # sectors.append(yf.Ticker(stocks[i]).get_info()['sector'])
    #         # countries.append(yf.Ticker(stocks[i]).get_info()['country'])
    #         # market_caps.append(yf.Ticker(stocks[i]).get_info()['marketCap'])
    #         # industry.append(yf.Ticker(stocks[i]).get_info()['industry'])
    #         # fiftyTwoWeekLow.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekLow'])
    #         # fiftyTwoWeekHigh.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekHigh'])
