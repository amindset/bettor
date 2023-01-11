import streamlit as st
import json
import requests
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Home",
    page_icon="🏀",
    layout='wide'
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/002/018/246/original/abstract-colorful-pastel-gradient-background-free-video.jpg");
    background-size: cover;
}
.css-tic8ca {
    background-color: white;
}
.css-1bk6rk2 a {
    color: mediumvioletred;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

add_logo('https://github.com/amindset/nodestock/blob/main/LIVE%20BETS2.png?raw=true')

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title("🏀 Home")
with middle_column:
    st.title('')
with right_column:
    button(username="livebetcalc", floating=False, width=221)

## Add json image code here ###

# st_lottie(lottie_phone)

left_column, right_column = st.columns(2)
with left_column:
    st.write('')
    st.title('Hi, we are Live Bet Calculator 👋')
    st.write("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.")

#with right_column:
    #st_lottie(lottie_dunk, height=250, width=300)

st.markdown('---')

#left_column, right_column = st.columns(2)
#with left_column:
st.header('📈 What we do')
st.write('Welcome to Live Bet Calculator, where we are passionate about helping sports bettors increase their winning chances and make the most out of their sports betting experience! For those who don’t have the time to do the necessary research on their favorite sports teams before game time, we are the perfect platform to get the information you need quickly and accurately.')
st.write('We offer a wide range of services tailored to your specific needs, whether you’re an experienced bettor or a novice just starting out. We have developed our platform to provide accurate and real-time data as well as analysis of all the latest news and trends in the world of sports betting.')
#with right_column:
    #st_lottie(lottie_phone, height=250, width=300)

st.markdown('---')

st.header('🏠 Find a home')

url = "https://pa.sportsbook.fanduel.com/"
st.subheader("[Fanduel](%s)" % url)
url2 = "https://sports.pa.betmgm.com/en/sports"
st.subheader("[BetMGM](%s)" % url2)
url3 = "https://sportsbook.draftkings.com/"
st.subheader("[Draftkings](%s)" % url3)
