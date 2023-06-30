
# Project 2 of the UM FinTech Bootcamp

## Members:
    Samuel              Activity 4
    Eric                Activity 2
    Ricky               Activity 3
    Isidro              Activity 1

# Proposal:

# Develop an application to perform finance management : Graham

It will implement Algorithmic trading, machine learning and visualization 
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
    whose values vary from $15.00 to $400.00
    We'll use commodities: Gold, Silver and Copper
    We'll use the ETFs that represent the market sectors in the S&P500 as part of the
    portfolio.


## Work distribution

1. (IJL) Create a machine learning model that can predict the price of an equity
in the very short term. And provide a set of stocks for the user to analyze further to 
make the final decision
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
        
    We wil assume that we have a portfolio with a mix of stocks.. and the investment has been made 
    in the last 4 years.



4. (Samuel) Create a bot to use the selected ML model to do automated trading on 
    a paper account.


For project 3:
    This is a POC.Proof of Concept 
    Work on an experiment

    Have a user tell a story about what they want.


Email:

EH      erichines22insurance@gmail.com,
        ericjhines2223@hotmail.com
IJL     ijleon@hotmail.com
RM      ricky.mershad@gmail.com
Sam     samsanto96@gmail.com


** Meet on Saturday, 01July2023 7:00 pm

We are put our data 
