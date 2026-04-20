import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Generation
@st.cache
def generate_sample_data(num_games=100):
    teams = ['Team A', 'Team B', 'Team C', 'Team D']
    data = []
    for i in range(num_games):
        game = {
            'Date': pd.Timestamp('2023-01-01') + pd.DateOffset(days=i),
            'Home Team': np.random.choice(teams),
            'Away Team': np.random.choice(teams),
            'Home Score': np.random.randint(80, 120),
            'Away Score': np.random.randint(80, 120),
            'ATS Result': np.random.choice(['Win', 'Lose'], p=[0.5, 0.5])
        }
        data.append(game)
    return pd.DataFrame(data)

# Dashboard Title
st.title('NBA ATS Dashboard')

# Generate Sample Data
num_games = st.sidebar.slider('Number of Games', 10, 500, 100)

st.write(f'Generating data for {num_games} games...')

nba_data = generate_sample_data(num_games)

# Display DataFrame
if st.checkbox('Show raw data', False):
    st.write(nba_data)

# Visualization 1: Scores Overview
st.subheader('Scores Overview')
score_data = nba_data[['Date', 'Home Score', 'Away Score']]
score_data.set_index('Date', inplace=True)
st.line_chart(score_data)

# Visualization 2: ATS Results
st.subheader('ATS Results')
ats_count = nba_data['ATS Result'].value_counts()

fig, ax = plt.subplots()
seaborn.barplot(x=ats_count.index, y=ats_count.values, ax=ax)
ax.set_title('ATS Results Distribution')
ax.set_ylabel('Count')
ax.set_xlabel('ATS Result')
st.pyplot(fig)  

#Interactive Components
st.sidebar.markdown('### Interactive Filters')
home_team_filter = st.sidebar.selectbox('Select Home Team', ['All'] + teams)
if home_team_filter != 'All':
    nba_data = nba_data[nba_data['Home Team'] == home_team_filter]
    st.write(nba_data)

