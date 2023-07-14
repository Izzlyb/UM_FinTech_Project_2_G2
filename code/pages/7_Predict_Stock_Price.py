import streamlit as st
import pandas as pd
from datetime import date, time
import yfinance as yf
from pathlib import Path
from algoTraderLSTM import *

#################################################################
def main():
    st.markdown(
        """

        ## You are in the Prediction of Stock Price Page 🛠️

        """)

    pf_name = ""

    AlgoPredictPriceLSTM("MSFT")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


if __name__ == '__main__':
    main()

