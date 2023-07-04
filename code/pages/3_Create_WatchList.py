
import streamlit as st
from assets import portfolios

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    # st.checkbox("Disable selectbox widget", key="disabled")
    wl_action = st.radio(
        "Select what action you want to perform with watchlists 👉",
        options=["Create", "Modify", "Delete"],
    )
    
    if wl_action == "Create":
        type_asset = st.radio(
            "Select what action you want to perform with watchlists 👉",
            options=["Stocks", "ETFs", "Index"],
            )
    else:
        type_asset = ""


with col2:
    st.write(f"the options selected is: {wl_action}")
    st.write(f"the type of asset you would like to see: {type_asset}")
    
    if( wl_action == "Create"):
        new_portfolio = st.text_input("Enter a watch list name:", "")
    else:
        option = st.selectbox(
            "Which watchlist would you like to modify?",
            portfolios
            )

