import pandas as pd

# reading in the data sets
#nation_df = pd.read_csv("../data/2022_nation_data.csv")
#player_df = pd.read_csv("../data/2022_player_data.csv")

# def matchday(group_table, ...):

    #return group_table


#home = 'Japan'
## test function to retrieve teams lineup as a list
#print(f"\n{home} Line Up: {', '.join(player_df.loc[player_df['Country'] == home]['Name'].tolist())}")

# test function for more detailed lineup
#print(f"\n{home} Line Up:\n\n GK:{', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'GK'))]['Name'].tolist())}\n Defence: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'DEF'))]['Name'].tolist())}\n Midfield: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'MID'))]['Name'].tolist())}\n Attack: {', '.join(player_df.loc[((player_df['Country'] == home) & (player_df['Position'] == 'ATK'))]['Name'].tolist())}")

def match_data_collection(nation_df, player_df, home, away):
    # Retrieve all relevant data from nation_df, player df

    # home
    p_home = (float(nation_df.loc[nation_df['Country'] == home]['Attack']) / float(nation_df.loc[nation_df['Country'] == away]['Defense']))/90
    home_players = player_df.loc[player_df['Country'] == home]['Name'].tolist()
    home_atk = player_df.loc[player_df['Country'] == home]['Attack'].tolist()
    home_pass = player_df.loc[player_df['Country'] == home]['Passing'].tolist()

    # away
    p_away = (float(nation_df.loc[nation_df['Country'] == away]['Attack']) / float(nation_df.loc[nation_df['Country'] == home]['Defense']))/90
    away_players = player_df.loc[player_df['Country'] == away]['Name'].tolist()
    away_atk = player_df.loc[player_df['Country'] == away]['Attack'].tolist()
    away_pass = player_df.loc[player_df['Country'] == away]['Passing'].tolist()

    return p_home, home_players, home_atk, home_pass, p_away, away_players, away_atk, away_pass


