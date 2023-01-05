import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.metric_cards import style_metric_cards


add_logo('https://github.com/amindset/nodestock/blob/main/LIVE%20BETS2.png?raw=true')

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title("⛹️‍♂️ Player Projections")
with middle_column:
    st.title('')
with right_column:
    button(username="livebetcalc", floating=False, width=221)
st.subheader("Check out the player projections for today!")


### --- Load Dataframe
df = pd.read_excel(
    io="NBA_Smart_Bets.xlsx",
    engine='openpyxl',
    sheet_name='Stats',
    usecols='A:Z',
    nrows=1000,
)

# TOP KPI's
# Points
player = df['Players'].unique().tolist()
playerSelected = st.selectbox('Please Select A Players:', player)
thePlayer = str(playerSelected).replace("['","").replace("']","")
st.subheader(thePlayer)

pts_Player = df.loc[df['Players'] == thePlayer, 'PTS']
a = str(pts_Player)
pointer = a.split()[1]
    
ptsO_Player = df.loc[df['Players'] == thePlayer, 'PTS Over']
b = str(ptsO_Player)
pointerO = b.split()[1]
ptO = round(float(pointerO)*100)
pointO = f"{ptO}%"
    
ptsU_Player = df.loc[df['Players'] == thePlayer, 'PTS Under']
c = str(ptsU_Player)
pointerU = c.split()[1]
ptU = round(float(pointerU)*100)
pointU = f"{ptU}%"

left_column, middle_column, right_column = st.columns(3)
left_column.metric(label="Current Points Avg", value=pointer)
middle_column.metric(label="Percent Over", value=pointO)
right_column.metric(label="Percent Under", value=pointU)
style_metric_cards()

#Rebounds
rebs_Player = df.loc[df['Players'] == thePlayer, 'REBS']
d = str(rebs_Player)
rebounder = d.split()[1]

rebsO_Player = df.loc[df['Players'] == thePlayer, 'REBS Over']
e = str(rebsO_Player)
rebounderO = e.split()[1]
rebO = round(float(rebounderO)*100)
reboundO =f"{rebO}%"

rebsU_Player = df.loc[df['Players'] == thePlayer, 'REBS Under']
f = str(rebsU_Player)
rebounderU = f.split()[1]
rebU = round(float(rebounderU)*100)
reboundU = f"{rebU}%"

left_column, middle_column, right_column = st.columns(3)
left_column.metric(label="Current Rebounds Avg", value=rebounder)
middle_column.metric(label="Percent Over", value=reboundO)
right_column.metric(label="Percent Under", value=reboundU)
style_metric_cards()

# Assists
asts_Player = df.loc[df['Players'] == thePlayer, 'ASTS']
x = str(asts_Player)
assister = x.split()[1]

astsO_Player = df.loc[df['Players'] == thePlayer, 'ASTS Over']
y = str(astsO_Player)
assisterO = y.split()[1]
astO = round(float(assisterO)*100)
assistO = f"{astO}%"

astsU_Player = df.loc[df['Players'] == thePlayer, 'ASTS Under']
z = str(astsU_Player)
assisterU = z.split()[1]
astU = round(float(assisterU)*100)
assistU = f"{astU}%"

left_column, middle_column, right_column = st.columns(3)
left_column.metric(label="Current Assists Avg", value=assister)
middle_column.metric(label="Percent Over", value=assistO)
right_column.metric(label="Percent Under", value=assistU)
style_metric_cards()

