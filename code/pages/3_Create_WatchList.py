
import streamlit as st
from assets import portfolios

watchlists = []

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
if "watchlist" not in st.session_state:
    st.session_state.watchlist = ""

action_form = st.form(key='action_form')
col1, col2 = st.columns(2)

with action_form:
    col_11, col_12, col_13 = st.columns([1,1,1])

    with col_11:
        # st.checkbox("Disable selectbox widget", key="disabled")
        wl_action = st.radio(
            "Select action to perform with watchlists.👉",
            options=["View List", "Create", "Modify", "Delete"]
        )

    with col_12:
        type_asset = st.radio(
            "Select the kind of Asset to See 👉",
            options=["Stocks", "ETFs", "Index"],
            )

    with col_13:
        st.write(f"Action selected: {wl_action}")
        st.write(f"Asset like to see: {type_asset}")


if wl_action == "View List":
    pf_name = st.session_state.watchlist
    if pf_name == "":
        st.warning("There are no watchlists saved")
    else:
        pf_list = pf_name
        st.selectbox("Please make Selection:", pf_list)

    st.warning("Function still not implemented")

elif wl_action == "Create":
    new_watchlist = st.text_input("Enter a watch list name:", "")

elif wl_action == "Modify":
    wl_select = st.selectbox("Please make Selection:", watchlists )

else:
    st.write("Please make Selection:")
