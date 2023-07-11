"""_summary_

Equity Index Performance Top Notch Dashboard [MUST WATCH]

ref: https://youtu.be/e4wIdB1gkS4?list=RDCMUC87aeHqMrlR6ED0w2SVi5nw

Video showing streamlit basics:

 • Streamlit Interac...  https://www.youtube.com/watch?v=Km2KDo6tFpQ&t=0s

Video showing a streamlit Dashboard and using a SQL Database in the backend:

 • How to build a Cr...  https://www.youtube.com/watch?v=Ml6LUH2wxgc&t=0s


Returns:
    _type_: _description_
"""


import yfinance as yf
import pandas as pd
import streamlit as st
from pandas.tseries.offsets import DateOffset



def get_reg(df, n):
    previous_prices = df[:df.index[-1] - DateOffset(month=n)].tail(1).squeeze()
    recent_prices = df.loc[df.index[-1]]
    ret_df = recent_prices/previous_prices -1
    
    return previous_prices.name, ret_df, 



@st.cache_data
def get_data(tickers):
    df = yf.download(tickers, start='2022-10-1')['Adj Close']
    return df



def indexPerformance(tickers_list, n):
    # tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0].Symbol
    # tickers_list = tickers.to_list()
    stocks_df = get_data(tickers_list)

    st.markdown(
        """
        ## Index component performance: Listing of the 10 best performers in the selected Index.
        """)

    n = st.number_input("Please provide the performance horizon in months, 1-5:", min_value=1, max_value=12)

    stocks_df.index[-1] - DateOffset(months = 1)
    
    stocks_df[:stocks_df.index[-1] - DateOffset(month=1)].tail(1).squeeze()
    
    date, ret_df = get_reg(stocks_df, n)
    
    winners, losers = ret_df.nlargest(10), ret_df.nsmallest(5)
    
    winners.name, losers.name = "winners", "losers"
    
    st.table(winners)
    ## st.table(losers)
    
    winnerpick = st.selectbox("Pick a winner to Visualize:", winners.index)
    st.line_chart(stocks_df[winnerpick][date:])
    
    # loserpick = st.selectbox("Pick a loser to Visualize:", losers.index)
    # st.line_chart(stocks_df[loserpick][date:])



if __name__ == "__main__":
    indexPerformance(10)


