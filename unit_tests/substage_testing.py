from functions.substage_functions import group_draw, group_simulation

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

nation_df = pd.read_csv('../data/nation_data.csv')
player_df = pd.read_csv('../data/player_data.csv')
list = nation_df.loc[nation_df['Confederation'] == 'UEFA']['Country'].to_list()
sim = 1
WC = 1

data = [nation_df, player_df]

group_draw(11, 4, list)

group_simulation(data, list[:4], 2, sim, WC)