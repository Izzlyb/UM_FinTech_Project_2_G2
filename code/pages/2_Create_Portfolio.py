import streamlit as st
import pandas as pd
import time
import yfinance as yf
from pathlib import Path
from assets import portfolios, PortfolioAssets
from PortfolioAsset import *
from GetStockData import concat_multi_stocks

TEST_FLAG = False
NewPortfolioStt = False
sel_portf_name = ""
submit_name = False
    
DJI_CSV = "DowJones.csv"
SP500_CSV = "SP500_sub.csv"
NASDAQ_CSV = "Nasdaq100"
RUS2000_CSV = "Russell2000.csv"

INDEX = 'Dow Jones Industrial'

################################################################
def create_portfolio(data):
    # Select some rows using st.multiselect. This will break down when you have >1000 rows.
    # data is a dataframe.
    st.write('### Full Dataset', data)
    selected_indices = st.multiselect('Select rows:', data.index)
    selected_rows = data.loc[selected_indices]
    st.write('### Selected Rows for your new portfolio', selected_rows)
    
    return selected_rows
# ---------------------------------------------------------------    


#################################################################
@st.cache_data
def get_stock_data(ticker, date1="", date2=""):
    
    data = yf.download(
        tickers = ticker,
        start=date1,
        end=date2,
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

    stock_df = data

    return data
#----------------------------------------------------------------


#################################################################
def get_index_stocks_data(index):
    sec_now = time.time()
    sec_ytrdy = time.time()-(24*60*60)
    now = time.localtime(sec_now)
    yesterday = time.localtime(sec_ytrdy)
    # print(time.strftime("%y/%m/%d %H:%M", now))
    # st.write(f">the start time is: {start_date}<, >the end time is: {end_date}<")
    # dji_tickers = pd.read_csv(Path("Resources/DowJones.csv"))

    if index == 'DJI':
        index_csv = DJI_CSV
    elif index == 'SP500':
        index_csv = SP500_CSV
    elif index == 'NASDAQ':
        index_csv = NASDAQ_CSV
    elif index == 'RUS2000':
        index_csv = RUS2000_CSV

    dji_tickers = pd.read_csv(Path(f"Resources/{index_csv}"))
    tickers_lst = list(dji_tickers.loc[:]['Symbol'])

    if TEST_FLAG == True:
        tkrs_df = pd.read_csv(Path("Resources/sp500_cont_prices.csv"))
    else:
        tkrs_df = concat_multi_stocks(tickers_lst)

    # data = { "Ticker" : (dji_tickers['Symbol'].sort_values()).values,
    #         "Open" : (df_dji['Open'].values)[0],
    #         "High" : (df_dji['High'].values)[0],
    #         "Low" : (df_dji['Low'].values)[0],
    #         "Close" : (df_dji['Close'].values)[0],
    #         "Adj Close" : (df_dji['Adj Close'].values)[0],
    #         "Volume" : (df_dji['Volume'].values)[0]
    #         }

    # # dji = tkrs_df.copy()
    # data_df = pd.DataFrame(data = {
    #     }, columns

    return tkrs_df
#----------------------------------------------------------------


#################################################################
def main():
    idx_stocks_df = pd.DataFrame()
    submit_name = False
    
    st.write("""
            # You are in the Create Portfolio Page 📊
            """)

    with st.form(key = 'form1'):
        new_portfolio_nm = ""
        st.write("To create a new Portfolio, Enter a Portfolio Name:")
        new_portfolio_nm = st.text_input("Enter a Portfolio Name:", "")

        submit_name = st.form_submit_button("Create Portfolio")
        if submit_name == True and new_portfolio_nm != "":
            idx_stocks_df = get_index_stocks_data('DJI')

    if new_portfolio_nm != "":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write(f"You can choose from the {INDEX} list to add to you portfolio")

            if new_portfolio_nm in portfolios:
                st.error("This name is already in use. Please enter another name.")
            else:
                new_portfolio_nm = new_portfolio_nm.replace(" ", "_")
                # selected_rows = create_portfolio(idx_stocks_df)
                st.write('### Full Dataset', idx_stocks_df)
                selected_indices = st.multiselect('Select rows:', idx_stocks_df.index)
                selected_rows = idx_stocks_df.loc[selected_indices]
                
        with col2:
            st.write(f"### We wil create a new portfolio: {new_portfolio_nm}.")
            st.write(" Selected Rows for your new portfolio", selected_rows)

        submit_creating = st.button("Done Creating")
        
        if submit_creating and len(selected_rows) > 0:
            if 'New_Portfolio' not in st.session_state:
                st.session_state['New_Portfolio'] = selected_rows
                st.success("Your portfolio has been created.")
        elif len(selected_rows):
            st.error("Portfolio was not created.")

    elif new_portfolio_nm == "" and submit_name == True:
        st.warning("Need to enter a Name.")
        submit_name = False
#------------------------------------------------------


if __name__ == '__main__':
    main()










    
# if [portfolios[i] for i in range(len(portfolios)) if i == portfolios.index(portfolios[i])]:
#     st.write("Portfolio name already exist")
# else:
#     st.write('You selected:', new_portfolio)
#     portfolios.append(new_portfolio)
# initialize all data.
# if portfolios[0] == "There are no portfolios stored":
#     st.write("There are no portfolios.")
# st.write("Select an existing portfolio from the list below:")
# sel_portf_name = st.selectbox(
#     label = "Enter a Name",
#     options = (portfolios),
#     label_visibility = "hidden"
#     )
# sel_portf_name
# if sel_portf_name !="":
#     st.write(f"The portfolio name is: {sel_portf_name}.")
#     df = CreatePortfolioDf(PortfoliosOwned[sel_portf_name])
#     df
# else:
#     st.write(f"No matching portfolio name.")

#     PortfoliosOwned["Hybrid Portfolio"]
#     df = CreatePortfolioDf(PortfolioStocks)
# else:
#     df = pd.DataFrame()
# df = CreatePortfolioDf(PortfolioStocks)
# df
# Text input
# st.write("")
