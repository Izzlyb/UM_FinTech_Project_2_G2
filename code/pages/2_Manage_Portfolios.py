import streamlit as st
import pandas as pd
from datetime import date, time
import yfinance as yf
from pathlib import Path
from assets import *
from PortfolioAsset import *
from GetStockData import *
from work_portfolios import *


TEST_FLAG = False
NewPortfolioStt = False
sel_portf_name = ""
submit_name = False
pf_stks_df = pd.DataFrame()
NewPortfolioStocks = []
stk_qty = 0
stk_tkr = ""

DJI_CSV = "DowJones.csv"
SP500_CSV = "SP500_sub.csv"
NASDAQ_CSV = "Nasdaq100"
RUS2000_CSV = "Russell2000.csv"

INDEX = 'Dow Jones Industrial'

################################
def display_stks_to_newpf():
    if len(st.session_state.stks_to_newpf) > 0:
        for i in range(len(st.session_state.stks_to_newpf)):
            st.write(st.session_state.stks_to_newpf[i].Quantity[0],
                     st.session_state.stks_to_newpf[i].Ticker[0],
                     st.session_state.stks_to_newpf[i].OriginalPrice[0],
                     st.session_state.stks_to_newpf[i].OriginalDate[0],
                     st.session_state.stks_to_newpf[i].ActualPrice[0],
                     st.session_state.stks_to_newpf[i].TransType)
    else:
        st.error("Error with stks_to_newpf")

#----------------------------------------------------------------


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def save_portfolio():
    save_df = pd.DataFrame()
    
    if len(st.session_state.stks_to_newpf) > 0:
        for i in range(len(st.session_state.stks_to_newpf)):
            # list of name, degree, score
            tkr = [st.session_state.stks_to_newpf[i].Ticker[0]]
            orgprc = [st.session_state.stks_to_newpf[i].OriginalPrice[0]]
            qty = [st.session_state.stks_to_newpf[i].Quantity[0]]
            orgdt = [st.session_state.stks_to_newpf[i].OriginalDate[0]]
            actprc = [st.session_state.stks_to_newpf[i].ActualPrice[0]]
            tt = [st.session_state.stks_to_newpf[i].TransType]
            # dictionary of lists 
            dict = {'Ticker': tkr, 'OriginalPrice': orgprc, 'Quantity': qty, 'OriginalDate' : orgdt, 'ActualPrice' : actprc, 'TransType' : tt} 
            df = pd.DataFrame(dict)
            save_df = pd.concat([save_df, df])
    else:
        st.error("Error with save_portfolio")

    save_df.set_index('Ticker', inplace=True)
    
    save_df.to_csv(f"data/pf__{st.session_state.new_portfolio_nm}.csv")
    st.session_state.new_portfolio_nm = ""
    st.session_state.stks_to_newpf = []
#----------------------------------------------------------------


#################################################################
def main():
    st.markdown(
        """

        ## You are in the Create Portfolio Page 🛠️

        """)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # select_form = st.form(key="select_form")
    # with select_form:
    col_11, col_12 = st.columns(2)
    with col_11:
        # st.checkbox("Disable selectbox widget", key="disabled")
        type_action = st.radio(
            "Select action: 🎬",
            options=["Buy", "Sell", "View"]
        )

        with col_12:
            type_portfolio = st.radio(
                "Select: 👉",
                options=["New", "Existing"],
                )

        # select_btn = st.form_submit_button("Submit Selection")

    pf_list = get_portfolio_names()
    if type_action == "Buy":
        st.session_state.stock_list_action = "Buy"
        if type_portfolio == "New":
            pf_name = st.text_input("Enter name for new Portfolio:")
            st.write(f"Start creating portfolio:>{pf_name}<")
            st.session_state.stock_list_name = pf_name

            # st.text_input(f"Do you want to {type_action} the portfolio {pf_name}")
        else:
            pf_name = st.selectbox("Select a Portfolio", pf_list)
            st.write(f"Adding to portfolio:>{pf_name}<")
            if pf_name == "Make Selection from List":
                st.session_state.stock_list_name = ""
            else:
                st.session_state.stock_list_name = pf_name


    elif type_action== "Sell":
        st.session_state.stock_list_action = "Sell"
        pf_list = get_portfolio_names()

        if type_portfolio == "New":
            pf_name = st.text_input("Enter name for new Portfolio:")
            st.write(f"Start creating portfolio:>{pf_name}<")
            st.session_state.stock_list_name = pf_name
        else:
            pf_name = st.selectbox("Select a Portfolio", pf_list)
            st.write(f"Selling from portfolio:>{pf_name}<")
            if pf_name == "Make Selection from List":
                st.session_state.stock_list_name = ""
            else:
                st.session_state.stock_list_name = pf_name
                # st.text_input(f"Do you want to {type_action} the portfolio >{pf_name}<")




    elif type_action == "View":
        st.session_state.stock_list_action = "View"
        # st.write(f"Modify a portfolio:>{type_action}<")

        pf_name = st.selectbox("Select a Portfolio", pf_list)
        st.write(f"Start revising portfolio:>{pf_name}<")                        

        if pf_name == "Make Selection from List":
            st.session_state.stock_list_name = ""
        else:
            st.session_state.stock_list_name = pf_name
            # st.text_input(f"Do you want to {type_action} the portfolio >{pf_name}<")




    elif type_action == "Delete":
        st.write(f"Delete a portfolio:>{type_action}<")
        st.write("Function not yet Implemented...")


    # else:
    #     st.write("NO action specified...")
    if type_action == "View":
        col_11, col_12, col_13 = st.columns([1,4,2])
        with col_12:
            if st.session_state.stock_list_name == "Make Selection from List":
                st.session_state.stock_list_name = ""
            elif st.session_state.stock_list_name != "":
                st.write(f"portfolio: >{st.session_state.stock_list_name}<")
                pf_df = get_portfolio_assets(st.session_state.stock_list_name)
                pf_df
            else:
                st.write("Need to select Portfolio from list:")


        # with col_13:
            # if type_action == "Modify":
            #     type_action = st.radio(
            #         "Select action to perform: 🎬",
            #         options=["Sell", "Buy"]
            #         )
                
            #     st.text_input("enter the row number of the stock you want to modify:")

            # else:
            #     st.text_input("Press enter when finish viewing Portfolio", value="Yes")

    elif type_action == "Buy" and  st.session_state.stock_list_name != "":
        col_11, col_12 = st.columns(2)
        stocks_df = get_index_stocks_data("DJI")
        with col_11:
            stocks_df
        
        with col_12:
            stk = ""
            qty = 0

            qty_str = st.text_input("enter quantity of stocks:", value = "1")
            qty = int(qty_str)
            stk = st.text_input("enter stocks symbol:", value="", key="text")
            st.session_state.stock_qty=qty
            if qty > 0 and stk != "":
                close = stocks_df.loc[stocks_df['Symbol'] == "KO"]['Close'].values[0]
                
                add_ticker_to_list(stk, close, qty)
                
                # data = {'Ticker':[stk],
                #         'OriginalPrice': [close],
                #         'Quantity': [qty],
                #         'OriginalDate': [date.today()],
                #         'ActualPrice' : [close],
                #         'TransType' : ['BTO'] 
                # }

                # pf_stk = pd.DataFrame(data)
                # st.write("sell stock and add to portfolio:")
                # st.session_state.watchlist_df = pd.concat([st.session_state.watchlist_df, pf_stk])

    else:
        if st.session_state.stock_list_name != "":
            st.write("Missing name for Portfolio.")

    if len(st.session_state.watchlist_df) > 0:
        st.session_state.watchlist_df

# pf_asset_cols = ('Ticker', 
#                  'OriginalPrice', 
#                  'Quantity', 
#                  'OriginalDate', 
#                  'ActualPrice',
#                  'TransType')

    # work_frm_btn = st.form_submit_button("work_frm_btn")
    # with work_frm_btn.open:
    #     if work_pf == "view_pf":
    #     work_frm_btn = st.form_submit_button("Finish")
    # if action_submit_btn == False:
    #    if action_submit_btn == False:
    #        st.warning("select portfolio name:")
    #     pf_selected_form = st.form(key="pf_selected_form")
    #     with pf_selected_form:
    #         st.write("in the selected portfolio form to work the portfolio:")
    #         # st.write(f"Start >{type_action}< portfolio:>{pf_name}<")
    #         done_submit_btn = st.form_submit_button("Done Working with Portfolio")
    



        
#----------------------------------------------------------------
    # if select_btn == True:
    #     name_form = st.form(key='name_form', clear_on_submit=True)
    #     with name_form:
    #         if type_action == "Create":
    #             st.write("create a porfolio:")
                
    #         elif type_action == "View":
    #             st.write("View a portfolio:")
                
    #         elif type_action == "Modify":
    #             st.write("Modify a portfolio:")

    #         else:
    #             st.write("Delete a portfolio:")
    #             st.write("Function not Implemented Yet...")
                
    #     st.form_submit_button("Submit portfolio")


    # else:
    #     st.write("** select an action. **")
#------------------------------------------------------


if __name__ == '__main__':
    main()

