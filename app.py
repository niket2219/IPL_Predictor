import streamlit as st
import pickle
import pandas as pd

with open('./pipe.pkl', 'rb') as f:
    model = pickle.load(f)

teams = ['Rajasthan Royals', 'Royal Challengers Bangalore',
       'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
       'Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders',
       'Punjab Kings', 'Mumbai Indians']

cities = ['Chennai', 'Mumbai', 'Jaipur', 'Pune', 'Durban', 'Hyderabad',
       'Bangalore', 'Bengaluru', 'Delhi', 'Port Elizabeth',
       'East London', 'Dubai', 'Chandigarh', 'Kolkata', 'Bloemfontein',
       'Ranchi', 'Abu Dhabi', 'Johannesburg', 'Dharamsala', 'Ahmedabad',
       'Centurion', 'Cape Town', 'Indore', 'Visakhapatnam', 'Sharjah',
       'Raipur', 'Nagpur', 'Kimberley', 'Cuttack', 'Navi Mumbai']

st.title("IPL Predictor")

col1 , col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team",sorted(teams),key="bat")
with col2:
    bowling_team = st.selectbox("Select Batting Team",sorted(teams),key="bowl")

selected_city = st.selectbox("Select Venue",sorted(cities))

col3,col4 = st.columns(2)

with col3:
    target = st.number_input("Target Score",step=5)
with col4:
    score = st.number_input("Current Score",step=5)

col5,col6 = st.columns(2)

with col5:
    overs = st.number_input("Overs Completed",step=1)
with col6:
    wickets = st.number_input("Wickets Down",step=1)

if st.button("Predict Probability"):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = (score/overs)
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'BattingTeam':[batting_team],	'BowlingTeam':[bowling_team],	'City':[selected_city],	'runs_left':[runs_left],	'balls_left':[balls_left],	'wickets':[wickets]	,'total_run_x':[target]	,'crr':[crr]	,'rrr':[rrr]})
    
    result = model.predict_proba(input_df)
    win = result[0][1]
    loss = result[0][0]

    st.header(batting_team+"- "+str(round(win*100))+"%")
    st.header(bowling_team+"- "+str(round(loss*100))+"%")




