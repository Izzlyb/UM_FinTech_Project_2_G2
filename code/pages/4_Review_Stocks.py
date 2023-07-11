import streamlit as st
import pandas as pd
from pathlib import Path
from PortfolioAsset import *
from GetStockData import *
from EquityIndexPerf import *


st.title('Review stock of the US Market Indexes... 👁️‍🗨️')

st.markdown("""
    This app retrieves the list of the index componenets:

        - Dow Jones Industrial Average
        - S&P 500
        - Nasdaq 100
        - Russell 2000

    it also display the corresponding **stock closing price** (year-to-date)!
""")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Web scraping of S&P 500 data
@st.cache_data(persist=True)
def upload_idx_components():
    DowJones_df = pd.read(Path("Resouces/DowJones.csv"))
    Nasdaq100_df = pd.read(Path("Resouces/Nasdaq100.csv"))
    Russell2000_df = pd.read(Path("Resouces/Russell2000.csv"))
    SP500_df = pd.read(Path("Resouces/SP500_sub.csv"))

#----------------------------------------------------------------

ix_list = []
for i in index_dict:
    ix_list.append(f"{i}")

# Web scraping of S&P 500 data
@st.cache_data(persist=True)
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

stocks_df = load_data()
# sector = stocks_df.groupby('GICS Sector')

# Index selection from the Sidebar Selection
selected_idx = st.sidebar.selectbox('Index', ix_list)
ix_seltd = index_dict[selected_idx]
# index_csv = select_file_name(ix_seltd)
if ix_seltd == 'DJI':
    index_csv = DJI_CSV
elif ix_seltd == 'SP500':
    index_csv = SP500_CSV
elif ix_seltd == 'NASDAQ':
    index_csv = NASDAQ_CSV
elif ix_seltd == 'RUS2000':
    index_csv = RUS2000_CSV

# st.write(f"the index code is {ix_seltd}.")
# st.write(f"the file is: {index_csv}.")

view_form = st.form('view_form')
with view_form:
    col_1, col_2, col_3 = st.columns([1, 6, 1])
    with col_2:
        stocks_df = get_index_stocks_data(ix_seltd)

        if selected_idx == "Dow Jones Industrial":
            st.write(f"we will review the {selected_idx} index")
            st.write(stocks_df)

        if selected_idx == "S&P 500":
            st.write(f"We will review the {selected_idx} index")
            # Sidebar - Sector selection
            # sorted_sector_unique = sorted( stocks_df['GICS Sector'].unique() )
            # selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)
            # Filtering data
            # df_selected_sector = stocks_df[ (stocks_df['GICS Sector'].isin(selected_sector)) ]
            st.write(stocks_df)

        if selected_idx == "Nasdaq 100":
            st.write(f"We will review the {selected_idx} index")
            st.write(stocks_df)


        if selected_idx == "Russell 2000":
            st.write(f"We will review the {selected_idx} index")
            st.write(stocks_df)

        # flavor_slctd = st.selectbox('Select flavor', 
        #                             ['Vanilla', 'Chocolate'], key=1)
        # st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
        # st.write(f"flavor selected: {flavor_slctd}")

    submitted1 = st.form_submit_button('Submit 1')

tkr_list = get_idx_stocks_list(index_csv)
indexPerformance(tkr_list, 10)

st.markdown("Columns inside form")



