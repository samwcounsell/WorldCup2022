from functions.group_stage import group_draw, group_simulation
from functions.progression import progression
from functions.knockout import knockout

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

nation_df = pd.read_csv('../data/nation_data.csv')
player_df = pd.read_csv('../data/player_data.csv')
list = nation_df.loc[nation_df['Confederation'] == 'UEFA']['Country'].to_list()
sim = 1
WC = 1

teams = list[:8]

data = [nation_df, player_df]

for i in range(10):
    a = knockout(data, teams, 2, 1, 0)
    print("\n", a)

from functions.knockout import penalties

for i in range(100):
    penalties()