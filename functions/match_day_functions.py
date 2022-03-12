import pandas as pd

# reading in the data sets
nation_df = pd.read_csv("../data/nation_data.csv")
player_df = pd.read_csv("../data/player_data.csv")

def matchday(group_table, ...):

    return group_table


home = 'Japan'
# test function to retrieve teams lineup as a list
print(f"\n{home} Line Up: {', '.join(player_df.loc[player_df['Country'] == home]['Name'].tolist())}")

# test function for more detailed lineup
print(f"\n{home} Line Up:\n\n GK:{', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'GK'))]['Name'].tolist())}\n Defence: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'DEF'))]['Name'].tolist())}\n Midfield: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'MID'))]['Name'].tolist())}\n Attack: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'ATK'))]['Name'].tolist())}")

# retrieves all data from the dataframes, ready for the match engine
def match_data_collection(home, away):
    # Retrieve all relevant data from nation_df, player df

    return p_home, p_away, home_players, away_players, home_ratings, away_ratings


