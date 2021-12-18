import pandas as pd

# reading in the data sets
nation_df = pd.read_csv("../data/nation_data.csv")
player_df = pd.read_csv("../data/player_data.csv")


# test function to retrieve teams lineup as a list
home_lineup = player_df.loc[player_df['Country'] == 'Japan']['Name'].tolist()
print(', '.join(map(str, home_lineup)))


# retrieves all data from the dataframes, ready for the match engine
def match_data_collection(home, away):
    # Retrieve all relevant data from nation_df, player df

    return p_home, p_away, home_players, away_players
