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
import pickle
import mplfinance

plt.style.use("dark_background")

fiftyTwoWeekLow = []
fiftyTwoWeekHigh = []

run_all_code = True

def PortfolioDiversificationAnalysis(tickers):

    sectors = []
    countries = []
    market_caps = []
    industry = []
    values = []
    etf_values = []
    crypto_values = []
    sector_dist = {}
    country_dist = {}

    stocks = ['AAPL', 'PANW', 'ABBV', 'KO', 'MSFT', 'NVDA', 'JPM', 'DIS', 'WM', 'CVX', 'AMZN' ]
    amounts = [20, 15, 80, 70, 32, 40, 60, 7, 14, 45, 100, 33]
    cash = 100_000

    market_cap_dist = {'small' : 0.0, 'mid' : 0.0, 'large' : 0.0, 'huge' : 0.0}
    
    if tickers == "":
        stocks = stocks
    else:
        stocks = tickers

    st.write("There seems to be a problem with the yfinance API to get information about a stock.")
    stocks = ""

    if run_all_code:
        for i in range(0, len(stocks)):
            # print(yf.Ticker(stocks[i]).get_info()['marketCap'])
            sectors.append(yf.Ticker(stocks[i]).get_info()['sector'])
            countries.append(yf.Ticker(stocks[i]).get_info()['country'])
            market_caps.append(yf.Ticker(stocks[i]).get_info()['marketCap'])
            industry.append(yf.Ticker(stocks[i]).get_info()['industry'])
            # fiftyTwoWeekLow.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekLow'])
            # fiftyTwoWeekHigh.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekHigh'])

        for i in range(0, len(stocks)):
            values.append(yf.Ticker(stocks[i]).get_info()['previousClose'] * amounts[i])
            # print(yf.Ticker(stocks[i]).get_info()['marketCap'])
            # sectors.append(yf.Ticker(stocks[i]).get_info()['sector'])
            # countries.append(yf.Ticker(stocks[i]).get_info()['country'])
            # market_caps.append(yf.Ticker(stocks[i]).get_info()['marketCap'])
            # industry.append(yf.Ticker(stocks[i]).get_info()['industry'])
            # fiftyTwoWeekLow.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekLow'])
            # fiftyTwoWeekHigh.append(yf.Ticker(stocks[i]).get_info()['fiftyTwoWeekHigh'])

        etfs = ['SCHX', 'IVV', 'DGRO', 'VIG', 'FTEC', 'NOBL']
        etf_amounts = [ 10, 20, 28, 16, 12, 7 ]

        ### ERROR
        etfs = ""
        for i in range(0, len(etfs)):
            etf_values.append(yf.Ticker(etfs[i]).get_info()['previousClose'] * etf_amounts[i])

        cryptos = ['BTC-USD', 'ADA-USD', 'DOGE-USD']
        crypto_amounts = [.64, 1.33, 200, 500]

        ### ERROR 
        cryptos = ""
        for i in range(0, len(cryptos)):
            crypto_values.append(yf.Ticker(cryptos[i]).get_info()['previousClose'])

        ### ERROR
        sectors = ""
        for i in range(len(sectors)):
            if sectors[i] not in sector_dist.keys():
                sector_dist[sectors[i]] = 0
                
            sector_dist[sectors[i]] += values[i]

        #### ERROR
        countries = ""        
        for i in range(len(countries)):
            if countries[i] not in country_dist.keys():
                country_dist[countries[i]] = 0
                
            country_dist[countries[i]] += values[i]

        ### ERROR
        market_cap = ""
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

        if cryptos == "" or etfs == "" or stocks == "":
            st.write("There is an error with the yfinance Ticker() function.")
        else:
            with open('general.pickle', 'wb') as f:
                pickle.dump(general_dist, f)
                
            with open('sector.pickle', 'wb') as f:
                pickle.dump(sector_dist, f)
                
            with open('country.pickle', 'wb') as f:
                pickle.dump(country_dist, f)
                
            with open('market_cap.pickle', 'wb') as f:
                pickle.dump(market_cap_dist, f)

    else:
        # --------------------------------------------
        # read the pickle files safed in a previous run:
        
        with open("general.pickle", 'rb') as f:
            general_dist = pickle.load()

        with open("industry.pickle", 'rb') as f:
            sector_dist = pickle.load()

        with open("country.pickle", 'rb') as f:
            country_dist = pickle.load()

        with open("market_cap.pickle", 'rb') as f:
            market_cap_dist = pickle.load()

    if cryptos == "" or etfs == "" or stocks == "":
        st.write("There is an error with the yfinance Ticker() function.")
    else:
        fig, axs = plt.subplots(2,2)
        fig.suptitle("Portfolio Diversification Analysis", fontsize=9)

        axs[0,0].pie(general_dist.values(), labels=general_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[0,0].set_title("General Distribution")

        axs[0,1].pie(sector_dist.values(), labels=sector_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[0,1].set_title("Stocks by Industry")

        axs[1,0].pie(country_dist.values(), labels=country_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[1,0].set_title("Stocks by Country")

        axs[1,1].pie(market_cap_dist.values(), labels=market_cap_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
        axs[1,1].set_title("Stocks by Market Cap.")

        # plt.show()
        
        st.pyplot(fig)

