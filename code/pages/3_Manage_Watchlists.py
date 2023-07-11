import streamlit as st
from assets import portfolios
from GetStockData import *

watchlists = []


def WorkWatchlist():
    creat_wl_form = st.form(key="CreateWatchlist", clear_on_submit=True)
    with creat_wl_form:
        pass
    
    finishCreate = st.form_submit_button("Finish Watchlist")
    



def main():
    st.markdown(
    """
    ### Tell me what would you like to do with your lists:
    
    """
    )

    select_form = st.form(key='select_form')
    col1, col2 = st.columns(2)

#++++++++++++++++++++++++++++++++++++++++++++++++
    with select_form:
        col_11, col_12 = st.columns(2)

        with col_11:
            # st.checkbox("Disable selectbox widget", key="disabled")
            type_action = st.radio(
                "Select action to perform: 🎬",
                options=["View", "Create", "Modify", "Delete"]
            )

        with col_12:
            type_asset = st.radio(
                "Select the kind of Asset: 👉",
                options=["Stocks", "ETFs", "Index"],
                )

        selection = st.form_submit_button("Submit Selection")


    action_form = st.form(key='action_form')
    # if type_list == "Portfolio":
    #     pf_list = get_portfolios()

    with action_form:
        if type_asset == "Stocks":
            st.write(f"Action selected: {type_action}")
            #st.write(f"Asset like to see: {type_asset}")
            #st.write(f"List to see: {type_list}")

            if type_action == "View":
                st.session_state.stock_list_action = "View"
                watchlists = get_watchlist_names()
                if len(watchlists) == 0:
                    st.warning("There are no watchlists saved")
                else:
                    wl_select = st.selectbox("Please make Selection:", watchlists)
                    st.session_state.stock_list_name = wl_select
                    if wl_select != "Make Selection from List":
                        st.write(f"getting watchlist:>{wl_select}<")
                        watchlist_df = get_watchlist_df(wl_select)
                        watchlist_df
                    else:
                        st.write("Make Selection from List:")


            elif type_action == "Modify":
                st.session_state.stock_list_action = "Modify"
                watchlists = get_watchlist_names()
                if len(watchlists) == 0:
                    st.warning("There are no watchlists saved")
                else:
                    wl_select = st.selectbox("Please make Selection:", watchlists)
                    st.session_state.stock_list_name = wl_select
                    if wl_select != "Make Selection from List":
                        st.write(f"getting watchlist:>{wl_select}<")
                        watchlist_df = get_watchlist_df(wl_select)
                        watchlist_df
                    else:
                        st.write("Make Selection from List:")


            elif type_action == "Create":
                st.session_state.stock_list_action = "Create"
                wl_select = st.text_input("Enter a Name:")
                st.session_state.stock_list_name = wl_select


            elif type_action == "Delete":
                st.warning("Function still not implemented")

            else:
                st.write("Please make Selection:")
            
        elif type_action == "ETFs":
            st.warning("Function still not implemented")

        else:
            st.warning("Function still not implemented")

        action = st.form_submit_button("Make Selection")    

    if(type_action == "Create"):
        create_form = st.form(key="create_form")
        with create_form:
            st.write(f"Ready to Create new Watchlist: {st.session_state.stock_list_name}")
            if type_action == "Create" and type_asset == "Stocks":
                col_1, col_2 = st.columns(2)
                with col_1:
                    stocks_df = get_index_stocks_data("DJI")
                    st.session_state.idx_stock_df = stocks_df
                    st.write("Select from the stocks below:")
                    stocks_df

                with col_2:
                    # qty_str = st.text_input("Enter amount of shares:", key="quantity")
                    # if len(qty_str) > 0:
                    #     st.session_state.stock_qty = int(qty_str)
                    # else:
                    #     st.session_state.stock_qty = 0

                    stk_name = st.text_input("Enter a Stock Ticker:", key="stk_name")
                    if len(stk_name) > 0:
                        st.session_state.ticker_name = stk_name
                    else:
                        st.session_state.ticker_name = ""
            
            create_fr_btn = st.form_submit_button("Make Selection")

    if type_action == "Create" and st.session_state.ticker_name != "":

        add_ticker_to_list(st.session_state.ticker_name, 0, 0)

        if len(st.session_state.watchlist_df) > 0:
            st.session_state.watchlist_df
    else:
        st.write("Missing name for Portfolio.")



    save_btn = st.button("Save Watchlist")
    if save_btn == True:
        save_watchlist()
        st.write("Watchlist has been saved")






if __name__ == "__main__":
    main()
