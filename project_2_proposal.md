# Project 2 of the UM FinTech Bootcamp

## Members:
    Samuel              Activity 4
    Eric                Activity 2
    Ricky               Activity 3
    Isidro              Activity 1

# Proposal:

# Develop an application to perform finance management : Graham

This app will implement Algorithmic trading, machine learning and visualization 
and portfolio management and evaluation.

We would be using the following libraries, these would be the 
dependencies of the project:

    - yfinance library to get data.                                             use to retrieve data from yfinance
    - alpaca-api to get data and perform trades on a papertrading account.      use for trades
    - use streamlit library for presentaion of results.
    - sqlite database library to store data that needs to be persistent
    - backtesting.py to perform backtesting of algorithms.
    - pandas-ta to get indicators and tend studies to create trading strategies
    - use RSI and stochastics indicator
    - use bollinger bands


## Setup of project:
A. We need to identify a set of stocks and ETF that and even cryptocurrencies that 
we want to work with so we use the same dataset.

B. Let's define what machine model we would be using for the project.

C. We will be work during the implementation phase with stocks from the S&P500 index
    whose values vary from $15.00 to $400.00. 
    (take note if this assumption has any impact on performance of the model. It should NOT.)
    We'll use commodities: Gold, Silver and Copper
    We'll use the ETFs that represent the market sectors in the S&P500 as part of the
    portfolio.

We have definitions of portfolios, stocks and ETFs that have aggressive or defensive behavior.
meaning, the aggressive stocks have more volatility and can have more dramatic swings.
The defensive stocks and ETFs have less volatility and would react less dramatic.

These definitions are in the files: 
        PortfolioAsset.py
        assets.py


## Work distribution

1. (IJL) Create a machine learning model that can predict the price of an equity
for the very short term. 
The application could provide a set of stocks for the user to analyze further to 
make the final decision on whether to invest or not in the recommendations. The user 
has to make the final decision as to what equity to trade.
The recommendation would be a set of stocks to buy or to sell from the portfolio 
of the owned equities.

This set of stocks would be selected according to a risk profile pre-selected by the user.
Also the stocks to be analyzed would be taken from a watchlist provided by the user.

    I.- Package the model to be used by other people
    II.- Test the model with stocks, etf and commodities
    III.- Plot the results
    IV.- Use Stremlit to present the results
    V. Create risk profiles

    Notes: Machine learning model to recommend stocks to buy or sell.
        Can you select analysis of market down-turns or up-turns.
        Use data during bearish or bullish time of the market.



2. (Eric) Create a backtesting model to evaluate two or three selected strategies.
    - use RSI and stochastics indicator and Bollinger Band
    - use SMA indicators 5-, 50- and 100-day windows
    - Let's identify/add a third strategy



3. (Ricky) With the selected strategies, evaluate each one by creating a portfolio and 
    computing the projected annual return.
    Make a recommendation based on personal preference or risk profile of a portfolio.
        This portfolio would have several components depending on the preferences or risk profile:
            A. A combination of selected stocks from the S&P 500.
            B. ETFs
            C. Bonds

            Let's propose a portfolio with different mix of stocks ETF and commodities. 
            Determine the risk profile. 
        
    We will assume that we have a portfolio with a mix of stocks.. and the investment has been made 
    in the last 4 years.



4. (Samuel) Create a trading bot to use the selected ML model to do automated trading on 
    a paper account. Setup alarms if selected stocks are moving on either direction.
    We would use as strategy:
    1. EMA's : 13 - 30 -100
    2. Double Bollinger Bands
    3. MACD + Stochastics Band

    We can take advantage of the backsteting.py


For project 3:
    This is a POC.Proof of Concept
    Work on an experiment
    Have a user tell a story about what they want.

Email:

EH      erichines22insurance@gmail.com,     678-642-3254
        ericjhines2223@hotmail.com              
IJL     ijleon@hotmail.com                  305-720-1410     
RM      ricky.mershad@gmail.com             614-439-3012
Sam     samsanto96@gmail.com                904-855-5888


** Meet on Saturday, 01July2023 7:00 pm
