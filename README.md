# NBA ATS

## Setup Instructions
1. Clone the repository.
2. Install the dependencies from `requirements.txt`.
3. Run the scripts as needed for data processing and model generation.
4. import random
import pandas as pd

# Mock NBA team names
teams = [
    'Lakers', 'Warriors', 'Nets', 'Bucks', 'Celtics', 'Heat',
    'Suns', '76ers', 'Mavericks', 'Clippers', 'Raptors', 'Jazz',
    'Blazers', 'Nuggets', 'Grizzlies', 'Spurs', 'Pelicans', 'Magic'
]

# Function to generate random ATS results
def generate_ats_results(score_a, score_b, spread):
    ats_result_a = score_a - score_b - spread
    if ats_result_a > 0:
        return 'Win'
    else:
        return 'Loss'

# Function to generate mock game data
def generate_game_data(num_games):
    data = []
    for _ in range(num_games):
        team_a = random.choice(teams)
        team_b = random.choice(teams)
        while team_b == team_a:
            team_b = random.choice(teams)

        score_a = random.randint(80, 150)
        score_b = random.randint(80, 150)
        spread = random.uniform(-10, 10)
        ats_result_a = generate_ats_results(score_a, score_b, spread)
        prediction = random.choice(['Win', 'Loss'])
        confidence_score = round(random.uniform(0.5, 1.0), 2)

        game_info = {
            'Team A': team_a,
            'Team B': team_b,
            'Score A': score_a,
            'Score B': score_b,
            'Spread': round(spread, 2),
            'ATS Result A': ats_result_a,
            'Prediction': prediction,
            'Confidence Score': confidence_score
        }
        data.append(game_info)

    return pd.DataFrame(data)

# Generate sample data for 500 games
sample_data = generate_game_data(500)

# Save to CSV
sample_data.to_csv('nba_ats_sample_data.csv', index=False)
