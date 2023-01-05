import streamlit as st 
import pandas as pd
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards

add_logo('https://github.com/amindset/nodestock/blob/main/LIVE%20BETS2.png?raw=true')


st.markdown("""
    <style>
    .css-184tjsw p{
        color: blue;
    }
    .css-1xarl3l{
        color: black;
    }

    [data-testid = "stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/002/018/246/original/abstract-colorful-pastel-gradient-background-free-video.jpg");
    background-size: cover;
    }
    .css-tic8ca {
        background-color: white;
    }
    [data-baseweb = "popover"] {
        background-color: #fcc86d;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(5) > div > div > div {
        background-color: black;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title("💻 Live Bet Calculator")
with middle_column:
    st.title('')
with right_column:
    button(username="livebetcalc", floating=False, width=221)

whatLeague = st.header('Pick the League')
st.write('Below you can enter your information into the calculator for the current game. For better odds check out team parlays. The over/under tends to be better.')
st.write('')

stoggle(
    "Click me for Notes",
    """\nIf you are doing a bet based on the quarter be sure to set the quarter tab to 4.
        \nSetting your bets around half time or later in the game helps improve win rates.""",
)

contact_options = ['NBA','NFL','NCAAB','NCAAF','Overseas BBall']
contact_selected = st.selectbox("Choose a league!", options=contact_options)

defense = pd.read_excel(
    io="NBA_Smart_Bets.xlsx",
    engine='openpyxl',
    sheet_name='defense',
    usecols='B:M',
    nrows=1000,
)

left_column, right_column = st.columns(2)
with left_column:
    st.header("Home Team")
    home_Team = defense['Team'].unique().tolist()
    teamSelected = st.selectbox('Please Select Home Team:', home_Team)
    x = str(teamSelected).replace("['","").replace("']","")
    st.subheader(x)
    home_score = st.number_input("Enter the Home team score!")
    dataHome = defense.loc[defense["Team"] == x,'Home2']
    dataHome2 = defense.loc[defense["Team"] == x,'Current']
    c = str(dataHome)
    c2 = str(dataHome2)
    homer = c.split()[1]
    homer2 = c2.split()[1]
    #st.subheader(homer)
    #st.subheader(homer2)
    
with right_column:
    st.header("Away Team")
    away_Team = defense['Team'].unique().tolist()
    teamSelected2 = st.selectbox('Please Select Away Team:', away_Team)
    y = str(teamSelected2).replace("['","").replace("']","")
    st.subheader(y)
    away_score = st.number_input("Enter the Away team score!")
    dataAway = defense.loc[defense["Team"] == y,'Away2']
    dataAway2 = defense.loc[defense["Team"] == y,'Current']
    d = str(dataAway)
    d2 = str(dataAway2)
    awayer = d.split()[1]
    awayer2 = d2.split()[1]
    #st.subheader(awayer)
    #st.subheader(awayer2)

st.markdown("---")

total_score = home_score+away_score

left_column, middle_column, right_colum = st.columns(3, gap='medium')
with left_column:
    whatQTR = st.number_input('What quarter are we in?',value=1)
    
with middle_column:
    timeLeft = st.number_input('Enter the remaining time in quarter!', value=1)

with right_colum:
    platformBet = st.number_input('Enter the current Over/Under bet for your platform!', value=50)


if contact_selected == "NBA":
    theLeague = 48
    timeLeftinGame = (float(theLeague) -(float(theLeague)/4)*float(whatQTR))+float(timeLeft)
elif contact_selected == "NFL" or contact_selected == "NCAAF":
    theLeague = st.text(60)
    timeLeftinGame = (float(theLeague)-(float(theLeague)/4)*float(whatQTR))+float(timeLeft)
elif contact_selected == "Overseas BBall":
    theLeague = st.text(40)
    timeLeftinGame = (float(theLeague)-(float(theLeague)/4)*float(whatQTR))+float(timeLeft)
elif contact_selected == "NCAAB":
    theLeague = st.text(40)
    timeLeftinGame = (float(theLeague)-(float(theLeague)/2)*float(whatQTR))+float(timeLeft)
else:
    theLeague = st.text("There was an error")

#print(timeLeftinGame)
#print(theLeague)
#print(total_score)
#print(platformBet)

myPace = total_score/((float(theLeague)-float(timeLeftinGame)))
platformPace = (float(platformBet)-total_score)/float(timeLeftinGame)
#print(myPace)
#print(platformPace)
high_Pts = ((myPace+(float(homer)+float(awayer))/100))*float(timeLeftinGame)+total_score
norm_Pts = ((myPace+(float(homer2)+float(awayer2))/100))*float(timeLeftinGame)+total_score
norm_Pts2 = ((myPace-(float(homer2)+float(awayer2))/100))*float(timeLeftinGame)+total_score
low_Pts = ((myPace-(float(homer)+float(awayer))/100))*float(timeLeftinGame)+total_score



# Create the Strategies
strat1 = round((float(total_score)/(float(theLeague)-float(timeLeftinGame)))*float(timeLeftinGame)+float(total_score),0)
# Strategy 2
if strat1 > float(platformBet):
    s1 = 'Over'
else:
    s1 = 'Under'

if high_Pts<float(platformBet) and norm_Pts<float(platformBet):
    res1 = 'Under'
else:
    res1 = 'Over'

if strat1>float(platformBet) and high_Pts>float(platformBet) and norm_Pts>float(platformBet):
    res2 = 'Over'
else:
    res2 = 'Under'

if strat1<float(platformBet) and low_Pts<float(platformBet) and norm_Pts2<float(platformBet):
    res3 = 'Under'
else:
    res3 = 'Over'

if low_Pts<float(platformBet) and norm_Pts2<float(platformBet):
    res4 = 'Under'
else:
    res4 = 'Over'

# Strategy 2
if res2 == 'Over' and res3 == 'Over':
    r1 = 2 
elif res2 == 'Under' and res3 == 'Under':
    r1 = 2
else:
    r1 = 0

avg = (norm_Pts + norm_Pts2)/2
avg2 = (high_Pts + norm_Pts2)/2

if avg>float(platformBet):
    res5 = 'Over'
else:
    res5 = 'Under'

if r1==2:
    if res5 == 'Over':
        s2 = 'Over'
    else:
        s2 = 'Under'
else:
    print('')

# Strategy 3
if res1 == 'Over' and res3 == 'Over':
    r2 = 2 
elif res1 == 'Under' and res3 == 'Under':
    r2 = 2
else:
    r2 = 0

if avg2>float(platformBet):
    res6 = 'Over'
else:
    res6 = 'Under'

if r2==2:
    if res6 == 'Over':
        s3 = 'Over'
    else:
        s3 = 'Under'
else:
    print('')

left_column, middle_column, right_column = st.columns(3)
left_column.metric(label="Strategy 1", value=s1)
middle_column.metric(label="Strategy 2", value=s2)
right_column.metric(label="Strategy 3", value=s3)
style_metric_cards()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    stoggle(
    "Strategy 1 Based On",
    """\nThis strategy focuses more on the pace of the game.""",
    )
with middle_column:
    stoggle(
    "Strategy 2 Based On",
    """\nThis strategy focuses more on each team's defense.""",
    )
with right_column:
    stoggle(
    "Strategy 3 Based On",
    """\nThis strategy is a mix both the pace of the game and each team's defense.""",
    )

st.markdown("---")

#st.dataframe(defense)