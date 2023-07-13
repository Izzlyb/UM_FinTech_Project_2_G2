
import streamlit as st
import pandas as pd
from assets import stock_portfolio, portfolios, PortfolioAssets
import PortfolioAsset 
from PortfolioAsset import PortfoliosOwned, HybridPortfolio, Portfolio2023, PortfolioETF, PortfolioStocks, CreatePortfolioDf

st.write("""
         # You are in the Create Portfolio Page 📊
         """)
st.sidebar.success("Select a demo above.")

# initialize all data.
df = pd.DataFrame()
sel_portf_name = ""

# if portfolios[0] == "There are no portfolios stored":
#     st.write("There are no portfolios.")
st.write("Select an existing portfolio from the list below:")
sel_portf_name = st.selectbox(
    label = "Enter a Name",
    options = (portfolios),
    label_visibility = "hidden"
    )

sel_portf_name

if sel_portf_name !="":
    st.write(f"The portfolio name is: {sel_portf_name}.")
    df = CreatePortfolioDf(PortfoliosOwned[sel_portf_name])
    df
else:
    st.write(f"No matching portfolio name.")

#     PortfoliosOwned["Hybrid Portfolio"]
#     df = CreatePortfolioDf(PortfolioStocks)
# else:
#     df = pd.DataFrame()
# df = CreatePortfolioDf(PortfolioStocks)
# df

# Text input
st.write("")
new_portfolio = ""
st.write("To create a new Portfolio, Enter a Portfolio Name:")
new_portfolio = st.text_input("Enter a Portfolio Name:", "")

if new_portfolio != "":
    if new_portfolio in portfolios:
        st.error("This name is already in use. Please enter another name.")
    else:
        new_portfolio = new_portfolio.replace(" ", "_")
        st.write(f"We wil create a new portfolio: {new_portfolio}.")

    # if [portfolios[i] for i in range(len(portfolios)) if i == portfolios.index(portfolios[i])]:
    #     st.write("Portfolio name already exist")
    # else:
    #     st.write('You selected:', new_portfolio)
    #     portfolios.append(new_portfolio)


