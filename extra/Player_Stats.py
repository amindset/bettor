import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button

page_bg_img = """
<style>
#root > div:nth-child(1) > div.withScreencast > div > div {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/002/018/246/original/abstract-colorful-pastel-gradient-background-free-video.jpg");
    background-size: cover;
}
.css-tic8ca {
        background-color: white;
    }
    [data-baseweb = "popover"], #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(5) > div > div > div {
        background-color: white;
    }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

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

