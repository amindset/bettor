import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button


add_logo('https://github.com/amindset/nodestock/blob/main/LIVE%20BETS2.png?raw=true')

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title("⛹️ Player Stats")
with middle_column:
    st.title('')
with right_column:
    button(username="livebetcalc", floating=False, width=221)

df = pd.read_excel(
    io="NBA_Smart_Bets.xlsx",
    engine='openpyxl',
    sheet_name='PlayerStats',
    usecols='B:AD',
    nrows=1000,
)

st.dataframe(df)

