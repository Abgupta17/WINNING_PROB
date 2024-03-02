import pickle
import pandas as pd
import numpy as np
import streamlit as st

# Load data and model
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))

# Streamlit UI
st.set_page_config(layout="wide")
st.title('IPL Win Predictor')

# Sidebar
with st.sidebar:
    st.subheader('Select Teams and City')
    batting_team = st.selectbox('Batting Team', sorted(teams))
    bowling_team = st.selectbox('Bowling Team', sorted(teams))
    selected_city = st.selectbox('Host City', sorted(cities))

    st.subheader('Match Details')
    target = st.number_input('Target', min_value=0, step=1, format='%d')
    score = st.number_input('Score', min_value=0, step=1, format='%d')
    overs = st.number_input('Overs Completed', min_value=0.0, step=0.1, format="%.1f")
    wickets = st.number_input('Wickets Out', min_value=0, step=1, format='%d')

    st.markdown('---')
    if st.button('Predict Probability'):
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                                  'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets_left],
                                  'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

        result = pipe.predict_proba(input_df)
        win_probability = round(result[0][1] * 100)
        loss_probability = round(result[0][0] * 100)

# Main content
st.subheader('Match Details')
st.write(f'**Batting Team:** {batting_team}')
st.write(f'**Bowling Team:** {bowling_team}')
st.write(f'**Host City:** {selected_city}')
st.write(f'**Target:** {target}')
st.write(f'**Score:** {score}')
st.write(f'**Overs Completed:** {overs}')
st.write(f'**Wickets Out:** {wickets}')

if 'win_probability' in locals():
    st.subheader('Predicted Probabilities')
    st.write(f'**{batting_team} Win Probability:** {win_probability}%')
    st.write(f'**{bowling_team} Win Probability:** {loss_probability}%')


































# import pickle
# import pandas as pd
# import numpy as np
# import sklearn
# import streamlit as st
#
# teams = ['Sunrisers Hyderabad',
#  'Mumbai Indians',
#  'Royal Challengers Bangalore',
#   'Kolkata Knight Riders',
#  'Kings XI Punjab',
#  'Chennai Super Kings',
#  'Rajasthan Royals',
#  'Delhi Capitals']
#
# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
#        'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#        'Sharjah', 'Mohali', 'Bengaluru']
#
# pipe = pickle.load(open('pipe.pkl', 'rb'))
# st.title('IPL Win Predictor')
#
#
#
# col1, col2 = st.columns(2)
#
# with col1:
#     batting_team = st.selectbox('Select the batting team',sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select the bowling team',sorted(teams))
#
# selected_city = st.selectbox('Select host city',sorted(cities))
#
# target = st.number_input('Target')
#
# col3,col4,col5 = st.columns(3)
#
# with col3:
#     score = st.number_input('Score')
# with col4:
#     overs = st.number_input('Overs completed')
# with col5:
#     wickets = st.number_input('Wickets out')
#
# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs*6)
#     wickets = 10 - wickets
#     crr = score/overs
#     rrr = (runs_left*6)/balls_left
#
#     input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
#
#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]
#     st.header(batting_team + "- " + str(round(win*100)) + "%")
#     st.header(bowling_team + "- " + str(round(loss*100)) + "%")

